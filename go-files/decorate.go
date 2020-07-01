import (
	"log"
)

type addFn func(int, int) int

// Decorator
func withLog(addFn, *logger log.Logger) addFn {
	var sum int
	
	defer func(sum int) {
		logger.Printf("The sum is %d", sum)
	}
	sum := addFn
}

func add(a,b int) int {
	return a + b
}

func main() {
	sum := add(1,2)
}