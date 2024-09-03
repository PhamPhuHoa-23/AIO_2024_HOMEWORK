from M1_W3_Ex_02 import *

if __name__ == '__main__':
    stu1 = Student(name="a", yob=2010, grade=7)
    tec1 = Teacher(name="a", yob=1969, subject="M")
    tec2 = Teacher(name="b", yob=1995, subject="H")
    doc1 = Doctor(name="A", yob=1945, specialist="A")
    assert ward1.count_doctor() == 1
    doc2 = Doctor(name="b", yob=1975, specialist="nnn")
    ward1 = Ward()
    ward1.add_person(stu1)
    ward1.add_person(tec1)
    ward1.add_person(tec2)
    ward1.add_person(doc1)
    ward1.add_person(doc2)
    print(ward1.count_doctor())
