a = [17,28,30]
b = [99,16,8]

def compareTriplets(a, b):
    # Write your code here
    note_a = 0
    note_b = 0
    for number in range(3):
        if a[number] > b[number]:
            note_a += 1
        if a[number] < b[number]:
            note_b += 1
    return note_a, note_b

print(compareTriplets(a, b))

for number in range(3):
    print(number)