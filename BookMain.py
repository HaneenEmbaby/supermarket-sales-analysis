import Lab2

while True:
    print("Library Management System")
    print("1. Show available books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Show borrowed books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        Lab2.show_books()

    elif choice == "2":
        Lab2.borrow_book()

    elif choice == "3":
        Lab2.return_book()

    elif choice == "4":
        Lab2.show_borrowed_books()

    elif choice == "5":
        print("Thank you for using the Library Management System")
        break
    else:
        print("Invalid choice")