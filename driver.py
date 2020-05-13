# Evan Johanns
# 4/28/2020
# Final project
# Hello Prof. Lichtman
# Just a few things i would like to say before you explore this program
# First, I have fixed most of the mistakes from the last assignment in this one
# Second, there is no preset data in any of the tables in this program, some of the methods will require information to be in the tables for them to fully work
# thus, I suggest entering some random names and people that can be entered into the customers table. this also applies to the books table.
# unfortunately, I am not able to provide a table as I have run out of time on this project. sorry for the inconvenience.
# I hope you have, and will continue to, stay safe during this quarantine and hope that you have a very relaxing summer.
# thanks for a great experience for my first year at hartwick college and look forward to working again this coming fall.\
# Thanks,
# Evan Johanns

from methods import create_connections, execute_query, execute_read_query, execute_delete
print("Connecting to Database...")
connection = create_connections("myDatabase") # connection to database

                                                        # tables for order system
create_customer_table = """                          
CREATE TABLE IF NOT EXISTS customers    (
    customer_id     INTEGER     PRIMARY KEY     UNIQUE      AUTOINCREMENT,
    first_name      TEXT        NOT NULL,
    last_name       TEXT        NOT NULL,
    street_address  TEXT        NOT NULL,
    city            TEXT        NOT NULL,
    state           TEXT        NOT NULL,
    zip             INTEGER     NOT NULL
    );
    """
create_book_table = """
CREATE TABLE OF NOT EXISTS books    (
    book_id         INTEGER     PRIMARY KEY     UNIQUE      AUTOINCREMENT,
    title           TEXT        NOT NULL,
    author          TEXT        NOT NULL,
    ISBN            INTEGER     NOT NULL,
    edition         INTEGER,
    price           INTEGER     NOT NULL,
    publisher       TEXT        NOT NULL
    );
    """
create_order_table = """
CREATE TABLE IF NOT EXISTS order    (
    order#          INTEGER     PRIMARY KEY     UNIQUE      AUTOINCREMENT,
    order_date      DATETIME,
    order_total     REAL        NOT NULL,
    customer_id     INTEGER     NOT NULL        UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)"""
create__order_line_item_table = """
CREATE TABLE IF NOT EXISTS OrderLineItem    (
    order#          INTEGER     PRIMARY KEY     UNIQUE,
    book_id         INTEGER     PRIMARY KEY     UNIQUE,
    quantity        INTEGER     NOT NULL,
    FOREIGN KEY (order#) REFERENCES order (order#),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
    );
    """
execute_query(connection, create_customer_table) # creates the tables in the database
execute_query(connection, create_book_table)
execute_query(connection, create_order_table)
execute_query(connection, create__order_line_item_table)


M_menu_choice = 0         # main loop for whole program, contains all menu's and actions/programs
while M_menu_choice != 4: # main menu choices for sub menu's, if the number entered is 4 the program will stop and will need to be rerun
    print("Please choose from the options below.")
    print("1. Customers")
    print("2. Books")
    print("3. Order books")
    print("4. Exit")
    M_menu_choice = int(input(">>"))

    if M_menu_choice == 1:
        C_menu_choice = 0
        while C_menu_choice != 5: # customer menu, options for what the user wants to do, if the number entered is 5 the program will return to the first menu
            print("Please choose an action.")
            print("1. Add new customer")
            print("2. Modify an existing customer")
            print("3. Show all customers")
            print("4. Delete customer")
            print("5. Return to Main Menu")
            C_menu_choice = int(input(">>"))

            if C_menu_choice == 1: # first menu choice, allows the user to add a new customer to the customer table
                print("Please enter the customers required info.")
                first_name = input("First name:")
                last_name = input("Last name:")
                street_address = input("Street address:")
                city = input("City:")
                state = input("State:")
                                    # SQLite commands for adding a new customer, formatted for easier use
                add_customer = f""" 
                INSERT INTO
                    customers (first_name, last_name, street_address, city, state, zip)
                VALUES 
                    ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip}');
                """
                execute_query(connection, add_customer) # sends the query to the database to be executed

            elif C_menu_choice == 2: # second choice, allows the user to change any part of the customer table
                looking_for = input("What field would you like to change: ")
                old = input("Previous:")
                new = input("New: ")

                update_person = f"""
                UPDATE
                    customers
                SET 
                    {looking_for} = {new}
                WHERE 
                    {looking_for} = {old}
                """
                execute_query(connection, update_person)

            elif C_menu_choice == 3: # third choice, allows the user to print entire table of customers with all data
                select_people = "SELECT * from customers"
                people = execute_read_query(connection, select_people)
                print(people)

            elif C_menu_choice == 4: # fourth choice, allows the user to delete any customer
                print("who would you like to delete")
                first_name = input("First name:")
                last_name = input("Last name:")
                street_address = input("Street address:")
                delete_person = f"""DELETE from customer WHERE first_name = {first_name}, last_name = {last_name}, street_address = {street_address};"""
                execute_delete(connection, delete_person)
    if M_menu_choice == 2: # second main menu choice, the books table
        B_menu_choice = 0
        while B_menu_choice != 5: # main books table loop, submenu with different options
            print("Please choose an action from below")
            print("1. Add new book")
            print("2. Modify existing book")
            print("3. Show all books")
            print("4. Delete a book")
            print("5. Return to menu")
            B_menu_choice = int(input(">>"))
            if B_menu_choice == 1: # first choice, allows user to enter a new book
                print("Please enter the books required info.")
                title = input("Title:")
                author = input("Author")
                ISBN = int(input("ISBN:"))
                price = float(input("Price:"))
                publisher = input("Publisher:")

                add_book = f"""
                INSERT INTO
                    books (title, author, ISBN, price, publisher)
                VALUES 
                    ('{title}', '{author}', '{ISBN}', '{price}', '{publisher}');
                """
                execute_query(connection, add_book) # sends the query to the database to be executed

            elif B_menu_choice == 2: # second choice, allows user to change any part of the books table data
                looking_for = input("What field would you like to change")
                new = input("New: ")
                old = input("Previous:")

                update_book = f"""
                UPDATE
                    books
                SET 
                    {looking_for} = {new}
                WHERE 
                    {looking_for} = {old};
                """
                execute_query(connection, update_book)

            elif B_menu_choice == 3: # third choice, displays all books and data in the books table
                select_books = "SELECT * FROM books;"
                books = execute_read_query(connection, select_books)
                print(books)

            elif B_menu_choice == 4: # fourth choice, allows the user to delet any book from the table
                print("what book would you like to delete.")
                title = input("Title:")
                author = input("Author:")
                ISBN = input("ISBN:")
                delete_book = f"""DELETE from books WHERE title = {title}, author = {author}, ISBN = {ISBN};"""
                execute_delete(connection, delete_book)

    if M_menu_choice == 3: # last main menu choice, used to order/purchase books
        O_menu_choice = 0
        while O_menu_choice != 4: # loop for order menu
            print("Please type the number of the action you want below.")
            print("1. Place Order.")
            print("2. Show Order.")
            print("3. Cancel Order.")
            print("4. Exit")
            O_menu_choice = int(input(">>"))

            if O_menu_choice == 1: # first choice, allows person to order a book and place the order into the order table
                print("Please enter the required information for your order.")
                customer_Fname = input("First Name: ")
                customer_Lname = input("Last name: ")
                book_title = input("Book Title: ")
                quantity = int(input("Quantity: "))
                add_quantity = f"""INSERT INTO OrderLineItem (quantity) VALUES ('{quantity}';)"""
                execute_query(connection, add_quantity) # sends and inserts the quantity into the table

                find_customer_id = f"""
                SELECT customer_id FROM customers WHERE first_name = {customer_Fname}, last_name = {customer_Lname};"""
                customer_id = execute_query(connection, find_customer_id) # finds the customers ID based on first and last name, search is case sensitive so names need to exact matches with the table

                find_book_id = f"""
                SELECT book_id FROM books WHERE book_title = {book_title};"""
                book_id = execute_query(connection, find_book_id) # finds the book t be ordered in the books table

                order_price = (f"""
                SELECT price FROM books WHERE book_id = {book_id};""") * quantity
                order_total = execute_query(connection, order_price) # calculates the price of the order based on the quantity ans send it to the orderlineitem table

                add_order = f"""
                INSERT INTO 
                    order (order_total, customer_id)
                VALUES
                    ('{order_total}', '{customer_id};"""
                execute_query(connection, add_order) # adds the order to the order table

                order_number = f"""
                SELECT order# FROM order """
                order_num = execute_read_query(connection, order_number)
                print(f"Your order number is: {order_num}") # prints the order number for this order, is used for the rest of the program to function properly

            elif O_menu_choice == 2: # second choice, allows the user to see their order to confirm its been made.
                order_num = input("Please enter the order number you wish to find: ")
                find_order = f"""
                SELECT * FROM order WHERE order# = {order_num};"""
                execute_read_query(connection, find_order) # sends and executes the query to find the order number

            elif O_menu_choice == 3: # third choice, allows the user to cancel/delet any order as long as they have the order number
                order_num = input("Please type the order number you wish to cancel: ")
                print(f"Are you sure you want to cancel order number {order_num}?")
                question = input("yes/no >>") # confirmation question for deleting an order
                if question == "yes":
                    delete_order = f"""DELETE * FROM order WHERE order# = {order_num}; """
                    execute_delete(connection, delete_order)
                    print(f"Order number {order_num} has been cancelled")


