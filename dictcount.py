str = input("Enter a sentence:")
vowel_counts = {}

for vowel in "aeiou":
    count = str.count(vowel)
    vowel_counts[vowel] = count
print(vowel_counts)
