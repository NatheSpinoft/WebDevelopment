from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory storage for demo purposes)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.json)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# Endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
