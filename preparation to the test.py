
"""first lesson"""
# monday = float(input('Enter the expenses on monday:'))
# tuesday = float(input('Enter the expenses on tuesday:'))
# wednesday = float(input('Enter the expenses on wednesday:'))
# thursday = float(input('Enter the expenses on thursday:'))
# friday = float(input('Enter the expenses on friday:'))
# saturday = float(input('Enter the expenses on saturday:'))
# sunday = float(input('Enter the expenses on sunday:'))
# summ = (monday + tuesday /
#        + wednesday + thursday + friday + saturday + sunday)
# print('total summ is', summ)
#
# average_expenses = summ / 7
# roundd = round(average_expenses, 1)
# print('average_expenses', round)
# expenses = 0
# counter = 1
#
# while counter != 7+1:
#     print(expenses)
#     expenses += int(input(f'enter expenses for day: {counter}'))
#     counter += 1
#     print(expenses/counter)
#





"""second lesson"""

# counter = 0
# while counter > 7:
#     month = int(input('Whrite your month of birth: '))
#     day = int(input('Whrite your date of birth: '))
#
#     if ( month == 3 and day >= 21 and day <= 31 ) or (month == 4 and day >= 1 and day <= 20 ):
#         print('Aries')
#
#     elif (month == 4 and day >= 21 and day <=30) or (month == 5 and day >= 1 and day <= 21):
#         print('Taurus')
#
#     elif (month == 5 and day >= 22 and day <=31) or (month == 6 and day >= 1 and day <= 21):
#         print('Twins')
#
#     elif (month == 6 and day >= 22 and day <=30) or (month == 7 and day >= 1 and day <= 22):
#         print('Cancer')
#
#     elif (month == 7 and day >= 23 and day <=31) or (month == 8 and day >=1 and day <= 21):
#         print('Leo')
#
#     elif (month == 8 and day >= 22 and day<=31) or (month == 9 and day >=1 and day <= 23):
#         print('Virgo')
#
#     elif (month == 9 and day >= 24 and day <=31) or (month == 10 and day>=1 and day <= 23):
#         print('Scales')
#
#     elif (month == 10 and day >= 24 and day<=31) or (month == 11 and day>=1 and day <= 22):
#         print('Scorpio')
#
#     elif (month == 11 and day >= 23 and day<=31) or (month == 12 and day>=1 and day <= 22):
#         print('Sagitarus')
#
#     elif (month == 12 and day >= 23 and day<=31) or (month == 1 and day >= 1 and day <= 20):
#         print('Carpicorn')
#
#     elif (month == 1 and day >= 21 and day<=31) or (month == 2 and day >= 1 and day <= 19):
#         print('Aquarious')
#
#     elif (month == 2 and day >= 20 and day<=28) or (month == 3 and day >= 1 and day <= 19):
#         print('Fishes')
#     elif (month == 2 and day >=20 and day<=29) or (month ==3 and day>=1 and day<=19):
#         print('Fishes')
#
#     else:
#         print('Incorrect Date Entry')
#     counter += 1
#
# counter = 0
# for day in range (1,8):
#     counter += int(input(f'enter the expenses for {day}: '))




"""Third Lesson"""

# while True:
#     word = input('Whrite your word')
#     if word == "exit":
#         print('exited')
#         break
#     vowels = set('aeyuioауоиэыяюеё')
#     consonants = set('bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ')
#     quantity_of_word = len(word)
#     vowel_count = len([letter for letter in word.lower() if letter in vowels])
#     consonants_count = quantity_of_word - vowel_count
#     vowel_persenctage = round(vowel_count / quantity_of_word * 100, 2)
#     consonants_percentage = round(consonants_count / quantity_of_word * 100, 2)
#     print(f'quantity of the letters: {quantity_of_word} ')
#     print(f'quantity of vowels: {vowel_count}')
#     print(f'quantity of consentanse: {consonants_count}')
#     print(f'persentage of vowels: {vowel_persenctage}')
#     print(f'persentage of consentanse: {consonants_percentage}')


# summ_of_letters = 0
# vowels_counter = 0
# consonants_counter = 0
# # word = input('write your word')
# while True:
#     word = input('write your word')
#     if word == 'exit':
#         print('exited')
#         break
#     for i in word:
#       if i in vowels:
#         vowels_counter += 1
#       elif i in consonants:
#         consonants_counter += 1
#       elif i in summ:
#         summ_of_letters = vowels_counter + consonants_counter
#       # elif word == 'exit':
#       #  print('exited')
#       #  break
#       else:
#         print('word id not detected or the word contain the unknown symbols')
#
# print(word,'your word: ')
# print(summ_of_letters, 'summ of letters in the word: ')
# print(vowels_counter, 'total vowel letters in the word: ')
# print(consonants_counter, 'total cosonants letters in the word: ')







"""forth lesson"""
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# copy = list(data_tuple)
# words = []
# numbers = []
#
#
# for item in copy:
#     if type (item) == str:
#         words.append(item)
#     else:
#         numbers.append(item)
# numbers.remove(6.13)
# numbers.insert(2,2)
#
#
# true = []
# true.append(numbers.pop(0))
# words+=true
#
# numbers = [x**2 for x in numbers]
# numbers.sort()
#
# words.reverse()
# words[1] = 'G'
# words[-2] = 'c'
# words = tuple(words)
# numbers = tuple(numbers)
# print(words)
# print(numbers)


"""Fifth lesson"""
# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
# designations = []
# codes = []
# for item in data:
#     if item.isnumeric():
#         codes.append(item)
#     else:
#         designations.append(item)
#
#
#
# lolo = zip(designations, codes)
# operators = {
#     designations: {codes} for designations, codes in lolo
# }
# del operators['Katel']
# del operators['Fonex']
#
# operators['O!'].update({'0500', '0700'})
# operators['Beeline'].update({'0222', '0777'})
# operators['Megacom'].update({'0999', '0555'})
#
# for i, cat in operators.items():
#     print(i, '=', cat)
#
#
#
# print(operators)
# print(designations)
# print(codes)
#
#
"""sixth lesson"""
# def number(num):
#     if isinstance(num, int):
#         if num % 2 == 0:
#             return True
#         else:
#             return False
#     else:
#         None
# print(number(10))
#
#
#
# def sentece(word):
#     if word[0] == word[0].upper() and word[-1]=='.':
#         return True
#     else:
#         return False
#
# sentences=input('enter your sentence: ')
# print(sentece(sentences))
#
#
# def calculator(num1, operator, num2):
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == '-':
#         print(num1 - num2)
#     elif operator == '*':
#         print(num1 * num2)
#     elif operator == '/':
#         print(num1 / num2)
#     elif operator == '//':
#         print(num1 // num2)
#     elif operator == '**':
#         print(num1 ** num2)
#     else:
#         print('Unknown calculation ')
# calculator(10,'*',2)

# def nearest_number(numbers,target=0):
#     nearest_number = numbers[0]
#     min_difference = abs(target - numbers[0])
#
#
#     for num in numbers:
#         difference = abs(target - num)
#         if difference < min_difference:
#             min_difference = difference
#             nearest_number = num
#     return nearest_number
#
# numbers_list = [3443,4545,5555,6566]
# target_number = 1000
# nearest_number = nearest_number(numbers_list,target_number)
# print(f'{target_number} == {nearest_number}')


"""seventh lesson"""
# def nearest_number(num,target):
#     numbers=sorted(num, key=lambda x: abs(x - target))
#     return target, numbers
# result = nearest_number([10,17,68,90,77], 50)
#
#
#
# variants = list(range(0,50))
# while True:
#      try:
#          index =input('enter your number: ')
#          if index == 'exit':
#              break
#          index = int(index)
#          print(variants[index])
#
#      except IndexError:
#          print(f'enter the numbers from 0 to {len(variants)-1}')
#
#      except ValueError:
#          print('enter the numbers')
#
#
#
#
# numbers = list(range(1,20))
#
# mapped_numbers = tuple(map(lambda num: num **2, numbers))
# filtered_numbers = list(filter(lambda num: num%2==0, numbers))
#
# print(filtered_numbers)
# print(mapped_numbers)















