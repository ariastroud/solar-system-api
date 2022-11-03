from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    size = db.Column(db.String, nullable = False)

    @classmethod
    def from_dict(cls, planet_data):
        return Planet(name=planet_data["name"],
                    description=planet_data["description"],
                    size=planet_data["size"]
        )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            size=self.size
        )