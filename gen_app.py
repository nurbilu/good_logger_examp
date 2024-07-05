import csv

# Path to the CSV file
csv_file = 'functions.csv'

# Function to evaluate expressions from the CSV
def evaluate_expressions(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expression = row['functions']
            try:
                # Evaluate the expression and print the result
                result = eval(expression)
                print(f"Expression: {expression} => Result: {result}")
            except Exception as e:
                print(f"Error evaluating expression '{expression}': {str(e)}")

# Run the function
evaluate_expressions(csv_file)
