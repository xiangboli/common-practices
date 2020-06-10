package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()

	a := [...]string{"a", "b", "c", "d"}
	for i := range a {
		fmt.Printf("%s ", a[i])
	}
	fmt.Println()

	captials := map[string]string{"France": "Paris", "Italy": "Rome", "Japan": "Tokyo"}
	for key, val := range captials {
		fmt.Println("Contry: ", key, " captial: ", val)
	}

}
