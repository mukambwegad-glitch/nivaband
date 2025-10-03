from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import replicate
import os
from utils import build_prompt

app = FastAPI()

# Allow frontend (Vercel) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
