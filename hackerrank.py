a = [17,28,30]
b = [99,16,8]
#Compare the Triplets
def compareTriplets(a, b):
    note_a = 0
    note_b = 0
    for number in range(3):
        if a[number] > b[number]:
            note_a += 1
        if a[number] < b[number]:
            note_b += 1
    return note_a, note_b

print(compareTriplets(a, b))


#A Very Big Sum
def aVeryBigSum(ar):
    total = 0
    for number in ar:
        total += number
    return total


#Diagonal Difference
def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0 
    n = 0
    y = len(arr[1])-1
    for listt in arr:
        a += listt[n]
        b += listt[y]
        n += 1
        y -= 1
    c = a - b
    return abs(c)


#Diagonal Difference 2 
def diagonalDifference(arr):
    l, r = 0, 0
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1]
        print(r)
    return abs(l-r)


#Plus Minus
def plusMinus(arr):
    num = len(arr)
    # p positive, n negative , z zero
    p = 0
    n = 0
    z = 0
    for number in arr:
        if number > 0 :
            p += 1
        if number < 0 :
            n += 1
        if number == 0 :
            z += 1
    print(round((p/num),6))
    print(round((n/num),6))
    print(round((z/num),6))
    # round is for numbers after the comma


#Staircase
def staircase(n):
    for stair in range(1, n+1):
        n -= 1
        print(' '*n + '#'*stair)


#Mini-Max Sum
def miniMaxSum(arr):
    # Write your code here
    smaller = bigger = arr[0]
    minimum = 0
    maximum = 0
    for number in arr:
        if number < smaller:
            smaller = number
        if number > bigger:
            bigger = number   
        minimum += number 
        maximum += number  
          
    minimum = minimum - bigger
    maximum = maximum - smaller
    print(minimum, maximum )



#Birthday Cake Candles
def birthdayCakeCandles(candles):
    height = 0
    unit = 1
    for number in candles:
        if number >= height:
            if number == height:
                unit += 1
            height = number
        
    return unit   
            

#Grading Students
def gradingStudents(grades):
    list_grades = []
    for grade in grades:
        if grade < 38:
            list_grades.append(grade)
        if 38 <= grade <= 100:
            if (grade +1)% 5 == 0:
                list_grades.append(grade+1)
            elif (grade +2)% 5 == 0:
                list_grades.append(grade+2)
            else :
                list_grades.append(grade)
    return list_grades


#Apple and Orange
def countApplesAndOranges(s, t, a, b, apples, oranges):
    number_apples = 0
    number_oranges = 0
    for apple in apples:
        pos_apple = a + apple
        if s <= pos_apple <= t:
            number_apples += 1
            
    for orange in oranges:
        pos_orange = b + orange
        if s <= pos_orange <= t:
            number_oranges += 1    
    
    print(number_apples)
    print(number_oranges)
    