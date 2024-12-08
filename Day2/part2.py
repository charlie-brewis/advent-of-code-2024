'''
Now, the same rules apply as before, except if removing a single level from an unsafe report would 
make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from 
unsafe reports. How many reports are now safe?
'''


#* Parse data
with open('Day2/input.txt', 'r') as file:
    reports = [list(map(int, level.split(' '))) for level in file.readlines()]


#* Solution

# Function to check if a report is safe
def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    all_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)
    if not all_differences_valid: return False

    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    return is_increasing or is_decreasing

def is_safe_after_removing_one_level(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:] # Removes level i
        if is_safe(modified_report): return True
    return False


num_safe = 0
for report in reports:
    if is_safe(report) or is_safe_after_removing_one_level(report):
        num_safe += 1

print(num_safe)