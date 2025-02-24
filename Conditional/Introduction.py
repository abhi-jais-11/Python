'''
Conditional Statements in Python
    -Conditional statements in Python are used to execute certain blocks of code based on specific conditions.
    -These statements help control the flow of a program, making it behave differently in different situations.
    
    Conditiona statement in python
    1.if
    2.if else 
    3.if elif else
    4.match case
'''

'''
1. if statement 
   - If statement is the simplest form of a conditional statement.
   - It executes a block of code if the given condition is true.
   
   syntax:
        if condition:
            # statements

=> nested if 
    if condition:
        if condition:
            statement

'''

'''
2. if else
        - Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement evaluates to False. 
        - Else block provides a way to handle all other cases that don't meet the specified conditions.
        
    syntax:
        if condition:
            # statement
        else:
            # statement 

'''



'''
3.if elif else
    -elif statement in Python stands for "else if."
    -It allows us to check multiple conditions , providing a way to execute different blocks of code based on which condition is true.
    -Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.
    
    syntax:
        if condtion:
            #statement
        elif condtion:
            #statement
        elif condtion:
            #statement
        .
        .
        .
        else:
            # statement

'''


'''
4.Match-Case Statement in Python
    -match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.
    
    syntax:
        match matcher:
            case 1:
                # statemet
            case 2:
                # statement
            .
            .
            .
            case _:
                # statement it is the default case
            
'''