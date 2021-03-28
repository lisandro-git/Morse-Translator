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
    'space': '" "'
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

list_char = list(morse_alphabet) +\
            list(morse_number)   +\
            list(morse_special)  +\
            list(morse_prosigns)
mlist_char = []

[mlist_char.append(dit_dah[1]) for dit_dah in list(morse_alphabet.items())]
[mlist_char.append(dit_dah[1]) for dit_dah in list(morse_number.items())]
[mlist_char.append(dit_dah[1]) for dit_dah in list(morse_special.items())]
[mlist_char.append(dit_dah[1]) for dit_dah in list(morse_prosigns.items())]


class word_to_morse:
    def main(ltr, led=None):
        if (ltr != ""):
            li = word_to_morse.split(ltr)
            word_to_morse.toMorse(li, led=led)

    def split(word):
        li = [char for char in word.lower()]
        return li

    def toMorse(li, led=None):
        result = []
        i = 0
        a = 0
        x = 0
        while (x < len(li)):
            if li[i] in list_char or li[i] == " ":
                if(li[i] == list_char[a]):
                    result.append(mlist_char[a]+"  ") # 19111999
                    a=0
                    i+=1
                    x+=1
                else:
                    a+=1
            else:
                x+=1
                i+=1
        u.Color.cprint("".join(str(result) for result in result), "green")

class morse_to_word:
        def main(ltr=None, led=None):
            if ltr != "":
                li = morse_to_word.split(ltr)
                morse_to_word.toAlpha(li, ltr, led=led)
            else:
                main()

        def split(word):  # split the string into a list
            li = []
            nchar = ""
            x = 0
            for char in word.lower():
                if char == " ":
                    if len(nchar) != 0:
                        li.append(nchar)
                        nchar = ""
                if word[-1] == "." or word[-1] == "-" or word[-1] == " ":
                    if x + 1 == len(word):
                        nchar += char
                        li.append(nchar)
                        nchar = ""
                nchar += char
                if nchar == " ":
                    li.append(nchar)
                    nchar = ""
                x += 1
            return li  # word is returned as a list, 1 letter being 1 element of a list

        def wtSpace():  # printing the result whitout spaces (except for double spcaces)
            result = []
            for x in mlist_char:
                noSpace = ""
                noSpace = x
                if noSpace != " ":
                    nNoSpace = noSpace.replace(" ", "")  # nNoSpace = newNoSpace
                    result.append(nNoSpace)
                else:
                    result.append(noSpace)
            return result;

        def toAlpha(li, li_morse, led=None):  # Decrypted morse code goes here
            fResult = []
            i = 0
            a = 0
            x = 0
            rWSpace = morse_to_word.wtSpace()
            while x < len(li):
                if li[i] in rWSpace or li[i] == " ":
                    if li[i] == rWSpace[a]:
                        fResult.append(list_char[a])# + " ")
                        a = 0
                        i += 1
                        x += 1
                    else:
                        a += 1
                    if i == len(li):
                        morse_to_word.word(fResult, li_morse, led=led)
                else:
                    x+=1
                    i+=1

        def word(res, morse, led=None):  # Morse code finally comes here
            li = []
            nchar = ""
            i = 0
            for x in res:
                if res[i] == " ":
                    i += 1
                    nchar += res
                if res[i] == " " and res[i + 1] == " ":  # if there is 2 spaces, adds a space instead of 2 spaces
                    li.append(nchar + " ")
                    nchar = ""
                nchar += x[i]
                i = 0
            u.Color.cprint(nchar, "green")

def show_alphabet():
    equal = "="
    u.misc.clear()
    u.Color.cprint(equal*6 + " Alphabet " + equal*6 + " " + equal*6 + " Numbers " + equal*6, "yellow")

    sec_1 = list(morse_alphabet) + list(morse_number)
    sec_2 = list(morse_special)  + list(morse_prosigns)
    for i, letters in enumerate(sec_1):
        if i == len(morse_alphabet):
            break;
        if i <= 9:
            print(letters, "\t", morse_alphabet[letters], "\t\t",  str(i), morse_number[i])
        else:
            print(letters,  "\t",  morse_alphabet[letters])

    u.Color.cprint(equal * 6 + " Special " + equal * 6 + " " + equal * 6 + " Prosigns " + equal * 6, "yellow")

    for i, letters in enumerate(sec_2):
        if i == len(morse_special):
            break;
        if i < 7:
            print(letters,  "\t",  morse_special[letters], " \t", morse_prosigns[list(morse_prosigns)[i]], "\t", list(morse_prosigns)[i])
        else:
            print(letters, "\t", morse_special[letters])

def main(self=None):
    u.misc.clear()
    print("   _____                               _________            .___  ")
    print("  /     \   ___________  ______ ____   \_   ___ \  ____   __| _/____  ")
    print(" /  \ /  \ /  _ \_  __ \/  ___// __ \  /    \  \/ /  _ \ / __ |/ __ \ ")
    print("/    Y    (  <_> )  | \/\___ \\  ___/  \     \___(  <_> ) /_/ \  ___/ ")
    print("\____|__  /\____/|__|  /____  >\___  >  \______  /\____/\____ |\___  >")
    print("        \/                  \/     \/          \/            \/    \/ ")

    u.Color.cprint("1) Word to Morse", "green")
    u.Color.cprint("2) Morse to Word", "green")
    u.Color.cprint("3) Display the Alphabet", "green")
    u.Color.cprint("4) Exit", "green")
    try:
        choice = int(input(""))
        if choice == 1:
            ltr = input("\nEnter your word : ")
            word_to_morse.main(ltr=ltr, led=None)
            input("Enter to continue...")
            main()
        elif choice == 2:
            ltr = input("\nEnter your morse code : ")
            morse_to_word.main(ltr=ltr, led=None)
            input("Enter to continue...")
            main()
        elif choice == 3:
            show_alphabet()
            input("Enter to continue...")
            main()
        elif choice == 4:
            exit()
        else:
            main()
    except KeyboardInterrupt:
        exit()
    except ValueError:
        u.Color.cprint("Enter a numeric value", "red")
        main()

if __name__ == '__main__':
    main()








