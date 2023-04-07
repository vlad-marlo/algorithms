package main

import "testing"

func TeskItemsWithMaximumSum(t *testing.T) {
	tt := []struct {
		name       string
		numOnes    int
		numZeros   int
		numNegOnes int
		k          int
		want       int
	}{
		{"test case #1", 3, 2, 0, 2, 2},
		{"test case #1", 3, 2, 0, 4, 3},
	}
	for _, tc := range tt {
		t.Run("", func(t *testing.T) {
			if res := kItemsWithMaximumSum(tc.numOnes, tc.numZeros, tc.numNegOnes, tc.k); res != tc.want {
				t.Errorf("got unexpected result; want: %d; got: %d", tc.want, res)
			}
		})
	}

}
