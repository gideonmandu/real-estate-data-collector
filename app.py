from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://hlvekkwbehktde:94d8937f5213d34558719db1ea2ad62dc5a6480e90df8e37e079227dfd5c3594@ec2-18-214-119-135.compute-1.amazonaws.com:5432/d9bvfm7jtqjn7m?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    """Create from model class of SQLAlchemy a database table."""
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template('index.html', btn='')

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        # email=request.form["email_name"]
        file=request.files["file"]
        file.save(secure_filename("Uploaded"+file.filename))
        with open("Uploaded"+file.filename, 'a') as f:
            f.write('This was added later!')
        print(file)
        print(type(file))
        # height=request.form["height_name"]
        # if db.session.query(Data).filter(Data.email_==email).count() ==0:
        #     data=Data(email,height)
        #     db.session.add(data)
        #     db.session.commit()
        #     average_height=db.session.query(func.avg(Data.height_)).scalar()
        #     average_height=round(average_height, 1)
        #     count=db.session.query(Data.height_).count()
        #     send_email( email, height, average_height, count) 
        return render_template('index.html', btn='download.html')
    # return render_template('index.html', 
    # text='Seems like we have got something from that email address already!')
@app.route('/download')
def download():
    return send_file("Uploaded"+file.filename, attachment_filename='yourfile.csv', as_attachment=True)

if __name__ == '__main__':
    app.debug=True
    app.run()
