package main

import (
	"bufio"
	"fmt"
	"morse-translator/morse"
	"os"
)

func from_text() {
	fmt.Printf("Plaintext -> ")
	in := bufio.NewReader(os.Stdin)
	
	line, err := in.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		return
	}
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

	var decoded string = morse.Decode(line, morse.All_signs)
	fmt.Println(decoded)
}

func main() {
	from_text()
	from_morse()
}
