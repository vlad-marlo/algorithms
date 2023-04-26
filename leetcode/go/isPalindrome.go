package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	s := fmt.Sprint(x)
	for i := 0; i < len(s); i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}
