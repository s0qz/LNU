Files submitted:
	countdigits.py
	birthday_candles.py
	abcd.py
	pi_approx.py
	tic_tac_toe.py
	salary_revision.py

Description:
	countdigits.py:
		I take input of a large integer and pass it to a function that
		runs it through a for loop for each digit in input and checks if it is
		zero, even or odd and adds on to the counter of the one it is.
		After entire input as been ran through it prints the result.
	
	birthday_candles.py:
		I create to constants one for the maximum age and one for the amount of
		candles per each box you buy. Then it runs a for loop that for age in the 
		range 1 to and including 100. Then checks if you have enough candles 
		remaining for current age  if enough just removes that amount from 
		the variable that holds the number of remaining candles, if not enough
		candles remaining then we get to a while loop that goes until the amount
		of remaining candles are more or equal to current age.

	abcd.py:
		I use a quadruple for loop to generate all number combinations abcd except
		for a != 0 and d != 0, for each combination of abcd I pass it to a function
		that makes all the individual digits to one whole integer and also the 
		integer of dcba to compare to then we check if current value of abcd * 4
		equals the value of dcba if it does print abcd if not continue.

	pi_approx.py:
		I create two constants Radius and Square Area and a list for all points that
		are within the unit circle(check image in exercise). I run program for
		first with 100 points then 10000 points and lastly for 1000000 points.
		Pass each of the previously mentioned values to a function that generates
		the passed amount of points and if generated point is within the unit circle
		which it checks by passing point x, y to another function it then gets 
		appended in the points list if not it generates a new point.
		When the passed amount of points have been generated it then prints the 
		approximation of PI that we get from 
		squareArea * (length of points/ passed amount of points).
		And lastly we print our approximation of PI against actual PI to see the 
		difference.

	tic_tac_toe.py:
		I create five different functions: winner(Checks if there is a winning set
		on the board), check_for_win(is used by winner to make sure it doesn't 
		give a win if neither player has made a move), display_board(which prints
		the board to the screen), get_row_col(ask for input from the player and then
		calls the move function with that input), move(gets input passed to it and
		checks if that given square is already occupied if so requests new input
		if square is not occupied then places current players symbol in given
		location), get_attribute(is used by display_board and move functions to
		make sure right symbol is placed and to check if a square is neutral and
		in that case print that symbol). After a player has made their move the
		program checks for a win and if no win it checks if turn counter equal
		to 8 and if it is there is a draw.

	salary_revision.py:
		I create a list to store all the different salaries in then I take a 
		long string input of all the salaries and split that string at every
		space character so that all the salaries become their own value.
		Afterwards I convert every index of the list to integers and add all
		of the stored values together to compute the average salary later.
		Then I divide the value of all summed up salaries by the amount of
		salaries in the list, then I sort the list to compute the median
		value of the list.
