package main

import (
	"strconv"
)

func MultiplyByString(str string, number int) int {
	// Write your code here.
	a, _ := strconv.Atoi(str)
	product := a * number
	return product
}

func main () {
	MultiplyByString("22", 5)
}