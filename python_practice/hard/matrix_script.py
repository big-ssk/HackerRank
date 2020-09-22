# https://www.hackerrank.com/challenges/matrix-script/problem


res = ''.join(''.join(i) for i in zip(*matrix))  # ''.join(matrix[i][j] for j in range(m) for i in range(n))
print(re.sub(r'\b(\W+)\b', ' ', res))
