from app import books

User_choice = """
    Enter one of the following:
    
    - 'b' to look at the best books
    - 'c' to look at the cheapest books
    - 'n' to look at the next book in the store
    - 'q' to quit the menu
    
    Enter your choice:
"""


def print_high_rated_books():
    high_rated = sorted(books, key=lambda x: x.book_ratings * -1)[:10]
    for book in high_rated:
        print(book)


def print_cheapest_books():
    cheapest = sorted(books, key=lambda x: x.book_price)[:10]
    for book in cheapest:
        print(book)


book_generator = (x for x in books)


def get_next_book():
    print(next(book_generator))


def menu():
    user_choice = input(User_choice)

    while user_choice != "q":
        if user_choice == "b":
            print_high_rated_books()

        elif user_choice == "c":
            print_cheapest_books()

        elif user_choice == "n":
            get_next_book()

        else:
            print("Enter a valid command")

        user_choice = input(User_choice)


menu()