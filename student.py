class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {'chinese':0, 'math':0, 'english':0}

    def set_scores(self, subject, score):
        if subject in self.scores:
            self.scores[subject] = score

    def get_scores(self):
        print(f'name: {self.name.title()}, ( studentID : {self.student_id} )')
        for subject in self.scores.keys():
            print(f'subject: {subject.title()},  score: {self.scores[subject]} ')

student1 = Student('zhang san', '001')
student2 = Student('li si', '002')

student1.set_scores('chinese', 90)
student1.set_scores('math', 92)
student1.set_scores('english', 98)

student1.get_scores()