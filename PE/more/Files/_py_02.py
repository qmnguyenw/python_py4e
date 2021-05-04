# Student class
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def to_String(self):
        return str(self.name) + '\t' + str(self.age) + '\t' + str(self.score)

# Input student list (stop when user confirms finish entering)
student_list = list()
while True:
    student_name = input("Enter student name: ")
    student_age = input("Enter student age: ")
    test_score = input("Enter test score: ")
    student = Student(student_name, student_age, test_score)
    student_list.append(student)
    finish = input("Finish? (Y/N) ")
    # Stop entering when user confirms finish entering
    if finish[0] == 'y' or finish[0] == 'Y':
        break

# Sort student list by name (ascending)
def sort_student_list(student_list):
    list_size = len(student_list)
    for i in range(list_size):
        for j in range(list_size - 1):
            if student_list[j].get_name() > student_list[j + 1].get_name():
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

def show_students(student_list):
    print("Name\tAge\tTest Score")
    for student in student_list:
        print(student.to_String())

# Print the list before & after sorting
show_students(student_list)
sort_student_list(student_list)
show_students(student_list)