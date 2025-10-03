document.getElementById("generateBtn").addEventListener("click", async () => {
    const prompt = document.getElementById("promptInput").value;
    const duration = document.getElementById("durationSelect").value;

    const response = await fetch("https://nivaband.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt: prompt,
            duration: parseInt(duration)
        })
    });

    const result = await response.json();

    if (result.status === "success") {
        const audioPlayer = document.getElementById("outputTrack");
        audioPlayer.src = result.audio_url;
        audioPlayer.style.display = "block";
        audioPlayer.play();
    } else {
        alert("Error: " + result.message);
    }
});
