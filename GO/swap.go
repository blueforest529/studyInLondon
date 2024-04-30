package piscine

func Swap(a *int, b *int) {
	var aa int = *b
	var bb int = *a
	*a = aa
	*b = bb
}
