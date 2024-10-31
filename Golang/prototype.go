package main

import (
	"fmt"
)

// Prototype interface
type Prototype interface {
	Clone() Prototype
}

// ConcretePrototype1
type ConcretePrototype1 struct {
	ID   int
	Name string
}

// Clone method for ConcretePrototype1
func (p *ConcretePrototype1) Clone() Prototype {
	return &ConcretePrototype1{
		ID:   p.ID,
		Name: p.Name,
	}
}

// ConcretePrototype2
type ConcretePrototype2 struct {
	ID   int
	Age  int
}

// Clone method for ConcretePrototype2
func (p *ConcretePrototype2) Clone() Prototype {
	return &ConcretePrototype2{
		ID:  p.ID,
		Age: p.Age,
	}
}

// PrototypeRegistry
type PrototypeRegistry struct {
	prototypes map[string]Prototype
}

// NewPrototypeRegistry initializes the registry
func NewPrototypeRegistry() *PrototypeRegistry {
	return &PrototypeRegistry{prototypes: make(map[string]Prototype)}
}

// RegisterPrototype adds a prototype to the registry
func (r *PrototypeRegistry) RegisterPrototype(name string, prototype Prototype) {
	r.prototypes[name] = prototype
}

// ClonePrototype retrieves and clones a prototype from the registry
func (r *PrototypeRegistry) ClonePrototype(name string) Prototype {
	if prototype, exists := r.prototypes[name]; exists {
		return prototype.Clone()
	}
	return nil
}

// Client code
func main() {
	// Create a prototype registry
	registry := NewPrototypeRegistry()

	// Create and register prototypes
	prototype1 := &ConcretePrototype1{ID: 1, Name: "Prototype 1"}
	prototype2 := &ConcretePrototype2{ID: 2, Age: 30}

	registry.RegisterPrototype("prototype1", prototype1)
	registry.RegisterPrototype("prototype2", prototype2)

	// Clone prototypes
	clonedPrototype1 := registry.ClonePrototype("prototype1")
	clonedPrototype2 := registry.ClonePrototype("prototype2")

	// Display the cloned objects
	fmt.Println("Cloned Prototype 1:", clonedPrototype1)
	fmt.Println("Cloned Prototype 2:", clonedPrototype2)

	// Modify the cloned objects
	clonedPrototype1.(*ConcretePrototype1).Name = "Modified Clone 1"
	clonedPrototype2.(*ConcretePrototype2).Age = 40

	fmt.Println("After modifying clones:")
	fmt.Println("Original Prototype 1:", prototype1)
	fmt.Println("Cloned Prototype 1:", clonedPrototype1)
	fmt.Println("Original Prototype 2:", prototype2)
	fmt.Println("Cloned Prototype 2:", clonedPrototype2)
}
