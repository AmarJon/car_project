class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def to_string(self):
        return self.make + " " + self.model + " " + self.color

    def export_prepared_string(self):
        return [self.make, self.model, self.color]

