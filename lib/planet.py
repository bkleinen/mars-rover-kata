from lib.rover import World


class Planet(World):
    def next(self, rover_state, command):
        if not self.on_pole():
            return super().next(rover_state, command)
    
    def on_pole(self):
        return False
