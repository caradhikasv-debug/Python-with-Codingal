# 1) Create a list `L` with some integer values and print it as the original list.
l=[45,65,5,9,2,69]
print("ORIGINAL LIST:",l)
# 2) Initialize a variable `count = 0` to store the sum of all elements in the list.
c=0
# 3) Use a `for` loop to iterate through each element `i` in the list `L`:

# a) Add each element to `count` using `count += i`.
for i in l:
    c+=i
# 4) Calculate the average of the list:

# a) Divide the total sum `count` by the number of elements `len(L)`.

# b) Store the result in `avg`.
avg=c/len(l)
# 5) Print the total sum and the average.
print("total sum:",c)
print("average:",avg)
# 6) Sort the list `L` in ascending order using `L.sort()`.
l.sort()
# 7) After sorting:

# a) The smallest element will be at index 0 → print `L[0]`.

# b) The largest element will be at the last index → print `L[-1]`.
print(l[0])
print(l[-1])