with open("books/frankenstein.txt") as f:
    text = f.read()

word_count = len(text.split())
char_counts = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")

# Your existing code up to the word count print...

# Convert dictionary to list of dictionaries
char_list = []
for char, count in char_counts.items():
    char_list.append({"char": char, "num": count})

# Sort the list by count (remember the sort_on function from the example?)
def sort_on(dict):
    return dict["num"]

char_list.sort(reverse=True, key=sort_on)

# Now try printing each character's count
# Can you write the loop to print each character in the correct format?
for char_dict in char_list:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
print("--- End report ---")