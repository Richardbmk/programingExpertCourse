package main

import (
	"fmt"
	"math"
)

func main() {
	// fmt.Println(Factorial01(7))
	// fmt.Println(Factorial02(7))
	fmt.Println(MatchingCharacters("AlgoExpert", "Alligator"))
}

//Exercise 01
func Factorial01(n int) int {
	factorial := 1
	for i := 1; i <= n; i++ {
		factorial *= i

	}

	return factorial
}

//Exercise 02 --- The same but with a while loop
func Factorial02(n int) int {
	f := 1
	i := 1
	for i <= n {
		f *= i
		i++
	}

	return f
}

//Exercise 03 
func MatchingCharacters(string1 string, string2 string) int {
	// Write your code here.
	matchingChars := 0
	minLength := math.Min(float64(len(string1)), float64(len(string2)))

	for i := 0; i < int(minLength); i++ {
		char1 := string1[i]
		char2 := string2[i]

		if char1 == char2 {
			matchingChars++
		}
	}
	return matchingChars
}
