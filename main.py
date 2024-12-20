import random
from statistics import mean, median, variance
import psycopg2
from collections import Counter

# Sample color data for the week (fictional)
colors = ['red', 'blue', 'red', 'green', 'blue', 'red', 'yellow', 
          'blue', 'green', 'red', 'blue', 'red', 'blue', 'green']

def analyze_colors():
    # 1. Mean color (most frequent)
    color_counts = Counter(colors)
    mean_color = max(color_counts, key=color_counts.get)
    print(f"Mean color: {mean_color}")
    
    # 2. Most worn color throughout the week
    most_common = color_counts.most_common(1)[0][0]
    print(f"Most worn color: {most_common}")
    
    # 3. Median color (middle value when sorted)
    sorted_colors = sorted(colors)
    median_color = sorted_colors[len(colors)//2]
    print(f"Median color: {median_color}")
    
    # 4. Calculate variance (treating colors as categorical data)
    # This is a simplified version for demonstration
    frequencies = list(color_counts.values())
    var = variance(frequencies)
    print(f"Variance of color frequencies: {var}")
    
    # 5. Probability of randomly selecting red
    red_count = color_counts['red']
    red_probability = red_count / len(colors)
    print(f"Probability of randomly selecting red: {red_probability}")

def save_to_postgresql():
    try:
        # Connection parameters would go here
        conn = psycopg2.connect(
            database="newdb",
            user="jay",
            password="default",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        
        # Create table and insert data
        cur.execute("""
            CREATE TABLE IF NOT EXISTS color_frequencies (
                color VARCHAR(50),
                frequency INTEGER
            )
        """)
        
        color_counts = Counter(colors)
        for color, freq in color_counts.items():
            cur.execute("INSERT INTO color_frequencies VALUES (%s, %s)", 
                       (color, freq))
            
        conn.commit()
        print("Data saved to PostgreSQL")
        
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def recursive_search(numbers, target, start=0):
    if start >= len(numbers):
        return -1
    if numbers[start] == target:
        return start
    return recursive_search(numbers, target, start + 1)

def generate_binary():
    binary = ''.join([str(random.randint(0, 1)) for _ in range(4)])
    decimal = int(binary, 2)
    print(f"Binary: {binary}, Decimal: {decimal}")

def fibonacci_sum(n=50):
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    fib_gen = fib()
    return sum(next(fib_gen) for _ in range(n))

if __name__ == "__main__":
    # Main analysis
    analyze_colors()
    
    # Additional features
    save_to_postgresql()
    
    # Test recursive search
    test_numbers = [1, 3, 5, 7, 9]
    print(f"Searching for 5: {recursive_search(test_numbers, 5)}")
    
    # Generate random binary
    generate_binary()
    
    # Calculate fibonacci sum
    print(f"Sum of first 50 Fibonacci numbers: {fibonacci_sum()}")
