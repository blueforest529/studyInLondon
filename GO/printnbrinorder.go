package piscine

import (
	"github.com/01-edu/z01"
)

func PrintNbrInOrder(n int) {
	if n < 0 {
		return // Do not handle negative numbers
	}

	// Use an array to count occurrences of each digit from 0 to 9
	counts := make([]int, 10)

	// Special case to handle zero specifically
	if n == 0 {
		counts[0] = 1
	}

	// Extract digits and count their occurrences
	for n > 0 {
		digit := n % 10
		counts[digit]++
		n /= 10
	}

	// Print digits in order from 0 to 9 based on their count
	for digit, count := range counts {
		for i := 0; i < count; i++ {
			z01.PrintRune(rune(digit + '0'))
		}
	}
}
