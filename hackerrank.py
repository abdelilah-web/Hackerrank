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
    

#Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x2> x1 and v2>= v1:
        return 'NO'    
    elif (x1-x2) % (v2-v1) == 0:
        return 'YES'
    else:
        return 'NO'


#Between Two Sets
def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)
    count = 0
    for i in range(maxA, minB+1):
        if all([i%x==0 for x in a]):
            if all([y%i==0 for y in b]):
                count += 1
    return count 


#Time Conversion
def timeConversion(s):
    hour = int(s[:2])
    h24 = 12
    if s[-2]=='P':
        if s[:2]=='12':
            return s[:-2]
        for h in range(1,hour+1):
            h24 += 1
            if h == hour:
                STR = str(h24),':',s[3:-2]
                big_str = ''.join(STR)
                return big_str
    elif s[-2]=='A':
        if s[:2]=='12':
            STR = '00',s[2:-2]
            big_str = ''.join(STR)
            return big_str
        else:
            return s[:-2]


#Breaking the Records
def breakingRecords(scores):
    H_score = scores[0]
    L_score = scores[0]
    N_H_score = 0
    N_L_score = 0
    for score in scores:
        if score > H_score:
            H_score = score
            N_H_score += 1
        elif score < L_score:
            L_score = score
            N_L_score += 1
    return str(N_H_score),str(N_L_score)


#Subarray Division
def birthday(s, d, m):
    square = 0
    try:        
        for n in range(len(s)):
            k = 0
            for x in range(1,m+1):
                k += s[n]
                n += 1
                if k == d and x == m :
                    square += 1          
    except:
        pass            
    return square 


#Divisible Sum Pairs
def divisibleSumPairs(n, k, ar):
    pairs=0
    for i in range(len(ar)):
        number_1 = ar[i]
        for j in range(len(ar)):
            number_2 = ar[j]
            if i<j and (number_1+number_2)%k ==0:
                pairs +=1            
    return pairs  


#Migratory Birds
def migratoryBirds(arr):
    Dic = {}
    for x in range(max(arr)+1):
        z = 0
        for y in arr:
            if x==y :
                z += 1
                Dic[x]= z
    return max(Dic, key=Dic.get)  


#Day of the Programmer
def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif 1700<= year<=1917 :
        return f'12.09.{year}' if year % 4 == 0 else  f'13.09.{year}'
    elif 1918 < year:
        return f'12.09.{year}' if year %400 ==0 or (year %4 ==0 and year % 100 !=0) else f'13.09.{year}'


#Bill Division
def bonAppetit(bill, k, b):
    anna_part = (sum(bill)-bill[k])/2
    print('Bon Appetit') if anna_part == b else print(int(b-anna_part))


#Reverse Word and Swap Cases
def reverse_words_order_and_swap_cases(sentence):
    sentence_list = sentence.split()
    reversed_list = sentence_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()


#Sales by Match
def sockMerchant(n, ar):
    pairs = 0
    ar_sorted = sorted(ar)
    for a in range(len(ar)):
        try :
            if ar_sorted[0]==ar_sorted[1]:
                ar_sorted.remove(ar_sorted[1])
                ar_sorted.remove(ar_sorted[0])  
                pairs += 1
            else :
                ar_sorted.remove(ar_sorted[0])
        except:
            pass
    return pairs


#Drawing Book
def pageCount(n, p):
    book =[]
    number_pages1 = 0
    number_pages2 = 0
    for x in range(1,n+1):
        if x%2 ==0:
            book.append('page')
        book.append(x)
    for y in book:
        if y=='page':
            number_pages1+=1
        elif y==p:
            break
    reverse_book = book[::-1]
    for z in reverse_book:
        if z =='page':
            number_pages2 += 1
        elif z == p:
            break
    minimum = min(number_pages1,number_pages2)
    return minimum


#Counting Valleys
def countingValleys(steps, path):
    sealevel = valey = 0
    for step in path:
        if step == 'U':
            sealevel += 1
        else :
            sealevel -= 1
        if step == 'U' and sealevel == 0:
            valey +=1
    return valey


#Electronics Shop
def getMoneySpent(keyboards, drives, b):
    l = []
    for x in keyboards:
        for y in drives:
            if x+y <= b:
                l.append(x+y)
    if not l:
        return -1
    else:
        return max(l)


#Cats and a Mouse
def catAndMouse(x, y, z):
    if abs(x-z)<abs(y-z):
        return 'Cat A'
    if abs(x-z)>abs(y-z):
        return 'Cat B'
    if abs(x-z)==abs(y-z):
        return 'Mouse C' 


#Forming a Magic Square
def formingMagicSquare(s):
    base = [
        [4,9,2,3,5,7,8,1,6],
        [4,3,8,9,5,1,2,7,6],
        [2,9,4,7,5,3,6,1,8],
        [2,7,6,9,5,1,4,3,8],
        [8,1,6,3,5,7,4,9,2],
        [8,3,4,1,5,9,6,7,2],
        [6,7,2,1,5,9,8,3,4],
        [6,1,8,7,5,3,2,9,4],
    ]
    s = s[0]+s[1]+s[2]
    count = 100        
    for square in base:
        a =0
        for i,j in zip(square,s):
            a += abs(i-j)
        if a<count :
            count = a
    return count       


#Picking Numbers
def pickingNumbers(a):
    total_count = []
    for number in a:
        count = 0
        for number_1 in a:
            if number-number_1 == 1 or number-number_1 == 0:
                count+=1
        total_count.append(count)
    return max(total_count) 


#The Hurdle Race
def hurdleRace(k, height):
    if max(height)>k:
        return max(height)-k
    else:
        return 0
            

#Designer PDF Viewer
def designerPdfViewer(h, word):
    a_z = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    L = []
    for letter in word:
        L.append(a_z.index(letter))
    for indx in L:
        if h[indx]>count:
            count = h[indx]  
    return count*len(word)


#Utopian Tree
def utopianTree(n):
    height = 1
    for period in range(n):  
        if height % 2 ==0:
            height += 1
        else:
            height *= 2
    return height


#Angry Professor
def angryProfessor(k, a):
    count = 0
    for i in a :
        if i<=0 :
            count += 1
    if k>count:
        return 'YES' 
    else:
        return 'NO'


#Angry Professor(using lambda_map_sum)
def angryProfessor(k, a):
    return 'YES' if sum(map(lambda x: x <= 0, a)) < k else 'NO'


#Angry Professor(using lambda_filter)
def angryProfessor(k, a):
    return "NO" if len(list(filter(lambda x: x<=0, a))) >= k else "YES"


#Beautiful Days at the Movies
def beautifulDays(i, j, k):
    count = 0
    for day in range(i,j+1):
        if abs(day-int(str(day)[::-1]))%k==0:
            count +=1
    return count


##Beautiful Days at the Movies '2'
def beautifulDays(i, j, k):
    return sum([5 for day in range(i,j+1) if abs(day-int(str(day)[::-1]))%k==0 ])


#Viral Advertising
def viralAdvertising(n):
    count = 2
    var = 2
    for i in range(2,n+1):
        day = var*3
        var = day//2
        count += var 
    return count


#Climbing the Leaderboard -1- 
def climbingLeaderboard(ranked, player):
    L = []
    for game in player:
        ranked.append(game)
        ranked = sorted(ranked, reverse = True)
        rank = {max(ranked):1}
        number = 1
        for i in range(1,len(ranked)):
            if ranked[i] != ranked[i-1]:
                number +=1
            rank[ranked[i]] = number
        L.append(rank.get(game))
    return L


#Climbing the Leaderboard -2- 
def climbingLeaderboard(ranked, player):
      rank = list(set(ranked))
      rank.sort()
      player.sort()
      resp = list()
      x = len(rank)+1
      for item in player:
           resp.append(x - bisect.bisect(rank, item))
      return resp


#Save the Prisoner!
def saveThePrisoner(n, m, s):
    result = s+m-1   
    if result > n :
        if result %n ==0:
            return n
        else:
            a = result //n
            b = a*n
            result -= b  
    return result


#Circular Array Rotation
def circularArrayRotation(a, k, queries):
    if k > len(a):
        k = k % len(a)
    k = len(a) - k
    a = a[k:] + a[:k]
    return [a[i] for i in queries] 


#Sequence Equation
def permutationEquation(p):
    p = [0]+p
    L = list()
    number = 1
    for _ in p:
        for indx in range(len(p)):
            try :
                if p[p[indx]] == number:
                    L.append(indx)
                    number +=1
            except:
                pass   
    return L    


#Find Digits
def findDigits(n):
    n = str(n)
    count = 0
    for i in n:
        i = int(i)
        n = int(n)
        if i == 0:
            pass
        elif n%i==0:
            count +=1
    return count 
#2
def findDigits(n):
    return sum([1 for i in str(n) if int(i) !=0 and n%int(i)==0])


#Append and Delete
def appendAndDelete(s, t, k):
    s_length = len(s)
    t_length = len(t)
    if s_length + t_length < k: return 'Yes'
    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l: same += 1
        else: break 
    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t
    if difference <= k and difference % 2 == k % 2: return 'Yes'
    return 'No'


#Sherlock and Squares
def squares(a, b):
    number_of_square = 0
    for n in range(a,b+1):
        square_n = math.sqrt(n)
        if int(square_n)**2 == n:
            number_of_square = 1
            break 
    square_n += 1
    while int(square_n)**2 <= b:
        number_of_square += 1
        square_n += 1
    return number_of_square


#Library Fine
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2 == y1:
        if m1 > m2: 
            return 500* (m1-m2)
        elif m1 == m2:
            if d1 <= d2:
                return 0
            else: 
                return 15* (d1-d2)
        else : return 0
    elif y1<y2: return 0
    else : return 10000 


#Cut the sticks
def cutTheSticks(arr):
    result = [len(arr)]
    while True:                 
        arr = [x for x in arr if x != min(arr)] 
        
        if len(arr)==0:
            break
        result.append(len(arr))
    return result


# Non-Divisible Subset
def nonDivisibleSubset(k, s):
    counts = [0] * k
    for number in s:
        counts[number % k] += 1
    count = min(counts[0], 1)
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0: 
        count += 1
    return count


#Repeated String
def repeatedString(s, n):
    only_a = list(set(s))
    if len(only_a)==1 and only_a[0]=='a':
        return n
    counts = s.count('a')
    copy = n//len(s)
    remainders = n%len(s)
    remainders_a = s[:remainders]

    counts *= copy 
    counts += remainders_a.count('a')
    return counts


#Jumping on the Clouds
def jumpingOnClouds(c):
    count = 0
    cloud = 0
    for x in range(len(c)+1):
        cloud += 2
        if cloud >= len(c) :
            try :
                c[cloud-1]
                count +=1
                break
            except:
                break
        if c[cloud]==1:
            cloud -= 1
        count +=1
    return count


#Equalize the Array
def equalizeArray(arr):
    equal_value = max(set(arr), key=arr.count)
    other_value = len(arr)-arr.count(equal_value)
    return other_value


#Queen's Attack II
def queensAttack(n, k, r_q, c_q, obstacles):
    up = n- r_q
    right = n- c_q
    down = r_q -1
    left = c_q - 1
    up_right = min(up,right)
    down_right = min(right,down)
    down_left = min(down,left)
    up_left = min(left,up)

    for o in obstacles:
        if o[0] == r_q:
            if o[1]>c_q:
                right = min(right,o[1]-c_q-1)
            elif o[1]<c_q:
                left = min(left,c_q-o[1]-1)
        elif o[1] == c_q:
            if o[0]>r_q:
                up = min(up,o[0]-r_q-1)
            elif o[0]<r_q:
                down = min(down,r_q-o[0]-1)       
        elif abs(o[0]-r_q) == abs(o[1]-c_q) :
            if o[0] > r_q:
                if o[1]<c_q:
                    up_left = min(up_left,o[0]-r_q-1) 
                elif o[1]>c_q:
                    up_right = min(up_right, o[0]-r_q-1)
            elif o[0]< r_q:
                if o[1]<c_q:
                    down_left = min(down_left, r_q-o[0]-1)
                elif o[1]>c_q:
                    down_right = min(down_right, r_q-o[0]-1)
    return up+right+down+left+up_right+down_right+down_left+up_left


#Organizing Containers of Balls
def organizingContainers(container):
    r = sorted([sum(x) for x in container])
    c = sorted([sum(x) for x in zip(*container)])
    return "Possible" if r == c else "Impossible"


#Encryption
def encryption(s):
    s= s.replace(' ','')
    sqrt = math.sqrt(len(s))
    if sqrt.is_integer() == True:
        column = int(sqrt)
    else :
        column = int(sqrt)+1

    ListbeforeEncryption = []
    for i in range(0,len(s),column):
        L = s[i:i+column]
        ListbeforeEncryption += [L]

    ListEncrypt = []
    for zipped in zip_longest(*ListbeforeEncryption):
        remove_None = list(filter(None, zipped))
        JoinLettersInAWord = ''
        JoinLettersInAWord = JoinLettersInAWord.join(remove_None)
        ListEncrypt.append(JoinLettersInAWord)
        
    result = ' '.join(ListEncrypt)
    return result


#Bigger is Greater
def biggerIsGreater(w):
    org = w
    w = list(w)
    n = len(w)
    zeta = n
    for i in range(n-2,-1,-1):
        j = [b for b in w[i+1:] if b>w[i]]
        if len(j)!=0:
            zeta=i
            k = min(j)
            myind = i+(w[i+1:].index(k))+1
            w.insert(i,k)
            del w[myind+1]
            break
    newstri = ''.join(w[:zeta+1]+sorted(w[zeta+1:n]))
    if newstri==org:
        newstri='no answer'
    return newstri

#Modified Kaprekar Numbers
def IsKaprekar(n):
    square = str(n**2)
    L_sqr = len(square)
    try :
        if n == 1:
            return True 
        elif 10**(L_sqr-1) == n:
            return False
        elif int(square[:L_sqr//2])+int(square[L_sqr//2:]) == n :
            return True
        else:
            return False
    except:
        return False
def kaprekarNumbers(p, q):
    numbers = range(p,q+1)
    result = list(filter(IsKaprekar,numbers ))
    if len(result)==0:
        print('INVALID RANGE')
    else:
        print(*result)