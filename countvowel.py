str = input("Enter a sentence:")
vowel_count = {}
for vowel in "aeiou":
    count = str.count(vowel)
    vowel_count[vowel] = count

print(vowel_count)
