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
		want  string
	}{
		{"#1", "abcabcbb", "bcb"},
		{"single character", strings.Repeat("b", 100), strings.Repeat("b", 100)},
		{"xd", "pwwkew", "ww"},
	}
	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			assert.Equal(t, tc.want, longestPalindromeOld(tc.input))
		})
	}
}
