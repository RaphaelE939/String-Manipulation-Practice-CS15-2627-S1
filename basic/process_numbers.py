string_to_process = "  18,27,35,20  "
numbas = string_to_process.strip().split(",")
a = int(numbas[0])
b = int(numbas[1])
c = int(numbas[2])
d = int(numbas[3])
tot = (a+b+c+d)
avg = tot/4
print(f"Total: {tot}")
print(f"Average: {avg}")

# Expected Output:
# "Total: 100"
# "Average: 25.0"