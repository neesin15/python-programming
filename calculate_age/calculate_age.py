from datetime import date
 
def calculateAge(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
 
    return age
     
print(f"You are now {calculateAge(date(1980, 2, 15))} years old")
