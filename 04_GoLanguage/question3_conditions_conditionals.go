package main

// My way of do it
func XOR1(x bool, y bool) bool {
	// Write your code here.
	if x == false && y == false {
		return false
	} else if x == false && y == true {
		return true
	} else if x == true && y == false {
		return true
	} else if x == true && y == true {
		return false
	} else {
		return false
	}
}

// Tim way of doing this
func XOR2(x bool, y bool) bool {
	return (x && !y) || (!x && y)
}
