# Author: Muniba Maududi
# Date: 1/16/25
# Student ID: 101000747
# Description: Analyze movie budgets and save results to a file.

def calculate_average_budget(movies):
    """Calculate the average budget of all movies."""
    budgets = [int(budget) for _,(budget) in movies]
    return sum(budgets) / len(budgets)

def high_budget_movies(movies, average_budget):
    """Find movies with budgets higher than the average."""
    high_budget_movies= []
    for name, budget in movies:
        budget= int(budget)
        if budget > average_budget:
            difference= budget - average_budget
            high_budget_movies.append((name, budget, difference))
    return high_budget_movies

def read_movies_from_file(file_name):
    """Read movies from a file."""
    movies = []
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            name, budget = line.strip().split(", ")
            movies.append((name,budget))
    return movies

def write_results_to_file(file_name, average_budget, high_budget_movies, sorted_movies):
    """Write analysis results to a file."""
    with open(file_name, "w") as file:
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        file.write("Movies with Budgets Higher than Average:\n")
        for name, budget, difference in high_budget_movies:
            file.write(f"{name}: ${budget:,} (Higher by ${difference:,.2f})\n")
        file.write(f"Total High-Budget Movies:{len(high_budget_movies)}\n")

        #Sorted budget
        file.write(f"Movies Sorted by Budget (Ascending):\n")
        for name, budget in sorted_movies:
            file.write(f"{name}: ${budget:,}\n")

def add_movie(movies):
    try:
        movie_num= int(input("How many movies would you like to add? "))
        for _ in range(movie_num):
            movie_name= input("Enter the movie name: ")
            movie_budget= int(input("Enter the movie budget (in dollars): "))
            movies.append((movie_name, movie_budget))
    except ValueError:
        print("Invalid input. Please enter numeric values for the number of movies and their budgets.")

if __name__ == "__main__":

    # Read movies from file
    movies = read_movies_from_file("MovieList.txt")
    movies = [(name, int(budget)) for name, budget in movies]

    add_movie(movies)

    # Display all movies
    # print("Full Movie List:")
    # for name, budget in movies:
    #    print(f"  {name}: ${budget:,}")

    # Calculate average budget
    average_budget = calculate_average_budget(movies)

    # Find high-budget movies
    high_budget_movies = high_budget_movies(movies, average_budget)

    #Sorting movies by budget
    sorted_movies = sorted(movies, key=lambda x: x[1])

    # Print results
    print(f"Average Budget: ${average_budget:,.2f}")
    print("Movies with Budgets Higher than Average:")
    for name, budget, difference in high_budget_movies:
        print(f"{name}: ${budget:,} (Higher by ${difference:,.2f})\n")
    print(f"Total High-Budget Movies:{len(high_budget_movies)}\n")
    print(f"Movies Sorted by Budget (Ascending):\n")
    for name, budget in sorted_movies:
        print(f"{name}: ${budget:,}\n")


    # Write results to output file
    write_results_to_file("Output.txt", average_budget, high_budget_movies, sorted_movies)
    print("Results saved to 'Output.txt'.")

