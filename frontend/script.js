document.getElementById("musicForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const genre = document.getElementById("genre").value;
  const mood = document.getElementById("mood").value;
  const instruments = document.getElementById("instruments").value;
  const bpm = document.getElementById("bpm").value;
  const duration = document.getElementById("duration").value;
  const extra_notes = document.getElementById("extra_notes").value;

  const response = await fetch("https://nivaband.onrender.com/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ genre, mood, instruments, bpm, duration, extra_notes })
  });

  const data = await response.json();
  document.getElementById("outputAudio").src = data.audio_url;
});
