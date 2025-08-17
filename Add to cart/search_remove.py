
# class RemoveBook:
#     def __init__(self, title, book_id):
#         self.title = title
#         self.book_id = book_id
    
#     def remove_book(self):
#         try:
#             with open("Book_Stor.txt", "r") as f:
#                 lines = f.readlines()
            
#             new_lines = []
#             found = False
#             i = 0
            
#             while i < len(lines):
#                 if lines[i].startswith("Title") and self.title in lines[i]:
#                     if i + 2 < len(lines) and lines[i + 2].startswith("Book ID") and self.book_id in lines[i + 2]:
#                         found = True
#                         i += 7  # Skip the 7 lines of the book entry
#                         continue
#                 new_lines.append(lines[i])
#                 i += 1
            
#             if found:
#                 with open("Book_Stor.txt", "w") as f:
#                     f.writelines(new_lines)
#                 print(f"Book '{self.title}' with ID {self.book_id} has been removed.")
#             else:
#                 print("Book not found!")
#         except FileNotFoundError:
#             print("Book storage file not found!")

import json
class SearchBook:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id
    
    def Search_book(self):
        try:
            with open("BookStore.json", "r") as f:
                lines = json.load(f)
                for book in lines:
                    if book.get("Title")==self.title and book.get("Book ID") ==self.book_id:
                        print(json.dumps(book, indent=4))
                        print("This is your Book Details")
                        print("<!----- Search ----->")
                        break
                    else:
                        print("Book is not Found!!")
                        break
        except FileNotFoundError:
            print("Book storage file not found!")
# Example usage


# from search_remove import RemoveBook

# remove1 = RemoveBook("Himu", "00547")
# remove1.remove_book()

# remove2 = RemoveBook("Himu", "00547")
# remove2.remove_book()