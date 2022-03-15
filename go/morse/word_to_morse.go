package morse

func Encode(word string, morse_signs map[string]string) []string {
	var result []string
	var i int
	for i = 0; i < len(word); i++ {
		if v, found := morse_signs[string(word[i])]; found {
			result = append(result, v)
		} else {
			result = append(result, "")
		}
	}
	return result;
}
