class Character:
    def __init__(self, name=None, kind=None, planet=None):
        self.name = name
        self.kind = kind
        self.planet = planet

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind

    def set_planet(self, planet):
        self.planet = planet

    def get_planet(self):
        return self.planet

    def to_string(self):
        return f'{self.name} is a(n) {self.kind} from {self.planet}'
