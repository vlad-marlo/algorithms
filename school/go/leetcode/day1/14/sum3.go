package main

func partition(arr []int, low, high int) ([]int, int) {
	pivot := arr[high]
	i := low
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

func quickSort(arr []int, low, high int) []int {
	if low < high {
		var p int
		arr, p = partition(arr, low, high)
		arr = quickSort(arr, low, p-1)
		arr = quickSort(arr, p+1, high)
	}
	return arr
}

func sort(arr []int) []int {
	return quickSort(arr, 0, len(arr)-1)
}

func threeSum(nums []int) [][]int {
	exists := map[string]struct{}{}
	var ans [][]int
	for i := 0; i+2 < len(nums); i++ {
		iNum := nums[i]
		for j := i + 1; j+1 < len(nums); j++ {
			jNum := nums[j]
			var status bool
			wantK := -(iNum + jNum)
			for k := j + 1; k < len(nums) && !status; k++ {
				kNum := nums[k]
				arr := sort([]int{iNum, jNum, kNum})
				sarr := string(rune(arr[0])) + " " + string(rune(arr[1])) + " " + string(rune(arr[2]))
				if _, ok := exists[sarr]; !ok && kNum == wantK {
					ans = append(ans, []int{iNum, jNum, kNum})
					exists[sarr] = struct{}{}
				}
			}
		}
	}
	return ans
}
