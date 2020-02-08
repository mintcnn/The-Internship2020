start = input().split()
answer = ['_','_','_','_','_','_','_','_','_','_','_','_']
score = 0
print(' '.join(answer))
for n in range(5):
    ans = input()
    if ans in start:
        number = start.count(ans)
        score += number
        address = 0
        while number > 0:
            index = start.index(ans, address, len(start))
            address = index+1
            answer[index] = ans
            number -= 1
    else:
        answer.append(ans)
    print(' '.join(answer))
print(score)

