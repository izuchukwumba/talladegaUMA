const express = require("express");
const app = express();
const port = 3000; // You can choose any available port

// Set up a route to serve an HTML file
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/dashboard/index.html");
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
