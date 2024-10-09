import pandas as pd


df = pd.read_csv("amazon\\amazon.csv")
texts = ""
with open ("amazon\\reviews.txt", "w") as f:
    for review in df['Text']:
        f.write(review + '\n')

with open ("amazon\\reviews.txt", "r") as f:
    for line in f.readlines():
        texts += (line + '\n')

