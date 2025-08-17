import json

class RemoveBook:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id

    def remove_book(self):
        try:
            with open("BookStore.json", "r") as f:
                data = json.load(f)

            book_list=[]
            for book in data :
                if not(book.get("Title") == self.title and book.get("Book ID") == self.book_id):
                    book_list.append(book)

            with open ("BookStore.json", 'w') as f:
                json.dump(book_list,f, indent=4)
                print("<!----- Book successfully removed! ----->")
                
        except FileNotFoundError:
            print("Error: Book database not found")
        except json.JSONDecodeError:
            print("Error: Invalid data format in database")



# try:
#     # risky code
# except Exception as e:
#     print("Error:", e