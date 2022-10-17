Files submitted:
    count_lines.py
    morse.py
    pretty_recursive_print.py

Description:
    count_lines.py
        Go from the current working directory up one "level" and then send the path to
        a function which ignores "hidden" files and for every file ending with .py computes
        the total amount of rows with actual written code/comments on them and does that for
        every .py file within that path and returns the sum of all the lines of code/comments
        of those files.

    morse.py
        Create a dictionary and set every lowercase letter equal to its morse code equivalent
        then request an input string which then is translated into morse code using the dictionary
        that was created before. Then it interchanges all the key with their respective values
        and takes new input string which is in morse code and translates it to alphabetic letters.

    pretty_recursive_print.py
        Gets current working directory and send the path to a function which scans the current directory
        then for every entry in that scan checks if it is a directory or file if directory then prints it
        to the screen with a depth in front of it to show if it is located within a previously printed
        directory and does this recursively for every folder within the original given path. 
