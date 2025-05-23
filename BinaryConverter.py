global output
output = ""
global digits
digits = []

def DtoB(n):
    global output
    global digits
    q = n // 2
    r = n % 2
    if len(digits) == 0:
        output += f"{n}/2 = {q}R{r} (LSB)"
    else:
        output += f", {n}/2 = {q}R{r}"
    digits.insert(0, r)
    if q == 0:
        output += " (MSB), Result = "
        for var in digits:
            output += f"{var}"
        print(output)
    else:
        DtoB(q)
        
def BtoD(string):
    global output
    global digits
    sol = 0
    string = string[::-1]
    for i in range(len(string)):
        digit = int(string[i]) * 2 ** i
        sol += digit
        output += f"{string[i]}x2^{i} = {digit}, "
        digits.append(digit)
    output += "Result = "
    for i in range(len(digits)):
        if i == len(digits) - 1:
            output += f"{digits[i]} = {sol}"
            break
        output += f"{digits[i]}+"
    print(output)
print()
print("Benny's Ultimate Decimal/Binary Converter")
while True:
    print()
    cat = input("[D]ecimal or [B]inary Result: ")
    if cat.lower() == "b" or cat.lower() == "binary":
        n = input("Decimal Number(s): ").replace(" ", "").split(",")
        for i in range(len(n)):
            output = f"{chr(ord('a') + i)}. {n[i]}: "
            digits = []
            try:
                DtoB(int(n[i]))
            except:
                output += "Invalid Input"
        continue
    elif cat.lower() == "d" or cat.lower() == "decimal":
        n = input("Binary Number(s): ").replace(" ", "").split(",")
        for i in range(len(n)):
            output = f"{chr(ord('a') + i)}. {n[i]}: "
            digits = []
            BtoD(n[i])
        continue
    else:
        continue
    
    
    