package main

import "fmt"

func main() {
	a := 1.2
	b := 1
	c := a < float64(b)
	z := a >= float64(b) && b <= 1.0
	fmt.Println(c)
	fmt.Println(z)

	if a < 2 {
		fmt.Println("a is less than 2")
	} else if a == 3 {
		fmt.Println("a is equal to 3")
	} else if a == 4 {
		fmt.Println("a is equal to 4 ")
	} else {
		fmt.Println("a is greater than 3")
	}
}