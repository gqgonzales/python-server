import sqlite3
import json
from models import Animal

ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "Goldendoodle",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 1,
        "customer_id": 1,
    },
    {
        "id": 2,
        "name": "Kaiah",
        "breed": "Huskey",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 2,
        "customer_id": 4,
    },
    {
        "id": 3,
        "name": "Rocky",
        "breed": "Australian Shepherd",
        "status": "Admitted",
        "species": "Dog",
        "customer_id": 3,
        "location_id": 2,
    },
    {
        "id": 4,
        "name": "Keiko",
        "breed": "Huskey",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 2,
        "customer_id": 4,
    },
    {
        "name": "Lupin",
        "breed": "Greyhound",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 1,
        "customer_id": 1,
        "id": 5,
    },
    {
        "name": "Izzy",
        "breed": "Great Dane",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 2,
        "customer_id": 1,
        "id": 6,
    },
    {
        "id": 7,
        "name": "Cuzco",
        "breed": "Chihuahua",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 3,
        "customer_id": 3,
    },
    {
        "name": "Comet",
        "breed": "Rhodesian Ridgeback",
        "species": "Dog",
        "status": "Admitted",
        "location_id": 4,
        "customer_id": 4,
        "id": 8,
    },
]


# def get_all_animals():
#     return ANIMALS

# Function with a single parameter


def get_all_animals():
    # Open a connection to the database, save it as conn
    with sqlite3.connect("./kennel.db") as conn:

        # The type of rows returned when we fetch
        conn.row_factory = sqlite3.Row
        # What let's us execute queries
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.species,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """
        )

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(
                row["id"],
                row["name"],
                row["breed"],
                row["species"],
                row["status"],
                row["location_id"],
                row["customer_id"],
            )
            # Converting an object into a dictionary
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


# def get_single_animal(id):
#     # Variable to hold the found animal, if it exists
#     requested_animal = None

#     # Iterate the ANIMALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for animal in ANIMALS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.species,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(
            data["id"],
            data["name"],
            data["breed"],
            data["species"],
            data["status"],
            data["location_id"],
            data["customer_id"],
        )

        return json.dumps(animal.__dict__)


def get_animals_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.species,
            a.status,
            a.location_id,
            a.customer_id
        from Animal a
        WHERE a.location_id = ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['species'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.species,
            a.status,
            a.location_id,
            a.customer_id
        from Animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['species'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))


# def delete_animal(id):
#     # Initial -1 value for animal index, in case one isn't found
#     animal_index = -1

#     # Iterate the ANIMALS list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Store the current index.
#             animal_index = index

#     # If the animal was found, use pop(int) to remove it from list
#     if animal_index >= 0:
#         ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                species = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


# def update_animal(id, new_animal):
#     # Iterate the ANIMALS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             ANIMALS[index] = new_animal
#             break
