type Pricing interface {
	getDiscount() float64
	getTax() float64
}