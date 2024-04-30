package piscine

func MakeRange(min, max int) []int {
	if min >= max {
		return nil
	}
	length := max - min
	slice := make([]int, length)
	for i := 0; i < length; i++ {
		slice[i] = min + i
	}
	return slice
}
