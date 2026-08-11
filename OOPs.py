
"""OOPs"""
class calculations:
    def addition(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(f"The sum of {self.num1} and {self.num2} is {self.num1 + self.num2}")

obj1=calculations()
obj1.addition(3463, 23536)
obj1.add()



"""Constructor"""

class house:
    def __init__(self, rooms, fans, ACs):
        self.num1=rooms
        self.num2=fans
        self.num3=ACs


    def add(self):
        print(f"The House will have {self.num1} rooms, {self.num2} fans and {self.num3} ACs")

obj1=house(2,7,1)
obj1.add()


"""Encapsulation"""

class Hospital:
    def __init__(self,patient,disease):
        self.patient=patient
        self.__disease=disease

    def patientdatails(self):
        print("Patient name is {self.patient} and disease is {self.disease}")   #it wont printthe disease, cuz it's private

    def whatdisease(self):
        print(self.__disease)    # to know disease

obj1=Hospital("Ali", "Diabetes")
obj1.patientdetails()
obj1.whatdisease()
