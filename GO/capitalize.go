package piscine

func Capitalize(s string) string {
	result := []rune(s)
	capitalizeNext := true

	for i, char := range result {
		if (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || (char >= '0' && char <= '9') {
			if capitalizeNext {
				if char >= 'a' && char <= 'z' {
					result[i] = char - 32
				}
				capitalizeNext = false
			} else if char >= 'A' && char <= 'Z' {
				result[i] = char + 32
			}
		} else {
			capitalizeNext = true
		}
	}
	return string(result)
}
