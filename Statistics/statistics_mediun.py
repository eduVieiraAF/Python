# ? The statistics.median() method calculates the median (middle value) of the given data set. This method also sorts
# the data in ascending order before calculating the median.

# * The mathematical formula for Median is: Median = {(n + 1) / 2}th value, where n is the number of values in a set
# of data. In order to calculate the median, * the data must first be sorted in ascending order. The median is the
# number in the middle.

# ! Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is
# even, it returns the average of the two middle values.

import statistics

print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 11]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))
