class Unit:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __repr__(self):
        return f'{self.value} {self.index}'

    def get_value(self):
        return int(self.value)
    def set_value(self, value):
        self.value = value

    def get_index(self):
        return int(self.index)
    def set_index(self, value):
        self.index = value
