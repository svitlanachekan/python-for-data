import pandas as pd

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
