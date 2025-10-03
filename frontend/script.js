document.getElementById("musicForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const response = await fetch("https://your-backend.onrender.com/generate", {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  document.getElementById("output").innerHTML = `
    <h3>Generated Track:</h3>
    <audio controls src="${result.url}"></audio>
  `;
});
