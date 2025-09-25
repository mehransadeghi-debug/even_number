# even_number
An Algorithm that sums exclusively even values from a list.  judgment used to solve problems  Problem Understanding
Identify the objective and what needs to be discovered or calculated.
Model the problem mathematically if possible
“Now, to define an algorithm that exclusively sums even values from a list, we first need to understand what makes a number even.
It isn’t necessary to be proficient in math to recall that every even number, when divided by 2, results in two whole numbers.
This is different from, for example, 5 divided by 2, which equals 2.5.
But If we only consider integers, 5 divided by 2 gives us 2 with a remainder of 1. When working with integers, every odd number will have a remainder different from 0, and every even number will have a remainder equal to 0.”
Solution Planning

Recall if similar problems have been solved before.
Utilize solutions by analogy, generalization, or specialization.
Break down complex problems into smaller, manageable parts.
The main part of the solution is to filter the numbers from the list that have a remainder equal to 0. Fortunately, Python provides an arithmetic operator that precisely calculates the remainder of a division.
It’s “%” operator
result = 10 % 3 # is 1
result = 10 % 2 # is 0
So, Here’s the Flowchart Solution:


We useded many of programming structures, let’s see step by step in the code:

def sum_even_numbers(list):
We start a function definition with the keyword ‘def.’

and inside the parentheses ‘()’ is where we specify the variable(s) needed for the function to work

def sum_even_numbers(list):
    sum_even = 0
Inside the function, we declare our first variable, sum_even, which starts with a value of zero

def sum_even_numbers(list):
    sum_even = 0
    
    for number in list:
Now, we initiate a loop. As you may recall from ‘Programming Structures Simplified,’ there is more than one type of loop, including ‘for’ and ‘while,’ which work similarly in various programming languages. In this case, the ‘for’ loop will iterate through each number in the list, checking each number one by one.

def sum_even_numbers(list):
    sum_even = 0
    for number in list:
        if number % 2 == 0:
            sum_even += number
“ another basic programming structure comes into play:

Conditional Statements, specifically the if statement. Within the for loop, each number undergoes scrutiny by the if statement, which checks whether the remainder of its division by 2 is equal to 0. If this condition holds true, the number is then added to the variable sum_even. On the other hand, in the absence of a corresponding else statement, if the condition evaluates to false, nothing is added."

def sum_even_numbers(list):=
    sum_even = 0
    for number in list:=
        if number % 2 == 0:
            sum_even += number
    return sum_even
Finally, after the for loop iterates through the entire list, the return statement captures the cumulative sum and assigns it to the variable sum_even. Thus, sum_even holds the total sum of the even numbers in the list, ranging from 0 to the sum of the even values.

Advantage of functions

The advantage of functions is that you can choose the list you want to sum. In this case, let’s suppose that you have these lists

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [1, 6, 3, 7, 5, 9, 7, 10, 9, 10]
list_3 = [1, 9, 3, 4, 4, 6, 7, 11, 9, 10]
list_4 = [1, 2, 6, 5, 6, 6, 7, 13, 9, 10]
def sum_even_numbers(list):
-----
print(sum_even_numbers(list_1)) # to list 1
print(sum_even_numbers(list_2)) # to list 2
# you got 
To calculate the sum of even numbers for any list, once the function is defined, you simply need to call the function ‘sum_even_numbers,’ providing the list as an argument. Then, you can print the result
