'''
- Create a book
- Create more books
- Read a book
- Read a list of Books
- Update a book
- Delete a book using Flask.
'''
from flask import Flask, render_template, request
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

class Books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    author=db.Column(db.String(120), unique=True, nullable=False)
    category=db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Books %r>' %self.id

@app.route('/', methods=['POST', 'GET']) #add book &more book
def index(): 
    if request.method == 'POST':
        book_name = request.form['name']
        book_author= request.form['author']
        book_category = request.form['category']
        new_book = Books(name=book_name, author=book_author, category=book_category)

        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect('/')
        except:
            return 'Cannot add book'
    else:
        all_books = Books.query.order_by(Books.name).all()
        return render_template('index.html', all_books=all_books)

@app.route('/delete/<int:id>') #delete book
def delete(id):
    delete_book = Books.query.get_or_404(id)
    try:
        db.session.delete(delete_book)
        db.session.commit()
        return redirect('/')
    except:
        return 'Cannot delete book'

@app.route('/update/<int:id>', methods=['GET', 'POST']) #update book
def update(id):
    update_book = Books.query.get_or_404(id)
    if request.method=='POST':
        update_book.name = request.form['name']
        update_book.author=request.form['author']
        update_book.category = request.form['category']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Cannot update book'
    else:
        return render_template('update.html', book=update_book)

#if want to see error display on webpage, or automatically saved on web, do this
if __name__=='__main__':
    app.run(debug=True)