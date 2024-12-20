# Color Analysis Program

## Description
This Python program analyzes color data from a dataset of staff dress colors. It performs statistical analysis, database operations, and includes additional utility functions for searching and number generation.

## Requirements
- Python 2.x or Python 3.x
- PostgreSQL database
- psycopg2 library (`pip install psycopg2`)

## Features
The program includes the following functionality:
- Color frequency analysis (mean, median, most worn)
- Statistical calculations (variance, probability)
- PostgreSQL database integration
- Recursive search implementation
- Binary number generation and conversion
- Fibonacci sequence calculations

## Setup
1. Install required dependencies:
   ```bash
   pip install psycopg2
   ```

2. Configure PostgreSQL connection:
   Update the following parameters in the code:
   - database
   - user
   - password
   - host
   - port

3. Modify the sample color data array with your actual data.

## Usage
Run the program using Python:
```bash
python main.py
```

## Output
The program will display:
- Mean color
- Most frequently worn color
- Median color
- Variance of color frequencies
- Probability of randomly selecting red
- Database operation status
- Results of recursive search
- Generated binary number and its decimal conversion
- Sum of first 50 Fibonacci numbers

## Database Schema
The program creates a table named `color_frequencies` with the following structure:
- color (VARCHAR)
- frequency (INTEGER)
