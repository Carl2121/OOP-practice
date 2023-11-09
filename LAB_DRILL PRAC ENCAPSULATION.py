class School:
    _school_name = "ABC School"

    def __init__(self,location: str):
        self.location = location
        self._staff = []
        self._student = []
        self._population = []

    def get_location(self):
        return self.location

class Student(School):
    _total_students = 0

    def __init__(self, name:str, age:int, location:str):
        super().__init__(location)
        self._name = name
        self._age = age
        Student._total_students += 1

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    @classmethod
    def get_total_students(cls):
        return cls._total_students


class Teacher(School):
    _total_teacher = 0

    def __init__(self, name:str, subject:str, location:str):
        super().__init__(location)
        self._name = name
        self._subject = subject
        Teacher._total_teacher += 1

    def get_name(self):
        return self._name
    def get_subject(self):
        return  self._subject

    @classmethod
    def get_total_teachers(cls):
        return cls._total_teacher


def add_staff_member(school, staff_member):
    school._staff.append(staff_member)

def add_student_member(school, student_member):
    school._student.append(student_member)

def add_total_population(school, population):
    school._population.append(population)


def main():
    school = School("Calamba")
    student1 = Student("David", 19, "Calamba")
    student2 = Student("Goliath", 20, "Calamba")
    student3 = Student("Sage", 20, "Mindoro")
    teacher1 = Teacher("Raiden", "Rocket Science", "Albay")
    teacher2 = Teacher("Sam", "Bladesmithing", "Miami")

    add_student_member(school, student1)
    add_student_member(school, student2)
    add_student_member(school, student3)

    add_staff_member(school, teacher1)
    add_staff_member(school, teacher2)

    add_total_population(school, student1)
    add_total_population(school, student2)
    add_total_population(school, teacher1)
    add_total_population(school, teacher2)

    print("-----------------Statistics--------------")
    print(f"School: {school._school_name} located in {school.get_location()}")
    print(f"Total students: {Student.get_total_students()}")
    print(f"Total teachers: {Teacher.get_total_teachers()}")
    print(f"Total population {Student.get_total_students() + Teacher.get_total_teachers()}")
    print("\n")
    print("----------------Names-------------------")
    print(f"Student: {[student.get_name() for student in school._student]}")
    print(f"Staff: {[staff.get_name() for staff in school._staff]}")
    print(f"Subjects taught respectively: {[staff.get_subject() for staff in school._staff]}")
    print(f"Population Names: {[population.get_name() for population in school._population]}")






if __name__ == "__main__":
    main()



