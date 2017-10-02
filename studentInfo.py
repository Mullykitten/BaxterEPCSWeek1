import random

def main():
    students = [
    Student("Halsted","Larsson", 37),
    Student("John","BonJovi", 55),
    Student("Kathryn","Coombs", 16),
    Student("Tucker","Brooks", 16),
    Student("Al","Paccino", 78),
    Student("Heather", "Duke", 17),
    Student("Ben","Kiesel", 37),
    Student("Clark","Kent", 42),
    Student("Elijah","Booker", 18),
    Student("Star","Lord", 37),

    randomfirstName =[
"Olivia",
"Cora",
"Isla",
"Charlotte",
"Khaleesi",
"Amelia",
"Isabella",
"Aurora",
"Amara",
"Audrey",
"Penelope",
"Luna",
"Genevieve",
"Imogen",
"Rose",
"Ava",
"Hazel",
"Violet",
"Thea",
"Ophelia",
"Eleanor",
"Arabella",
"Esme",
"Adeline",
"Alice",
"Emilia",
"Ada",
"Maeve",
"Evelyn",
"Aurelia",
"Elizabeth",
"Jane",
"Eloise",
"Stella",
"Lucy",
"Julia",
"Emma",
"Claire",
"Lila",
"Iris",
"Ivy",
"Nora",
"Elise",
"Naomi",
"Astrid",
"Lydia",
"Anna",
"Atticus",
"Harvey",
"Bodhi",
"Asher",
"Jack",
"Milo",
"Jasper",
"Theodore",
"Oliver",
"Henry",
"Silas",
"Oscar",
"Leo",
"Declan",
"Kai",
"Xavier",
"Axel",
"Felix",
"Wyatt",
"Thomas",
"Levi",
"Finn",
"Sebastian",
"Julian",
"Ethan",
"Soren",
"Benjamin",
"Arthur",
"James",
"Caleb",
"Matthew",
"Liam",
"Aryan",
"William",
"Miles",
"Elijah",
"Callum",
"Ryker",
"Ezra",
"Zachary",
"Tobias",
"Alexander",
"John",
"Eli",
"Jude",
"Cassius",
"Harry",
]

    randomlastName = [
"Smith",
"Johnson",
"Williams",
"Jones",
"Brown",
"Davis",
"Miller",
"Wilson",
"Moore",
"Taylor",
"Anderson",
"Thomas",
"Jackson",
"White",
"Harris",
"Martin",
"Thompson",
"Garcia",
"Martinez",
"Robinson",
"Clark",
"Rodriguez",
"Lewis",
"Lee",
"Walker",
"Hall",
"Allen",
"Young",
"Hernandez",
"King',
"Wright",
"Lopez",
"Hill",
"Scott",
"Green",
"Adams",
"Baker",
"Gonzalez",
"Nelson",
"Carter",
"Mitchell",
"Perez",
"Roberts",
"Turner",
"Phillips",
"Campbell",
"Parker",
"Evans",
"Edwards",
"Collins",
]


  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  else:
    print ("SELECTION NOT RECOGNIZED")


class Student:
  def __init__(self,firstName, lastName, age):
    self.lastName = random.choice
    self.age = random.choice
    self.firstName = random.choice

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  print (inputQuestions[4])
  return input("Type selection and press enter:")

def printHeader():
    print("STUDENT INFO")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByLName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByFName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()
