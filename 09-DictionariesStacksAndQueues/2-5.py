###
# Merges two contact lists without duplicates
#
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# Union: all elements from both sets, every element only once
merged_contacts = contacts_A | contacts_B  # Union
print("Merged contacts:", merged_contacts)