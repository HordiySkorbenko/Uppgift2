from collections import Counter
import os

os.system('cls')

values = [1, 2, 3, 6, 4, 4, 8]

most_common_numbers = Counter(values)

most_common = most_common_numbers.most_common(1)[0]
print("mest vanligt är", most_common[0])
print("det är så här många", most_common[1])

most_common_letters = Counter("abcbadfbcb").most_common(3)
print(most_common_letters)
