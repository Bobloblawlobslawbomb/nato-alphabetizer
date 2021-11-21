with open("nato_phonetic_alphabet.csv") as file:
    alphabet_main_list = file.read().split("\n")
alphabet_main_list.pop(0)
