
EMPLOYEES = [

    {
        "id": 1,
        "name": "Emma Beaton",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Carla Ruidiaz",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Jeremy Bakker",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Nora Clement",
        "locationId": 2
    },
    {
        "id": 7,
        "name": "Merlyn Wood",
        "locationId": 4
    },
    {
        "name": "Matt Champion",
        "locationId": 3,
        "id": 8
    }

]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
