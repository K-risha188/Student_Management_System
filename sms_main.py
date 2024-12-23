import random
from tabulate import tabulate

listOfStudents = []
listOfCourses = []
listOfTeachers = []

class Student:
    def __init__(self,name,email,phone, address,course):
     self.student_id = random.randint(1,1000000)
     self.name = name
     self.email = email
     self.phone = phone
     self.address = address
     self.course = course

class Teacher:
    def __init__(self,name,email,phone,address,course):
     self.teacher_id = random.randint(1,1000000)
     self.name = name
     self.email = email
     self.phone = phone
     self.address = address
     self.course = course

class Course:
    def __init__(self, course_name, course_description):
      self.course_id = random.randint(1,1000)
      self.course_name = course_name
      self.course_description = course_description

class SchoolManagementSystem:

    def __init__(self):
        pass

    #validates the id and returns "false" if the same id exists in the database.
    def validate_id(self, entity_type, entity_id):
      if entity_type=='Student': # Validates Student_ID
          if entity_id in listOfStudents:
              return False
          else :
              return True

      elif entity_type=='Teacher': #Validates Teacher_ID
          if entity_id in listOfTeachers:
              return False
          else :
              return True

      elif entity_type=='Course': #Validates Course_ID
          if entity_id in listOfCourses:
              return False
          else :
              return True

    # Adds Student to the database(ListOfStudents)
    def add_student(self, student_id, name, email, phone, add,course):
        if self.validate_id('Student',student_id):
            listOfStudents.append([student_id,name,email,phone,add,course])

    # Adds Teacher to the database(ListOfTeachers)
    def add_teacher(self, teacher_id, name, email, phone, add,course):
        if self.validate_id('Teacher', teacher_id):
            listOfTeachers.append([teacher_id, name, email, phone, add,course])

    #Adds Course to the database(ListOfCourses)
    def add_course(self,course_id,course_name,course_description):
        if self.validate_id('Course', course_id):
               listOfCourses.append([course_id, course_name, course_description])

    #Displays details from the database as per the requirements of the user
    def display_details(self,entity_type,entity_id):
        if entity_type == 'Student' and entity_id == 1:
            row = ["Student ID","Name","Email","Phone","Address","Course"]
            print("\n")
            print(tabulate(listOfStudents,headers=row,tablefmt="grid"))
            self.main_code()

        elif entity_type == 'Teacher' and entity_id == 1:
            row = ["Teacher ID", "Name", "Email", "Phone", "Address", "Course"]
            print("\n")
            print(tabulate(listOfTeachers, headers=row, tablefmt="grid"))
            self.main_code()

        elif entity_type == 'Course' and entity_id == 1:
            row = ["Course ID", "Course Name", "Description"]
            print("\n")
            print(tabulate(listOfCourses, headers=row, tablefmt="grid"))
            self.main_code()

        else:
            target = entity_id
            if entity_type =='Student':
                for i in listOfStudents:
                  if i[0] == target:
                    row = ["Student ID", "Name", "Email", "Phone", "Address", "Course"]
                    print("\n")
                    print(tabulate([i],headers = row,tablefmt="grid"))
                    break

                  else:
                   print("Not Found. :(")
                self.main_code()

            elif entity_type =='Teacher':
                for i in listOfTeachers:
                  if i[0] == target:
                     row = ["Teacher ID", "Name", "Email", "Phone", "Address", "Course"]
                     print("\n")
                     print(tabulate([i],headers = row,tablefmt="grid"))
                     break

                  else:
                   print("Not Found. :(")
                self.main_code()

            elif entity_type =='Course':
                for i in listOfCourses:
                  if i[0] == target:
                     row = ["Course ID", "Course Name", "Description"]
                     print("\n")
                     print(tabulate([i],headers = row,tablefmt="grid"))
                     break

                  else:
                   print("Not Found. :(")
                self.main_code()

    def delete_by_id(self,entity_type,entity_id):

        if entity_type == 'Student':
          id_to_delete = entity_id
          listOfStudents[:] = [inner_list for inner_list in listOfStudents if inner_list[0] != id_to_delete]
          row = ["ID", "Name","Email","phone","Address","Course"]
          print(tabulate(listOfStudents,headers = row,tablefmt="grid"))
          print("Student data of id", entity_id,"has been deleted successfully.")

        elif entity_type == 'Teacher':
          id_to_delete = entity_id
          listOfTeachers[:] = [inner_list for inner_list in listOfTeachers if inner_list[0] != id_to_delete]
          row = ["ID", "Name","Email","phone","Address","Course"]
          print(tabulate(listOfTeachers,headers = row,tablefmt="grid"))
          print("Teacher data of id", entity_id, "has been deleted successfully.")

        else :
          id_to_delete = entity_id
          listOfCourses[:] = [inner_list for inner_list in listOfCourses if inner_list[0] != id_to_delete]
          row = ["ID", "Course Name", "Description"]
          print(tabulate(listOfCourses, headers=row, tablefmt="grid"))
          print("Course data of id", entity_id, "has been deleted successfully.")
        self.main_code()


    def main_code(self):
     print("\nOpt from the following options : \n1.Student Entry\n2.Teacher Entry\n3.Course Entry\n4.Display Details.\n5.Delete Details.\n6.Exit ")
     choice = int(input("Enter your choice here : "))

     if choice == 1:
          print("\n                                            ----------𝙁𝙞𝙡𝙡 𝙞𝙣 𝙩𝙝𝙚 𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘿𝙚𝙩𝙖𝙞𝙡𝙨----------")
          student = Student(input("Name : "),input("Email : "), int(input("Phone : ")), input("Address : "),input("Course opted : "))
          sms.add_student(student.student_id,student.name,student.email,student.phone,student.address,student.course)
          print("Student entry is successful. Student id is",student.student_id)
          self.main_code()

     elif choice == 2:
          print("\n                                            ----------𝙁𝙞𝙡𝙡 𝙞𝙣 𝙩𝙝𝙚 𝙏𝙚𝙖𝙘𝙝𝙚𝙧 𝘿𝙚𝙩𝙖𝙞𝙡𝙨:----------")
          teacher = Teacher(input("Name : "), input("Email : "), int(input("Phone : ")), input("Address : "),input("Course Enrolled in : "))
          sms.add_teacher(teacher.teacher_id, teacher.name, teacher.email, teacher.phone, teacher.address,teacher.course)
          print("Teacher entry is successful. Teacher id is",teacher.teacher_id)
          self.main_code()


     elif choice == 3:
          print("\n                                            ----------𝙁𝙞𝙡𝙡 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙪𝙧𝙨𝙚 𝘿𝙚𝙩𝙖𝙞𝙡𝙨----------")
          print("\nChoose from the following : \n1.Computer Science Engineering  2.Chemical Engineering  3.Mechanical Engineering  4.Civil Engineering")
          course = Course(input("Course Name : "),input("Brief Course Description : "))
          sms.add_course(course.course_id,course.course_name,course.course_description)
          print("Course entry is successful. Course id is",course.course_id)
          self.main_code()

     elif choice == 4:
         print(
             "\n1.Display Student details.\n2.Display Teacher Details.\n3.Display Course details.\n4.Exit.")
         a = int(input("Enter your choice here : "))

         if a == 1:
             s = int(input("Type '1' for printing all student details or else type student's id : "))
             self.display_details('Student',s)

         if a == 2:
             s = int(input("Type '1' for printing all teacher details or else type teacher's id : "))
             self.display_details('Teacher',s)

         if a == 3:
             s = int(input("Type '1' for printing all course details or else type course id : "))
             self.display_details('Course',s)

         if a == 4:
             exit(0)

     elif choice == 5:
         print("1.Delete Student by id.\n2.Delete Teacher details by id.\n3.Delete Course Details by id.\n4.Exit ")
         choice = int(input("Enter your choice here : "))

         if choice == 1:
            id_1 = int(input("Enter your Student ID :"))
            self.delete_by_id('Student',id_1)

         elif choice == 2:
            id_1 = int(input("Enter your Teacher ID :"))
            self.delete_by_id('Teacher',id_1)

         elif choice == 3:
            id_1 = int(input("Enter your Course ID :"))
            self.delete_by_id('Course',id_1)

         else:
             exit(0)

     else :
         exit(0)

if __name__ == "__main__":
    sms = SchoolManagementSystem()
    print(" \n                                    ...................SCHOOL MANAGEMENT SYSTEM...................")
    sms.main_code()
