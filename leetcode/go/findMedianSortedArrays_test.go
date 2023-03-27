package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestFindMedianSortedArrays(t *testing.T) {
	tt := []struct {
		name  string
		nums1 []int
		nums2 []int
		want  float64
	}{
		{"", []int{1, 3}, []int{2}, 2},
	}
	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			assert.Equal(t, tc.want, findMedianSortedArrays(tc.nums1, tc.nums2))
		})
	}
}
