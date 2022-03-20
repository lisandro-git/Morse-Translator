package morse

import (
	"strings"
)

func Encode(word string) []string {
	word = strings.TrimSuffix(word, "\n")
	word = strings.ToLower(word)
	var result []string
	var i int
	for i = 0; i < len(word); i++ {
		if v, found := All_signs[string(word[i])]; found {
			result = append(result, v)
		} else {
			result = append(result, "")
		}
	}
	return result;
}
