# 🎧 NivaBand — Infinite AI Music Studio

NivaBand is the **GarageBand of AI**, blending:
- 🎼 Free-text prompts
- 🎹 Optional chord input
- 🎨 Custom vibes, instruments, durations
- 🚀 Full-stack app (FastAPI + React)

---

## 🛠 Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn api:app --reload --port 8000

# Frontend
cd frontend
npm install
npm start
