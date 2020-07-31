kelv = ["K", "Kelvin"]
cels = ["°C", "C", "Celsius"]
fahren = ["°F", "F", "Fahrenheit"]
rank = ["°R", "°Ra", "R", "Ra", "Rankine"]
reau = ["°Ré", "°Re", "Re", "Ré", "Reaumur", "Réaumur"]

kelv2 = ["k", "kelvin"]
cels2 = ["°c", "c", "celsius"]
fahren2 = ["°f", "f", "fahrenheit"]
rank2 = ["°r", "°ra", "r", "ra", "rankine"]
reau2 = ["°re", "re", "°ré", "ré", "réaumur", "reaumur"]

units = [kelv, cels, fahren, rank, reau]
unitsList = []
for u in units:
    for item in u:
        unitsList.append(item.lower())

def currentKelv(unit, temp):
    if unit in kelv2:
        temp2 = temp
        return temp2
    elif unit in cels2:
        temp2 = temp - 273.15
        return temp2
    elif unit in fahren2:
        temp2 = (temp - 273.15) * 9/5 + 32
        return temp2
    elif unit in rank2:
        temp2 = temp * 1.8
        return temp2
    elif unit in reau2:
        temp2 = (temp - 273.15) * 1.8
        return temp2

def currentCels(unit, temp):
    if unit in kelv2:
        temp2 = temp + 273.15
        return temp2
    elif unit in cels2:
        temp2 = temp
        return temp2
    elif unit in fahren2:
        temp2 = (temp * 9/5) + 32
        return temp2
    elif unit in rank2:
        temp2 = temp * 9/5 + 491.67
        return temp2
    elif unit in reau2:
        temp2 = temp * 0.8
        return temp2

def currentFahren(unit, temp):
    if unit in kelv2:
        temp2 = (temp - 32) * 5/9 + 273.15
        return temp2
    elif unit in cels2:
        temp2 = (temp - 32) * 5/9
        return temp2
    elif unit in fahren2:
        temp2 = temp
        return temp2
    elif unit in rank2:
        temp2 = temp + 459.67
        return temp2
    elif unit in reau2:
        temp2 = (temp -32)/2.25
        return temp2

def currentRank(unit, temp):
    if unit in kelv2:
        temp2 = temp * 5/9
        return temp2
    elif unit in cels2:
        temp2 = (temp - 491.67) * 5/9
        return temp2
    elif unit in fahren2:
        temp2 = temp - 459.67
        return temp2
    elif unit in rank2:
        temp2 = temp 
        return temp2
    elif unit in reau2:
        temp2 = (temp - 491.67) * 4/9
        return temp2

def currentRank(unit, temp):
    if unit in kelv2:
        temp2 = temp * 5/9
        return temp2
    elif unit in cels2:
        temp2 = (temp - 491.67) * 5/9
        return temp2
    elif unit in fahren2:
        temp2 = temp - 459.67
        return temp2
    elif unit in rank2:
        temp2 = temp 
        return temp2
    elif unit in reau2:
        temp2 = (temp - 491.67) * 4/9
        return temp2

def currentReau(unit, temp):
    if unit in kelv2:
        temp2 = temp * 1.25 + 273.15
        return temp2
    elif unit in cels2:
        temp2 = temp * 1.25
        return temp2
    elif unit in fahren2:
        temp2 = temp * 2.25 + 32
        return temp2
    elif unit in rank2:
        temp2 = temp * 2.25 + 32 + 459.67
        return temp2
    elif unit in reau2:
        temp2 = temp
        return temp2

def convert(current, new, num):
    if current in kelv2:
        newTemp = currentKelv(new, num)
        return newTemp
    elif current in cels2:
        newTemp = currentCels(new, num)
        return newTemp
    elif current in fahren2:
        newTemp = currentFahren(new, num)
        return newTemp
    elif current in rank2:
        newTemp = currentRank(new, num)
        return newTemp
    elif current in reau2:
        newTemp = currentReau(new, num)
        return newTemp

def unit(current):
    unit1 = ""
    unit2 = ""
    current = current[0].upper() + current[1:]
    for u in units:
        if current in u:
            unit1 = u[-1]
            unit2 = u[0]
            break
    return unit1, unit2

def main(current, new, temp1, temp2):
    current, cUnit = unit(currentUnit.lower())
    new, nUnit = unit(newUnit.lower())
    print("\n***")
    print(f"Temperature in {current}: {temp1:.2f} {cUnit}")
    print(f"Temperature in {new}: {temp2:.2f} {nUnit}")
    print("\n***")
    
userCont = input("To exit type 'END': \n")
while userCont.lower() != "end":
    currentUnit = input("Please enter the current unit of temperature you have.\n")
    while currentUnit.lower() not in unitsList:
        print("Please enter an existing unit of temperature.")
        currentUnit = input("Please enter the current unit of temperature you have.\n")
    newUnit = input("Please enter the unit of conversion.\n")
    while newUnit.lower() not in unitsList:
        print("Please enter an existing unit of temperature.")
        newUnit = input("Please enter the unit of conversion.\n")
    temp = input("Please enter the temperature.\n")
    while temp.isnumeric() == False:
        print("Please enter a valid integer or decimal number for the temperature.")
        temp = input("Please enter the temperature.\n")
    temp = float(temp)
    final = convert(currentUnit.lower(), newUnit.lower(), temp)
    main(currentUnit, newUnit, temp, final)
    userCont = input("To exit type 'END': \n")
print("The program has ended.")
