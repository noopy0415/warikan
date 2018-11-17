total_price = int(input("合計金額をおしえてね(円): "))
number_of_people = int(input("人数を教えてね : "))

print(total_price)

print(total_price / number_of_people)
# print(type(total_price)) # <class 'str'>
# print(type(number_of_people)) # <class 'str'>

print(f"一人あたり {total_price // number_of_people} 円, 端数:{total_price % number_of_people}円")

