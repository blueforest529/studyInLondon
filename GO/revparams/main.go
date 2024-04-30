package main

import (
	"os"

	"github.com/01-edu/z01"
)

func main() {
	// os.Args[1:]를 사용하여 프로그램 이름을 제외한 인자들만 처리
	args := os.Args[1:]

	// 인자들을 역순으로 순회
	for i := len(args) - 1; i >= 0; i-- {
		for _, r := range args[i] {
			z01.PrintRune(r)
		}
		z01.PrintRune('\n')
	}
}
