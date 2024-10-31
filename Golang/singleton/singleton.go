// Eager initialization approach

package main

import (
	"fmt"
)

// Singleton struct
type Singleton struct {
	// Add fields here if necessary
}

var instance = &Singleton{} // Eager initialization

// GetInstance returns the single instance of the Singleton struct
// func GetInstance() *Singleton {
// 	return instance
// }

func main() {
	// Accessing the singleton instance
	s1 := instance
	s2 := instance

	fmt.Println(s1 == s2) // This will print true, confirming both are the same instance
}
