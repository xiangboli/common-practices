package main

// Kitchen is a struct
type Kitchen struct {
	numOfPlates int
}

// House is a struct
type House struct {
	Kitchen
	numOfRooms int
}

/* func main() {
	h := House{Kitchen{10}, 3}
	fmt.Println("Rooms: ", h.numOfRooms, " Kitchen: ", h.Kitchen, " Plates: ", h.numOfPlates)
} */
