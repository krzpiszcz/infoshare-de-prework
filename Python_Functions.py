# readable_timedelta
def readable_timedelta(days):
    """
        Return a string of the number of weeks and days included in days.
        
        Parameters:
        days -- number of days to convert (int)

        Returns:
        string of the number of weeks and days included in days
        """
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

### Lambda
"""
The lambda keyword is used to indicate that this is a lambda expression.
Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
"""
def multiply(x, y):
    return x * y

#>>

multiply = lambda x, y: x * y
print(multiply(3,4))

### Lambda with Map
"""
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. 
"""
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

### Lambda with Filter
"""
filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True.
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)