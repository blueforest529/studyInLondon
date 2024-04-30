package piscine

func LastRune(s string) rune {
	for i, r := range s {
		if i == len(s)-1 {
			return r
		}
	}
	return 0
}
