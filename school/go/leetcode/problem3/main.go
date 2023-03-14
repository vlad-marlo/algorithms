package main

import (
	"fmt"
	"math"
)

func lengthOfLongestSubstring(s string) int {
	var keys map[rune][]int
	keys = make(map[rune][]int)
	for i, c := range s {
		keys[c] = append(keys[c], i)
	}
	max := 1
	for _, v := range keys {
		for i := 0; i < len(v)-1; i++ {
			l := int(math.Abs(float64(v[i] - v[i+1])))
			if l > max {
				max = l
			}
		}
	}
	return max
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
}
