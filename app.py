from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import scipy.io.wavfile
import torch
import uuid
import os

from music_parser import parse_chords

app = FastAPI(title="NivaBand API")

# Load MusicGen model
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-melody")
processor = AutoProcessor.from_pretrained("facebook/musicgen-melody")

@app.post("/generate")
async def generate_music(
    prompt: str = Form(...),
    chords: str = Form(None),
    duration: int = Form(15)
):
    # Map duration → tokens
    duration_map = {5: 256, 15: 768, 30: 1536, 60: 3072}
    tokens = duration_map.get(duration, 768)

    # Parse chord guide
    chord_text = ""
    if chords:
        chord_text = parse_chords(chords)

    # Final prompt
    final_prompt = f"{prompt} {chord_text}".strip()

    # Generate
    inputs = processor(text=[final_prompt], return_tensors="pt")
    audio_values = model.generate(
        **inputs, 
        do_sample=True, 
        guidance_scale=3, 
        max_new_tokens=tokens
    )

    # Save output
    sr = model.config.audio_encoder.sampling_rate
    filename = f"{uuid.uuid4().hex}.wav"
    filepath = os.path.join("outputs", filename)
    os.makedirs("outputs", exist_ok=True)
    scipy.io.wavfile.write(filepath, sr, audio_values[0, 0].numpy())

    return {"file": f"/download/{filename}", "prompt_used": final_prompt}

@app.get("/download/{filename}")
async def download_file(filename: str):
    filepath = os.path.join("outputs", filename)
    return FileResponse(filepath, media_type="audio/wav")
