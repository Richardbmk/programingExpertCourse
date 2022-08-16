type Person struct {
	firstName string
	lastName string
	age int
}

func (p Person) getName() string {
	return p.firstName + " " + p.lastName
}

// Sample code
type ContactInformation struct {
	address string
	city    string
	state   string
	country string
}

type Employee struct {
	firstName string
	lastName  string
	salary    float64
	contact   ContactInformation
}