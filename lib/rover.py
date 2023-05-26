class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y

    def execute(self, command):
        if "f" == command:
            self.y += 1
        else:
            self.y -= 1
        pass

    def position(self):
        return self.x, self.y