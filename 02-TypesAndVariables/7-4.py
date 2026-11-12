# sprawdza czy drzewo mozna ściąc na podstawie srednicy pnia drzewa
import math
circumference = float(input("Enter tree circumference in cm: "))
d = circumference / math.pi
can_cut = d >= 50
print(f"Tree diameter: {d:.2f} cm")
print(f"Can the tree be cut down? {can_cut}")
