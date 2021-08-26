import re
from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres123@localhost/contact_info"
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer,primary_key=True)
    name_=db.Column(db.String(120),unique=True)
    email_=db.Column(db.String(220),unique=True)
    phone_=db.Column(db.Integer,unique=True)
    website_=db.Column(db.String(220),unique=True)

    def __init__(self,name_,email_,phone_,website_):
        self.name_=name_
        self.email_=email_
        self.phone_=phone_
        self.website_=website_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])
def success():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email_name']
        phone=request.form['phone_no']
        website=request.form['website']
        data=Data(name,email,phone,website)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

if __name__=="__main__":
    app.debug=True
    app.run()