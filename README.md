# Ice-Skating-Snow-Drifts-Problem
Updated personal solution for Ice Skating Snow Drifts Problem.


Some issues that existed with my previous solution submitted:
```
- Assumed that pairs exist. It is possible that there are no matching values for any n tuples in the list
	ie. (1,3) and (2,4) do not share a common value, thus it would not pair any values

- Loop conditions. If there were no matching pairs, it would result in a timeout due to infinite looping.

- Efficiency. Assuming that the proposed solution actually did work, it would have been highly inefficient due to:
	Calling the matching function -> For loop to iterate through the entire list of coordinates
	Loop in main function -> Looping multiple times through the list of coordinates until every matched pair was created
	(NEW FUNCTION NOT WRITTEN) Looping through 2D list of tuples -> Nested Loop to find each optimal direction to take
```


New Solution:
The new solution is built to check for edge cases and more than two unique coordinates.
The overall process is:

```
1. Insert all coordinates as keys into a dictionary. Their value will default to the x-coordinate.
  This ensures that if there is a case where there are no groupings that can be made, it will return n-1
2. Runs a nested loop (i and j) with both loops iterating through the same dictionary.
3. When the inner loop and outer loop shares a common coordinate, calls the update_shared_values function
4. In update_shared_values, loop through the dictionary. If any has the value of i, update the value to j
5. Return the number of unique values in the dictionary, minus 1
```

Flaws:
```
1. Ineffiency. Running at O(N^3) due to 3 loops nested
2. Did not utilize # of coordinates. Given that it was one of the inputs, it's likely that it
   had some relation to a better solution
3. Did not utilize transitivity/chain logic (ie. a = b = c)
```

Example Case:
```
Given a list of tuples: (1,1), (1,10), (5,10)

Insert to dictionary, the dictonary is now:
          {(1, 1): 1, (1, 10): 1, (5, 10): 5}

First Loop:
i = (1,1) | j = (1,1)
Result: Ignore

Second Loop:
i = (1,1) | j = (1,10)
Result: Match, the values remain as 1

Third Loop:
i = (1,1) | j = (5,10)
Result: No match

.
.
.

Sixth Loop:
i = (1,10) | j = (5,10)
Result: Update all values to 10
.
.
.
```
End:
```
Dictionary: {(1, 1): 10, (1, 10): 10, (5, 10): 10}

Unique Values: 1

Return: 1 - 0 = 0
```

```
