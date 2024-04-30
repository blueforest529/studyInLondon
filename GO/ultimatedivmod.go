package piscine

func UltimateDivMod(a *int, b *int) {
	var aa int = *a
	var bb int = *b
	*a = aa / bb
	*b = aa % bb
}
