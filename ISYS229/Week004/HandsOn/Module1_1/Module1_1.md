


Function Main
    Declare String fname
    Declare String lname
    Declare Integer age
    Declare Integer lbs
    Declare Integer ft
    Declare Integer kg
    Declare Integer ounces
    Declare Integer m
    Declare String space
    
    Assign space = " "
    Output "Please enter your first name"
    Input fname
    Output "Please enter your last name"
    Input lname
    Output "Please enter your age"
    Input age
    Output "Please enter your Weight"
    Input lbs
    Output "Please enter your height in feet"
    Input ft
    Assign kg = lbs*.045
    Assign ounces = lbs*16
    Assign m = ft*0.3048
    If m<=1
        Output "Thank you,"&space&fname&space&lname&"."&space&"You are"&space&age&"."&" You weigh"&space&kg&space&"Kilograms, or"&space&ounces&space&"ounces."&space&"You are"&space&m&space&"meter tall."
    Else
        Output "Thank you,"&space&fname&space&lname&"."&space&"You are"&space&age&"."&" You weigh"&space&kg&space&"Kilograms, or"&space&ounces&space&"ounces."&space&"You are"&space&m&space&"meters tall."
    End
End
