import streamlit as st
import mysql.connector
from mysql.connector import Error
# import C, R, U, D

# Function to create a MySQL connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pa@28042003",
            database='concert_management'
        )
        if connection.is_connected():
            st.success("Connected to MySQL database")
    except Error as e:
        st.error(f"Error: {e}")
    return connection

# Function to execute MySQL queries and return results as a Pandas DataFrame
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "artist" table
def get_all_artists(connection):
    query = "SELECT * FROM artist"
    return execute_query(connection, query)

# Function to insert data into the "artist" table
def insert_artist(connection,artist_id, artist_name, genre_id):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO artist (artist_id, artist_name, genre_id) VALUES ({artist_id},'{artist_name}', {genre_id})"
        cursor.execute(query)
        connection.commit()
        st.success("Artist added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_artist(connection, artist_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM artist WHERE artist_id = {artist_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Artist with ID {artist_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_artist(connection, artist_id, new_artist_name, new_genre_id):
    try:
        cursor = connection.cursor()
        query = f"UPDATE artist SET artist_name = '{new_artist_name}', genre_id = {new_genre_id} WHERE artist_id = {artist_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Artist updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "concert" table
def get_all_concerts(connection):
    query = "SELECT * FROM concert"
    return execute_query(connection, query)

# Function to insert data into the "concert" table
def insert_concert(connection,concert_id, concert_name, artist_id, date, venue_id, concert_group_id):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO concert (concert_id, concert_name, artist_id, date, venue_id, concert_group_id) " \
                f"VALUES ({concert_id},'{concert_name}', {artist_id}, '{date}', {venue_id}, {concert_group_id})"
        cursor.execute(query)
        connection.commit()
        st.success("Concert added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_concert(connection, concert_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM concert WHERE concert_id = {concert_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Concert with ID {concert_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_concert(connection, concert_id, new_concert_name, new_artist_id, new_date, new_venue_id, new_concert_group_id):
    try:
        cursor = connection.cursor()
        query = f"UPDATE concert SET concert_name = '{new_concert_name}', artist_id = {new_artist_id}, " \
                f"date = '{new_date}', venue_id = {new_venue_id}, " \
                f"concert_group_id = {new_concert_group_id} WHERE concert_id = {concert_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Concert updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "concert_group" table
def get_all_concert_groups(connection):
    query = "SELECT * FROM concert_group"
    return execute_query(connection, query)

# Function to insert data into the "concert_group" table
def insert_concert_group(connection, concert_group_id, concert_group_name):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO concert_group (concert_group_id, concert_group_name) VALUES ({concert_group_id},'{concert_group_name}')"
        cursor.execute(query)
        connection.commit()
        st.success("Concert group added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_concert_group(connection, concert_group_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM concert_group WHERE concert_group_id = {concert_group_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Concert Group with ID {concert_group_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_concert_group(connection, concert_group_id, new_concert_group_name):
    try:
        cursor = connection.cursor()
        query = f"UPDATE concert_group SET concert_group_name = '{new_concert_group_name}' WHERE concert_group_id = {concert_group_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Concert Group updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "customer" table
def get_all_customers(connection):
    query = "SELECT * FROM customer"
    return execute_query(connection, query)

# Function to insert data into the "customer" table
def insert_customer(connection,customer_id, customer_name, email, user_name, password):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO customer (customer_id, customer_name, email, user_name, password) " \
                f"VALUES ({customer_id}, '{customer_name}', '{email}', '{user_name}', '{password}')"
        cursor.execute(query)
        connection.commit()
        st.success("Customer added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_customer(connection, customer_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM customer WHERE customer_id = {customer_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Customer with ID {customer_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_customer(connection, customer_id, new_customer_name, new_email, new_user_name, new_password):
    try:
        cursor = connection.cursor()
        query = f"UPDATE customer SET customer_name = '{new_customer_name}', email = '{new_email}', " \
                f"user_name = '{new_user_name}', password = '{new_password}' WHERE customer_id = {customer_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Customer updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "customer_order" table
def get_all_customer_orders(connection):
    query = "SELECT * FROM customer_order"
    return execute_query(connection, query)

#Function to join two tables
def join_tables(connection, table1, table2, join_condition, columns):
    columns_str = ', '.join(columns)
    query = f"""
    SELECT {columns_str}
    FROM {table1} t1
    INNER JOIN {table2} t2 ON {join_condition}
    """
    return execute_query(connection, query)

# Function to insert data into the "customer_order" table
def insert_customer_order(connection,customer_order_id, customer_id, registered_email_address, total_price, discount, final_price):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO customer_order (customer_order_id, customer_id, registered_email_address, total_price, discount, final_price) " \
                f"VALUES ({customer_order_id}, {customer_id}, '{registered_email_address}', {total_price}, {discount}, {final_price})"
        cursor.execute(query)
        connection.commit()
        st.success("Customer order added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_customer_order(connection, customer_order_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM customer_order WHERE customer_order_id = {customer_order_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Customer Order with ID {customer_order_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_customer_order(connection, customer_order_id, new_customer_id, new_registered_email_address, new_total_price, new_discount, new_final_price):
    try:
        cursor = connection.cursor()
        query = f"UPDATE customer_order SET customer_id = {new_customer_id}, " \
                f"registered_email_address = '{new_registered_email_address}', total_price = {new_total_price}, " \
                f"discount = {new_discount}, final_price = {new_final_price} WHERE customer_order_id = {customer_order_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Customer Order updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "genre" table
def get_all_genres(connection):
    query = "SELECT * FROM genre"
    return execute_query(connection, query)

# Function to insert data into the "genre" table
def insert_genre(connection,genre_id, genre_name):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO genre (genre_id,genre_name) VALUES ({genre_id}, '{genre_name}')"
        cursor.execute(query)
        connection.commit()
        st.success("Genre added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_genre(connection, genre_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM genre WHERE genre_id = {genre_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Genre with ID {genre_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_genre(connection, genre_id, new_genre_name):
    try:
        cursor = connection.cursor()
        query = f"UPDATE genre SET genre_name = '{new_genre_name}' WHERE genre_id = {genre_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Genre updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "order_ticket" table
def get_all_order_tickets(connection):
    query = "SELECT * FROM order_ticket"
    return execute_query(connection, query)

# Function to insert data into the "order_ticket" table
def insert_order_ticket(connection, order_ticket_id, customer_order_id, ticket_id):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO order_ticket (order_ticket_id, customer_order_id, ticket_id) VALUES ({order_ticket_id},{customer_order_id}, {ticket_id})"
        cursor.execute(query)
        connection.commit()
        st.success("Order ticket added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_order_ticket(connection, order_ticket_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM order_ticket WHERE order_ticket_id = {order_ticket_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Order Ticket with ID {order_ticket_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_order_ticket(connection, order_ticket_id, new_customer_order_id, new_ticket_id):
    try:
        cursor = connection.cursor()
        query = f"UPDATE order_ticket SET customer_order_id = {new_customer_order_id}, " \
                f"ticket_id = {new_ticket_id} WHERE order_ticket_id = {order_ticket_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Order Ticket updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "ticket" table
def get_all_tickets(connection):
    query = "SELECT * FROM ticket"
    return execute_query(connection, query)

# Function to insert data into the "ticket" table
def insert_ticket(connection, ticket_id, serial_number, concert_id, ticket_category_id, seat, purchase_date):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO ticket (ticket_id, serial_number, concert_id, ticket_category_id, seat, purchase_date) " \
                f"VALUES ({ticket_id},'{serial_number}', {concert_id}, {ticket_category_id}, '{seat}', '{purchase_date}')"
        cursor.execute(query)
        connection.commit()
        st.success("Ticket added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_ticket(connection, ticket_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM ticket WHERE ticket_id = {ticket_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Ticket with ID {ticket_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_ticket(connection, ticket_id, new_serial_number, new_concert_id, new_ticket_category_id, new_seat, new_purchase_date):
    try:
        cursor = connection.cursor()
        query = f"UPDATE ticket SET serial_number = '{new_serial_number}', concert_id = {new_concert_id}, " \
                f"ticket_category_id = {new_ticket_category_id}, seat = '{new_seat}', " \
                f"purchase_date = '{new_purchase_date}' WHERE ticket_id = {ticket_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Ticket updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "ticket_category" table
def get_all_ticket_categories(connection):
    query = "SELECT * FROM ticket_category"
    return execute_query(connection, query)

# Function to insert data into the "ticket_category" table
def insert_ticket_category(connection,ticket_category_id, description, price, start_date, end_date, area, concert_id):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO ticket_category (ticket_category_id, description, price, start_date, end_date, area, concert_id) " \
                f"VALUES ({ticket_category_id},'{description}', {price}, '{start_date}', '{end_date}', '{area}', {concert_id})"
        cursor.execute(query)
        connection.commit()
        st.success("Ticket category added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_ticket_category(connection, ticket_category_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM ticket_category WHERE ticket_category_id = {ticket_category_id}"
        cursor.execute(query)
        connection.commit()
        st.success(f"Ticket Category with ID {ticket_category_id} deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_ticket_category(connection, ticket_category_id, new_description, new_price, new_start_date, new_end_date, new_area, new_concert_id):
    try:
        cursor = connection.cursor()
        query = f"UPDATE ticket_category SET description = '{new_description}', price = {new_price}, " \
                f"start_date = '{new_start_date}', end_date = '{new_end_date}', " \
                f"area = '{new_area}', concert_id = {new_concert_id} WHERE ticket_category_id = {ticket_category_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Ticket Category updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get all data from the "venue" table
def get_all_venues(connection):
    query = "SELECT * FROM venue"
    return execute_query(connection, query)

# Function to insert data into the "venue" table
def insert_venue(connection,venue_id, venue_name, location, type, capacity):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO venue (venue_id, venue_name, location, type, capacity) " \
                f"VALUES ({venue_id},'{venue_name}', '{location}', '{type}', {capacity})"
        cursor.execute(query)
        connection.commit()
        st.success("Venue added successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def delete_venue(connection, venue_id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM venue WHERE venue_id = {venue_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Venue deleted successfully!")
    except Error as e:
        st.error(f"Error: {e}")
def update_venue(connection, venue_id, new_venue_name, new_location, new_type, new_capacity):
    try:
        cursor = connection.cursor()
        query = f"UPDATE venue SET venue_name = '{new_venue_name}', location = '{new_location}', type = '{new_type}', capacity = {new_capacity} WHERE venue_id = {venue_id}"
        cursor.execute(query)
        connection.commit()
        st.success("Venue updated successfully!")
    except Error as e:
        st.error(f"Error: {e}")
        
def join_artist_genre(connection):
    query = """
    SELECT artist.artist_name, genre.genre_name
    FROM artist
    INNER JOIN genre ON artist.genre_id = genre.genre_id
    """
    return execute_query(connection, query)

# Function to calculate total amount generated
def calculate_total_amount(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT SUM(final_price) AS total_amount_generated FROM customer_order"
        cursor.execute(query)
        result = cursor.fetchone()
        total_amount = result[0]
        st.write(f"Total Amount Generated: {total_amount}")
    except Error as e:
        st.error(f"Error: {e}")

# Function to get the number of tickets sold
def get_tickets_sold_per_concert(connection):
    query = """
    SELECT concert.concert_name, COUNT(ticket.ticket_id) as tickets_sold
    FROM concert
    LEFT JOIN ticket ON concert.concert_id = ticket.concert_id
    GROUP BY concert.concert_id
    """
    result = execute_query(connection, query)
    return result

# Streamlit app
def main():
    st.title("Concert Management Web App")

    # Connect to the MySQL database
    connection = create_connection()

    if connection:
        # Sidebar for selecting a table
        selected_table = st.sidebar.selectbox("Concert", ["artist", "concert", "concert_group", "customer", "customer_order", "genre", "order_ticket", "ticket", "ticket_category", "venue", "artist--genre","tickets sold"])

        if selected_table == "artist":
            # Add artist CRUD operations
            st.sidebar.subheader("Artist CRUD Operations")
            select_crud = st.sidebar.selectbox("CRUD", ["create","delete"])

            # Display all artists
            st.write("## All Artists")
            artists = get_all_artists(connection)
            # st.write(artists)
            st.dataframe(artists, width=700)

            # Add a new artist
            if select_crud == "create": 
                st.sidebar.subheader("Add New Artist:")
                artist_id = st.sidebar.number_input("Artist ID:", min_value=1)
                artist_name = st.sidebar.text_input("Artist Name:")
                genre_id = st.sidebar.number_input("Genre ID:", min_value=1)

                if st.sidebar.button("Add Artist", key="add_artist_button"):
                    insert_artist(connection, artist_id, artist_name, genre_id)
            elif select_crud == 'delete':
                st.sidebar.subheader("Delete Artist:")
                delete_artist_id = st.sidebar.number_input("Artist ID to delete:", min_value=1)

                if st.sidebar.button("Delete Artist", key="delete_artist_button"):
                   delete_artist(connection, delete_artist_id)        
    
        elif selected_table == "concert":
            # Add concert CRUD operations
            st.sidebar.subheader("Concert CRUD Operations")
            select_crud = st.sidebar.selectbox("CRUD", ["create","delete"])

            # Display all concerts
            st.write("## All Concerts")
            concerts = get_all_concerts(connection)
            st.dataframe(concerts, width=700)

            # Add a new concert
            if select_crud == "create":
                st.sidebar.subheader("Add New Concert:")
                concert_id = st.sidebar.number_input("Concert ID:", min_value=1)
                concert_name = st.sidebar.text_input("Concert Name:")
                artist_id = st.sidebar.number_input("Artist ID:", min_value=1)
                date = st.sidebar.date_input("Date:")
                venue_id = st.sidebar.number_input("Venue ID:", min_value=1)
                concert_group_id = st.sidebar.number_input("Concert Group ID:", min_value=1)
                
                if st.sidebar.button("Add Concert"):
                    insert_concert(connection, concert_id, concert_name, artist_id, date, venue_id, concert_group_id)
            elif select_crud == 'delete':
                st.sidebar.subheader("Delete Concert:")
                delete_concert_id = st.sidebar.number_input("Concert ID to delete:", min_value=1)

                if st.sidebar.button("Delete Concert", key="delete_concert_button"):
                   delete_concert(connection, delete_concert_id)
        
        elif selected_table == "concert_group":
            # Add concert_group CRUD operations
            st.sidebar.subheader("Concert Group CRUD Operations")
            select_crud = st.sidebar.selectbox("CRUD", ["create","delete"])

            # Display all concert groups
            st.write("## All Concert Groups")
            concert_groups = get_all_concert_groups(connection)
            st.dataframe(concert_groups, width=700)

            # Add a new concert group
            if select_crud == "create":
                st.sidebar.subheader("Add New Concert Group:") 
                concert_group_id = st.sidebar.number_input("Concert Group ID:", min_value=1)
                concert_group_name = st.sidebar.text_input("Concert Group Name:")
                
                if st.sidebar.button("Add Concert Group"):
                    insert_concert_group(connection, concert_group_id, concert_group_name)
            elif select_crud == 'delete':
                st.sidebar.subheader("Delete Concert Group:")
                delete_concert_group_id = st.sidebar.number_input("Concert Group ID to delete:", min_value=1)

                if st.sidebar.button("Delete Concert Group", key="delete_group_button"):
                   delete_concert_group(connection, delete_concert_group_id)
                
                
        elif selected_table == "customer":
            # Add customer CRUD operations
            st.sidebar.subheader("Customer CRUD Operations")

            # Display all customers
            st.write("## All Customers")
            customers = get_all_customers(connection)
            st.dataframe(customers, width=700)

            # Add a new customer
            st.sidebar.subheader("Add New Customer:")
            customer_id = st.sidebar.number_input("Customer ID:", min_value=1)
            customer_name = st.sidebar.text_input("Customer Name:")
            email = st.sidebar.text_input("Email:")
            user_name = st.sidebar.text_input("User Name:")
            password = st.sidebar.text_input("Password:", type="password")

            if st.sidebar.button("Add Customer"):
                insert_customer(connection, customer_id, customer_name, email, user_name, password)
                
        elif selected_table == "customer_order":
            # Add customer_order CRUD operations
            st.sidebar.subheader("Customer Order CRUD Operations")
            select_crud = st.sidebar.selectbox("CRUD", ["create","delete"])

            # Display all customer orders
            st.write("## All Customer Orders")
            customer_orders = get_all_customer_orders(connection)
            st.dataframe(customer_orders, width=700)
            if select_crud == "create":
                # Add a new customer order
                st.sidebar.subheader("Add New Customer Order:")
                customer_order_id = st.sidebar.number_input("Customer Order ID:", min_value=1)
                customer_id = st.sidebar.number_input("Customer ID:", min_value=1)
                registered_email_address = st.sidebar.text_input("Registered Email Address:")
                total_price = st.sidebar.number_input("Total Price:", min_value=0.0)
                discount = st.sidebar.number_input("Discount:", min_value=0.0)
                final_price = total_price-discount

                if st.sidebar.button("Add Customer Order"):
                    insert_customer_order(connection, customer_order_id, customer_id, registered_email_address, total_price, discount, final_price)
                

            elif select_crud == 'delete':
                st.sidebar.subheader("Delete Customer Order:")
                delete_order_id = st.sidebar.number_input("Customer order ID to delete:", min_value=1)

                if st.sidebar.button("Delete Customer order", key="delete_order_button"):
                   delete_customer_order(connection, delete_order_id)
            calculate_total_amount(connection)

        elif selected_table == "genre":
            # Add genre CRUD operations
            st.sidebar.subheader("Genre CRUD Operations")

            # Display all genres
            st.write("## All Genres")
            genres = get_all_genres(connection)
            st.dataframe(genres, width=700)

            # Add a new genre
            st.sidebar.subheader("Add New Genre:")
            genre_id = st.sidebar.number_input("Genre ID:", min_value=1)
            genre_name = st.sidebar.text_input("Genre Name:")

            if st.sidebar.button("Add Genre"):
                insert_genre(connection, genre_id, genre_name)
            
        elif selected_table == "order_ticket":
            # Add order_ticket CRUD operations
            st.sidebar.subheader("Order Ticket CRUD Operations")

            # Display all order tickets
            st.write("## All Order Tickets")
            order_tickets = get_all_order_tickets(connection)
            st.dataframe(order_tickets, width=700)

            # Add a new order ticket
            st.sidebar.subheader("Add New Order Ticket:")
            order_ticket_id = st.sidebar.number_input("Order Ticket ID:", min_value=1)
            customer_order_id = st.sidebar.number_input("Customer Order ID:", min_value=1)
            ticket_id = st.sidebar.number_input("Ticket ID:", min_value=1)

            if st.sidebar.button("Add Order Ticket"):
                insert_order_ticket(connection,order_ticket_id, customer_order_id, ticket_id)
            
        elif selected_table == "ticket":
            # Add ticket CRUD operations
            st.sidebar.subheader("Ticket CRUD Operations")

            # Display all tickets
            st.write("## All Tickets")
            tickets = get_all_tickets(connection)
            st.dataframe(tickets, width=700)

            # Add a new ticket
            st.sidebar.subheader("Add New Ticket:")
            ticket_id = st.sidebar.number_input("Ticket ID:", min_value=1)
            serial_number = st.sidebar.text_input("Serial Number:")
            concert_id = st.sidebar.number_input("Concert ID:", min_value=1)
            ticket_category_id = st.sidebar.number_input("Ticket Category ID:", min_value=1)
            seat = st.sidebar.text_input("Seat:")
            purchase_date = st.sidebar.date_input("Purchase Date:")

            if st.sidebar.button("Add Ticket"):
                insert_ticket(connection,ticket_id, serial_number, concert_id, ticket_category_id, seat, purchase_date)

            

        elif selected_table == "ticket_category":
            # Add ticket_category CRUD operations
            st.sidebar.subheader("Ticket Category CRUD Operations")

            # Display all ticket categories
            st.write("## All Ticket Categories")
            ticket_categories = get_all_ticket_categories(connection)
            st.dataframe(ticket_categories, width=700)

            # Add a new ticket category
            st.sidebar.subheader("Add New Ticket Category:")
            ticket_category_id = st.sidebar.number_input("Ticket Category ID:", min_value=1)
            description = st.sidebar.text_input("Description:")
            price = st.sidebar.number_input("Price:", min_value=0.0)
            start_date = st.sidebar.date_input("Start Date:")
            end_date = st.sidebar.date_input("End Date:")
            area = st.sidebar.text_input("Area:")
            concert_id_tc = st.sidebar.number_input("Concert ID:", min_value=1)

            if st.sidebar.button("Add Ticket Category"):
                insert_ticket_category(connection,ticket_category_id, description, price, start_date, end_date, area, concert_id_tc)

            
        elif selected_table == "venue":
            # Add venue CRUD operations
            st.sidebar.subheader("Venue CRUD Operations")
            select_crud = st.sidebar.selectbox("CRUD", ["create","delete", "update"])

            # Display all venues
            st.write("## All Venues")
            venues = get_all_venues(connection)
            st.dataframe(venues, width=700)

            # Add a new venue
            if select_crud == "create":
                st.sidebar.subheader("Add New Venue:")
                venue_id = st.sidebar.number_input("Venue ID:", min_value=1)
                venue_name = st.sidebar.text_input("Venue Name:")
                location = st.sidebar.text_input("Location:")
                venue_type = st.sidebar.text_input("Venue Type:")
                capacity = st.sidebar.number_input("Capacity:", min_value=1)
                
                if st.sidebar.button("Add Venue"):
                    insert_venue(connection,venue_id, venue_name, location, venue_type, capacity)
                
            elif select_crud == "delete":
                # Delete venue CRUD operation
                st.sidebar.subheader("Delete Venue Operation")

                # Delete a venue
                st.sidebar.subheader("Delete Venue:")
                venue_id_to_delete = st.sidebar.number_input("Venue ID to Delete:", min_value=1)
                
                if st.sidebar.button("Delete Venue"):
                    delete_venue(connection, venue_id_to_delete)        
            elif select_crud == "update":
                # Update venue CRUD operation
                st.sidebar.subheader("Update Venue Operation")

                # Update a venue
                st.sidebar.subheader("Update Venue:")
                venue_id_to_update = st.sidebar.number_input("Venue ID to Update:", min_value=1)
                new_venue_name = st.sidebar.text_input("New Venue Name:")
                new_location = st.sidebar.text_input("New Location:")
                new_type = st.sidebar.text_input("New Venue Type:")
                new_capacity = st.sidebar.number_input("New Capacity:", min_value=1)
                
                if st.sidebar.button("Update Venue"):
                    update_venue(connection, venue_id_to_update, new_venue_name, new_location, new_type, new_capacity)
                    
                # Close the database connection
                connection.close()
            
        elif selected_table == "artist--genre":
            # Display the joined data
            st.write("## Joined Data from Artist and Genre Tables")
            joined_data = None
            joined_data = join_artist_genre(connection)
            st.dataframe(joined_data, width=700)

        elif selected_table == "tickets sold":
            st.title("Ticket Sales Information Per Concert")
            tickets_sold_per_concert = get_tickets_sold_per_concert(connection)
            st.write("## Number of Tickets Sold Per Concert")
            st.dataframe(tickets_sold_per_concert, width=700)


if __name__ == '__main__':
    main()
