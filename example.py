# Implement the quadratic function below
def quadratic(a, b, c, x):
    # YOUR CODE STARTS HERE
    return a * (x ** 2) + b * x  + c
    # YOUR CODE ENDS HERE

# test 1
a = 2
b = -5
c = 10
x = 2
y = quadratic(a, b, c, x)
expected_y = 8
if (expected_y != y):
    print("*** Test Failed! ***\nThe expeceted output is %s" %(8))
else:
    print("*** Test Passed! ***")