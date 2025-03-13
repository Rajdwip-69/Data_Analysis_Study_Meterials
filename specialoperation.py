import pandas as pd
data = {
    "Name" : ["Rajdwip","Shivam","Sayak","Raushan","Amit"],
    "Age":[22,18,21,27,21],
    "Salary":[5000,4000,3000,7000,6000],
    "City":["Kolkata","Brindaban","Kolakata","Sbastipur","Jamui"],
    "Performance":[90,67,88,56,77]
}


df = pd.DataFrame(data)

# column = df["Name"]
# print(column)

# subset = df[["Name","Salary"]]
# print(subset)

#Filtering the Data

# filtering_rows = df[df["Salary"]>5000]
# print(filtering_rows)

#Multiple Condition

filtering_rows = df[(df["Salary"]>5000) & (df["Age"]>25)]
print(filtering_rows)