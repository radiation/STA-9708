import math


def calculate_combinations(n: int, k: int) -> int:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def calculate_permutations(n: int, k: int) -> int:
    return math.factorial(n) // math.factorial(n - k)


def main():
    try:
        n = int(input("Enter total number of items (n): "))
        k = int(input("Enter number of items to choose (k): "))
    except ValueError:
        print("Invalid input: Please enter integer values for n and k.")
        exit(1)

    if k > n or k < 0:
        print("Invalid input: k must be between 0 and n.")
        exit(1)

    perms = format(calculate_permutations(n, k), ",d")
    print(f"Number of ways to ARRANGE {k} items from {n} items: {perms}")

    combinations = format(calculate_combinations(n, k), ",d")
    print(f"Number of ways to CHOOSE {k} items from {n} items: {combinations}")


if __name__ == "__main__":
    main()
