package piscine

func AppendRange(min, max int) []int {
	if max <= min {
		return []int(nil)
	}

	var mySlice []int

	for i := min; i < max; i++ {
		mySlice = append(mySlice, i)
	}

	return mySlice
}
