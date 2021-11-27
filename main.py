with open("nato_phonetic_alphabet.csv") as file:
    alphabet_main_list = file.read().split("\n")
alphabet_main_list.pop(0)

alphabet_dict = {item[0]: item[2::] for item in alphabet_main_list}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    try:
        new_list = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()
