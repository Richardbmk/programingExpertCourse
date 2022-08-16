package main

import (
	"fmt"
	"math"
)

func RoundedSquareRoot(number float64) float64 {
	// Write your code here.
	a := math.Round( math.Sqrt(number))
	return a
}

func main() {
	fmt.Println(RoundedSquareRoot(10))
}
