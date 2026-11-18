# Returns the dice value that was rolled the most times in a row
def f(dice):
    # The longest series found so far
    best_digit = dice[0]
    best_length = 1
    # Length of the current series
    current_length = 1
    for i in range(1, len(dice)):
        # Same value as the previous one - the series continues
        if dice[i] == dice[i - 1]:
            current_length += 1
        else:
            # A new series starts
            current_length = 1
        # Remember the series if it is the longest so far
        if current_length > best_length:
            best_length = current_length
            best_digit = dice[i]
    return int(best_digit)

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))