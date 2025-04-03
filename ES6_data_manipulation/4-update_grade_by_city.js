export default function updateStudentGradeByCity(studentlist, city, newgrade) {
  return studentlist
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newgrade.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
