import math
from pint import UnitRegistry

operation = input("Enter operation (+, -, *, /, **, //, %, sin, cos, tan, cot, sec, cosec, log, ln, fact, sqrt, per, convert, rad, deg, gradians, temp): ")

# -------------------- Arithmetic Operations --------------------
if operation in ["+", "-", "*", "/", "**", "//", "%"]:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        if num_2 != 0:
            result = num_1 / num_2
        else:
            result = "Not defined"
    elif operation == "**":
        result = num_1 ** num_2
    elif operation == "//":
        result = num_1 // num_2
    elif operation == "%":
        result = num_1 % num_2

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print("Result:", result)

# -------------------- Trigonometric Functions --------------------
elif operation in ["sin", "cos", "tan", "cot", "sec", "cosec"]:
    angle = float(input("Enter angle in degree: "))
    radians = math.radians(angle)

    try:
        if operation == "sin":
            result = math.sin(radians)
        elif operation == "cos":
            result = math.cos(radians)
        elif operation == "tan":
            if angle % 180 == 90:
                result = "Undefined (infinite)"
            else:
                result = math.tan(radians)
        elif operation == "cot":
            result = 1 / math.tan(radians)
        elif operation == "sec":
            result = 1 / math.cos(radians)
        elif operation == "cosec":
            result = 1 / math.sin(radians)

        result = round(result, 4)
        angle_clean = int(angle) if angle.is_integer() else angle
        print(f"{operation}({angle_clean}) = {result}")

    except ZeroDivisionError:
        print(f"{operation}({angle}) is undefined (division by zero)")

# -------------------- Logarithmic --------------------
elif operation in ["log", "ln"]:
    num = float(input("Enter the number: "))
    if num > 0:
        result = math.log10(num) if operation == "log" else math.log(num)
        result = round(result, 4)
        if result.is_integer():
            result = int(result)
        print(f"{operation}({num}) = {result}")
    else:
        print("Error: log is undefined for 0 or negative numbers.")

# -------------------- Factorial --------------------
elif operation == "fact":
    num = float(input("Enter the number: "))
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    elif not num.is_integer():
        print("Error: Factorial is only defined for whole numbers.")
    else:
        result = math.factorial(int(num))
        print(f"Factorial of {int(num)} is {result}")

# -------------------- Square Root --------------------
elif operation == "sqrt":
    num = float(input("Enter the number: "))
    if num < 0:
        print("Error: Negative numbers do not have a real square root.")
    else:
        result = round(math.sqrt(num), 4)
        if result.is_integer():
            result = int(result)
        print(f"Square root of {int(num) if num.is_integer() else num} is {result}")

# -------------------- Percentage --------------------
elif operation == "per":
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    if num_2 == 0:
        print("Not defined")
    else:
        result = (num_1 / num_2) * 100
        print(f"Result is {result}%")

# -------------------- Unit Conversion --------------------
elif operation == "convert":
    from_unit = input("Enter the first unit: ")
    to_unit = input("Enter the second unit: ")
    value = float(input(f"Enter the value in {from_unit}: "))

    try:
        ureg = UnitRegistry()
        quantity = value * ureg(from_unit)
        converted = quantity.to(to_unit)
        result = converted.magnitude
        if result.is_integer():
            result = int(result)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except Exception as e:
        print("Conversion error:", e)

# -------------------- Radian to Degree --------------------
elif operation == "rad":
    num = float(input("Enter the number in degree: "))
    result = round(math.radians(num), 4)
    print(f"{int(num) if num.is_integer() else num} degree = {result} radian")

elif operation == "deg":
    num = float(input("Enter the number in radian: "))
    result = round(math.degrees(num), 4)
    print(f"{num} radian = {result} degree")

# -------------------- Gradians Conversion --------------------
elif operation == "gradians":
    try:
        angle = float(input("Enter the angle: "))
        from_unit = input("Enter the unit (degrees/radians/gradians): ").lower()
        to_unit = input("Convert to (degrees/radians/gradians): ").lower()

        if from_unit == "degrees" and to_unit == "gradians":
            result = (10 / 9) * angle
        elif from_unit == "radians" and to_unit == "gradians":
            result = (200 * angle) / math.pi
        elif from_unit == "gradians" and to_unit == "degrees":
            result = (9 / 10) * angle
        elif from_unit == "gradians" and to_unit == "radians":
            result = (math.pi * angle) / 200
        else:
            print("Error: Invalid conversion!")
            exit()

        result = round(result, 4)
        print(f"{int(angle) if angle.is_integer() else angle} {from_unit} = {result} {to_unit}")

    except ValueError:
        print("Invalid input. Please enter numeric angle value.")

# -------------------- Temperature Conversion --------------------
elif operation == "temp":
    def c_to_f(c): return (c * 9 / 5) + 32
    def f_to_c(f): return (f - 32) * 5 / 9
    def c_to_k(c): return c + 273.15
    def k_to_c(k): return k - 273.15
    def f_to_k(f): return (f - 32) * 5 / 9 + 273.15
    def k_to_f(k): return (k - 273.15) * 9 / 5 + 32

    conversions = {
        "C TO F": c_to_f,
        "F TO C": f_to_c,
        "C TO K": c_to_k,
        "K TO C": k_to_c,
        "F TO K": f_to_k,
        "K TO F": k_to_f,
    }

    print("Supported conversions: C to F, F to C, C to K, K to C, F to K, K to F")
    conversion = input("Enter conversion type (e.g., C to F): ").strip().upper()

    try:
        value = float(input("Enter temperature value: "))
        if conversion in conversions:
            result = conversions[conversion](value)
            from_unit, to_unit = conversion.split(" TO ")
            print(f"{value}° {from_unit} = {round(result, 2)}° {to_unit}")
        else:
            print("Error: Invalid conversion type.")
    except ValueError:
        print("Error: Please enter a valid number.")

# -------------------- Invalid Input --------------------
else:
    print("Invalid input.")
