#Dictionaries
monthConversions = {

    "Jan": "Janury",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",  
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

mon=input("Enter the month of 3 letter short form: ")
mon = mon.capitalize()

if mon in monthConversions:
    print(monthConversions[mon])
else:
    print("Invalid month")
