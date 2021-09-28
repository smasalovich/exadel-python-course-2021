
def create_user(name, surname, age=42,**data):
   
    usercard = {'name': name, 'surname': surname, 'age': age}
    usercard["extra"] = {}
    for key, value in data.items():
        usercard['extra'][key] = value
    return (usercard)


assert create_user("John", "Doe") == {"name": "John","surname": "Doe","age": 42 ,"extra": {} }, "incorrect usercard"

card = create_user("John", "Doe")
print(card)
card = create_user("Bill", "Gates", age=65)
print(card)

card = create_user("Marie", "Curie", age=66, occupation="physicist",won_nobel=True)
print(card)

