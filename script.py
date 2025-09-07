# Roman ↔ Numbers Converter (Human-Friendly Edition)

# Mapping of Roman numerals
roman_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def number_to_roman(num: int) -> str:
    """Convert integer to Roman numeral"""
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman = ""
    for val, sym in values:
        while num >= val:
            roman += sym
            num -= val
    return roman


def roman_to_number(s: str) -> int:
    """Convert Roman numeral to integer"""
    s = s.upper()
    result = 0
    for i, j in zip(s, s[1:]):
        if roman_map[i] < roman_map[j]:
            result -= roman_map[i]
        else:
            result += roman_map[i]
    result += roman_map[s[-1]]
    return result


print("👋 Welcome to the Roman ↔ Numbers Converter!")
print("You can convert in both directions:")
print("  1️⃣  Numbers ➝ Roman numerals")
print("  2️⃣  Roman numerals ➝ Numbers")

choice = input("\n👉 What would you like to do? (1 or 2): ").strip()

if choice == "1":
    num = int(input("\n🔢 Enter a number (1–3999): "))
    print(f"✅ The Roman numeral for {num} is → {number_to_roman(num)}")

elif choice == "2":
    roman = input("\n🔤 Enter a Roman numeral: ")
    print(f"✅ The number for {roman.upper()} is → {roman_to_number(roman)}")

else:
    print("\n⚠️ Oops! That’s not a valid choice. Please restart and pick 1 or 2.")
