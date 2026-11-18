# Returns the month name for a month number (1-12)
def month(n):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    # List indexes start at 0, month numbers start at 1
    return months[n - 1]