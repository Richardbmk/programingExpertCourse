package main

import "fmt"

// Sample code 01
func main() {
	a := 1
	switch a {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	default:
		fmt.Println("default value")
	}
}

// Sample code 02
func sample02() {
	// The order in the switch case is important
	switch {
	case 1 < 2:
		fmt.Println("One is less than two")
	case 2 < 3:
		fmt.Println("tree is less than tree")
	default:
		fmt.Println("default value")
	}
}

// Sample code 03
func sample03() {
	// The order in the switch case is important
	switch a := 2; {
	case a < 2:
		fmt.Println("One is less than two")
	case a < 3:
		fmt.Println("tree is less than tree")
	default:
		fmt.Println("default value")
	}
}

// Sample code 04
func sample04() {
	// The order in the switch case is important
	switch a := 0; {
	case a < 1:
		fmt.Println("One is less than two")
		fallthrough
	case a <= 2:
		fmt.Println("tree is less than tree")
	default:
		fmt.Println("default value")
	}
}

// Sample code 05
func sample05() {
	a := "b"
	switch a {	
	case "h", "a", "j":
		fmt.Println("One is less than two")
	}
}



// Exercise Proble 1
func DailyRoutine(time string) string {
	switch time {
	case "morning":
		return "Time to get up!"
	case "afternoon":
		return "Time for lunch!"
	case "night":
		return "Time to sleep"
	default:
		return "Have a great day :)"
	}
}