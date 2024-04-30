package piscine

func ToLower(s string) string {
	result := make([]byte, len(s))

	for i := 0; i < len(s); i++ {
		char := s[i]
		if char >= 'A' && char <= 'Z' {
			char += 32
		}
		result[i] = char
	}

	return string(result)
}
