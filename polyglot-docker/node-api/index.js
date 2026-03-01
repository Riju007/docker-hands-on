const express = require("express")
const app = express()

function logJson(level, message, extra = {}) {
    const log = {
        "service": "node",
        level,
        message,
        timestamp: new Date().toISOString(),
        ...extra
    }
    console.log(JSON.stringify(log));
}

app.get("/health", (req, res) => {
    logJson("info", "health check called");
    res.json({ service: "node", status: "ok" });
});

app.get("/info", (req, res) => {
    res.json({ language: "Node.js", runtime: process.version });
});

app.listen(3000, () => {
    console.log("Node api is running on port 3000");
});