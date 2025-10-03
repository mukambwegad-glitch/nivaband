import gradio as gr
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import scipy.io.wavfile
import uuid

# Load model (small = faster, medium/large = better quality but heavier)
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")

# Map duration to token length
duration_map = {
    "Short (5s)": 256,
    "Medium (15s)": 768,
    "Long (30s)": 1536
}

# Optional Smart Enhancer
def smarten_prompt(raw_prompt, vibe, instrument, tempo, chords):
    base = f"{raw_prompt.strip()}, in a {vibe} style with {instrument}, tempo: {tempo} BPM"
    if chords:
        base += f", guided by chords: {chords}"
    return base

# Generate music
def generate_music(prompt, duration_label, vibe, instrument, tempo, chords):
    tokens = duration_map[duration_label]
    final_prompt = smarten_prompt(prompt, vibe, instrument, tempo, chords)

    inputs = processor(text=[final_prompt], return_tensors="pt")
    audio_values = model.generate(
        **inputs,
        do_sample=True,
        guidance_scale=3,
        max_new_tokens=tokens
    )

    sr = model.config.audio_encoder.sampling_rate
    file_path = f"/tmp/{uuid.uuid4().hex}.wav"
    scipy.io.wavfile.write(file_path, sr, audio_values[0, 0].numpy())
    return file_path, final_prompt

# Gradio UI
with gr.Blocks(title="NivaBand: AI Music Composer") as app:
    gr.HTML("<link rel='stylesheet' href='theme.css'>")

    gr.Markdown("""
    # 🎧 NivaBand — AI Music Composer  
    _Generate high-quality music from your ideas. Style it. Control it. Share it._
    """)

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="📝 Describe your music idea", placeholder="e.g., Triumphant anthem with deep bass and strings...")
            vibe = gr.Radio(["Cinematic", "Lo-Fi", "Energetic", "Peaceful", "Mysterious"], label="🎨 Vibe", value="Cinematic")
            instrument = gr.Dropdown(["Piano", "Guitar", "Synth", "Strings", "Drums", "Ambient Pads"], label="🎸 Instrument", value="Synth")
            tempo = gr.Slider(60, 160, step=5, value=100, label="🎼 Tempo (BPM)")
            chords = gr.Textbox(label="🎵 Chords (Optional)", placeholder="Cmaj7, G, Am, F")
            duration = gr.Radio(list(duration_map.keys()), label="⏱️ Duration", value="Short (5s)")
            submit_btn = gr.Button("🎶 Generate Music")

        with gr.Column():
            output_audio = gr.Audio(label="🔊 Your Generated Track", type="filepath")
            display_prompt = gr.Textbox(label="🔍 Final Prompt Sent to Model", interactive=False)

    submit_btn.click(
        fn=generate_music,
        inputs=[prompt, duration, vibe, instrument, tempo, chords],
        outputs=[output_audio, display_prompt]
    )

app.launch()
