from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import replicate
from utils import build_prompt

app = FastAPI()

# Allow frontend to connect (adjust allow_origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "NivaBand backend is live!"}

@app.post("/generate")
async def generate_music(
    genre: str = Form(...),
    mood: str = Form(...),
    instruments: str = Form(""),
    bpm: int = Form(120),
    duration: int = Form(30),
    notes: str = Form("")
):
    prompt = build_prompt(genre, mood, instruments, bpm, duration, notes)

    output = replicate.run(
        "riffusion/riffusion:latest",
        input={"prompt_a": prompt}
    )

    return {"url": output[0]}
