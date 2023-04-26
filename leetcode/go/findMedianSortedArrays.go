package main

func max[T int64 | int32 | int | float64 | float32](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	return 0
}
