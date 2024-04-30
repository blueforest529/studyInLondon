package piscine

func RecursiveFactorial(nb int) int {
	return factorialHelper(nb, 1)
}

func factorialHelper(n, acc int) int {
	// Check for non-possible values or overflows
	if n < 0 || n > 20 {
		return 0
	}
	// Base case: factorial of 0 is 1
	if n == 0 {
		return acc
	}
	// Recursive case: multiply acc by n and decrement n
	return factorialHelper(n-1, acc*n)
}
