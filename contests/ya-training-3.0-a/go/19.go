package main

type Heap struct {
	slice []int
}

func (heap *Heap) find(item int) int {
	head, tail := 0, len(heap.slice)
	var mid, guess int
	for head <= tail {
		mid = (head + tail) / 2
		guess = heap.slice[mid]
		if guess == item {
			return mid
		}
		if guess > item {
			tail = mid - 1
		} else {
			head = mid + 1
		}
	}
	if head == tail {
		if heap.slice[head] > item {
			return head
		} else {
			return head - 1
		}
	}
	return -1
}

func (heap *Heap) Insert(k int) {
	if len(heap.slice) == 0 {
		heap.slice = append(heap.slice, k)
	}
	mid := heap.find(k)
	heap.slice = append(append(heap.slice[0:mid], k), heap.slice[mid:]...)
}

func (heap *Heap) Extract() int {
	if len(heap.slice) > 0 {
		return heap.slice[len(heap.slice)-1]
	}
	return -1
}
