from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    size = db.Column(db.String, nullable = False)

    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            size=self.size
            )