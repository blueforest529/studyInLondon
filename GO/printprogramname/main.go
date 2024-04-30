package main

import (
	"os"

	"github.com/01-edu/z01"
)

func main() {
	path := os.Args[0]

	nameStart := 0
	for i := len(path) - 1; i >= 0; i-- {
		if path[i] == '/' {
			nameStart = i + 1
			break
		}
	}

	programName := path[nameStart:]

	for _, r := range programName {
		z01.PrintRune(r)
	}
	z01.PrintRune('\n') // 각 인자를 개행 문자로 구분
}
