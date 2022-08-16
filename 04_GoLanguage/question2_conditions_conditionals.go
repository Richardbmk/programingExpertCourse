// Copyright © 2022 AlgoExpert LLC. All rights reserved.

package main

func ColorMaker(color1 string, color2 string) string {
	if color1 == color2 {
		return color1
	}

	if color1 == "red" {
		if color2 == "blue" {
			return "violet"
		}
		return "orange"
	} else if color1 == "blue" {
		if color2 == "yellow" {
			return "green"
		}
		return "violet"
	} else {
		if color2 == "red" {
			return "orange"
		}
		return "green"
	}
}
