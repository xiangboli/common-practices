package main

import "fmt"

// Rectangle represts a struct
type Rectangle struct {
	length, width int
}

// Area is area
func (r Rectangle) Area() int {
	return r.length * r.width
}

func main() {
	r1 := Rectangle{4, 3}
	fmt.Println("Area is: ", r1.Area())
}
