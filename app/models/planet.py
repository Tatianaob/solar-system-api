from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    number_of_moons = db.Column(db.Integer)

    def to_dict(self):
        return {"name": self.name, "description": self.description, "number_of_moons": self.number_of_moons}