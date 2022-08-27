import sys


class Library:
    availablebooks=[]
    def __init__(self,listofbooks):
        self.availablebooks=listofbooks

    def displayAvailablebooks(self):
        print("\n The books we have in our library are: \n")
        for book in range(0,len(self.availablebooks)):
            print(f"{book+1}. {self.availablebooks[book].title()}")

class Student(Library):
    myBooks=[]

    def requestBook(self):
        print("\n Enter the name of the book you would like to have:")
        self.book=input()
        p=False
        for i in self.availablebooks:
            if(self.book==i):
                self.myBooks.append(i)
                self.availablebooks.remove(i)
                p=True
        if(p==False):
            print(f"Book {self.book} is not available")
        else:
            print(f"You borrowed {self.book}")

    def returnBook(self):
        print("\nEnter the name of the book you would like to return: ") 
        self.book=input()
        print(f"Returned {self.book} Successfully")

    def MyBooks(self):
        print("\n The books You have in our List are: \n")
        for book in range(0,len(self.myBooks)):
            print(f"{book+1}.{self.myBooks[book].title()}")

def main():
    library=Student(["Akbar and Birbal","Wings of Fire","Man mein hain Vishwas"]) 
      
    while True:
        print("""\n--------Library Menu--------\n
              1. All the available books
              2. Request a book
              3. Return a book
              4. Display my list
              5. Exit\n""")
        choice=int(input("Enter the choice: "))
        if choice==1:
            library.displayAvailablebooks()
        elif choice==2:
            library.requestBook()
        elif choice==3:
            library.returnBook()
        elif choice==4:
            library.MyBooks()
        elif choice==5:
            sys.exit()

main()

        
        
        



