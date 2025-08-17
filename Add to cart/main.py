from add_book import AddBook
from view_book import ViewBook
from search_remove import SearchBook
from remove import RemoveBook

print("\n<!-----Start Process----->")
print(f"\nThere Have 4 Type of Operation")
print("1. Add Book Info")
print("2. View Book Info")
print("3. Search Book Details")
print("4. Remove Books Info")
print("5. Exit")

n= input(f"\nSelect Your Operation: ")
while True:
    if n.isalpha() or n.upper() == "EXIT" :
        print("<!-----End----->")
        break
    elif int(n)==1:
        book = AddBook(input("Name: ").capitalize(), input("Author: ").capitalize(),input("Book ID: "),input("Genre: ").capitalize(),input("Price: "), input("Quantity in Stock: "))
        book.add_book()
    elif int(n) == 2:
        book = ViewBook(input("Enter the Book Name: ").capitalize())
        book.view_book()
    elif int(n)== 3:
        book = SearchBook(input("Name: ").capitalize(), input("Book Id: "))
        book.Search_book()
    elif int(n) == 4:
        book = RemoveBook(input("Name: ").capitalize(), input("Book Id: "))
        book.remove_book()
    elif int(n) == 5:
        print("<!-----End----->")
        break
    elif int(n) < 5 or int(n)>1:
        print("<!-----Please Select the Valid Operation----->")
    else:
        break
    n= input(f"\nSelect Again Your Operation: ")
