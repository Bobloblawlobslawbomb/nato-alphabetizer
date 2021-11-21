with open("nato_phonetic_alphabet.csv") as file:
    alphabet_main_list = file.read().split("\n")
alphabet_main_list.pop(0)

alphabet_dict = {item[0]: item[2::] for item in alphabet_main_list}

user_word = input("Enter a word: ").upper()

new_list = [alphabet_dict[letter] for letter in user_word]

print(new_list)
