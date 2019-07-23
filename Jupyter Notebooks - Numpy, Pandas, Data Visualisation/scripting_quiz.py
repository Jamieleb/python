names =  input("Enter names separted by commas.".lower()).split(',')
assignments =  input("Enter assignments separted by commas.").split(',')
grades =  input("Enter grades separated by commas.").split(',')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

names_array = list(zip(names, assignments, grades))

for name, assignment, grade in names_array:
	print(message.format(name.title, assignment, grade, int(grade) + int(assignment)*2))