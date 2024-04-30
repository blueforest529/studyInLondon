package main

import (
	"github.com/01-edu/z01"
)

type point struct {
	x int
	y int
}

func setPoint(ptr *point) {
	ptr.x = 42
	ptr.y = 21
}

// 개별 숫자를 rune으로 변환하고 출력하는 함수
func printNumber(n int) {
	if n >= 10 { // 두 자릿수 숫자의 경우
		printNumber(n / 10) // 첫 번째 자릿수를 재귀적으로 처리
	}
	z01.PrintRune(rune(n%10 + '0')) // 마지막 숫자를 출력
}

func printStr(s string) {
	for _, r := range s {
		z01.PrintRune(r)
	}
	// z01.PrintRune('\n')
}

func main() {
	points := &point{}
	setPoint(points)

	// 구조체의 x와 y 값을 출력
	printStr("x = ")
	printNumber(points.x)
	printStr(", y = ")
	printNumber(points.y)
	z01.PrintRune('\n')
}
