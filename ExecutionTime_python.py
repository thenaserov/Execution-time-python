# coded by Naser Rezayi
# The lib for time
import time

# start time
start = time.time()

# calculation
a = int(input("Enter a number to calculate the factorial of it: "))
if (a > 0):
    ans = 1
    for i in range(1, a+1):
        ans *= i
print(f"The factorial of {a} is : {ans}")

#end time
end = time.time()

# results >>>
print(f"The time of calculation of {a} took :", end-start)
