database = [
    {
        "id": 12345678,
        "town": "Moscow",
        "traffic": 321
    },
    {
        "id": 87654321,
        "town": "Surgut",
        "traffic": 123
    }
]


for date in database:
    if date["id"] == 12345678:
        print(date)
