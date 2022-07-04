class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def grade_counter(self):
        grade_list = sum(list(self.grades.values()), [])
        avg_grade = sum(grade_list) / len(grade_list)
        return avg_grade

    def __str__(self):
        result = f'''
        Имя : {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.grade_counter()}
        Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
        Завершенные курсы: {", ".join(self.finished_courses)}
        '''
        return result

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
             return 'Это не студент!'
        return self.grade_counter() < other.grade_counter()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def grade_counter(self):
        grade_list = sum(list(self.grades.values()), [])
        avg_grade = sum(grade_list) / len(grade_list)
        return avg_grade

    def __str__(self):
        result = f''' 
        Имя : {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.grade_counter()}
        '''
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это не лектор!'
        return self.grade_counter() < other.grade_counter()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f''' 
        Имя : {self.name}
        Фамилия: {self.surname}
        '''
        return result


students_list = []
lecturer_list = []

def avg_grade_for_course(list, course):
    grade_list = []
    for student in list:
        if course in student.grades.keys():
            for keys, values in student.grades.items():
                if keys == course:
                    grade_list.extend(values)
    avg_grade = sum(grade_list) / len(grade_list)
    return avg_grade

def avg_grade_for_lecture(list, course):
    grade_list = []
    for lecturer in list:
        if course in lecturer.grades.keys():
            for keys, values in lecturer.grades.items():
                if keys == course:
                    grade_list.extend(values)
    avg_grade = sum(grade_list) / len(grade_list)
    return avg_grade

lecturer1 = Lecturer('Иван', 'Ионов')
lecturer1.courses_attached.append('История')

lecturer2 = Lecturer('Сергей', 'Ждун')
lecturer2.courses_attached.append('Математика')

student1 = Student('Вася', 'Пупкин', 'Мужчина')
student1.finished_courses.append('Психология')
student1.finished_courses.append('Аналитика')
student1.courses_in_progress.append('История')
student1.courses_in_progress.append('Математика')
student1.rate_lecture(lecturer1, 'История', 10)
student1.rate_lecture(lecturer1, 'История', 8)
student1.rate_lecture(lecturer2, 'Математика', 2)
student1.rate_lecture(lecturer2, 'Математика', 5)

student2 = Student('Катя', 'Мурина', 'Женщина')
student2.finished_courses.append('Антропология')
student2.finished_courses.append('Аналитика')
student2.courses_in_progress.append('Программирование')
student2.courses_in_progress.append('История')
student2.rate_lecture(lecturer1, 'История', 1)
student2.rate_lecture(lecturer1, 'История', 4)
student2.rate_lecture(lecturer2, 'Математика', 6)
student2.rate_lecture(lecturer2, 'Математика', 10)

reviewer1 = Reviewer('Александр', 'Бубович')
reviewer1.courses_attached.append('История')
reviewer1.courses_attached.append('Программирование')
reviewer1.rate_hw(student1, 'История', 9)
reviewer1.rate_hw(student1, 'История', 3)
reviewer1.rate_hw(student2, 'История', 4)
reviewer1.rate_hw(student2, 'Программирование', 3)
reviewer1.rate_hw(student2, 'Программирование', 6)

reviewer2 = Reviewer('Яна', 'Адамовская')
reviewer2.courses_attached.append('Математика')
reviewer2.courses_attached.append('Программирование')
reviewer2.rate_hw(student1, 'Математика', 6)
reviewer2.rate_hw(student1, 'Математика', 3)
reviewer2.rate_hw(student2, 'Программирование', 5)
reviewer2.rate_hw(student2, 'Программирование', 10)

print(student1)
print(lecturer1)
print(reviewer1)
print(avg_grade_for_course(students_list, 'Математика'))
print(avg_grade_for_lecture(lecturer_list, 'История'))
print(student1 < student2)
print(lecturer1 > lecturer2)