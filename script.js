document.getElementById("videoForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const prompt = document.getElementById("prompt").value;
  const voice = document.getElementById("voice").value;
  const duration = document.getElementById("duration").value;

  document.getElementById("status").innerText = "Generating video... Please wait.";

  const response = await fetch("http://localhost:5000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt, voice, duration })
  });

  const result = await response.json();

  if (result.videoUrl) {
    document.getElementById("videoResult").innerHTML = `
      <video src="${result.videoUrl}" controls width="100%"></video>
      <a href="${result.videoUrl}" download>Download Video</a>
    `;
    document.getElementById("status").innerText = "Video ready!";
  } else {
    document.getElementById("status").innerText = "Error generating video.";
  }
});