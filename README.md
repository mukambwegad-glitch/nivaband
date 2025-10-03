# 🎵 NivaBand — AI Music Composer

NivaBand is an AI-powered music generator that composes **cinematic, emotional, and genre-rich tracks**.  
Users can choose **genre, mood, instruments, BPM, and extra notes** to create **original AI music** in seconds.  

---

## 🚀 How It Works
1. **Frontend (Vercel)** → Users interact with a clean UI to select genre, mood, and musical details.  
2. **Backend (Render)** → A **FastAPI server** connects to **Replicate’s MusicGen model**.  
3. **Replicate API** → Generates a playable audio track from your prompt.  
4. **Response** → The app returns an **audio URL** you can play instantly in the browser.  

---

## 🔧 Setup & Deployment

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nivaband.git
cd nivaband
