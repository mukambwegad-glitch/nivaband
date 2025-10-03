async function generateMusic() {
  const genre = document.getElementById("genre").value;
  const mood = document.getElementById("mood").value;
  const instruments = document.getElementById("instruments").value;
  const bpm = document.getElementById("bpm").value;
  const duration = document.getElementById("duration").value;

  const response = await fetch("https://nivaband.onrender.com", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ genre, mood, instruments, bpm, duration })
  });

  const data = await response.json();

  if (data && data[0]) {
    document.getElementById("output").src = data[0];
  } else {
    alert("Error: No music generated.");
  }
}
