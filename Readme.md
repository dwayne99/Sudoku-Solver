# Sudoku Solver

This program solves any 9x9 sudoku. 
It is based on the Back-Tracking algorithm. 

## Installation

```bash
pip install python
```

## Usage

step 1: Edit the sudoku.py file i.e change the initial matrix variable to the desired sudoku starting board that you want to solve.

Empty spaces are represented by 0.

matrix = [

        [0,0,0,0,0,0,6,8,0],    
        [0,0,0,0,7,3,0,0,9],    
        [3,0,9,0,0,0,0,4,5],    
        [4,9,0,0,0,0,0,0,0],    
        [8,0,3,0,5,0,9,0,2],    
        [0,0,0,0,0,0,0,3,6],    
        [9,6,0,0,0,0,3,0,8],    
        [7,0,0,6,8,0,0,0,0],    
        [0,2,8,0,0,0,0,0,0],    
]

step 2: Run the Sudoku.py file and all the solutions pertaining to the puzzle would be generated.
```bash
python sudoku.py
```
