###
# Removes duplicate email addresses
#
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

# A set keeps only unique elements, so duplicates disappear
unique_emails = set(emails)  # Removes duplicates
print(unique_emails)