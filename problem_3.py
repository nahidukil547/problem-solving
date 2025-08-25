"""
Problem Statement
You have an empty box and several books with some id. There will be N tasks of two types.

Put a book into the box. If there are already some books, you must put the book on top of the others.
Remove the topmost book and print the id of the book. If the box is empty then print -1.
Input
The input consists of N+1 lines. First one having one integer N. Next N lines contains two type of tasks. First read an integer x. If x=1 then read another integer i, id of the book to put into the box. If x=2 then do the second task.

Output
For each second type of the task print the id of the topmost book. If there is no book in the box then print -1.

Constraints 1 ≤ N ≤1 ≤10 5
 
id of the books are between 1 ≤ l≤r ≤10 9 .
There may be multiple books with the same id.
"""

n=int(input().strip())
books=[]
for _ in range(n):
    task = list(map(int, input().split()))

    if task[0]== 1 :
        books.append(task[1])
    elif task[0]==2:
        if books:
            print(books.pop())
        else:
            print(-1)


# class Stack:
#     def __init__(self):
#         self.books=[]
#     def push(self, book_id):
#         self.books.append(book_id)
#     def pop(self):
#         if books:
#             print(self.books.pop())
#         else:
#             print(-1)

# def solve():
#     n = int(input().strip())
#     stack = Stack() 
#     for _ in range(n):
#         task = list(map(int, input().split()))
#         if task[0] == 1:
#             stack.push(task[1])        
#         elif task[0] == 2:
#             print(stack.pop())
