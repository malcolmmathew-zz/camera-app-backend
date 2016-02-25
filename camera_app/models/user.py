from app import db

class User(db.Model):
	__tablename__ = 'user'
	id = db.column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), index=True, nullable=False)
	#groups = db.relationship('Group', secondary=group_relationship_table, backref='users')

	def __repr__(self):
		return 'User: %r' % self.name