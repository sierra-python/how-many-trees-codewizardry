# Author: Frank DiDonato - Copyright 2019 - All Rights Reserved.
# This is an algorithm that provides an approximation of
# the number of trees in the city of Sacramento, in California.
#
# Can use Google Maps to sample the number of trees in 3 different regions
# within the city of Sacramento. This will establish the median. But using Google is not necessary,
# can just get approximate perimeter and compute number of trees per mile across permiter with 
#
# Get approximate permiter of city
# Square root of 994 (994 square is the area), so the square root x 4 gives us an estimate of the permiter - factor a margin of error of 30%

import math

perimeter = math.sqrt(994) * 4 # The area for the city of Sacramento is about 994 mi²


number_of_trees_sample_one = 50  # Number of trees derived from sample 1 (1/50 of one mile)
number_of_trees_sample_two = 55 # Number of trees derived from sample 2  (1/50 of one mile)
number_of_trees_sample_three = 75 # Number of trees derived from sample 3  (1/50 of one mile)

MEDIAN_TREES = int(number_of_trees_sample_one + number_of_trees_sample_two + number_of_trees_sample_three) / 2 # Median of number of trees from sample of data derived from Google Maps.

DEVIATION = MEDIAN_TREES / 100


# establishes approximate number of trees deep inland across the permiter
number_of_trees_on_perimeter_unit = MEDIAN_TREES

number_of_trees_per_mile = number_of_trees_on_perimeter_unit * perimeter # number of collective trees from sample per mile

number_of_trees = number_of_trees_per_mile * perimeter

number_of_trees = int(number_of_trees * DEVIATION)

print(number_of_trees, " is an approximation of the number of trees in the city of Sacramento!")

"""
================ OUTPUT ================
14313599.999999996  is an approximation of the number of trees in the city of Sacramento!
"""

