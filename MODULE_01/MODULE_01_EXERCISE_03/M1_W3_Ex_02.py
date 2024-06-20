class Person:
    def __init__(self, name: str, yob: int):
        self.__name = name
        self.__yob = yob

    def get_name(self): return self.__name

    def set_name(self, new_name: str): self.__name = new_name

    def get_yob(self): return self.__yob

    def set_yob(self, new_yob: int): self.__yob = new_yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)

        self.__grade = grade

    def get_grade(self): return self.__grade

    def set_grade(self, new_grade: str): self.__grade = new_grade

    def describe(self):
        print(f"Student - Name: {self.get_name()}, YoB: {self.get_yob()}, Grade: {self.get_grade()}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)

        self.__subject = subject

    def get_subject(self): return self.__subject

    def set_subject(self, new_subject: str): self.__subject = new_subject

    def describe(self):
        print(f"Teacher - Name: {self.get_name()}, YoB: {self.get_yob()}, Subject: {self.get_subject()}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)

        self.__specialist = specialist

    def get_specialist(self): return self.__specialist

    def set_specialist(self, new_specialist): self.__specialist = new_specialist

    def describe(self):
        print(f"Doctor - Name: {self.get_name()}, YoB: {self.get_yob()}, Specialist: {self.get_specialist()}")


class Ward:
    def __init__(self):
        self.__population = []

    def get_population(self): return self.__population

    def add_person(self, person: Person):
        self.__population.append(person)

    def describe(self):
        for person in self.get_population():
            person.describe()

    def count_doctor(self):
        count = 0

        for person in self.get_population():
            if type(person) is Doctor:
                count += 1

        return count

    def sort_age(self):
        self.__population.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        yob_average = 0
        teacher_count = 0
        for person in self.get_population():
            if type(person) is Teacher:
                yob_average += person.get_yob()
                teacher_count += 1

        try: return yob_average / teacher_count
        except ZeroDivisionError: return 0


# Unit test
if __name__ == '__main__':
    ward = Ward()

    ward.add_person(person=Student(name="studentA", yob=2010, grade="7"))
    ward.add_person(person=Teacher(name="teacherA", yob=1969, subject='Math'))
    ward.add_person(person=Teacher(name="teacherB", yob=1995, subject="History"))
    ward.add_person(person=Doctor(name="doctorA", yob=1945, specialist="Endocrinologist"))
    ward.add_person(person=Doctor(name="doctorB", yob=1975, specialist="Cardiologist"))

    ward.describe()

    print(f"\nNumber of Doctor: {ward.count_doctor()}")

    ward.sort_age()
    ward.describe()

    print(f"\nAverage year of birth (teacher): {ward.compute_average()}")
