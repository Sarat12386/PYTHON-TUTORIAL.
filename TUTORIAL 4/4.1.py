class afit:
    def read(self):
        self.f = float(input("First number: "))
        self.s = float(input("Second number: "))
    def add(self):
        return self.f + self.s
obj = afit()
obj.read()
print("Sum:", obj.add())
