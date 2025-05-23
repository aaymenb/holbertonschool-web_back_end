const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];
  res.write('This is the list of our students\n');

  countStudents(database)
    .then((output) => {
      res.end(output);
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(1245);

module.exports = app;