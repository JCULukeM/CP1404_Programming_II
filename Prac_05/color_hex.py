

COLOR_CODE = {"BLUE": "#0000ff", "CORAL": "#ff7f50", "WHITESMOKE": "#f5f5f5",
              "RED": "#ee0000"}

color = input("Enter color: ").upper()
while color != "":
    if color in COLOR_CODE:
        print(color, "is",COLOR_CODE[color])
    else:
        print("Invalid short color")
    color = input("Enter color name: ").upper()