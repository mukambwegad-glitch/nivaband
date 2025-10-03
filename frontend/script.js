const API_URL = "https://nivaband.onrender.com"; // Your Render backend

document.getElementById("generate").addEventListener("click", async () => {
  const prompt = document.getElementById("prompt").value;
  const duration = document.getElementById("duration").value;
  const outputAudio = document.getElementById("output-audio");
  const finalPrompt = document.getElementById("final-prompt");

  if (!prompt) {
    alert("Please enter a music idea!");
    return;
  }

  finalPrompt.textContent = `${prompt} | Duration: ${duration}s`;

  try {
    const response = await fetch(`${API_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, duration: parseInt(duration) })
    });

    const data = await response.json();
    if (data && data.output) {
      outputAudio.src = data.output;
      outputAudio.load();
      outputAudio.play();
    } else {
      alert("Something went wrong. Try again.");
    }
  } catch (err) {
    console.error(err);
    alert("Error connecting to backend.");
  }
});
