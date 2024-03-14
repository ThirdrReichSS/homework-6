# def nearest_number(num, target):
#     numbers = sorted(num, key=lambda x: abs(x - target))
#     return target, numbers
#
#
# result = nearest_number([10, 17, 68, 90, 77], 50)
# print(result)
#
# variants = list(range(0, 50))
# while True:
#     try:
#         index = input('enter your number: ')
#         if index == 'exit':
#             break
#         index = int(index)
#         print(variants[index])
#
#     except IndexError:
#         print(f'enter the numbers from 0 to {len(variants) - 1}')
#
#     except ValueError:
#         print('enter the numbers')
#
# numbers = list(range(1, 20))
#
# mapped_numbers = tuple(map(lambda num: num ** 2, numbers))
# filtered_numbers = list(filter(lambda num: num % 2 == 0, numbers))
#
# print(filtered_numbers)
# print(mapped_numbers)
