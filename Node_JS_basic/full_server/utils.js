import fs from 'fs';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = {};
      
      // Skip header line
      for (let i = 1; i < lines.length; i++) {
        const [firstname, , , field] = lines[i].split(',');
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }

      // Sort students in each field
      Object.keys(students).forEach(field => {
        students[field].sort();
      });

      resolve(students);
    });
  });
}; 