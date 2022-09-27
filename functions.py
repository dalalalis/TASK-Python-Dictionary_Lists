from books import books

#  number_of_authors(book)
#  recieves a book dictionary
#  returns the number of authors that the book has
def number_of_authors(book):
        numberofauthors = len(book["authors"])
        return numberofauthors

    #return return len(book["author"])



print(number_of_authors(books[0]))

#  get_book_by_id(book_id, books)
#  # receives a book id
#  # recieves a list of book dictionaries
#  # returns the book dictionary with the same id as the book_id provided
def get_book_by_id(book_id, books):
    for book in books:
        if book["id"] == book_id:
            return book
        

print(get_book_by_id(38, books))


# add_summary_to_book(summary, book)
# receives a book dictionary
# recieves a summary string
# adds the summary to the book dictionary
# return the book dictionary
def add_summary_to_book(summary, book):
    #not loop because one book only
       return book ["summary"]=summary



print(add_summary_to_book("this is a good book about", books[0]))


# CHALLENGE 1
# get_book_property(property, book)
# receives a book dictionary
# recieves a property (string)
# return the book property


def get_book_property(property, book):
    '''for book in books:
        if property in book: 
        bookvalue=books.get["property"]
    return bookvalue 
    this is wrong because we dont need a loop its one book '''
    return book[property]
    #return book.get(property) better option it has added value of validation 
    #so if the property doesnt exist it will return none instead of giving an erroe


print(get_book_property("color", books[0]))
print(get_book_property("title", books[0]))


# CHALLENGE 2
# calculate_available_books(books)
# receives a list of books
# return a new list of unavailable books


def calculate_not_available_books(books):
    unavailable_books=[]
    for book in books:
        if books["available"] != True:
            unavailable_books.append[book]
    return unavailable_books
            
#instead of != we could write 
# if not books["available"]: or if books ["available"] is True:


print(calculate_not_available_books(books))

# CHALLENGE 3
# get_book_by_author_name(author_name, books)
# receives a author name (string)
# recieves a list of book dictionaries
# returns the book dictionary that contains an author with the author name provided
def get_book_by_author_name(author_name, books):
    for book in books:
        for author in book["author"]:
         if author_name == author["name"]:
            return book 

print(get_book_by_author_name("Neil Gaiman", books))
