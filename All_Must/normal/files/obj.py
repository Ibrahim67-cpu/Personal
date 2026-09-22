class Child:
    def __init__(self, name, field, marks):
        self.name = name
        self.field = field
        self.marks = marks

    def on(self):
        if self.marks >= 3.5:
            return True
        else:
            return False