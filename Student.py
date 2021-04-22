class Student:
    # constructor
    def __init__(self, name, major, gpa, is_on_prob):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_prob = is_on_prob
    # Class functions

    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


class NewStudent(Student):

    def __init__(self, start_date, name, major, gpa, is_on_prob):
        super().__init__(name, major, gpa, is_on_prob)
        self.start_date = start_date
