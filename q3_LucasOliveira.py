import mysql.connector
from mysql.connector import Error

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",      
        user="root",   
        password="12345678", 
        database="sys" 
    )

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# Inicializa o banco de dados e inseri os dados
def setup_database():
    table_queries = [
        """
        CREATE TABLE IF NOT EXISTS COMPANY (
            id_company INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            country VARCHAR(100)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS VIDEOGAMES (
            id_console INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            id_company INT,
            release_date DATE,
            FOREIGN KEY (id_company) REFERENCES COMPANY(id_company)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS USERS (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            country VARCHAR(100),
            id_console INT,
            FOREIGN KEY (id_console) REFERENCES VIDEOGAMES(id_console)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS GAMES (
            id_game INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            genre VARCHAR(100),
            release_date DATE,
            id_console INT,
            FOREIGN KEY (id_console) REFERENCES VIDEOGAMES(id_console)
        );
        """,
        """INSERT INTO COMPANY (name, country) VALUES ('Nintendo', 'Japan');""",
        """INSERT INTO VIDEOGAMES (name, id_company, release_date) VALUES ('Nintendo Switch', LAST_INSERT_ID(), '2017-03-03');""",
        """INSERT INTO USERS (name, country, id_console) VALUES ('John Doe', 'USA', LAST_INSERT_ID());""",
        """INSERT INTO GAMES (title, genre, release_date, id_console) VALUES ('The Legend of Zelda: Breath of the Wild', 'Action-adventure', '2017-03-03', LAST_INSERT_ID());"""
    ]

    connection = connect_to_db()
    if connection.is_connected():
        for query in table_queries:
            execute_query(connection, query)
        connection.close()

if __name__ == '__main__':
    setup_database()
