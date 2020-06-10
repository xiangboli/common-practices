package main

import (
	"fmt"
	"net/http"
)

func hellowHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "hello world")
}

func customeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello %s", r.URL.Path[1:])
}

func main() {
	http.HandleFunc("/", hellowHandler)
	http.HandleFunc("/bill", customeHandler)
	http.ListenAndServe(":8080", nil)
}
