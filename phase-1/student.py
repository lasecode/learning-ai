import json

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
    
    def update_grade(self, subject):
        score = int(input('Score: '))
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

def top_bottom(avg_list):
    avg_list = sorted(avg_list)
    top = avg_list[-1]
    bottom = avg_list[0]
    return f"Top: {top}, Bottom: {bottom}"

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






        





        