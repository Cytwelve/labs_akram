def describe_person(name, age=30):
    return(f"{name}, {age}")

person=str(input("Введите ваше имя: "))
# opt=str(input("Желаете Ввести возраст?(да/нет): "))
# if opt=="да":
#     years=str(input("Введите ваш возраст: "))
#     describe_person(person, years)
# else:
#     describe_person(person)
age = input()
if age:
    print(describe_person(person, age))
else:
    print(describe_person(person))
