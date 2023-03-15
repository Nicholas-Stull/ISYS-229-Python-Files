# Week 3 Hands On Project 1 Psudocode
-----

## Declare Variables
    Declare Real bill
    Declare Real tip
    Declare Real total
## Begin Program
    Output "Please enter the amount of the bill."
    Input bill
    If bill < 25
        Assign tip = bill*0.15
    Else
        Assign tip = bill*.20
    End
    Assign total = bill+tip
    Output "Your total bill including tip is $"&total
    End

Project 1 Psudocode Flowchart
---------------
---------------
```mermaid
graph TD
    A[Start] --> B[Declare Real bill]
    B --> C[Declare Real tip]
    C --> D[Declare Real total]
    D --> E["Please enter the amount of the bill."]
    E --> F[Input bill];
    F --> G{bill < 25};
    G -- Yes --> H[Assign tip = bill*0.15];
    G -- No --> I[Assign tip = bill*.20];
    H --> J[Assign total = bill+tip];
    I --> J
    J --> K["Your total bill including tip is $ "Total""];
    K --> L[End];
```


