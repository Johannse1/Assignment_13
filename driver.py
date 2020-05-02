# Evan Johanns
# 4/28/2020
# Assignment 13

from methods import create_connections, execute_query, execute_read_query, execute_delete
print("Connecting to Database...")
connection = create_connections("myDatabase")


create_customer_table = """
CREATE TABLE IF NOT EXISTS customers    (
    customer_id     INTEGER     PRIMARY KEY     UNIQUE      AUTOINCREMENT,
    first_name      TEXT        NOT NULL,
    last_name       TEXT        NOT NULL,
    street_address  TEXT        NOT NULL,
    city            TEXT        NOT NULL,
    state           TEXT        NOT NULL,
    zip             INTEGER     NOT NULL,
    );
    """
create_book_table = """
CREATE TABLE OF NOT EXISTS books    (
    book_id         INTEGER     PRIMARY KEY     UNIQUE      AUTOINCREMENT,
    title           TEXT        NOT NULL,
    author          TEXT        NOT NULL,
    ISBN            INTEGER     NOT NULL,
    edition         INTEGER     NOT NULL,
    price           INTEGER     NOT NULL,
    publisher       TEXT        NOT NULL
    );
    """

execute_query(connection, create_customer_table)
execute_query(connection, create_book_table)

M_menu_choice = 0

while M_menu_choice != 3:
    print("Please choose from the options below.")
    print("1. Customers.")
    print("2. Books.")
    print("3. Exit")
    M_menu_choice = int(input(">>"))
    if M_menu_choice == 1:
        C_menu_choice = 0
        B_menu_choice = 0
        while C_menu_choice != 5:
            print("Please choose an action.")
            print("1. Add new customer")
            print("2. Modify an existing customer")
            print("3. Show all customers")
            print("4. Delete customer")
            print("5. Return to Main Menu")
            C_menu_choice = int(input(">>"))

            if C_menu_choice == 1:
                print("Please enter the customers required info.")
                first_name = input("First name:")
                last_name = input("Last name:")
                street_address = input("Street address:")
                city = input("City:")
                state = input("State:")

                add_customer = f"""
                INSERT INTO
                    customers (first_name, last_name, street_address, city, state, zip)
                VALUES 
                    ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip}');
                """
                execute_query(connection, add_customer)
            elif C_menu_choice == 2:
                looking_for = input("What field would you like to change")
                new = input("New: ")
                old = input("Previous:")

                update_person = f"""
                UPDATE
                    customers
                SET 
                    {looking_for} = {new}
                WHERE 
                    {looking_for} = {old}
                """
                execute_query(connection, update_person)

            elif C_menu_choice == 3:
                select_people = "SELECT * from customers"
                people = execute_read_query(connection, select_people)

            elif C_menu_choice == 4:
                print("who would you like to delete")
                first_name = input("First name:")
                last_name = input("Last name:")
                street_address = input("Street address:")
                delete_person = f"""DELETE from customer WHERE first_name = {first_name}, last_name = {last_name}, street_address = {street_address}"""
                execute_delete(connection, delete_person)


        while B_menu_choice != 5:
            print("Please choose an action from below")
            print("1. Add new book")
            print("2. Modify existing book")
            print("3. Show all books")
            print("4. Delete a book")
            print("5. Return to menu")
            B_menu_choice = int(input(">>"))
            if B_menu_choice == 1:
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
                execute_query(connection, add_book)
            elif B_menu_choice == 2:
                looking_for = input("What field would you like to change")
                new = input("New: ")
                old = input("Previous:")

                update_book = f"""
                UPDATE
                    books
                SET 
                    {looking_for} = {new}
                WHERE 
                    {looking_for} = {old}
                """
                execute_query(connection, update_book)
            elif B_menu_choice == 3:
                select_books = "SELECT * from books"
                people = execute_read_query(connection, select_books)
            elif B_menu_choice == 4:
                print("what book would you like to delete")
                title = input("Title:")
                author = input("Author:")
                ISBN = input("ISBN:")
                delete_book = f"""DELETE from books WHERE title = {title}, author = {author}, ISBN = {ISBN}"""
                execute_delete(connection, delete_book)










