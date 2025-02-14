import pickle
from student import Student

# creez un obiect
obiect_de_tip_student = Student("George")

with open("student.pkl", "wb") as file_writer:
    pickle.dump(obiect_de_tip_student, file_writer)