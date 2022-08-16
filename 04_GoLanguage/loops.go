package main

import "fmt"

func main() {
	// forLoop()
	// whileLoop()
	// strings01()
	// strings02()
	strings03()
}

// for loop
func forLoop() {
	for i := 0; i < 10; i += 2 {
		fmt.Println(i)
	}
}

// While loops in Go
func whileLoop() {
	x := 0
	for x < 10 {
		x++
		fmt.Println(x)
	}
}

// Sample code 01
func strings01() {
	str := "hello"
	// fmt.Println(str[0])
	fmt.Println(string(str[0]))
}

// Sample code 02
func strings02() {
	str := "hello"

	for i := 0; i < len(str); i++ {
		// fmt.Println(str[i])
		// fmt.Println(string(str[i]))
		fmt.Printf("%c\n", str[i])
	}
}

// Sample code 03
func strings03() {
	str := "hellow"

	for i, char := range str {
		// fmt.Println(i, char)
		fmt.Println(i, string(char))
	}
}