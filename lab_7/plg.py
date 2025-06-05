from lab_7 import finite_automaton_search

f = open(r"random_text.txt")
haystack = f.read()
needle = "AFDB"
result = finite_automaton_search(haystack, needle)

print(f"Знайдено {len(result)} збігів")
print("Індекси входжень:", result)  