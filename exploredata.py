import pandas as pd
data = {
    "Name" : ["Rajdwip","Shivam","Sayak","Raushan","Amit"],
    "Age":[22,18,21,27,21],
    "Salary":[5000,4000,3000,7000,6000],
    "City":["Kolkata","Brindaban","Kolakata","Sbastipur","Jamui"],
    "Performance":[90,67,88,56,77]
}


df = pd.DataFrame(data)
print(df)

# #Top Five Data
# print(df.head(2))

#Last row 

# print(df.tail(1))

#Information about data

# print(df.info())

#Check Null Value in Data
# null_value = df.isnull().sum()


#Check all Description of the table 

# print(df.describe())


#Check the shape of the table 

print(f"Shape:{df.shape}")

print(f"Shape:{df.columns}")


