import pandas as pd # 13.11.2025
import matplotlib.pyplot as plt # 14.11.2025
import seaborn as sns

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


# ---------#---------
# 14.11.2025

# print(df.head()) # повертає
# print(df.genres)


genres_counts = df['genres'].value_counts() # окремо виводимо жари, рахує, строврила змінну, звертаюся до жанрів, хочу , чтоб поархувала скілько жанрів є: порахувати значення і вивести змінну
# print(genres_counts)

# print(genres_counts.index)  # окремо виношу елементи, що там є, щоб врахувати до графіка , додаємо принт , індекс, і передаємо по іксу ,а занчення передам по ігреку
# print(genres_counts.values)

plt.figure(figsize=(10,6))  # 2D міціе для графіка, розмір задаємо, 1-0 на 6 одиниц = розмір вконечка, в цьому віконечку, будемо наповнювати, шоу повинно бути остсннім = допомогає сторити додаткове вікно

plt.title("Count film for genres")
plt.ylabel("genres")
plt.ylabel("counts")

plt.xticks(rotation=45) #  розміщення індескоів = перевертаємо графік під кутом


sns.barplot(x=genres_counts.index, y=genres_counts.values) # будуємо графік, будує залежніть, по іксу = найменнування. і по ігреку - значення = кількість
plt.show()