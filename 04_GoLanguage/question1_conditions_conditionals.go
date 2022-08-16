package main

import "fmt"

func VerifyLogin(username string, password string, attempt int8) bool {
	// Write your code here.
	login := username == "ProgrammingExpert" && password == "LearnToCode" && attempt <= 4
	if login {
		return login
	}

	return false
}

func main() {
	fmt.Println(VerifyLogin("ProgrammingExpert", "LearnToCode", 3))
}
