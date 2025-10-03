import os
import replicate
import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize Replicate client with API token from environment
replicate_client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

# FastAPI app
app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your Vercel domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Music generator
def generate_music(genre, mood, instruments, bpm, duration, extra_notes=""):
    # Build a detailed music prompt
    prompt = f"""{genre} music with {instruments}, {bpm} BPM, {mood} mood.
    {extra_notes}"""
    print(f"🎵 Final Prompt: {prompt}")

    output = replicate_client.run(
        "facebook/musicgen:latest",
        input={
            "prompt": prompt,
            "duration": duration
        }
    )
    return output

# REST API endpoint
@app.post("/generate")
async def generate_api(data: dict):
    genre = data.get("genre", "Electronic")
    mood = data.get("mood", "Energetic")
    instruments = data.get("instruments", "synths and drums")
    bpm = data.get("bpm", 120)
    duration = data.get("duration", 15)
    extra_notes = data.get("extra_notes", "")

    audio_url = generate_music(genre, mood, instruments, bpm, duration, extra_notes)
    return {"audio_url": audio_url}

# Gradio UI (for testing/debugging)
def gradio_ui(genre, mood, instruments, bpm, duration, extra_notes):
    return generate_music(genre, mood, instruments, bpm, duration, extra_notes)

demo = gr.Interface(
    fn=gradio_ui,
    inputs=[
        gr.Dropdown(["Electronic", "Hip hop", "Jazz", "Rock"], label="Genre"),
        gr.Dropdown(["Energetic", "Peaceful", "Mysterious", "Happy"], label="Mood"),
        gr.Textbox(label="Instruments (e.g. guitar, piano, synth)"),
        gr.Slider(60, 180, value=120, step=5, label="BPM"),
        gr.Radio([5, 15, 30], value=15, label="Duration (seconds)"),
        gr.Textbox(label="Extra Notes (optional)")
    ],
    outputs="audio",
    title="🎵 NivaBand AI Composer"
)

# Mount Gradio into FastAPI
app = gr.mount_gradio_app(app, demo, path="/")

# Local run
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
