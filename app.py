'''
- Create a book
- Create more books
- Read a book
- Read a list of Books
- Update a book
- Delete a book using Flask.
'''
from flask import Flask, render_template, request, jsonify
from flask import json

app=Flask(__name__)

all_books=[
    {
        "author":"Emma Donoghue",
        "book":["Asylum","Sanctum"],
        "genre":"horror"
    },
    {
        "author" : "Stephen King",
        "book" : ["Thinner", "The Shinning"],
        "genre" :"thriller"
    },
    {
        "author" : "Micheal Grant",
        "book" : ["Bzrk", "Bzrk Reloaded"],
        "genre" : "science fiction"
    }
]


@app.route('/')
def home():
    return jsonify({'message':'hello world'})

@app.route('/books', methods=['GET']) #give all books in list
def allbooks():
    return jsonify(all_books)

@app.route('/books/<int:id>', methods=['GET']) #give only one book, according to id
def onebook(id):
    return jsonify(all_books[id])

@app.route('/books', methods= ['POST']) #create more books
def add_new_book():
    new_book = request.get_json()
    all_books.append(new_book)
    return jsonify(all_books)

@app.route('/books/<int:id>', methods=['DELETE']) #to delete specific book, using id
def delete_book(id):
    del all_books[id]
    return jsonify(all_books)
        
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.get_json()
    all_books[id] = updated_book
    return jsonify(all_books)

#if want to see error display on webpage, or automatically saved on web, do this
if __name__=='__main__':
    app.run(debug=True)