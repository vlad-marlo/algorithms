package main

func lengthOfLongestSubstring(s string) (result int) {
	charLastIndex := make(map[rune]int)
	current := 0
	start := 0
	for index, character := range s {
		lastIndex, ok := charLastIndex[character]
		if !ok || lastIndex < index-current {
			current++
		} else {
			start = lastIndex + 1
			current = index - start + 1
		}
		charLastIndex[character] = index
		if current > result {
			result = current
		}
	}
	return
}
