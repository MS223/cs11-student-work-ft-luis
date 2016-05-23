action = raw_input("What would you like to do?")
day = raw_input("What day?").capitalize()
days_of_week = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday"[],
    "Thursday"[],
    "Friday"[],
    "Saturday"[],
    "Sunday"[],
}

def add():
    # Should get our action variable and add it to our dictionary days_of_week with the key day
    days_of_week[day] = action
  
