class calculations:
    def addition(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(f"The sum of {self.num1} and {self.num2} is {self.num1 + self.num2}")

obj1=calculations()
obj1.addition(3463, 23536)
obj1.add()