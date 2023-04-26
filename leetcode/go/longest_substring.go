package main

func longestPalindromeOld(s string) string {
	n := len(s)
	table := make([][]int, n, n)
	for i := 0; i != n; i++ {
		table[i] = make([]int, n, n)
	}
	return ""
}
