import ProductionWorker

usrFName = input("Enter your first name: ")
usrLName = input("Enter your last name: ")
usrShift = input("Enter your shift number: ")
usrWage = input("Enter your hourly pay rate: ")

if usrShift == "1" :
    usrShift = "Day"
elif usrShift == "2":
    usrShift = "Night"
else:
    usrShift = "Incorrect Value"


