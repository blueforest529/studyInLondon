package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	// 인수 개수 확인
	args := os.Args[1:]
	if len(args) == 0 {
		fmt.Println("File name missing")
		return
	} else if len(args) > 1 {
		fmt.Println("Too many arguments")
		return
	}

	// 파일 읽기
	filename := args[0]
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		return
	}

	// 파일 내용 출력
	fmt.Print(string(content))
}
