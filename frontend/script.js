document.getElementById("music-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  const response = await fetch("https://nivaband-z8x2.onrender.com/generate", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  const outputDiv = document.getElementById("output");

  if (data.url) {
    outputDiv.innerHTML = `<p>Generated Music:</p><audio controls src="${data.url}"></audio>`;
  } else {
    outputDiv.innerHTML = `<p>Error generating music</p>`;
  }
});
