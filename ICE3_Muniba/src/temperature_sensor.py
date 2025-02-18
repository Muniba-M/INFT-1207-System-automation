import statistics

# Name: Muniba Maududi
# Date: 1/14/2025
# Description: ICE3_code_coverage of temperature sensor

def validate_temp(value):
    try:
        # Convert non-string values to string for consistent handling
        value = str(value).strip()

        if value == "":
            raise ValueError("Error: No input provided.")

        temp = float(value)  # Convert to float
        if -50 <= temp <= 150:
            return temp
        else:
            raise ValueError("Error: Out-of-bound value detected.")  # Raise if out of bound
    except ValueError as e:
        # Catch all invalid input cases
        if "Out-of-bound" in str(e):
            raise  # Propagate out-of-bound error
        if "No input provided." in str(e):
            raise # Propagate no input error
        raise ValueError(f"Error: Invalid input detected.")  # Handle invalid or non-convertible inputs


def temp_process(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    valid_temps = []

    for temp in temp_list:
        try:
            valid_temps.append(validate_temp(temp))
        except ValueError as e:
            return str(e)  # Return error message for invalid inputs

    if not valid_temps:
        return "Error: No valid input detected."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# ✅ Test Cases
test_cases = [
    [20],
    [15, 35],
    [],
    [10, -10, 30],
    [-50, 20, 150, 25],
    [10, "abc", 30],
    [2 ** 31 - 1, - 2 ** 31],
    [10, 10, 10],
    [34, -12, "hi", 121],
    [-30, 150, 79],
    [-51, 151],
    ["!#$s", 40, -40, -39]
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(temp_process(case))
    print("-" * 40)