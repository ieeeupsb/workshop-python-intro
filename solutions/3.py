num = int(input)
num2 = num  # Preserve the num for the verification

if (num == 0):  # If num is 0, it wouldn't enter the loop
    res = "0"
else:
    res = ""  # Create an empty string to construct our solution over it
    while num > 0:  # While there are digits to process
        res += str(int(num % 8))  # 12 % 8 = 4, add "4" to our result
        num = int(num / 8)  # 12 / 8 = 1, set our next num to 1

    res = res[::-1] # As we built our solution backwards, reverse the string

print("Result: 0o", res, sep="")
print("Confirmation:", oct(num2)) # Use this to confirm your results
