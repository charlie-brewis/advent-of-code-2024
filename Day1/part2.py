'''
This time, you'll need to figure out exactly how often each number from the left list appears in the
right list. Calculate a total similarity score by adding up each number in the left list after 
multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).
'''


#* Load data into lists
left_list = []
right_list = []
with open('Day1/input.txt', 'r') as file:
   for line in file:
       split_line = line.split('   ')
       left_list.append(int(split_line[0]))
       right_list.append(int(split_line[1]))

#* Precompute the counts of numbers in the right list
right_count = {}
for num in right_list:
    right_count[num] = right_count[num] + 1 if num in right_count else 1

#* Compute similarity score
similarity_score = 0
for num in left_list:
    if num in right_count:
        similarity_score += num * right_count[num]
        

print(right_count)
print(similarity_score)
