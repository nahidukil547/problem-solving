import json

class AddBook:
    def __init__(self, title, author, book_id, genre, price, quantity_in_stock):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.genre = genre
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def add_book(self):
        book_details = {
            "Title": self.title,
            "Author": self.author,
            "Book ID": self.book_id,
            "Genre": self.genre,
            "Price": self.price,
            "Quantity in Stock": self.quantity_in_stock
        }

        try: 
            with open("BookStore.json", "r") as f:
                book_info = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            book_info = []

        book_info.append(book_details)


        with open("BookStore.json", "w") as f:
            json.dump(book_info, f, indent=4)
            print("<!----- Successfully Add Book Info ----->")
            