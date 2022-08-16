package main

import "fmt"

func main() {

	fmt.Println(CharacterFrequency("hello world"))

}

func CharacterFrequency(sentence string) map[rune]int {
	// Write your code here.
	characters := make(map[rune]int)

	for _, char := range sentence {
		value, ok := characters[char]

		if !ok {
			characters[char] = 1
		} else {
			characters[char] = value + 1
		}
	}

	return characters
}