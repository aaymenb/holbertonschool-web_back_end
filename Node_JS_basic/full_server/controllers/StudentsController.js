import { readDatabase } from '../utils.js';

export class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(process.argv[2]);
      const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      
      let response = 'This is the list of our students\n';
      fields.forEach(field => {
        const count = students[field].length;
        const list = students[field].join(', ');
        response += `Number of students in ${field}: ${count}. List: ${list}\n`;
      });
      
      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(process.argv[2]);
      if (!students[major]) {
        res.status(200).send('List: ');
        return;
      }
      const list = students[major].join(', ');
      res.status(200).send(`List: ${list}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
} 