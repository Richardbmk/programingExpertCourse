package main

import (
	"fmt"
)

func Format(a float64, b bool, c string) string {
	// Write your code here
	str := fmt.Sprintf("%%%v:%v/%v", a, b, c)
	return str
}

func main(){
	fmt.Println(Format(27.2, true, "hello"))
}

