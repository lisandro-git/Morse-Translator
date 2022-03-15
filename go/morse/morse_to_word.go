package morse

func value_exist(userValue string, students map[string]string)bool{
	for _, value:= range students{
		if(value == userValue){
			return true
		}
	}
	return false
}

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