def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

if __name__ == "__main__":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    print("Suma:", add(num1, num2))
    print("Resta:", subtract(num1, num2))
    print("Multiplicación:", multiply(num1, num2))
    print("División:", divide(num1, num2))