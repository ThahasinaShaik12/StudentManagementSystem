
from flask import Flask, render_template,request,redirect,url_for

from flask_sqlalchemy import SQLAlchemy

#initialize flask
app=Flask(__name__)
#Database configuration
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin123@localhost/student_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Initialize the database
db=SQLAlchemy(app)

#Define the student model
class students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    course=db.Column(db.String(100),nullable=False)

    def _repr_(self):
        return f"Student('{self.name}','{self.age}','{self.course}')"

#define routes
@app.route('/')
def home():
    Student = students.query.all()
    return render_template('index.html',Student=Student)


@app.route('/add',methods=['POST'])
def add():
    formName=request.form['name']
    formAge=request.form['age']
    formCourse=request.form['course']

#create ne stuudent record
    newStudent=students(name = formName,age=formAge,course=formCourse)
    db.session.add(newStudent)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/edit/<int:id>',methods=['POST','GET'])
def edit_student(id):   
    std = students.query.get_or_404(id)
    if request.method=='POST':
        std.name = request.form['name']
        std.age = request.form['age']
        std.course = request.form['course']
        db.session.commit() 
        return redirect(url_for('home'))
    
    return render_template('edit.html',student = std)

@app.route('/delete/<int:id>',methods=['POST'])
def delete_student(id):   
    std = students.query.get_or_404(id)
    db.session.delete(std)
    db.session.commit() 
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)



