PROGRAM 
QUESTION:
Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.

LOGIC:
* Open the file using file location in read mode.
* Read the file content using read() and store it in a variable read_file.
* Split the content into separate words using split() and store it in a variable.
* Now find the unique words using set() function.
* Append all the unique words stored in a variable into a list.
* Sort the list based on the length of each word in ascending order.
* Print the sorted list.


PROGRAM 2:
QUESTION:
Program to read a CSV (CSV with n number of columns) and store it in DICT of list.

LOGIC:
* Open the csv file using file location in read mode.
* Each data in the csv is converted to Dictionary format using csv.DictReader().
* Each data is printed in the form of Dictionary.


PROGRAM 3:
QUESTION:
Program to Print all Prime Numbers in an Interval of 5 seconds.

LOGIC:
* Input the end limit from the user.
* for loop is generated from starting limit 2 to the end limit.
* A separate function to find if a number is prime is defined and is called for each iteration to check if it is a prime numberor not.
* If the number is prime the funtion will return 0.
* When the function returns 0, then sleep time is set for 5 seconds and the prime number is printed.


PROGRAM 4:
QUESTION:
Program to Find HCF or GCD

LOGIC:
* Input two numbers num1 and num2.
* A separate funtion to find hcf is defined.
* The smallest of both the numbers is set to a temporary variable as temp.
* for loop is generated from 1 to temp.
* If both num1 and num2 are divisible by the iterated value, then set hcf value tothe iterated value.
* After the loop breaks, return hcf value and is printed in the main function.


PROGRAM 5:
QUESTION:
Program to Convert Decimal to Binary, Octal and Hexadecimal.

LOGIC: 
TYPE 1:
* Input decimal value.
* To find binary equivalent, a separate function is defined.
* Check if the decimal number is greater than 1.
    -> If yes, then the same function is called by recursion and the number is divided by 2 and the modulus value of decimal value is printed each time.
    -> If no, the modulus value is printed and the function exits.
* To find octal equivalent, a separate function is defined.
* Check if the decimal number is greater than 7.
    -> If yes, then the same function is called by recursion and the number is divided by 8 and the modulus value of decimal value is printed each time.
    -> If no, the modulus value is printed and the function exits.
* To find hexadecimal equivalent, a separate function is defined.
* Check if the decimal number is greater than 15.
    -> If yes, then the same function is called by recursion and the number is divided by 16 and the modulus value of decimal value is printed each time.
    -> If no, the modulus value is printed and the function exits.

TYPE 2:
* Input decimal value.
* To find binary equivalent bin() function is used and the value is printed.
* To find octal equivalent oct() function is used and the value is printed.
* To find hexadecimal equivalent hex() function is used and the value is printed.


PROGRAM 6:
QUESTION:
Program to Find ASCII Value of Character.

LOGIC:
* Input a character.
* If the character length is greater than 1 then it raises an excpetion.
* To find ASCII value of the character ord() function is used and the ASCII value is printd.


PROGRAM 7:
QUESTION:
Program to get an application (name , age , gender, salary, state, city)

LOGIC:
* Input name, age, gender, salary, state and city from the user.
* print all the input values such as name, age, gender, salary, state and city accordingly.
