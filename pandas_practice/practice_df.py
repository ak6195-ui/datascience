import pandas as pd
employe=pd.DataFrame({ "Emp_ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    "Name": ["Ram","Hari","Sita","Gita","Mina","John","Rita","Amit","Nita","Rohan","Suman","Anita","Bibek","Roshan","Puja"],
    "Department": ["IT","HR","IT","Sales","HR","IT","Finance","Sales","Finance","HR","IT","Sales","Finance","IT","HR"],
    "City": ["Kathmandu","Pokhara","Kathmandu","Butwal","Pokhara","Kathmandu","Biratnagar","Butwal","Biratnagar","Pokhara","Kathmandu","Butwal","Biratnagar","Kathmandu","Pokhara"],
    "Age": [24,29,31,27,26,35,32,28,30,33,25,29,34,38,27],
    "Experience": [2,5,7,3,2,10,8,4,6,9,1,5,11,12,3],
    "Salary": [45000,55000,85000,50000,48000,120000,90000,65000,95000,70000,42000,60000,100000,130000,52000],
    "Performance": [85,75,92,80,70,98,88,82,90,76,68,84,94,99,78],
    "Gender": ["M","M","F","F","F","M","F","M","F","M","M","F","M","M","F"]})
print(employe)
print(employe.head(5))
print(employe.tail(3))
print(employe.shape)
print(employe.columns)
print(employe.info())
print(employe.isnull().sum())
print(employe.loc[:,["Name","Salary"]])
print("\n")
print(employe[employe["Salary"]>70000].loc[:,["Name","Salary"]])
print(employe[employe["Department"]=="IT"])
print(employe[employe["Age"]<30].loc[:,["Name","Age"]])
#LEVEL-2 ----------------------------------------------
#FILTERING
print(employe[employe["City"]=="Kathmandu"].loc[:,["Name","City"]])
print(employe[(employe["City"]=="Kathmandu")&(employe["Department"]=="IT")])
print(employe[(employe["Salary"]>50000)&(employe["Salary"]<90000)])
print(employe[(employe["Age"]>30)&(employe["Experience"]>5)])
print(employe[(employe["Gender"]=="F")&(employe["Department"]=="Finance")])
print(employe[employe["Performance"]>90])
print(employe[employe["Name"].str.startswith("R")].loc[:,"Name"])
print(employe[employe["Name"].str.endswith("a")].loc[:,"Name"])
#LEVEL-3----------------------------------------------
print(employe.sort_values(by="Salary"))
print(employe.sort_values(["Salary"],ascending=False))
print(employe.sort_values(["Department","Salary"]))
print(employe.sort_values("Salary",ascending=False).head(5))
print(employe.sort_values("Age").head(1))
#LEVEL-4-----------------------------------------------
print(employe["Salary"].mean())
print(employe[employe["Salary"]==employe["Salary"].max()])
print(employe[employe["Salary"]==employe["Salary"].min()])
print(f"TOTAL SALARY PAID BY COMPANY: {employe["Salary"].sum()}")
print(f"THE TOTAL NUMBER OF EMPLOYE ARE {len(employe)}")
print(f"THE STANDARD DEVIATION OF THE SALARY IS :{employe["Salary"].std()}")
#LEVEL-5-----------------------------------------------
department=employe.groupby("Department")
print(department["Salary"].mean())
print(department["Salary"].max())
print(department.size())
print(department["Performance"].mean())
city=employe.groupby("City")
print(city["Salary"].sum())
print(city["Experience"].mean())
print(employe.sort_values("Salary",ascending=False).groupby("Department").first())
print(employe.sort_values("Salary",ascending=False).groupby("Department")["Salary"].mean().head(1))
print(employe.groupby("Gender").size())
print(employe.groupby("Gender")["Salary"].mean())
#level-6------------------------------------------------
employe["BONUS"]=employe["Salary"].apply(lambda x: ((10/100)*x)+x)
print(employe)
print(employe["BONUS"])
def tax_add(group):
    if group["Salary"]>100000:
        return (20/100)*group["Salary"]
    elif group["Salary"]>70000:
        return (15/100)*group["Salary"]
    else :
        return (10/100)*group["Salary"]
employe["Tax"]=employe.apply(tax_add,axis=1)
print(employe)
employe["NET"]=employe["Salary"]+employe["BONUS"]
print(employe)
def grade(group):
    if group["Performance"]>90:
        return f"EXCELLENT"
    elif group["Performance"]>80 & group["Performance"]<89:
        return f"GOOD"
    elif group["Performance"]>70 & group["Performance"]<60:
        return f"AVERAGE"
    else: 
        return f"POOR"
employe["GRADE"]=employe.apply(grade,axis=1)    
print(employe)
#LEVEL-8------------------------------------------------
print(department["Salary"].max().head(1))
print(city["Salary"].mean().sort_values(ascending=False).head(1))
print(employe.sort_values("Salary",ascending=False).head(1))
# print(employe.sort_values("Performance",ascending=False).groupby("Department").first())
print(employe.groupby("Department")["Performance"].sum().sort_values(ascending=False))
#print(department[department.size()>3])
