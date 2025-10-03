import gradio as gr
import replicate
import os

# Load Replicate API token
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("⚠️ Missing REPLICATE_API_TOKEN in environment variables!")

# Generate music
def generate_music(prompt, duration):
    output = replicate.run(
        "facebook/musicgen:latest",
        input={
            "prompt": prompt,
            "duration": duration
        }
    )
    return output[0] if isinstance(output, list) else output

# UI
with gr.Blocks(theme="gradio/soft") as demo:
    gr.Markdown("## 🎧 NivaBand — Pro Mode")
    gr.Markdown("Write detailed prompts. More detail = better music.")

    with gr.Row():
        prompt = gr.Textbox(
            label="Your Music Idea",
            placeholder="Example: Afrobeat groove with jazzy piano, soulful horns, and electronic drums, uplifting vibe, 120 BPM",
            lines=5
        )
        duration = gr.Slider(
            label="Duration (seconds)",
            minimum=5,
            maximum=300,
            value=60,
            step=5
        )

    btn = gr.Button("🎶 Generate Music", variant="primary")
    output_audio = gr.Audio(label="Generated Track", type="filepath")
    final_prompt = gr.Textbox(label="🔍 Final Prompt Used")

    btn.click(fn=generate_music, inputs=[prompt, duration], outputs=[output_audio])
    btn.click(fn=lambda p: p, inputs=[prompt], outputs=[final_prompt])

demo.launch(server_name="0.0.0.0", server_port=7860)
