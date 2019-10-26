db = {
    "person": {
        "name": ["Vladimir", "Maryia"],
        "lname": ["Ivanov", "Sidorova"],
        "inn": ["123", "332"]
    },
    "employment": {
        "firm": ["Firm 1", "Firm 2", "Firm 2", "Firm 3"],
        "person_inn": ["123", "123", "332", "332"]
    }
}

people = list(map(list, zip(*[db.get("person").get("name"),db.get("person").get("lname"),db.get("person").get("inn")])))
empl=list(map(list, zip(*[db.get("employment").get("firm") , db.get("employment").get("person_inn")])))
print(people)
print(empl)
for i in (set((db.get("employment")).get("person_inn"))&set((db.get("person")).get("inn"))    ):

    print(i)