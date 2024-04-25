"""Seed file to make sample data for db."""

from models import Post, User, db
from app import app

# Function to set up the database
def setup_database():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create all tables
        db.create_all()

        user1 = User(first_name="f1",last_name="l1")
        user2 = User(first_name="f2",last_name="l2")
        user3 = User(first_name="f3",last_name="l3")
        user4 = User(first_name="f4",last_name="l4")
        user5 = User(first_name="f5",last_name="l5")
        
        db.session.add_all([user1, user2, user3, user4, user5])

        db.session.commit()
        # Make a bunch of posts
        p1= Post(title='post 1',content='111',user_id=1)
        p2= Post(title=' p2',content='222',user_id=2)
        p3= Post(title='p3 ',content='333',user_id=3)
        p4= Post(title=' p4',content='444',user_id=4)
        p5= Post(title=' p5',content='555',user_id=5)
        p6= Post(title=' p6',content='6666',user_id=5)
                

        db.session.add_all([p1,p2,p3,p4,p5,p6])

        db.session.commit()

if __name__ == "__main__":
    setup_database()
