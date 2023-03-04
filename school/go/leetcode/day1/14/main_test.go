package main

import (
	sort2 "sort"
	"testing"
)

func TestSort(t *testing.T) {
	arr := []int{1, 3, 2, 4, 5, 4}
	arr2 := []int{1, 3, 2, 4, 5, 4}
	t.Log(arr2, arr)
	sort(arr)
	t.Log(arr2, arr)
	sort2.Ints(arr2)

}
