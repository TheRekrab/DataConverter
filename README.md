# DataConverter
A basic python script where I can convert different data types.
Basically, I needed an easy way to convert a binch of types of data to other forms in the command line, so I invented this.
It works by taking in three input fields:
1) The 'FROM' section, where the user specifies what data format the inputted data is in.
2) The 'TO' section, where the user specifies what format the data SHOULD become
3) The data section, where the user can enter the data in (With spaces, if they choose).

Then, the program will get the correct function from each input, and then call those functions on the data, in order. The way it works is as follows:
The "FROM" functions will assume that the user is correct in the data type, and convert that data type to binary.
The "TO" functions will take that binary, and convert it to a specified other data format.

This process makes it very easy to create new functions, and add them to the function dictionary.

Thank you for checking this out! :)
