from flask import Flask
from flask_marshmallow import Marshmallow
from your_orm import Column, DateTime, Model, String, Integer
# ORM is high level abstraction over RDMS that allows to perform CRUD operations using python

app = Flask(__name__)
ma = Marshmallow(app)

class User(Model):
    email = Column(String)
    password = Column(String)
    date = Column(DateTime, auto_now_add = True)

class User_Schema(ma.Schema):
    class Meta:
        fields = ("email", "date","_links")

    _links = ma.Hyperlinks(
        {
            "self" : ma.URLFor("user_details", values=dict(id = "<id>")),
            "collection" : ma.URLFor("users"),
        }
    )

user_schema = User_Schema()
users_schema = User_Schema(many = True)


@app.route('/users')
def users():
    getUsers = User.all()
    return users_schema.dump(getUsers)

@app.route('/users/<id>')
def user_details(id):
    user = User.get(id)
    return user_schema.dump(user)


if __name__ == '__main__':
    app.run(debug = True, port = 8888)
