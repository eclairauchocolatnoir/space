class Healthbar(object):
    def __init__(self, owner, unit_character="█", blank_unit_character="░", max_length=50):
        self.owner = owner
        self.unit = unit_character
        self.max_length = max_length
        self.blank_unit_character = blank_unit_character
        self.amount = lambda: int((((100 * owner.health) / owner.health_max) / 100) * max_length)

    def __repr__(self):
        return "HP {}{}|{}".format(self.owner.name.upper(), (20 - len(self.owner.name)) * " ", self.unit * self.amount() + (self.max_length - self.amount()) * self.blank_unit_character)