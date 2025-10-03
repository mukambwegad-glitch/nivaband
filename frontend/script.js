const form = document.getElementById("musicForm");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const audioPlayer = document.getElementById("audioPlayer");

// Backend API (Render)
const API_URL = "https://nivaband.onrender.com/generate";

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    genre: document.getElementById("genre").value,
    mood: document.getElementById("mood").value,
    instruments: document.getElementById("instruments").value,
    bpm: parseInt(document.getElementById("bpm").value),
    duration: parseInt(document.getElementById("duration").value),
    extra_notes: document.getElementById("extra_notes").value
  };

  loading.classList.remove("hidden");
  result.classList.add("hidden");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const resultData = await response.json();

    if (resultData.audio_url) {
      audioPlayer.src = resultData.audio_url;
      result.classList.remove("hidden");
    } else {
      alert("No audio was generated.");
    }
  } catch (err) {
    alert("Failed to generate music. Check API or token.");
    console.error(err);
  } finally {
    loading.classList.add("hidden");
  }
});
