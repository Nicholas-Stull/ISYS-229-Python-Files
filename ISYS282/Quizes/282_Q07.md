1. Which of the following will take output from a command and append it to the end of a file?  
>">>"
2. Which of the following commands will count the number of lines in a file named data.csv?        
>wc -l data.csv
3. Which of the following files can you add filenames to so that the git add * command will not stage them?                    
>gitignore
4. Which of the following can be used for comparing values within an if statement?    
> -lt
> =
5. Which of the following will look at the /etc/passwd file for any lines containing the word root and display them out to the screen while simultaneously writing the results to a file?                 
>grep root /etc/passwd | tee ~/root.txt
6. Which of the following results would be created by the command sequence:
	echo 'apple banana carrot dog elephant' | while read a b c; do echo result: $c $b $a; done
>carrot dog elephant banana apple
7. Which of the following will the split command do on a file when no other options are specified? 
>It will split a file into new equally sized files that are 1/10th of the original file size
8. Which of the following characters can be entered at the beginning of a line in a shell script to ensure that line is recognized as a comment rather than try to execute it?    
>#
