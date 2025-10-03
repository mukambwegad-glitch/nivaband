import os
import gradio as gr
import replicate

# Load API token from environment
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def generate_music(genre, mood, instruments, bpm, duration):
    # Build a smarter prompt
    prompt = f"{genre} music, {mood}, featuring {instruments}, {bpm} BPM"
    
    output = replicate.run(
        "facebook/musicgen:latest",
        input={
            "prompt": prompt,
            "duration": duration
        }
    )
    return output

with gr.Blocks(css="theme.css") as demo:
    gr.Markdown("# 🎵 NivaBand — AI Music Composer")

    genre = gr.Textbox(label="Genre", placeholder="Rock, Jazz, EDM...")
    mood = gr.Textbox(label="Mood/Emotion", placeholder="Energetic, Calm...")
    instruments = gr.Textbox(label="Instruments", placeholder="Guitar, Drums, Synth...")
    bpm = gr.Slider(60, 180, value=120, label="Tempo (BPM)")
    duration = gr.Radio([5, 15, 30], value=15, label="Duration (seconds)")

    generate_btn = gr.Button("🎶 Generate Music")
    output_audio = gr.Audio(label="Output Track")

    def process(genre, mood, instruments, bpm, duration):
        return generate_music(genre, mood, instruments, bpm, duration)

    generate_btn.click(process, inputs=[genre, mood, instruments, bpm, duration], outputs=output_audio)

# ✅ Needed for Render (gunicorn looks for 'app')
app = demo
