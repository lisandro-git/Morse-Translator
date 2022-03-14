import utilities as u

morse_alphabet = {
     'a': '.-',
     'b': '-...',
     'c': '-.-.',
     'd': '-..',
     'e': '.',
     'f': '..-.',
     'g': '--.',
     'h': '....',
     'i': '..',
     'j': '.---',
     'k': '-.-',
     'l': '.-..',
     'm': '--',
     'n': '-.',
     'o': '---',
     'p': '.--.',
     'q': '--.-',
     'r': '.-.',
     's': '...',
     't': '-',
     'u': '..-',
     'v': '...-',
     'w': '.--',
     'x': '-..-',
     'y': '-.--',
     'z': '--..'
    }
morse_number   = {
     0: '-----',
     1: '.----',
     2: '..---',
     3: '...--',
     4: '....-',
     5: '.....',
     6: '-....',
     7: '--...',
     8: '---..',
     9: '----.'}
morse_special  = {
    '!': '-.-.--',
    '"': '.-..-.',
    '&': '.-...',
    "'": '.----.',
    '(': '-.--.',
    ')': '-.--.-',
    '+': '.-.-.',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '?': '..--..',
    '@': '.--.-.',
    '_': '..--.-',
    ' ': ' '
}
morse_prosigns = {
    'End of work':            '...-.-',
    'Error':                  '········',
    'Invitation to transmit': '-.-',
    'Starting signal':        '-.-.-',
    'New page signal':        '.-.-.',
    'Understood':             '...-.',
    'Wait':                   '.-...'
}

all_morse_letter = list(morse_alphabet) + \
                   list(morse_number) + \
                   list(morse_special) + \
                   list(morse_prosigns)

all_morse_code = []
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_alphabet.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_number.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_special.items())]
[all_morse_code.append(dit_dah[1]) for dit_dah in list(morse_prosigns.items())]

class word_to_morse:
    def main(self, word: str, led: bool=None):
        if word != "":
            word_as_list = self.split(word)
            translated_string = self.to_morse(word_as_list)
            u.Color.cprint(u.misc.join_list(translated_string), "green")

    def split(self, word: str):
        return [char for char in word];

    def to_morse(self, word_list, led=None):
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
    def main(self, morse: str=None, led: bool=None):
        if morse != "":
            morse_as_list = self.split(morse)
            translated_string = self.translate_morse_letter(morse_as_list, led=led)
            u.Color.cprint(u.misc.join_list(translated_string), "green")
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

    def translate_morse_letter(self, morse_letters: list, led: bool=None) -> list[str]:
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
    u.misc.clear()
    u.Color.cprint(f"{equal * 6} Alphabet {equal * 6} {equal * 6} Numbers {equal * 6}", "yellow")

    alpha_and_num = list(morse_alphabet) + list(morse_number)
    spec_and_pros = list(morse_special)  + list(morse_prosigns)

    for i, letters in enumerate(alpha_and_num):
        if i == len(morse_alphabet):
            break;
        if i <= 9:
            print(f"{letters} \t {morse_alphabet[letters]}  \t\t\t\t {i} {morse_number[i]}")
        else:
            print(f"{letters} \t {morse_alphabet[letters]}")

    u.Color.cprint(f"{equal * 6} Special {equal * 6} {equal * 6} Prosigns {equal * 6}", "yellow")
    for i, letters in enumerate(spec_and_pros):
        if i == len(morse_special):
            break;
        if i < 7:
            print(f"{letters} \t {morse_special[letters]}  \t\t {morse_prosigns[list(morse_prosigns)[i]]} \t {list(morse_prosigns)[i]}")
        else:
            print(f"{letters} \t {morse_special[letters]}")

def main():
    u.misc.clear()
    u.Color.cprint(r"""
   _____                               _________            .___      
  /     \   ___________  ______ ____   \_   ___ \  ____   __| _/____  
 /  \ /  \ /  _ \_  __ \/  ___// __ \  /    \  \/ /  _ \ / __ |/ __ \ 
/    Y    (  <_> )  | \/\___ \\  ___/  \     \___(  <_> ) /_/ \  ___/ 
\____|__  /\____/|__|  /____  >\___  >  \______  /\____/\____ |\___  >
        \/                  \/     \/          \/            \/    \/ 
    """, "green")

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
        u.Color.cprint("Enter a numeric value", "red")
        main()

if __name__ == '__main__':
    main()
