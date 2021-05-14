import sqlite3

#connect
conn = sqlite3.connect("student.sqlite")

cur = conn.cursor()

#find students who failed in atleast 1 subject
def get_failed_students():
  cur.execute("SELECT name,COUNT(Subjects.subject) FROM Students INNER JOIN Subjects ON Students.id = Subjects.id WHERE Subjects.grade = 'E' OR Subjects.grade = 'F' GROUP BY Students.id")
  cur_tuple = tuple(cur)
  if len(cur_tuple) > 0:
   return cur_tuple
  else:
      return -1

#find students who had A in all subjects
def get_student_with_all_As():
    cur.execute("SELECT name FROM Students INNER JOIN Subjects ON Students.id = Subjects .id WHERE grade = 'A' GROUP BY name HAVING count(name) = 3")
    cur_tuple = tuple(cur)
    if len(cur_tuple) > 0:
     return cur_tuple
    else:
        return -1

#find most A subject
def get_subject_with_most_As():
    cur.execute("SELECT subject FROM Subjects WHERE grade = 'A' GROUP BY subject ORDER BY count(subject) DESC")
    cur_tuple = tuple(cur)
    if len(cur_tuple) > 0:
     subject = cur_tuple[0][0]
     return subject
    else:
        return -1

if __name__ == "__main__":
  print(get_student_with_all_As())