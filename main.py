import pandas as pd # 13.11.2025
import matplotlib.pyplot as plt # 14.11.2025
import seaborn as sns
import ast

url = "data/movies_metadata.csv"

df = pd.read_csv(url) # df = DataFrame

# print(df.head()) #
# df.info() # виводить інфо без print
# print(df.describe()) #
# print(df.isnull().sum()) #

print(df[["belongs_to_collection", "homepage", "tagline"]])

# print(df.tagline)
# старий варіант
# df["tagline"].fillna("without tagline", inplace=True) #заповнює пропуски 

# Нова альтернатива старому варіантові - НЕ ДОПИСАНО
df["tagline"] = df["tagline"].fillna("without tagline")

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