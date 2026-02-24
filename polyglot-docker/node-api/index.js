const express = require("express")
const app = express()

app.get("/health", (req, res) => {
    res.json({ service: "node", status: "ok" })
});

app.get("/info", (req, res) => {
    res.json({ language: "Node.js", runtime: process.version })
});

app.listen(3000, () => {
    console.log("Node api is running on port 3000")
});