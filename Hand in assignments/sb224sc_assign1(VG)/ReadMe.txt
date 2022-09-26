Files submitted:
    sumofthree.py
    change.py
    tax.py
    quadratic.py

Description:
    sumofthree.py:
        I solved the problem given by taking the given input running it through a while loop.
        That first took the input modulo ten that I then added on to an variable that stated from zero.
        I then took the floor division operator to the input and repeated which gives the correct answer due to mathematical operations.

    change.py:
        I take two inputs price and amount_payed and from those I get the total_change by easy subtraction and rounding.
        Then I pass the total_change through a function calc_change that takes one parameter(total_change).
        In the function I have an for loop which goes through a list of all the different values of bills and coins and then with the help of the modulo and floor division operators,
        computes how many of each bill/coin you will get back and prints it to the screen.
    
    tax.py:
        I take one input (income) and immediately checks that is more then 0, then i pass it through a function calc_taxes that takes one parameter(income).
        Then I check from highest to lowest which income bracket a person with the income entered falls under an computes along the way if they are a part of them,
        this is done with the help of if statements. And finally returns your income_tax that you will have to pay.

    quadratic.py:
        I take three inputs (num_a, num_b, num_c) which stand for the different values in an quadratic equation.
        Then I pass them to a function quadratic_equation which takes all three inputs as parameters.
        Firstly I compute the discriminant for the equation then I use nested if statements to get check how many roots the equation has if any and if it does,
        prints it to the screen along side the roots them selves.
