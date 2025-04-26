const express = require('express');
const app = express();
const path = require('path');

// Static folder set karna (public folder serve karega)
app.use(express.static(path.join(__dirname, '../public')));

// Root route ("/") ke liye index.html dikhe
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Server ko run karwana
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
