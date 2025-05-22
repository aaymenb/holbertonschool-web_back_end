const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  countStudents(databasePath)
    .then(() => {
      res.status(200).send('This is the list of our students');
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
