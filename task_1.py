def divide(div, denom):
    return div / denom


divider = float(input("Enter divider: "))
while True:
    denominator = float(input("Enter denominator: "))
    if denominator == 0:
        print("Denominator should not be 0")
    else:
        print(f"Result = {divide(divider,denominator) :.2f}")
        break
