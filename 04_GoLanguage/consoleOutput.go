package main

import "fmt"

func main() {
	// x := 10
	// y := "shell"
	// z := 10.389593
	// str := fmt.Sprintf("%T", 1)
	// fmt.Println("hello\n", x, 2.45)
	// fmt.Println("hello", 2, 2.45)
	// fmt.Printf("%T %T", x, y)
	// fmt.Printf("%v %T", x, y)
	// fmt.Printf("%v %T %b", x, y, x)
	// fmt.Printf("%.2f", z)
	// fmt.Println(str)
	x := fmt.Sprintf("%.2f + %d", 4.359, 1)
	fmt.Println(x, 1)
}

// Example of functions
func DefineConstant() string {
	return "1"
}

func DefineConstants(x string) string {
	return "1"
}

func DefineConstants01(x string) (string, int) {
	return x, 1
}

