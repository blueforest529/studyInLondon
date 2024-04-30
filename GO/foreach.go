// piscine.go 파일 내용
package piscine

// ForEach takes a function and applies it to each element of an int slice.
func ForEach(f func(int), a []int) {
	for _, num := range a {
		f(num)
	}
}

// PrintNbr prints an integer to standard output.
func PrintNbr(n int) {
	// 여기서 간단한 방법으로 정수를 문자로 변환하고 출력
	if n < 0 {
		print("-")
		n = -n
	}
	if n >= 10 {
		PrintNbr(n / 10)
	}
	print(n%10 + '0')
}
