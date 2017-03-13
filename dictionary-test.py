# dict_name = {'hello': 'goodbye', 'up': 'down', 'come back': 'get out'}

# print(str(dict_name.keys()) + ': ' + str(dict_name[dict_name.keys()]))

# As an exercise, write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2). Then use this function in a function called intercept(x1, y1, x2, y2) that returns the y-intercept of the line through the points (x1, y1) and (x2, y2).

# import math

# def distance(x1, y1, x2, y2):

	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2))
	# return distance_or_hypotenuse

# def slope(x1, y1, x2, y2, degrees=False):
	
	# # Do my basic distance as hypotenuse, where d**2 = a** + b**
	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2)
	
	# if degrees: return round(math.atan(opposite/adjacent) * 57.2958, 2)
	# return math.atan(opposite/adjacent)
	
# def intercept(x1, y1, x2, y2):
	
	# if x1 > 0 and x2 > 0: return None
	# if x1 < 0 and x2 < 0: return None
	
	# y_intercept = ((1 / math.tan(slope(x1, y1, x2, y2)) / distance(0, y1, x2, y1)) - (0-x1)**2)**0.5 + y1
	# return y_intercept
	
# print(intercept(0, 3, 5, 10))

# 1. The Y-Intercept in this case should be 3. Why isn't it working? Also, depending on the value, I* get a 'not divisible by zero' error.

# import math

# def distance(x1, y1, x2, y2):

	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2))
	# return distance_or_hypotenuse

# def slope(x1, y1, x2, y2, degrees=False):
	
	# # Do my basic distance as hypotenuse, where d**2 = a** + b**
	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2)
	
	# if degrees: return round(math.atan(opposite/adjacent) * 57.2958, 2)
	# return math.atan(opposite/adjacent)
	
# def intercept(x1, y1, x2, y2):
	
	# if x1 > 0 and x2 > 0: return None
	# if x1 < 0 and x2 < 0: return None
	
	# y_intercept = ((1 / math.cos(slope(x1, y1, x2, y2)) / x1) - (0-x1)**2)**0.5 + y1
	# return y_intercept
	
# print(intercept(0, 3, 5, 10))

# 2. Tried to simplify it. Updated the tan to a cos (which is what my calculations use). Got a ZeroDivisionError, though. Need to handle that. 

# import math

# def distance(x1, y1, x2, y2):

	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2))
	# return distance_or_hypotenuse

# def slope(x1, y1, x2, y2, degrees=False):
	
	# # Do my basic distance as hypotenuse, where d**2 = a** + b**
	# opposite = y2 - y1
	# adjacent = x2 - x1
	# distance_or_hypotenuse = (adjacent**2 + opposite**2)**0.5 # square root of (a**2 + b**2)
	
	# if degrees: return round(math.atan(opposite/adjacent) * 57.2958, 2)
	# return math.atan(opposite/adjacent)
	
# def intercept(x1, y1, x2, y2):
	
	# if x1 > 0 and x2 > 0: return None
	# if x1 < 0 and x2 < 0: return None
	
	# y_intercept = y1 - x1*slope(x1, y1, x2, y2)
	# return y_intercept
	
# print(intercept(3, 50, 5, 10))

# 3. Got it. Had the idea of a y-intercept all wrong. Was acting as if the line wasn't infinite. 

# def isBetween(x, y, z):
	
	# return x < y < z
	
# print(isBetween(4, 2, 3))

tel = {'jack': 4098, 'sape': 4139}

print(list(tel.keys()))



































