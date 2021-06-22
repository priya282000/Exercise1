PROGRAM 1a:
QUESTION:
Print the number of words having prefix with “To” in the input file.

LOGIC:
* Open the file using file location in read mode.
* Set count to 0 and start the for loop till the end of the file.
* Convert all the words to lower case and check if the word starts with 'to' using startwith().
    -> If yes, increase count by 1
    -> If no, continue the loop
* Print the count and close the file.


PROGRAM 1b:
QUESTION:
Print the number of words ending with “ing” in the input file.

LOGIC:
* Open the file using file loction in read mode.
* Set count to 0 and start the loop till the end of the file and split the words.
* Check if the word ends with 'ing' using endswith().
    -> If yes, increase the count by 1
    -> If no, continue the loop
* Print the count and close the file. 


PROGRAM 1c:
QUESTION:
Print the word that was repeated maximum number of times.

LOGIC:
* Open the file using file location in read mode.
* Read the content of the file and split the string into separate words.
* Set max as 0 and count as 0.
* Start a for loop till the last word.
* Count the occurence of the word in the list using count()
* Check if count > max
    -> If yes, replace max as count and note the word in temp.
    -> If no, continue the loop.
* Print the temp value which consists of the word which occured maximum times.


PROGRAM 1d:
QUESTION:
Print the palindrome present in the file.

LOGIC:
* Open the file using file location in read mode.
* Find the dupliacte elements in the file using set() and store it in a list.
* Iterate the loop till the end of the list.
* Reverse each word and check if it is equal to the original word.
    -> If yes, print the word
    -> If no, continue the loop
 
 
 PROGRAM 1e:
 QUESTION:
 Convert all words into unique list and print in command line
 
 LOGIC:
 * Open the file using file location in read mode.
 * Read the content of the file and find duplicate elemets in it using set().
 * convert the content to list and rint the list.
 
 
 PROGRAM 1f:
 QUESTION:
 Create a Word dict with Key as counter index and value as the words present in file and print them   
 on screen.
 
 LOGIC:
 * Open the file using file location in read mode.
 * Read the content of the file and split into separate words.
 * Using collections.Counter(), we can count the occurence of each word.
 * Print the counter in which the word and its occerence is printed.
 
 
 PROGRAM 1g:
 QUESTION:
 Write new file with following actions
     i. Split the words based on the vowels
    ii. Capitalize 3rd letter of every word
   iii. Capitalize all characters of every 5th word in the file.
    iv. Use – in place of blank space
     v. Use ; (semi-colon) for new line.
    vi. Output file name should be generated with unique name.

LOGIC:
* Open a file using file loaction in write mode.
* Write the content required into the file.
 
 
