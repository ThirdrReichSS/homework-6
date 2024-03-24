import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


create_table_countries = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
'''

connection.execute(create_table_countries)
connection.commit()


def additions_countries():
    insert_countries = '''
    INSERT INTO countries (title)
    VALUES (?);
    '''
    countries = [
        ('Netherlands',),
        ('Germany',),
        ('UAE',)
    ]
    cursor.executemany(insert_countries, countries)
    connection.commit()

additions_countries()

create_table_cities = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area TEXT DEFAULT '0',
    country_id INTEGER REFERENCES countries(id)
);
'''

connection.execute(create_table_cities)
connection.commit()

def additions_cities():
    insert_cities = '''
    INSERT INTO cities (title, area, country_id)
    VALUES (?, ?, ?);
    '''
    cities = [
        ('Amsterdam', '89 kм²', 1),
        ('Dusseldorf', '89 kм²', 2),
        ('Abu_Dhabi', '55 kм²', 3),
        ('Texel', '65 kм²', 1),
        ('Dubai', '67 kм²', 3),
        ('Munchen', '110,7 kм²', 2),
        ('Essen', '35,2 kм²', 2)
    ]
    cursor.executemany(insert_cities, cities)
    connection.commit()

additions_cities()

create_table_employees = '''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER INTEGER REFERENCES cities(id)
    );
    '''
connection.execute(create_table_employees)
connection.commit()

def additions_emploees():
    insert_employees = '''
    INSERT INTO employees (first_name, last_name, city_id)
    VALUES (?, ?, ?);
    '''
    employees = [
    ("Adolf", "Hitler", 2),
    ("Nikola", "Tesla", 2),
    ("Benito", "Mussolini", 1),
    ("Greta", "Tunberg", 3),
    ("Almazbek", "Bakiev", 7),
    ("Josef", "Stalin", 3),
    ("Bill", "Schifpr", 1),
    ("Luxury", "Girl", 4),
    ("Sweetie", "Fox", 6),
    ("Tera", "Lee", 3),
    ("Sasha", "Grey", 5),
    ("Lana", "Rhoades", 1),
    ("Emilly", "Wheelies", 7),
    ("Sadyr", "Tashiev", 4)
]

    cursor.executemany(insert_employees, employees)
    connection.commit()

# additions_emploees()


def list_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]} - {city[1]}")

def employees_in_city(city_id):
    join_f = '''
    SELECT e.first_name, e.last_name, c.title AS city_name, c.area, co.title AS country_name
    FROM employees e
    JOIN cities c ON e.city_id = c.id
    JOIN countries co ON c.country_id = co.id
    WHERE c.id = ?
    '''
    cursor.execute(join_f, (city_id,))
    employees = cursor.fetchall()
    for employee in employees:
        print(f"Name: {employee[0]}, Surname: {employee[1]}, City: {employee[2]}, Capital: {employee[3]}, Country: {employee[4]}")


while 1:
    print("You can see a list of employees according to the id of the choosen city")
    print("From the list below:")
    list_cities()

    input_id = int(input(" Enter the id of the city(print 'exit' to break the programm): "))

    if input_id == 0:
        break

    employees_in_city(input_id)

connection.close()