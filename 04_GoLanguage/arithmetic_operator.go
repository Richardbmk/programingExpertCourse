package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	a := 5
	b := int8(2)
	c := float64(a) / float64(b)
	a++
	d := 1
	e := math.Min(float64(d), 10)
	// e := math.Max(float64(d), 10)
	// z := math.Sqrt(21)
	// z := math.Pow(10, 2)
	f := math.Round(20.87)
	// f := math.Cel(20.87)
	fmt.Println(c)
	fmt.Println(a)
	fmt.Println(e)
	fmt.Println(f)

	str := "1234"
	a, err := strconv.Atoi(str)
	t, err := strconv.ParseInt(str, 10, 64)
	fmt.Println(a, err)
	fmt.Println(t, err)

}