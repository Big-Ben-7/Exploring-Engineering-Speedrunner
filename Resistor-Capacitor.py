firstColors = {
    "black": 0, 
    "brown": 1, 
    "red": 2, 
    "orange": 3, 
    "yellow": 4, 
    "green": 5, 
    "blue": 6, 
    "purple": 7, 
    "violet": 7, 
    "gray": 8, 
    "grey": 8, 
    "white": 9
}
multipliers = {
    "silver": 0.01,
    "gold": 0.1,
    "black": 1, 
    "brown": 10, 
    "red": 100, 
    "orange": 1000, 
    "yellow": 10000, 
    "green": 100000, 
    "blue": 1000000, 
    "purple": 10000000, 
    "violet": 10000000, 
    "gray": 100000000,
    "grey": 100000000, 
    "white": 1000000000
}
resistanceTolerances = {
    "white": 20,
    "gray": 10,
    "grey": 10,
    "silver": 10,
    "gold": 5
}
capacitorTolerances = {
    "A": [0.05],
    "B": [0.1],
    "C": [0.25],
    "D": [0.5],
    "F": [1],
    "G": [2],
    "J": [5],
    "K": [10],
    "M": [20],
    "NONE": [20],
    "N": [30],
    "Q": [-10, 30],
    "S": [-20, 50],
    "T": [-10, 50],
    "Z": [-20, 80]
}

while True:
    print()
    cat = input("[R]esistor or [C]apacitor: ").lower().replace(" ", "")
    if cat == "r" or cat == "resistor":
        color1 = input("Band 1 Color: ").lower().replace(" ", "")
        if color1 == "": continue
        color2 = input("Band 2 Color: ").lower().replace(" ", "")
        if color2 == "": continue
        color3 = input("Band 3 Color: ").lower().replace(" ", "")
        if color3 == "": continue
        color4 = input("Band 4 Color: ").lower().replace(" ", "")
        if color4 == "": continue
        resistance = (firstColors[color1] * 10 + firstColors[color2]) * multipliers[color3]
        unit = "Ω"
        if resistance >= 1000:
            resistance /= 1000
            unit = "kΩ"
        tolerance = resistanceTolerances[color4]
        minValue = round(resistance * (1 - tolerance / 100), 3)
        maxValue = round(resistance * (1 + tolerance / 100), 3)
        print()
        print(f"Resistance: {resistance}{unit}")
        print(f"Tolerance: +-{tolerance}%")
        print(f"Tolerance Range: {minValue}{unit}/{maxValue}{unit}")
    elif cat == "c" or cat == "capacitor":
        n1 = int(input("Digit 1: "))
        if n1 == "": continue
        n2 = int(input("Digit 2: "))
        if n2 == "": continue
        n3 = int(input("Digit 3: "))
        if n3 == "": continue
        letter = input("Letter (or 'none'): ").upper().replace(" ", "")
        if letter == "": continue
        print()
        capacitance = (n1 * 10 + n2) * 10 ** n3
        unit = "pF"
        if capacitance >= 1000:
            capacitance /= 1000000
            unit = "µF"
        print(f"Capacitance: {capacitance}{unit}")
        tolerance = capacitorTolerances[letter]
        if len(tolerance) == 1:
            print(f"Tolerance: +-{tolerance[0]}%")
        else:
            print(f"Tolerance: {tolerance[0]}%, +{tolerance[1]}%")
    else: continue