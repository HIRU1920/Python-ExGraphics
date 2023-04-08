def is_subset(seq, subset):
    """
    Checks if subset is a subset of seq.
    Returns True if subset is a subset of seq, False otherwise.
    """
    seq_idx = 0
    subset_idx = 0

    while seq_idx < len(seq) and subset_idx < len(subset):
        if seq[seq_idx] == subset[subset_idx]:
            subset_idx += 1
        seq_idx += 1

    return subset_idx == len(subset)

# Example usage
S = [1, 2, 3, 4, 5]
T = [2, 3, 4]
print(is_subset(S, T)) # Output: True

U = [2, 5]
print(is_subset(S, U)) # Output: False
