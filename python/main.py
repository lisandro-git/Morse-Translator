import json
import os

with open(os.path.join(os.path.dirname(__file__), 'morse_code.json'), "r") as f:
    morse_code = json.load(f)
f.close()

morse_alphabet = morse_code["alphabet"]
morse_number   = morse_code["number"]
morse_special  = morse_code["special"]
morse_prosigns = morse_code["prosigns"]

all_morse_letter = list(morse_alphabet) + \
                   list(morse_number)   + \
                   list(morse_special)  + \
                   list(morse_prosigns)

all_morse_code = []
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_alphabet.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_number.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_special.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_prosigns.items())]

def join_list(word: str, sep: str="") -> str:
    return sep.join(str(x) for x in word);

class word_to_morse:
    def main(self, word: str):
        if word != "":
            word_as_list = self.split(word)
            translated_string = self.to_morse(word_as_list)
            print(join_list(translated_string))

    def split(self, word: str):
        return [char for char in word];

    def to_morse(self, word_list):
        result = []
        i = 0
        j = 0 # edode : Used to get the morse code of the character
        while (i < len(word_list)):
            if word_list[i] in all_morse_letter or word_list[i] == " ":
                if word_list[i] == all_morse_letter[j]:
                    result.append(all_morse_code[j] + "  ") # 19111999
                    j = 0
                    i += 1
                else:
                    j += 1
            else:
                i += 1
        return result;

class morse_to_word:
    def main(self, morse: str=None):
        if morse != "":
            morse_as_list = self.split(morse)
            translated_string = self.translate_morse_letter(morse_as_list)
            print(join_list(translated_string))
        else:
            main()

    def split(self, morse: str) -> list[str]:  # split the string into a list
        morse_as_list = []
        morse_letter = ""
        i = 0
        morse += " " # edode : in order to add the last character to the list
        for char in morse:
            # edode : the loop reads the string letter by letter and adds it to the list as soon as it found a morse letter
            if char == " ":
                if len(morse_letter) != 0:
                    morse_as_list.append(morse_letter)
                    morse_letter = ""
                    continue;
            if morse[-1] == "." or morse[-1] == "-" or morse[-1] == " ":
                if i + 1 == len(morse):
                    morse_letter += char
                    morse_as_list.append(morse_letter) # edode : adding the morse letter to the list
                    morse_letter = ""
            if morse_letter == " ": # edode : adding the space to the list
                morse_as_list.append(morse_letter)
                morse_letter = ""
            morse_letter += char
            i += 1
        return morse_as_list;  # word is returned as a list, 1 letter being 1 element of a list

    def translate_morse_letter(self, morse_letters: list) -> list[str]:
        result = []
        i = 0
        j = 0
        while i < len(morse_letters):
            if morse_letters[i] in all_morse_code or morse_letters[i] == " ":
                if morse_letters[i] == all_morse_code[j]:
                    result.append(all_morse_letter[j])
                    j = 0
                    i += 1
                else:
                    j += 1
            else:
                i += 1
        return result;

def show_alphabet():
    equal = "="
    print(f"{equal * 6} Alphabet {equal * 6} {equal * 6} Numbers {equal * 6}")

    alpha_and_num = list(morse_alphabet) + list(morse_number)
    spec_and_pros = list(morse_special)  + list(morse_prosigns)

    for i, letters in enumerate(alpha_and_num):
        if i == len(morse_alphabet):
            break;
        if i <= 9:
            print(f"{letters} \t {morse_alphabet[letters]}  \t\t\t\t {i} {morse_number[str(i)]}")
        else:
            print(f"{letters} \t {morse_alphabet[letters]}")

    print(f"{equal * 6} Special {equal * 6} {equal * 6} Prosigns {equal * 6}")
    for i, letters in enumerate(spec_and_pros):
        if i == len(morse_special):
            break;
        if i < 7:
            print(f"{letters} \t {morse_special[letters]}  \t\t {morse_prosigns[list(morse_prosigns)[i]]} \t {list(morse_prosigns)[i]}")
        else:
            print(f"{letters} \t {morse_special[letters]}")

def main():
    print(r"""
   _____                               _________            .___      
  /     \   ___________  ______ ____   \_   ___ \  ____   __| _/____  
 /  \ /  \ /  _ \_  __ \/  ___// __ \  /    \  \/ /  _ \ / __ |/ __ \ 
/    Y    (  <_> )  | \/\___ \\  ___/  \     \___(  <_> ) /_/ \  ___/ 
\____|__  /\____/|__|  /____  >\___  >  \______  /\____/\____ |\___  >
        \/                  \/     \/          \/            \/    \/ 
    """)

    choice_list = [
        "Word to Morse",
        "Morse to Word",
        "Display the Alphabet",
        "Exit"
    ]
    [print(f"{i+1}) {choice}") for i, choice in enumerate(choice_list)]

    wtm = word_to_morse()
    mtw = morse_to_word()

    try:
        choice = int(input(""))
        if choice == 1:
            word = input("Enter your word : ")
            wtm.main(word.lower())
        elif choice == 2:
            word = input("Enter your morse code : ")
            mtw.main(word.lower())
        elif choice == 3:
            show_alphabet()
        elif choice == 4:
            exit()

        input("Enter to continue...")
        main()
    except KeyboardInterrupt:
        exit()
    except ValueError:
        print("Enter a numeric value")
        main()

if __name__ == '__main__':
    main()
