
def create_user(name, surname, age=42,**data):

    assert isinstance(age, int), "incorrect input"

    assert (isinstance(name, str) and isinstance(surname, str)), "incorrect input"
    
    usercard = {'name': name, 'surname': surname, 'age': age}
    usercard["extra"] = {}
    if data.__len__() != 0:
        for key, value in data.items():
            usercard['extra'][key] = value
    return (usercard)

card = create_user("John", "Doe")
print(card)
card = create_user("Bill", "Gates", age=65)
print(card)

card = create_user("Marie", "Curie", age=66, occupation="physicist",won_nobel=True)
print(card)

card = create_user("Marie", "Curie", age="rrrrrr")
print(card)
