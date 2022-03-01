from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    role = db.Column(db.String(120))
    avatar = db.Column(db.String(120))
    auth_token = db.Column(db.String(250))
    provider = db.Column(db.String(80))
    def __repr__(self):
        return '<User %r>' % self.username  
    
    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    def to_dict(self):
        user = {
            'id':self.id,
            'email':self.email,
            'role':self.role,
            'username':self.username,
            'avatar':self.avatar
        }
        return user

    def save(self):
        db.session.add(self)
        db.session.commit()
