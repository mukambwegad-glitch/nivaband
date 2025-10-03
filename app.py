import os
import gradio as gr
import replicate

def generate_music(prompt, genre, mood, instruments, tempo, chords, duration):
    final_prompt = f"{genre} {mood} with {instruments}, tempo {tempo} BPM, chords: {chords}. {prompt}"
    output = replicate.run(
        "facebook/musicgen:latest",
        input={"prompt": final_prompt, "duration": duration}
    )
    return output

iface = gr.Interface(
    fn=generate_music,
    inputs=[
        gr.Textbox(label="Your Music Idea"),
        gr.Radio(["Cinematic", "Lo-Fi", "Energetic", "Peaceful", "Mysterious"], label="Mood"),
        gr.Dropdown(["Piano", "Guitar", "Synth", "Drums"], label="Instruments"),
        gr.Slider(60, 200, value=90, step=1, label="Tempo BPM"),
        gr.Textbox(label="Optional Chords/Melody"),
        gr.Radio([5, 15, 30], label="Duration (sec)", value=15),
    ],
    outputs="audio",
    title="🎧 NivaBand — AI Music Composer"
)

# 🔑 Render fix: bind to the right port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    iface.launch(server_name="0.0.0.0", server_port=port)
