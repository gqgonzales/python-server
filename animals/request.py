ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "Goldendoodle",
        "locationId": 1,
        "customerId": 1
    },
    {
        "id": 2,
        "name": "Kaiah",
        "breed": "Huskey",
        "locationId": 2,
        "customerId": 4
    },
    {
        "id": 3,
        "name": "Rocky",
        "breed": "Australian Shepherd",
        "customerId": 3,
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Keiko",
        "breed": "Huskey",
        "locationId": 2,
        "customerId": 4
    },
    {
        "name": "Lupin",
        "breed": "Greyhound",
        "locationId": 1,
        "customerId": 1,
        "id": 5
    },
    {
        "name": "Izzy",
        "breed": "Great Dane",
        "locationId": 2,
        "customerId": 1,
        "id": 6
    },
    {
        "id": 7,
        "name": "Cuzco",
        "breed": "Chihuahua",
        "locationId": 3,
        "customerId": 3
    },
    {
        "name": "Comet",
        "breed": "Rhodesian Ridgeback",
        "locationId": 4,
        "customerId": 4,
        "id": 8
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
