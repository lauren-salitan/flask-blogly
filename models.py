# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.Text, nullable=False)
#     last_name = db.Column(db.Text, nullable=False)
#     image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"


# def connect_db(app):
#     db.app = app
#     db.init_app(app)

# import datetime
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# def connect_db(app):
#     """Connect to database."""
#     db.app = app
#     db.init_app(app)

# class User(db.Model):
#     """User in the blogly system."""

#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     image_url = db.Column(db.String(200), default='https://via.placeholder.com/150')

#     #posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

# ## unsure, from solution:
#     # @property
#     # def full_name(self):
#     #     """Return full name of the user."""
#     #     return f"{self.first_name} {self.last_name}"

# class Post(db.Model):
#     """Post in the blogly system"""
#     __tablename__ = 'posts'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(50), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     # created_at = db.Column(db.Date, default=db.DateTime, nullable=False, default=datetime.utcnow)
#     created_at = db.Column(db.Date, default=db.DateTime, nullable=False)
# #   created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
# #   creator_code = db.Column(db.Text, db.ForeignKey('creators.creator_code'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# #     @property
# #     def friendly_date(self):
# #         """Return nicely-formatted date."""
# #         return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

# #     creator = db.relationship('creator', backref='post')
#     user = db.relationship('User', backref=db.backref('posts', lazy=True))

from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User in the blogly system."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), default='https://via.placeholder.com/150')

class Post(db.Model):
    """Post in the blogly system"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.Date, default=db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    tags = db.relationship('Tag', secondary='post_tags', backref='posts')

class Tag(db.Model):
    """Tag that can be added to posts"""
    __tablename__ = 'tags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class PostTag(db.Model):
    """Association table between posts and tags"""
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
