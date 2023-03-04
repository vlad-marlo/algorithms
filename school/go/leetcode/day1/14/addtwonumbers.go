package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := new(ListNode)
	p1, p2 := l1, l2
	current := result
	dozenCarrier := 0
	for p1 != nil || p2 != nil {
		var p1v, p2v int
		if p1 != nil {
			p1v = p1.Val
		}
		if p2 != nil {
			p2v = p2.Val
		}
		sum := p1v + p2v + dozenCarrier
		dozenCarrier = sum / 10
		current.Next = &ListNode{Val: sum % 10}
		if p1 != nil {
			p1 = p1.Next
		}
		if p2 != nil {
			p2 = p2.Next
		}
		current = current.Next
	}
	if dozenCarrier > 0 {
		current.Next = &ListNode{Val: dozenCarrier}
	}

	return result.Next
}
