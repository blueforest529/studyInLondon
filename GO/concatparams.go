package piscine

func ConcatParams(args []string) string {
	ans := ""

	for idx, str := range args {
		ans += str

		if idx < len(args)-1 {
			ans += "\n"
		}
	}

	return ans
}
