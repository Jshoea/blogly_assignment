"""Models for Blogly."""
from msilib.schema import Property
from flask_sqlalchemy import SQLAlchemy

db = SQLALchemy()

DEFAULT_IMAGE_URL = "https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png"

class User(db.Model):
    """User site, name and picture"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.text, nullable=FALSE)
    last_name = db.Column(db.text, nullable=FALSE)
    image_url = db.Column(db.text, nullable=FALSE, default=DEFAULT_IMAGE_URL)

    @Property
    def full_name(self):
       """returns your full name""" 
        
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """connecting this db to the flask app"""

    db.app = app
    db.init_app(app)