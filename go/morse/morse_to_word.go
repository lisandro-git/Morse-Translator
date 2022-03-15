package morse

func Decode(morse_code []string, morse_signs map[string]string) string {
	var result string
	var i int
	
	for i = 0; i < len(morse_code); i++ {
		for key, value := range morse_signs {
			if (value == morse_code[i]){
				result += key
			}
		}
	}
	return result;
}