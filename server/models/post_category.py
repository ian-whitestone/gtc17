from server.server import db

class PostCategory(db.Model):
    __tablename__ = 'PostCategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }