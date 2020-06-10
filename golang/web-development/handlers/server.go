package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type Post struct {
	User    string
	Threads []string
}

func hello(w http.ResponseWriter, r *http.Request) {
	h := r.Header["User-Agent"]
	fmt.Fprintln(w, h)

	len := r.ContentLength
	body := make([]byte, len)
	r.Body.Read(body)
	fmt.Fprintf(w, string(body))
}

func process(w http.ResponseWriter, r *http.Request) {
	/* r.ParseForm()
	fmt.Fprintln(w, r.Form) */
	file, _, err := r.FormFile("uploaded")
	if err == nil {
		data, err := ioutil.ReadAll(file)
		if err == nil {
			fmt.Fprintln(w, string(data))
		}
	}
}

func write(w http.ResponseWriter, r *http.Request) {
	str := `<html><head><title>Go Web Programming</title></head> <body><h1>Hello World</h1></body></html>`
	w.Write([]byte(str))
}

func redirect(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Location", "http://google.com")
	w.WriteHeader((302))
}

func respondJson(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	post := &Post{
		User:    "Xiangbo Li",
		Threads: []string{"first", "second", "third"},
	}
	json, _ := json.Marshal(post)
	w.Write(json)
}

func setCookie(w http.ResponseWriter, r *http.Request) {
	c1 := http.Cookie{
		Name:     "first_cookie",
		Value:    "Go Web Programming",
		HttpOnly: true,
	}
	c2 := http.Cookie{
		Name:     "second_cookie",
		Value:    "Manning Publications Co",
		HttpOnly: true,
	}

	// w.Header().Set("Set-Cookie", c1.String())
	// w.Header().Add("Set-Cookie", c2.String())
	http.SetCookie(w, &c1)
	http.SetCookie(w, &c2)
}

func getCookie(w http.ResponseWriter, r *http.Request) {
	h := r.Header["Cookie"]
	fmt.Fprintln(w, h)
}

func main() {
	server := http.Server{
		Addr: "127.0.0.1:8080",
	}

	http.HandleFunc("/hello", hello)
	http.HandleFunc("/process", process)
	http.HandleFunc("/write", write)
	http.HandleFunc("/redirect", redirect)
	http.HandleFunc("/json", respondJson)
	http.HandleFunc("/set_cookie", setCookie)
	http.HandleFunc("/get_cookie", getCookie)
	server.ListenAndServe()
}
