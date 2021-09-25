
from flask import request, render_template, url_for, redirect
from models import db, Subject
from app import app


@app.route('/')
@app.route('/subjectlist')
def subjectlist():

    subject = Subject.query.all()
    return render_template('subjectlist.html', subjects=subject)

@app.route('/detail/<int:id>',methods=['GET','POST'])

def detail(id):
    detail = Subject.query.get(id)
    return render_template("detail.html",detail=detail)


@app.route('/addsubject', methods=['GET', 'POST'])
def add():
    add="科目を追加"
    return render_template('addsubject.html',add=add)

@app.route('/create',methods=['POST'])
def create():



    addlist=Subject(teacher=request.form['teacher'],subject=request.form['subject'],date=request.form['date'],
        comment=request.form['content']
    )
    db.session.add(addlist)
    db.session.commit()
    return redirect(url_for('subjectlist'))

@app.route('/delete/<int:id>',methods=['POST'])
def delete_subject(id):
    post=Subject.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('subjectlist'))

@app.route('/updatelink/<int:id>',methods=['POST'])
def update_link(id):
    post=Subject.query.get(id)
    return render_template('updatesubject.html',post=post)
@app.route('/updatesubject/<int:id>',methods=['POST'])
def update_subject(id):
    post=Subject.query.get(id)
    post.subject=request.form['subject']
    post.date=request.form['date']
    post.comment=request.form['content']
    post.teacher=request.form['teacher']
    db.session.commit()
    return redirect(url_for('subjectlist'))










if __name__ == '__main__':
    app.run(debug=True)
