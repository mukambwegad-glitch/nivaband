import gradio as gr
import replicate
import os

# Make sure you set your Replicate API key in environment
# export REPLICATE_API_TOKEN="your-token-here"
# On Render: add it in the Environment Variables panel

def generate_music(prompt, duration, vibe, instrument, tempo):
    # Smart enriched prompt
    final_prompt = f"{prompt}, style: {vibe}, instrument: {instrument}, tempo: {tempo} BPM"
    
    # Call replicate API (MusicGen)
    output = replicate.run(
        "facebook/musicgen:latest",
        input={
            "prompt": final_prompt,
            "duration": duration
        }
    )
    return output, final_prompt

with gr.Blocks(css="theme.css", title="NivaBand") as app:
    gr.Markdown("# 🎧 NivaBand — AI Music Composer\nCraft music with prompts, vibes, instruments, and tempo.")

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="📝 Your Music Idea")
            vibe = gr.Radio(["Cinematic","Lo-Fi","Energetic","Peaceful","Mysterious"], value="Cinematic")
            instrument = gr.Dropdown(["Piano","Guitar","Synth","Drums","Strings"], value="Synth")
            tempo = gr.Slider(60,160,90,step=5,label="Tempo BPM")
            duration = gr.Radio([5,15,30], value=15, label="Duration (sec)")
            btn = gr.Button("🎶 Generate")

        with gr.Column():
            audio = gr.Audio(label="🔊 Output Track")
            final = gr.Textbox(label="🔍 Final Prompt", interactive=False)

    btn.click(fn=generate_music, inputs=[prompt,duration,vibe,instrument,tempo], outputs=[audio,final])

app.launch(server_name="0.0.0.0", server_port=7860)
