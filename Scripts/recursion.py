# "Towers of Hanoi" Game
# A recursive solution almost forces itself on the programmer,
# while the iterative solution of the game is hard to find and to grasp.
# 
# "Recursion"
# Recursion is a method of programming or coding a problem,
# in which a function calls itself one or more times in its body.
# Usually, it is returning the return value of this function call.
# If a function definition satisfies the condition of recursion, we call this function a recursive function. 


def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n-1 to helper:
        hanoi(n-1, source, target, helper)
        # move disk from source to target:
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target:
        hanoi(n-1, helper, source, target)

if __name__ == "__main__":
    height = int(input("Enter the height of the tower: "))
    source = [disk for disk in range(1, height+1)]
    helper = []
    target = []
    print("Before calling the recursive function...")
    print("Source tower: ", str(source))
    print("Target tower: ", str(target))
    
    # call the hanoi function to start recursie execution
    hanoi(height, source, helper, target)
    print("After recursive calls...")
    print("Source tower: ", str(source))
    print("Target tower: ", str(target))
