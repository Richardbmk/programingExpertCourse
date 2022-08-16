package main

import "fmt"

func main() {
	// explicit assignment of a variable
	var x int = 1
	// implicit assignment of a variable
	y := "hello"
	z := 1
	// type cast
	m := uint(1)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Printf("%T", z)
}