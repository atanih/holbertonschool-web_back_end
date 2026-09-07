import readDatabase from '../utils';

function resolveDatabasePath() {
  const args = process.argv.slice(2);
  let skipNext = false;

  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];

    if (skipNext) {
      skipNext = false;
    } else if (arg.startsWith('-')) {
      skipNext = true;
    } else if (!arg.endsWith('.test.js') && !arg.includes('mocha')) {
      return arg;
    }
  }

  return 'database.csv';
}

export default class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(resolveDatabasePath())
      .then((fields) => {
        const lines = ['This is the list of our students'];
        const sorted = Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        sorted.forEach((field) => {
          const list = fields[field];
          lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        });

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(resolveDatabasePath())
      .then((fields) => {
        const list = fields[major] || [];
        response.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}
