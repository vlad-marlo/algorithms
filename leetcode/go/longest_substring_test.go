package main

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLongestSubstring(t *testing.T) {
	tt := []struct {
		name  string
		input string
		want  int
	}{
		{"#1", "abcabcbb", 3},
		{"single character", strings.Repeat("b", 100), 1},
		{"xd", "pwwkew", 3},
	}
	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			assert.Equal(t, tc.want, lengthOfLongestSubstring(tc.input))
		})
	}
}
