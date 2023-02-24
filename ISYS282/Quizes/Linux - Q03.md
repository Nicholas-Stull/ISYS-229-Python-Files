1. Which of the following commands will not interpret regular expressions, which translates into faster results being returned?        
>fgrep, grep -F
2. Kate wants to compare two text files to identify what might have been changed from one version to another. Which of the following commands can she use to do this?                
>diff document1.txt document2.txt
3. Chase is trying to extract records for employees 423 through 428 out of a comma separated values file and store them in another one. Which of the following commands would accomplish this?
>cat employees.csv | grep "42[3-8]" > employees-newhires.csv    
>grep "42[3-8]" employees.csv > employees-newhires.csv    
>grep "42[3-8]" < employees.csv > employees-newhires.csv
4. When using the vi text editor, which of the following keys, when in command mode, will change to insert mode and place the cursor at the end of the current line?        
>Shift + A
5. When using the vi text editor, which of the following keys, when in command mode, will move to the last line in the document?        
>Shift + G
6. Jo has received a text file which contains multiple instances of his name spelled correctly as well as multiple instances spelled as Joe. Which of the following commands would search a text file for any occurrences of either spelling and display them out to the terminal?    
>grep -E "Joe?" document1.txt    
> grep "Joe*" document1.txt    
> grep -E "Joe*" document1.txt
7. Mike has changed directory into one subdirectory after the next and has lost track of where he's at in the directory tree. Which of the following commands can he use to tell him the full path to the current subdirectory he is in?        
>pwd
8. Garrett wants to search through a csv file to find all rows that have either the name John or Bob in them and display them out to the terminal. Which of the following commands could Garrett use to perform this search?                        
>grep -E "(John|Bob)" salesemployees.csv
