package piscine

func TrimAtoi(s string) int {
	sign := 1
	result := 0
	digitFound := false

	for _, char := range s {
		if char >= '0' && char <= '9' {
			digitFound = true
			result = result*10 + int(char-'0')
		} else if char == '-' && !digitFound {
			sign = -1
		} else if char == '+' && !digitFound {
			sign = 1
		}
	}
	return sign * result
}
