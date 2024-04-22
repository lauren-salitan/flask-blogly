# from flask import Flask, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, User

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = 'secretkey'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

# connect_db(app)
# db.create_all()

# @app.route('/')
# def root():
#     return redirect("/users")

# @app.route('/users')
# def users_index():
#     users = User.query.order_by(User.last_name, User.first_name).all()
#     return render_template('users/index.html', users=users)

# @app.route('/users/new', methods=["GET"])
# def users_new_form():
#     return render_template('users/new.html')

# @app.route("/users/new", methods=["POST"])
# def users_new():
#     new_user = User(
#         first_name=request.form['first_name'],
#         last_name=request.form['last_name'],
#         image_url=request.form['image_url'] or None)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect("/users")

# @app.route('/users/<int:user_id>')
# def users_show(user_id):
#     user = User.query.get_or_404(user_id)
#     return render_template('users/show.html', user=user)

# @app.route('/users/<int:user_id>/edit')
# def users_edit(user_id):
#     user = User.query.get_or_404(user_id)
#     return render_template('users/edit.html', user=user)

# @app.route('/users/<int:user_id>/edit', methods=["POST"])
# def users_update(user_id):
#     user = User.query.get_or_404(user_id)
#     user.first_name = request.form['first_name']
#     user.last_name = request.form['last_name']
#     user.image_url = request.form['image_url']
#     db.session.add(user)
#     db.session.commit()
#     return redirect("/users")

# @app.route('/users/<int:user_id>/delete', methods=["POST"])
# def users_destroy(user_id):
#     user = User.query.get_or_404(user_id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect("/users")



# from flask import Flask, request, redirect, render_template, url_for
# from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, User

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = 'secretkey'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

# connect_db(app)
# db.create_all()

# @app.route('/')
# def home():
#     """Redirect to list of users."""
#     return redirect('/users')

# @app.route('/users')
# def users_index():
#     """Show all users."""
#     users = User.query.all()
#     return render_template('users.html', users=users)

# @app.route('/users/new', methods=['GET', 'POST'])
# def users_new():
#     if request.method == 'POST':
#         new_user = User(
#             first_name=request.form['first_name'],
#             last_name=request.form['last_name'],
#             image_url=request.form.get('image_url', User.image_url.default.arg)
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect('/users')
#     else:
#         return render_template('new_user.html')

# # Continue to add the other routes as specified in the assignment...


from flask import Flask, request, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)
# db.create_all()

@app.cli.command("create-db")
def create_db():
    """create db tables"""
    db.create_all()
    print("database tables created")
# def setup_database(app):
#     """Create database tables"""
#     with app.app_context():
#         db.create_all()

@app.route('/')
def home_redirect():
    """Redirect to list of users."""
    return redirect('/users')

@app.route('/users')
def users_index():
    """Show all users."""
    users = User.query.order_by(User.id).all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
    """Create a new user."""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        image_url = request.form['image_url'] or None
        user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    else:
        return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single user."""
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    """Edit an existing user."""
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url'] or None
        db.session.commit()
        return redirect('/users')
    else:
        return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

if __name__ == '__main__':
    setup_database(app)
    app.run(debug=True, port=5001)