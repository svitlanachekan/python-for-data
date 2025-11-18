# 18.11.2025

import random # звернись до модуля і знайди файл и дай звідти відповідь
# import random as r # звернись до модуля, наче він r і знайди файл и дай звідти відповідь => r.randrange(5)
# from random import * # звернись до модуля і візьми все => r.randrange(5)
# from random import randrange, randint # видає одне значення, а не весь діапазон, і тільки випадкове, а randin - тільки ціле число; якщо знаємо, що потрібно
# from random import randrange as rr # перейменувати на rr(5); якщо знаємо, що потрібно

comp_choice = random.randint(0,100) # видасть випадкове від 0 до 100
n_count = 0 # відлік спроб починається із 0

#1
# while n_count < 3:
#     try:
#         user_choice = int(input("Enter your number: "))
#     except ValueError:
#         print("Uncorrect number!")
#         continue
#     else:
#         print("Excelent! I remember your number")
#     finally:
#         n_count += 1
#         print(f"Your attempt {n_count}")
#         # print(f"Your choice")
#     if user_choice == comp_choice:
#         print("Congratulations")
#         break
#     print("Try again!")

# 2

while n_count < 3: # застосовуємо цикл для перевірки спроб
    try: # перевіряємо на помилку: чи правильно ввели число 
        user_choice = int(input("Enter your number: ")) 
    except ValueError: # 
        print("Uncorrect number!") # невідповідне значення числа
        continue # продовжує перебір чисел до правильного
    else: # якщо число введено правильно, то 
        print("Excelent! I remember your number") # друкує Excelent! I remember your number
    finally: # закінчується перевірка
        n_count += 1 # починає рахувати спроби: 
        print(f"Your attempt {n_count}") # при 1 напише Your attempt 1
    if user_choice == 13: # перевіряє число відповідність
        print("Congratulations")
        break # зупиняє цикл while
    elif 0 < user_choice < 13: # перевіряє від 0 до 13
        print("Wrong number")
    else: # 
        13 < user_choice < 100
        print("Wrong number")

    print("Try again!")
