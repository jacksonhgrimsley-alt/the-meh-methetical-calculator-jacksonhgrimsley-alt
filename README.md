# the-meh-thematical-calculator-jacksonhgrimsley-alt

**Purpose**

  -This project was an attempt at making a calculator that would give you a humorous responce after each use. The purpose of this project was to give users a fun and humorous way to solve math equations.it also exposed me to codes that i have never used before so practice with those type of codes help build my knowledge and expierance.istruggled with getting the simulation to loop after each use.

**requirments**
  
  -Python3
  
  -visual studio code

**Features**

  -Basic Math Operations: Addition, subtraction, multiplication, and division.

  -Unimpressed Commentary: Get half-hearted remarks after every calculation.

**installation**

  -clone repository into visual studio or see code through github.
  
  **testing**
   
    -Play button is on the top right of the visual studio

**contribution**
  
  -code reviews
    
    -other coders can give advise and imporvments to my currant code

  -readme reviews

**licences**
 
  -This project is licensed under the MIT License.


**decision tree**

  -                                ┌──────────────────────────────────────────────┐
                                │ Start: "Welcome to the calculator... I guess" │
                                └──────────────────────────────────────────────┘
                                                   │
                                                   ▼
                                  ┌──────────────────────────────────┐
                                  │ User enters first and second num │
                                  └──────────────────────────────────┘
                                                   │
                                       ┌───────────┴───────────┐
                                       ▼                       ▼
                         ┌────────────────────┐     ┌───────────────────────────┐
                         │ Numbers valid?     │     │ Invalid input (ValueError)│
                         └────────────────────┘     └───────────────────────────┘
                                       │                       │
                              Yes ─────┘                       │
                                       │                       ▼
                                       │        "Brilliant. You had one job."
                                       ▼
                     ┌────────────────────────────────────────────────────────┐
                     │ Display menu: +, -, *, /                              │
                     │ Ask user: "So, what's it gonna be?"                   │
                     └────────────────────────────────────────────────────────┘
                                       │
                                       ▼
                         ┌───────────────────────────────────────────┐
                         │ Read user's chosen operation              │
                         └───────────────────────────────────────────┘
                                       │
           ┌────────────┬──────────────┬───────────────┬──────────────────┐
           ▼            ▼              ▼               ▼
     (operation +) (operation -)  (operation *)   (operation /)
           │            │              │               │
           ▼            ▼              ▼               ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌──────────────────────────────┐
│ add(a, b)      │ │ subtract(a, b) │ │ multiply(a, b)│ │ if b == 0?                   │
│ → print "Yay…" │ │ → print "There"│ │ → print "Wow" │ │ ┌──────────────────────────┐ │
└────────────────┘ └────────────────┘ └────────────────┘ │ │ yes → "Wow. Genius move" │ │
                                                        │ └──────────────────────────┘ │
                                                        │ │ no → divide(a,b) & print  │ │
                                                        │ └──────────────────────────┘ │
                                                        └──────────────────────────────┘
                                       │
                                       ▼
                   ┌─────────────────────────────────────────────┐
                   │ If invalid operation: print "I can't even." │
                   └─────────────────────────────────────────────┘
                                       │
                                       ▼
                      ┌──────────────────────────────────────┐
                      │ Print "Can I go now?" and terminate. │
                      └──────────────────────────────────────┘

