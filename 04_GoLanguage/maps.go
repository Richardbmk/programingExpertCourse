package main

import "fmt"

func main() {

	// sample01()
	// sample02()
	// sample03()
	// sample04()

	// sample05()
	// sample06()
	sample07()
	// sample08()

}

func sample01() {
	var mp map[string]int
	fmt.Println(mp)
}

func sample02() {
	mp := map[string]int{"h":1, "a":3}
	fmt.Println(mp)
}

func sample03() {
	mp := map[string][]int{"h":{1}, "a":{3}}
	fmt.Println(mp)
}

func sample04() {
	mp := make(map[int]rune)
	fmt.Println(mp)
}

func sample05() {
	mp := make(map[int]rune)
	mp[5] = 2
	// delete(mp, 5)
	value, ok := mp[5]
	// fmt.Println(mp)
	fmt.Println(value, ok)
}

func sample06() {
	mp := map[string]int{"a": 1, "b":2, "c":3, "d":4}

	for key, value := range mp {
		fmt.Println(key, value)
	}
}

func sample07() {
	n := 100
	disvisibleMap := make(map[int]uint)

	for num := 1; num <= n; num++ {
		for d :=1; d <= 5; d++ {
			if num % d == 0 {
				disvisibleMap[d]++
			}
		}
	}

	fmt.Println(disvisibleMap)
}