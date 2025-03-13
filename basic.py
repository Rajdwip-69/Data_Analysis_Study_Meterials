import pandas as pd
data = {
    "Name" : ["Rajdwip","Shivam","Sayak","Raushan","Amit"],
    "Age":[22,18,21,27,21],
    "Salary":[5000,4000,3000,7000,6000],
    "City":["Kolkata","Brindaban","Kolakata","Sbastipur","Jamui"],
    "Performance":[90,67,88,56,77]
}
#Display the Table Data
df = pd.DataFrame(data)
print(df)