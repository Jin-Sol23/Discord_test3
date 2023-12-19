
# 문자열 t = "Returns the standard deviation, a measure of the spread of a distribution, of the array elements.
# The standard deviation is computed for the flattened array by default, otherwise over the specified axis.
# If this is a tuple of ints, a standard deviation is performed over multiple axes,
# instead of a single axis or all the axes as before. Alternative output array in which to place the result.
# If this is set to True, the axes which are reduced are left in the result as dimensions with size one.
# With this option, the result will broadcast correctly against the input array."
# 에 있는 모든 단어의 첫 글자만 출력하는 코드를 작성하세요

t = "Returns the standard deviation, a measure of the spread of a distribution, of the array elements. \
The standard deviation is computed for the flattened array by default, otherwise over the specified axis. \
If this is a tuple of ints, a standard deviation is performed over multiple axes, \
instead of a single axis or all the axes as before. Alternative output array in which to place the result. \
If this is set to True, the axes which are reduced are left in the result as dimensions with size one. \
With this option, the result will broadcast correctly against the input array."
tsplit = t.split()
a = []
for i in range(len(tsplit)):
  a.append(tsplit[i][0])
print(a)