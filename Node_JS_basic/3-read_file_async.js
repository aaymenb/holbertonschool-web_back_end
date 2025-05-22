const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const lines = data.trim().split('\n');

    lines.shift();

    const studentsByField = {};

    let totalStudents = 0;

    for (const line of lines) {
      const fields = line.split(',');
      if (fields.length === 4) {
        const firstName = fields[0].trim();
        const field = fields[3].trim();

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }

        studentsByField[field].push(firstName);
        totalStudents += 1;
      }
    }

    console.log(`Number of students: ${totalStudents}`);

    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const students = studentsByField[field];
        console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
      }
    }

    return Promise.resolve();
  } catch (err) {
    return Promise.reject(new Error('Cannot load the database'));
  }
}

module.exports = countStudents;
