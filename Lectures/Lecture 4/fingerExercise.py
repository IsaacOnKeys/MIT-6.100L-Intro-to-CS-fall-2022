myInteger = 27

guess = 0

while guess**3 < myInteger:
    guess += 1
    print(f"guess: {guess}, guess**3: {guess**3}")  # Debugging statement

if guess**3 == myInteger:
    print(f"The cube root of {myInteger} is {guess}")
else:
    print(f"{myInteger} is not a perfect cube :(")
