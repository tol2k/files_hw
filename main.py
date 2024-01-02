class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def avg_mark(self,grades):
        summ = 0
        counter = 0
        for i in grades.values():
            summ+= sum
            counter += len(i)
        return round(summ/counter,1)




    def __str__(self,name,surname,avg_mark,courses_in_progress,finished_courses,grades):
        return f"Имя: {name}\nФамилия: {surname}\nСредняя оценка за домашние задания: {avg_mark(grades)}\nКурсы в процессе изучения: {' '.join(courses_in_progress)}\nЗавершенные курсы:: {' '.join(finished_courses)}"




    def __gt__(self,other):
        return self.avg_mark() > other.avg_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.rating = {}
    def rate_from_st(self,course,mark,rating):
        if course not in rating.keys():
            rating[course] = []
            rating[course].append(mark)
    def avg_rate(self,rating):
        summ = 0
        counter = 0
        for i in rating.values():
            summ+= sum
            counter += len(i)
        return round(summ/counter,1)

    def __str__(self,name,surname,rating):
        return f"Имя: {name}\nФамилия: {surname}\nСредняя оценка за лекции: {self.avg_rate(rating)}"


    def __gt__(self,other):
        return self.avg_rate() > other.avg_rate()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self,name,surname):
        return f"Имя: {name}\nФамилия: {surname}"

def avg_mark_course(students,course):
    counter = 0
    summ = 0
    for std in students:
        if course in std.courses_in_progress():
            summ += std.avg_mark()
            counter += 1
    return round(summ/counter,1)

def avg_mark_course(lectors,course):
    counter = 0
    summ = 0
    for lct in lectors:
        if course in lct.courses_attached():
            summ += lct.avg_mark()
            counter += 1
    return round(summ/counter,1)

# tolya = Student('tolya','kokhno','male')
# tolya.courses_in_progress +=['python']
#
# alex = Lecturer('alex','kokhno')
# alex.courses_attached += ['Python']
#
# vika = Reviewer('vika','kokhno')
# vika.courses_attached += ['Python']








