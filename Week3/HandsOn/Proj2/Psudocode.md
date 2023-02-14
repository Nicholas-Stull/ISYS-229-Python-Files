# Week 3 Hands On Project 2 Psudocode
-----

## Declare Variables
    Declare Real leg0
    Declare Real leg1
    Declare Real leg2
    Declare Real table
## Input 1st Leg of the trip
    Output "Insert the millage for the first Leg of the trip"
    Input leg0
## Input 2nd Leg of the trip
    Output "Insert the millage for the 2nd Leg of the trip"
    Input leg1
## Input 3rd Leg of the trip
    Output "Insert the millage for the third Leg of the trip"
    Input leg2
## Calculate the total millage
    Assign table = leg0+leg1+leg2
## Output the total millage
    Output "You're Millage should be:" &table

Project 2 Psudocode Flowchart
---------------
```mermaid
graph TD
    A[Start] --> B[Declare Real leg0]
    B --> C[Declare Real leg1]
    C --> D[Declare Real leg2]
    D --> E[Declare Real table]
    E --> F["Insert the millage for the first Leg of the trip"]
    F --> G[Input leg0]
    G --> H["Insert the millage for the 2nd Leg of the trip"]
    H --> I[Input leg1]
    I --> J["Insert the millage for the third Leg of the trip"]
    J --> K[Input leg2]
    K --> L[Assign table = leg0+leg1+leg2]
    L --> M["You're Millage should be:"]
    M --> N[End]
```


