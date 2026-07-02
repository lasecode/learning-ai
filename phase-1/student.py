import json
import csv

class Student:
    def __init__(self, name, stud_id,):
        self.name = name
        self.stud_id = stud_id
        self.subject_score = {}

    def __str__(self):
        return f'{self.name} \n {self.stud_id} \n {self.subject_score}'
    

    def add_grade(self, subject, score):
        self.subject_score[subject] = score
        print("Grade created")
    
    def update_grade(self, subject, score):
        if subject in self.subject_score:
            self.subject_score.update({subject:score})
            print("Grade updated")
        else:
            print("Subject Does not exist")
    
    def remove_grade(self, subject):
        if subject in self.subject_score:
            self.subject_score.pop(subject)
            print("Grade deleted")
        else: 
            print("Subject does not exist")
    
    def average_calculation(self):
        try:
            total = 0
            for value in self.subject_score.values():
                total += int(value)
            average = total/int(len(self.subject_score))
            return average
        except ZeroDivisionError:
            print("No scores")

def top_bottom(students):
    pairs = []
    for student in students.values():
        avg = student.average_calculation()
        pairs.append((avg, student.name))
    pairs = sorted(pairs)
    bottom = pairs[0]
    top = pairs[-1]
    return f"Top: {top[1]} - {top[0]}, Bottom: {bottom[1]} - {bottom[0]}"

def save(student):
        filename = f"{student.stud_id}.json"
        with open(filename, 'w') as f:
            json.dump(student.subject_score, f)

def load(student):
        try:
            filename = f"{student.stud_id}.json"
            with open(filename, 'r') as f:
                scores = json.load(f)
            student.subject_score = scores
        except FileNotFoundError:
            print("File not found")

def export_csv(students_file):
    details = []
    for student in students_file.values():
        name = student.name
        id = student.stud_id
        scores = student.subject_score
        details.append({'name':name, 'id': id, 'scores':scores})
    with open('file.csv', 'w', newline='') as f:
        fieldnames = ['name', 'id', 'scores']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writeheader() 
        writer.writerows(details) 
        

def main():
    students = {}

    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Create Student")
        print("2. View All Students")
        print("3. Add Grade")
        print("4. Update Grade")
        print("5. Remove Grade")
        print("6. View Student Grades")
        print("7. Top/Bottom Performers")
        print("8. Export to CSV")
        print("9. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            name = input("name: ")
            stud_id = input("id: ")
            student = Student(name, stud_id)
            students[stud_id] = student
            save(student)
        elif option == "2":
            for key,value in students.items():
                print(f'Id: {key}, {value}')
        elif option == "3":
            stud_id = input("ID: ")
            if stud_id in students:
                subject = input('Subject: ')
                score = int(input("Score: "))
                students[stud_id].add_grade(subject, score)
                save(students[stud_id])
            else:
                print("Id not found")
        elif option == "4":
            stud_id = input("ID: ")
            if stud_id in students:
                subject = input('Subject: ')
                score = int(input("Score: "))
                students[stud_id].update_grade(subject, score)
                save(students[stud_id])
            else:
                print("Id not found")
        elif option == "5":
            stud_id = input("ID: ")
            if stud_id in students:
                subject = input('Subject: ')
                students[stud_id].remove_grade(subject)
                save(students[stud_id])
            else:
                print("Id not found")
        elif option == "6":
            stud_id = input("ID: ")
            if stud_id in students:
                load(students[stud_id])
                for index, (key, value) in enumerate(students[stud_id].subject_score.items()):
                    print(f"Index: {index} | Subject: {key} | Score: {value}")
            else:
                print("Id not found")
        elif option == "7":
            performance = top_bottom(students)
            print(performance)
        elif option == "8":
            export_csv(students)
            print("Exported")
        elif option == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

main()






        





        