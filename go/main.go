package main

import (
	"fmt"
	"morse-translator/morse"
	"strings"
)

func main()  {
	var x []string = morse.Encode(strings.ToLower("Hello world!"), morse.All_signs)
	fmt.Println(x)
	var y string = morse.Decode(x, morse.All_signs)
	fmt.Println(y)
}