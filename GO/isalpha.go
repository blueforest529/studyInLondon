package piscine

func IsAlpha(s string) bool {
	for _, char := range s {
		if !isAlphaNumeric(char) {
			return false
		}
	}
	return true
}

func isAlphaNumeric(char rune) bool {
	return (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || (char >= '0' && char <= '9')
}
