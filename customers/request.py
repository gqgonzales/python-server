CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hannah@nss.com"
    },
    {
        "id": 2,
        "name": "Clark Creswell",
        "address": "105 Vienna Ave",
        "email": "clark@nss.com"
    },
    {
        "id": 3,
        "name": "Nancy Nuñez",
        "address": "5 Cadmium Cir",
        "email": "nan@nss.com"
    },
    {
        "email": "gabe@nss.com",
        "address": "1 Infinite Loop",
        "name": "Gabriel Gonzales",
        "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
