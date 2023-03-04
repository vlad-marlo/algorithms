package main

import "fmt"

func f(a, b, c int) int {
	if a > b {
		return 0
	}
	if a == b {
		return 1
	}
	ans := 0
	if c != 1 {
		ans += f(a, b, 1)
	}
	if c != 2 {
		ans += f(a, b, 2)
	}
	if c != 3 {
		ans += f(a, b, 3)
	}
	return ans
}

func main() {
	fmt.Println(f(5001, 45789, 0))
}
