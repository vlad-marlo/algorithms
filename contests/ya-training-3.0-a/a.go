package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type sortRunes []rune

func readDataA() (s string) {
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		s += strings.ReplaceAll(input.Text(), " ", "")
	}
	return
}

func (s sortRunes) Less(i, j int) bool { return s[i] < s[j] }
func (s sortRunes) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s sortRunes) Len() int           { return len(s) }

func SortString(s string) string {
	r := []rune(s)
	sort.Sort(sortRunes(r))
	return string(r)
}

func SolutionA(data string) {
	set := make(map[rune]int)
	var s string
	var max int
	for _, c := range data {
		if val, ok := set[c]; !ok {
			s += string(c)
			set[c] = 1
		} else {
			if max < val+1 {
				max = val + 1
			}
			set[c]++
		}
	}
	ans := make([][]string, max, max)
	for i := 0; i < max; i++ {
		ans[i] = make([]string, len(set), len(set))
		for k, v := range data {
			if v > 0 {
				ans[i][k] = "#"
			} else {
				ans[i][k] = " "
			}
		}
	}
	for i := 0; i < len(ans); i++ {
		fmt.Println(strings.Join(ans[len(ans)-i], " "))
	}
}

func main() {
	SolutionA(readDataA())
}
