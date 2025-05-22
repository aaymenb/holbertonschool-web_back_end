import express from 'express';
import fs from 'fs';

const app = express();
const PORT = 1245;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.trim().split('\n').filter(line => line.trim() !== '');
      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }
      const students = lines.slice(1).map(line => line.split(','));
      const fields = {};
      let total = 0;
      students.forEach(student => {
        if (student.length < 4) return;
        const field = student[3];
        const firstname = student[0];
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
        total += 1;
      });
      let output = `Number of students: ${total}`;
      Object.keys(fields).forEach(field => {
        output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      });
      resolve(output);
    });
  });
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  const dbPath = process.argv[2];
  try {
    const output = await countStudents(dbPath);
    res.send(`This is the list of our students\n${output}`);
  } catch (err) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(PORT);

export default app;
