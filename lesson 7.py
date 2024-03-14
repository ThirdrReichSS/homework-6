#lambda function, работа с исключениям
# def up_letter(word: str):
#     return word.title()
# def show_words(func, iterable):
#     for i in iterable:
#         print(func(i))
#
# cities = ['tokmok', 'karakol', 'london']
# # show_words(up_letter,citites)
# # show_words(len, ['kant', 'balykchy', 'talas'])
# show_words(lambda word: word.title(), cities)
# numbers = list(range(1, 16))
# print(numbers)
#
# # filtered_numbers = list(filter(lambda num: num >= 10, numbers))
# # print(filtered_numbers)
# mapped_numbers = tuple(map(lambda num: num /2, numbers))
# print(mapped_numbers)


# regions = {
#     'chui': 6,
#     'naryn': 4,
#     'talas': 2,
#     'batken':3,
#     'jalal-abad': 3,
#     'yssyk-kul':3,
#     'osh': 2
# }
#
#fcfcd=
# sorted_regions = sorted(regions.items, key=lambda x: x)
# print(sorted_regons)


def get_data(name, surname='Unknown'):  # required positional parameter
    print(f'name: {name} surname: {surname}')

get_data('Azamat', 'Umarbekov')  # required positional argument
get_data(surname='Akmatov', name='Tilek')  # keyword arguments
get_data('Leo')
get_data(name=input('name: '), surname=input('sunmame: '))
