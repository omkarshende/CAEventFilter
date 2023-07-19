# CAEventFilter

A short Python script that reads in an input file of emails to check and lets you compare against as many rosters as you want or have. There is no checking for spelling (or misspelling) and for alternate emails.

To use, the syntax is straightforward. Make sure all files you need are in the same directory and that you do not have a file named `output.csv` already in your directory. Note that the input file of emails to check should be a one-column CSV file. The roster files are currently set to be what the IT CAs send as of 2022-2023 Summer. These formats can be changed by the user.

To run:
~~~
python CAEventFilter.py emails-to-check.csv roster-1.csv roster-2.csv ... 
~~~

The output file will show up as `output.csv` in the working directory, and the script will print a small message with the number of emails verified.
