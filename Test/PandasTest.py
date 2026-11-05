import pandas as pd

data = {
    "Name": ["Dara", "Sok", "John"],
    "Age": [20, 21, 22],
    "Major": ["Data Science", "IT", "Computer Science"]
}

df = pd.DataFrame(data)

print(df)