package main

func main() {
	addTwoNumbers(
		&ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 4,
				Next: &ListNode{
					Val:  3,
					Next: nil,
				},
			},
		},
		&ListNode{
			Val: 5,
			Next: &ListNode{
				Val: 6,
				Next: &ListNode{
					Val:  4,
					Next: nil,
				},
			},
		},
	)
}
