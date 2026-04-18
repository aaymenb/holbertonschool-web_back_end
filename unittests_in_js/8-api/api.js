const express = require('express');

const app = express();
const port = 7865;

// Route principale
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Lancement du serveur
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
