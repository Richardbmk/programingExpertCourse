package main

import "fmt"

func main() {

	// sample01()
	// sample02()
	// sample03()
	// sample04()

	// sample05()
	// sample06()
	// sample07()
	// sample08()
	// sample09()
	sample10()
}


// Array sample codes
func sample01() {
	var arr [2]int
	arr[0] = 100
	// fmt.Println(arr)
	// fmt.Println(arr[1])
	fmt.Println(len(arr))
}

func sample02() {
	arr01 := [2]int{4, 5}
	arr02 := [...]int{4, 5, 5, 2, 4, 2, 1, 0}
	arr03 := [2][2]string{{"hello", "word"}, {"code", "go"}}

	fmt.Println(arr01)
	fmt.Println(arr02)
	fmt.Println(arr03)
	fmt.Printf("%T", arr03)
}

func sample03() {

	arr03 := [2][2]string{{"hello", "word"}, {"code", "go"}}

	for i, nestedArr := range arr03 {
		fmt.Println(i, nestedArr)
	}
}

func sample04() {

	arr03 := [2][2]string{{"hello", "word"}, {"code", "go"}}

	for _, nestedArr := range arr03 {
		for j, str := range nestedArr {
			fmt.Println(j, str)
		}
	}
}

// Slice sample codes

func sample05() {
	arr := [5]int{1,3,4,5,6}
	sliceArr := arr[:4]
	fmt.Println(sliceArr, len(sliceArr), cap(sliceArr))
}

func sample06() {
	arr := []string{"hello", "world"}
	arr = arr[:1]
	arr = arr[:2]
	fmt.Println(arr, len(arr), cap(arr))
}

func sample07() {
	arr := []string{}
	fmt.Println(arr, len(arr), cap(arr))
}

func sample08() {
	arr := []string{}

	for i := 0; i < 10; i++ {
		arr = append(arr, "hello")
	}

	fmt.Println(arr, len(arr), cap(arr))
}

func sample09() {
	arr := make([][]int, 5, 10)
	fmt.Println(arr, len(arr), cap(arr))
}

func sample10() {
	arr := []bool{}
	arr2 := []bool{true, false, false}
	arr = append(arr, arr2...)
	fmt.Println(arr)
}