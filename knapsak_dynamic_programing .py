import os

def knapsack(file_name):
    # Get the absolute path of the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Join the absolute path with the relative file path
    file_path = os.path.join(current_dir, file_name)

    # Read the input file
    with open(file_path, 'r') as f:
        num_items, max_weight = map(int, f.readline().split())
        values, weights = [], []
        for line in f:
            v, w = map(int, line.split())
            values.append(v)
            weights.append(w)
    
    # Create a vector to store the optimal values for each subproblem
    opt = [0] * (max_weight + 1)
    
    # Fill in the vector using dynamic programming
    for i in range(num_items):
        for w in range(max_weight, weights[i]-1, -1):
            opt[w] = max(opt[w], values[i] + opt[w - weights[i]])
    
    # Find the optimal value for the knapsack
    optimal_value = opt[max_weight]
    
    # Backtrack through the vector to find the items that were included in the optimal solution
    included_items = ['0'] * num_items
    w = max_weight
    for i in range(num_items-1, -1, -1):
        if w >= weights[i] and opt[w] == values[i] + opt[w - weights[i]]:
            included_items[i] = '1'
            w -= weights[i]
    
    # Print the optimal value and the included items
    print("optimal value degeri :", optimal_value)
    print("", " ".join(included_items))
    #####
    print("------------"); print("Optimal cozume dahil edilen itemler:", end=" ")
    for i in range(num_items):
        if included_items[i] == '1':
            print(i+1, end=" ")
            

# Example usage
knapsack('ks_19_0')
