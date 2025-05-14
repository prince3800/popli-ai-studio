
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

app.post("/generate", (req, res) => {
  const { prompt, voice, duration } = req.body;

  // For now, use a placeholder video. Replace with AI logic later.
  console.log("Received:", prompt, voice, duration);

  res.json({
    videoUrl: "https://www.w3schools.com/html/mov_bbb.mp4"
  });
});

app.listen(PORT, () => {
  console.log(`Popli AI Studio backend running at http://localhost:${PORT}`);
});