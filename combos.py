import math

def calculate_combos(n: int, k: int) -> int:
    if k > n or k < 0:
        print("Invalid input: k must be between 0 and n.")
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def main():
    try:
        n = int(input("Enter total number of items (n): "))
        k = int(input("Enter number of items to choose (k): "))
        combos = calculate_combos(n, k)
        print(f"Number of ways to choose {k} items from {n} items: {combos}")
    except ValueError:
        print("Invalid input: Please enter integer values for n and k.")

if __name__ == "__main__":
    main()
