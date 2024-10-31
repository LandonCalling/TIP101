def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)

def repeat_hello_iterative(n):
    for num in range(n):
        print("Hello")

		
repeat_hello_iterative(5)
