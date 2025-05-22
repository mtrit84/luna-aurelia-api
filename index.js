const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

const openapi = {
  openapi: "3.0.0",
  info: {
    title: "LunaProxy API",
    version: "1.0.0"
  },
  paths: {
    "/proxy": {
      get: {
        summary: "Get proxy info",
        responses: {
          "200": {
            description: "Success"
          }
        }
      }
    }
  }
};

app.get('/openapi.json', (req, res) => {
  res.json(openapi);
});

app.get('/', (req, res) => {
  res.send('LunaProxy API Hosting via ngrok is live');
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});