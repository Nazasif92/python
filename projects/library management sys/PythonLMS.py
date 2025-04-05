import datetime
import os


class LMS:
    """ This Class is used to manage the library system.
    It has four modules: "Display Books","Issue Books","Return Books","Add Books" """
    def __init__(self, ist_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{'books_title':line.replace("\n",""),
            'lender_name': "",'Issue_date': "", 'Status': 'Available'}})
            Id = Id + 1

    def display_books(self):
        print("---------------List Of Books---------------")
        print("Books ID", "\t","Title")
        print("-------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"),"]")
         
    def issue_books(self):
        print("---------------Issue Book---------------")
        books_id = input("Enter Book ID:")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status'] == 'Available':
                print(f"Book is already issued to""{self.books_dict[books_id]['lender_name']}\
                    on {self.books_dict[books_id]['Issue_date']}")
                return self.issue_books()
            elif self.books_dict[books_id]['Status'] == 'Available':
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = 'Already Issued'
                print("Book Issued Successfully!!! \n")
        else:
             print("Book ID not found!!!")
             return self.issue_books()
    def add_books(self):
        print("---------------Add Book---------------")
        new_books = input("Enter Book title :")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title length is too long !!! Title length should be less than 25 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_books,"lender_name": "",
                "Issue_date":"","Status":"Available"}})
                print(f"This books '{new_books}' Added Successfully!!!")

    def return_books(self):
        print("---------------Return Book---------------")
        books_id = input("Enter Books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['Status'] == 'Available':
                print("This book is already available in the library. Check your book ID again.")
                return self.return_books()
            elif not self.books_dict[books_id]['Status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]['Status'] = 'Available'
                print("Updated Successfully!!! \n")
        else:
            print("Book ID not found!!!")
    def delete_books(self):
        print("---------------Delete Book---------------")
        books_id = input("Enter Books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['Status'] == 'Available':
                del self.books_dict[books_id]
                print("Book Deleted Successfully!!! \n")
            else:
                print("This book is already issued. You can't delete this book.")
                return self.delete_books()
        else:
            print("Book ID not found!!!")

try:
    myLMS = LMS("List_Of_books.txt", "Asif's")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "X": "Delete Books", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n---------------Welcome To {myLMS.library_name} LIbrary management System--------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press Key: ").lower()
        if  key_press == "i":
            print("\n Current Selection : Issue Books\n")
            myLMS.issue_books()
        elif key_press == "a":
            print("\n Current Selection : Add Books\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\n Current Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\n Current Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "x":
            print("\n Current Selection : Delete Books\n")
            myLMS.delete_books()
        elif key_press == "q":
            break
        else:
            continue    
except Exception as e:
    print("Invalid Key Pressed!!! Check your input again.")