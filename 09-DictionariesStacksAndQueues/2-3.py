###
# Finds absent students
#
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

# Difference: elements of the first set that are not in the second set
absent_students = all_students - attended_students  # Difference
print(absent_students)