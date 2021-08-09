# class Student():
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lect, course, grade):
        if isinstance(lect, Lecturer) and course in lect.courses_attached and course in self.courses_in_progress:
            if course in lect.grades:
                lect.grades[course] += [grade]
            else:
                lect.grades[course] = [grade]
        else:
            print('Ошибка')
            # return 'Ошибка'

    def __str__(self):
        average = {k:sum(x)/len(x) for k,x in self.grades.items()}
        res: str = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания: {average}\n' \
                   f'Курсы в процессе обучения: {self.courses_in_progress}\n' \
                   f'Завершенные курсы: {self.finished_courses}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average = {k: sum(x) / len(x) for k, x in self.grades.items()}
        res: str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res




# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(new_student, 'SQL', 10)




lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ["Python"]
lecturer.courses_attached += ["Git"]

lecturer2 = Lecturer('Some2', 'Buddy2')
lecturer2.courses_attached += ["Python"]
lecturer2.courses_attached += ["Git"]

new_student = Student('Student', 'One', 'Gender')
new_student.courses_in_progress += ["Python", "Git"]
new_student.finished_courses += ["Введение в программирование"]
new_student.rate_lecturer(lecturer, 'Python', 9)
new_student.rate_lecturer(lecturer, 'Git', 10)
new_student.rate_lecturer(lecturer2, 'Python', 6)
new_student.rate_lecturer(lecturer2, 'Git', 7)
# lecturer.rate_hw(new_student, "Python", 8)
new_student2 = Student('Second', 'Two', 'Gender')
new_student2.courses_in_progress += ["Python", "Git"]
new_student2.rate_lecturer(lecturer, 'Python', 9)
new_student2.rate_lecturer(lecturer, 'Git', 10)
new_student2.rate_lecturer(lecturer2, 'Python', 6)
new_student2.rate_lecturer(lecturer2, 'Git', 7)



reviewer = Reviewer("Tim", "Broccoli")
reviewer.courses_attached += ["Python", "Git"]
reviewer.rate_hw(new_student, "Python", 5)
reviewer.rate_hw(new_student, "Git", 8)

reviewer2 = Reviewer("Alex", "li")
reviewer2.courses_attached += ["Python", "Git"]
reviewer2.rate_hw(new_student2, "Python", 10)
reviewer2.rate_hw(new_student2, "Git", 7)




print(reviewer)
print(lecturer)
print(new_student)





