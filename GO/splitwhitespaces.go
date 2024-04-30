package piscine

func SplitWhiteSpaces(s string) []string {
	var result []string
	var word string
	for i, ch := range s {
		// Check if the character is a space, tab, or newline
		if ch == ' ' {
			if word != "" {
				result = append(result, word)
				word = ""
			}
		} else {
			word += string(ch)
		}
		// Append the last word if we're at the end of the string
		if i == len(s)-1 && word != "" {
			result = append(result, word)
		}
	}
	return result
}
