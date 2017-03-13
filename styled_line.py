# Problem Set AB-0
# Name: Aaron Bell
# Collaborators: None
# Time Spent: 0:10

# Write a program that creates a dashed line of varying size



def styled_line(style, line_length, styled_chars_per_space):

	styled_line = ''
	
	for part in range(0, line_length):
		
		styled_line = styled_line + (style * styled_chars_per_space) + ' '
	
	return styled_line
		
print(styled_line('#', 30, 4))