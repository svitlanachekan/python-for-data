import pandas as pd # 13.11.2025 імпортує бібліотеку pandas і дає їй коротке ім’я pd
import matplotlib.pyplot as plt # 14.11.2025 Імпортується модуль pyplot з бібліотеки matplotlib, який дозволяє створювати графіки.
import seaborn as sns # Це імпорт бібліотеки seaborn, яку будують поверх matplotlib (красивішими,більш інформативними, простішими в побудові)
import ast # Імпортується модуль ast (Abstract Syntax Trees). Перетворює текст, що виглядає як Python-структура (список, словник), у справжню структуру Python.


url = "data/movies_metadata.csv" # Цей рядок зберігає шлях до файлу у змінну url. У даному випадку "data/movies_metadata.csv" — це відносний шлях до CSV-файлу, який знаходиться у папці data.

df = pd.read_csv(url) # df = DataFrame # використовує бібліотеку pandas (скорочено pd); читає CSV-файл за шляхом, який зберігається в url; завантажує дані у змінну df.

# print(df.head()) # Показує перші 5 рядків DataFrame
# df.info() # виводить інфо без print # Показує структуру датафрейму: кількість рядків і стовпців, назви колонок, типи даних (int, float, object…),скільки непорожніх значень у кожній колонці. Це допомагає: побачити, де є пропуски, зрозуміти, які типи треба конвертувати.
# print(df.describe()) # статистичний опис числових колонок: count — скільки значень, mean — середнє значення, std — стандартне відхилення,min, max, Це допомагає: побачити розмахи даних, оцінити аномалії, визначити, чи є надмалі або дуже великі значення.percentiles (25%, 50%, 75%)
# print(df.isnull().sum()) # Показує кількість пропущених значень у кожній колонці. Це корисно для: пошуку проблемних колонок, вирішення, що робити: заповнювати, видаляти чи залишати пропуски.

print(df[["belongs_to_collection", "homepage", "tagline"]]) # виводить на екран лише три вибрані колонки з DataFrame df: belongs_to_collection, homepage, tagline. Gередаємо список з трьох елементів

# print(df.tagline)
# старий варіант
# df["tagline"].fillna("without tagline", inplace=True) #заповнює пропуски 

# Нова альтернатива старому варіантові
# df.fillna({"tagline": "without tagline"}, inplace=True) # Метод fillna() дозволяє замінити пропуски (NaN) у всьому DataFrame або в окремих колонках, тобто у колонці tagline → замінити NaN на "without tagline", інші колонки не змінюються. inplace=True означає змінити DataFrame без створення копії.
df["tagline"] = df["tagline"].fillna("without tagline") # замінює всі пропущені значення (NaN) у колонці tagline на текст "without tagline". Використовують для щоб не мати порожніх значень у колонці; щоб уникнути помилок під час аналізу чи візуалізації; щоб текстова колонка мала однаковий формат; щоб пізніше було легко відфільтрувати фільми без слогану.

print(df.tagline)

# print(df.homepage)
df.homepage = df.homepage.fillna("no homepage")
print(df.homepage)


print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection": "{}"}, inplace=True)
print(df["belongs_to_collection"]) 

df.info()

df.dropna(inplace=True)
print(df.isnull().sum())
df.info()

 # --------#---------

 # 14.11.2025 II part of lesson

def extract_genres(genre_str): # ижимка від наших жанрів,по кожному рядку проходимся, 
# сбір данних, пройдися поз наченнях і передай його: звертаюсь до жарніва, повертай виконати мій код і додаю ексепт через пасс
    try:
      genres = ast .literal_eval(genre_str)
      return [genre['name'] for genre in genres]
    except ValueError:  #задай порожнім списком
      return []
    
print(df['genres'].apply(extract_genres)) 
df['genres'] = df['genres'].apply(extract_genres)


# хочу скористатся другим нодулем: переводить рядки в пайтон-обєкти

# ast = використовуємо для перетворення пайтон-обєкту

# виводимо так, щоб пройтися по ньому, створюємо список: звертаюсь до списочку для яякось окремого жарну в переліку жанру, прозроджусь по них, звертаюсь до кожного і диввлюся ключ і складю новий список. Витягнуто всі слова по імені

# до кожного стовбчика

# ---------#---------
# 14.11.2025 I part of lesson

# print(df.head()) # повертає
# print(df.genres)

all_genres = df['genres'].explode() #створюєтьься список з усіма жарнами і до нього звертась
genres_counts = all_genres.value_counts() # окремо виводимо жари, рахує, строврила змінну, звертаюся до жанрів, хочу , чтоб поархувала скілько жанрів є: порахувати значення і вивести змінну
# print(genres_counts)

# print(genres_counts.index)  # окремо виношу елементи, що там є, щоб врахувати до графіка , додаємо принт , індекс, і передаємо по іксу ,а значення передам по ігреку
# print(genres_counts.values)

plt.figure(figsize=(10,6))  # 2D робимо місце для графіка, розмір задаємо, 10 на 6 одиниц = розмір віконечка, в цьому віконечку, будемо наповнювати, шоу повинно бути останнім = допомагає створити додаткове вікно

plt.title("Count film for genres")
plt.xlabel("genres")
plt.ylabel("counts")

plt.xticks(rotation=45) #  розміщення індекcів = перевертаємо графік під кутом


# sns.barplot(x=genres_counts.index, y=genres_counts.values) # будуємо графік, будує залежніть, по іксу = найменнування, а і по ігреку - значення = кількість

sns.barplot(x=genres_counts.index, y=genres_counts.values)
plt.show()

# це список словників - ми перероблюємо, окремо є кіно, в табличці потрібні жарнри, яким ими користуємося 