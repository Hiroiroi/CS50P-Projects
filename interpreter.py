user_input = input("Expression: ").strip()

x, y, z = user_input.split(" ")

x = float(x)
z = float(z)


match y:
    case "+":
        print(f"{x + z:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
    case "/":
        print(f"{x / z:.1f}")