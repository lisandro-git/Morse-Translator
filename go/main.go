package main

import (
	"bufio"
	"fmt"
	"morse-translator/morse"
	"os"
	"strings"
)

func from_text() {
	fmt.Printf("Plaintext -> ")
	in := bufio.NewReader(os.Stdin)
	
	line, err := in.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		return
	}
	line = strings.TrimSuffix(line, "\n")
	line = strings.ToLower(line)
	var encoded []string = morse.Encode(line, morse.All_signs)
	fmt.Println(encoded)
}

func from_morse() {
	fmt.Printf("Morse code -> ")
	in := bufio.NewReader(os.Stdin)
	
	line, err := in.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		return
	}
	line = strings.TrimSuffix(line, "\n")
	morse_arr := strings.Split(line, " ")
	var decoded string = morse.Decode(morse_arr, morse.All_signs)
	fmt.Println(decoded)
}

func main() {
	from_text()
	from_morse()
}
