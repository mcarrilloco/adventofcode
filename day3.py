import re
import fileinput




total_sum_multiplication = 0
enabled = True


for line in fileinput.input():
    matches = re.findall(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', line.rstrip())
    for match in matches:
        # print(match.string)
        if match[-1] == "don't()":
            enabled = False
        elif match[-2] == "do()":
            enabled = True
        else:
            if enabled:
                total_sum_multiplication += int(match[1]) * int(match[2])

print(total_sum_multiplication)
# python day3.py < data/day3.input
