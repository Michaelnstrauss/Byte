## Exercise - Pay

* Write a function ```prompt_hours()``` that prompts a user to input how many hours they have worked. The return value of the function should be a float.

```
# calling your function:
hours = prompt_hours()

# produces the effect:
How many hours did you work? 45

# which stores 45.0 in the variable hours
```

* Write a similar function called ```prompt_rate()``` that prompts for the rate of pay. It should return a float.

* Pay is the hourly rate for the first 40 hours and 1.5 times the rate for time over that.

So if someone worked 50 hours at $10.00 per hour, they would recieve $550.00

* Write another function ```compute_pay(hours, rate)``` that computes total pay given a number of hours worked. It should return a float.

* Use these functions together to complete the program that asks a user for pay and rate and computes their paycheck. After defining your functions your code should look like:

```
# function definitions above this

hours = prompt_hours()
rate = prompt_rate()
pay = compute_pay(hours, rate)

print("You will be paid ${:.2f}.".format(pay))

```