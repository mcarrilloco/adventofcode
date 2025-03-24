import re


total_sum_multiplication = 0
enabled = True


with open('data/day3.input', 'r') as file:
    # Read each line in the file
    for line in file:
        matches = re.findall(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', line)
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
