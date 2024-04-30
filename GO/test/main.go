package main

import "github.com/01-edu/z01"

// ForEach applies a function on each element of an int slice.
func ForEach(f func(int), a []int) {
	for _, value := range a {
		f(value)
	}
}

// PrintNbr prints an integer without a newline or space.
func PrintNbr(n int) {
	if n >= 10 { // 두 자릿수 숫자의 경우
		PrintNbr(n / 10) // 첫 번째 자릿수를 재귀적으로 처리
	}
	z01.PrintRune(rune(n%10 + '0')) // 마지막 숫자를 출력
}

func main() {
	a := []int{1, 2, 3, 4, 5, 6}
	ForEach(PrintNbr, a)
}
