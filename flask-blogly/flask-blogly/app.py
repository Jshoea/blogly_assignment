"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db
from  flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension
connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage"""
    return redirect("/users")



@app.route('/users')
def users_index():
    """Show page with user info"""
    users =  User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)


@app.route('/users/new', methods=["GET"])
def users_new_form():
    """Page to create a user"""
    return render_template('users/new.html')

@app.route("/user/new", methods= ["POST"])
def users_new():
    """Handle form submissions"""

    new_User = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url' or None]
    )

    db.sesssion.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route('users/<int:user_id>')
def users_show(user_id):
    """Page of info on user"""

    user = User.query.get_or_404(user_id),
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit existing user info"""

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Will handle the form submission and update the existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")
    #go back to users after this

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handles the form submission to delete a user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect ("/users")




