from datetime import datetime
import pytz #to make it time-Zone aware
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader #@ for specifying a decorater 
def load_user(user_id):
    return User.query.get(int(user_id))


#creating user model
class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default = 'default.jpg') #we will later hash the images files
    password= db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post',backref='author', lazy=True) #posts attribute has a relationship to the Post model, backref helps to provide the user who wrote the post, 'lazy' sql alchemy loads the data in one go
                                                              #it is a reltionship not a coloumn
    
    
    def get_reset_token(self,expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod #telling python not to expect 'self' as an argument
    def verify_reset_token(token):
         s = Serializer(current_app.config['SECRET_KEY'])
         try:
             user_id = s.loads(token)['user_id']
         except:
             return None
         return User.query.get('user_id')
    
    def __repr__(self): #defining how user obj will look on printing
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model): 
    id =db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=lambda: datetime.now(pytz.utc))
    content =db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self): 
        return f"Post('{self.title}','{self.date_posted}')"
 