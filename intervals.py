entered_number = int(input("Enter number: "))

def processInput(entered_number):
    if entered_number >= 19 :
        return "True"
    elif entered_number > -15 and entered_number <= 12 :
        return "True"
    elif entered_number > 14 and entered_number < 17 :
        return "True"
    else : 
        return "False"
    
print(processInput(entered_number))
