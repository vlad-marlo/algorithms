package main

import "strings"

func convert(s string, numRows int) string {
	var rows []string
	for i := 0; i != numRows; i++ {
		rows = append(rows, "")
	}
	row := 0
	for _, v := range s {
		rows[row%numRows] += string(v)
		row++
	}
	return strings.Join(rows, "")
}
