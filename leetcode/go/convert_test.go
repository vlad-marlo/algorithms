package main

import (
	"fmt"
	"testing"
)

func TestConvert(t *testing.T) {
	tt := []struct {
		input   string
		numRows int
		want    string
	}{
		{"PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"},
		{"PAYPALISHIRING", 4, "PINALSIGYAHRPI"},
	}
	for i, tc := range tt {
		t.Run(fmt.Sprintf("test case: %d", i), func(t *testing.T) {
			res := convert(tc.input, tc.numRows)
			if res != tc.want {
				t.Fatalf("got unexpected result; got=%s want=%s", res, tc.want)
			}
		})
	}
}
