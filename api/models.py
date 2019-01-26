from api import db

class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.Unicode, index = True)
    deployment_script = db.Column(db.Text)
    env_name = db.Column(db.String)
    env_file = db.Column(db.Text)
    last_deployed = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now())
