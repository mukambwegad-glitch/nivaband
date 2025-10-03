# 🎵 NivaBand — AI Music Composer

NivaBand is an AI-powered music generator that creates original compositions
based on genre, mood, instruments, BPM, and extra notes.

## 🚀 How It Works
- **Frontend (Vercel)** → User inputs (genre, mood, etc.)
- **Backend (Render)** → FastAPI + Replicate generates music
- Returns playable audio file

## 🔧 Setup
1. Clone this repo.
2. Add your Replicate API key in Render Environment:
   - Key: `REPLICATE_API_TOKEN`
   - Value: `r8_XXXXXXXXXXXXXXXXXXXXXXXX`
3. Deploy backend on **Render**.
4. Deploy frontend (your `/frontend` folder) on **Vercel**.
5. Update `script.js` → replace `https://your-backend.onrender.com` with your actual backend URL.

## ⚡ Example Prompt
A cinematic anthem fused with deep atmospheric bass, tribal drums, and ethereal synths.

## 🖥️ Tech Stack
- **Backend**: FastAPI, Uvicorn, Replicate
- **Frontend**: Vercel (static hosting)
