import json
class ViewBook:
    def __init__(self,title):
        self.title = title
    def view_book(self):
        try:
            with open ("BookStore.json","r+") as f:
               file= json.load(f)
            for i in file:
                if i.get("Title")== self.title :
                    print( json.dumps(i,indent=4))
            
        except FileNotFoundError:
            print("Invalid Book!! Kindly search other book")
