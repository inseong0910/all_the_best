# 파이썬 코딩 도장 학습_황인성
# Chapter 19
# 계단식으로 별 출력하기
# for 반복문과 if 조건문을 사용하여 계단식으로 별(*)을 출력

# 1 콘솔은 2차원 평면이므로 별을 일정한 모양으로 출력하려면 반복문을 두 개 사용하는 것이 편리
# 반복문 안에 반복문을 중첩루프(다중루프)라고 함

for i in range(5): # 5회 반복, 바깥쪽 루프는 세로 방향
    for j in range(5): # 5회 반복, 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ')

    print('i:', i, '\\n', sep = '')

print('----------------------------------------')

# 2 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
# print는 기본적으로 출력 후 다음 줄로 넘어감

print('----------------------------------------')

# 3 사각형 모양 바꾸기
for i in range(7):
    for j in range(3):
        print('*', end='')
    print()

print('----------------------------------------')

# 4 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

# ij and i >= j
# 00
# 10 / 11
# 20 / 21 / 22
# 30 / 31 / 32 / 33
# 40 / 41 / 42 / 43 / 44

print('----------------------------------------')

# 5 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('----------------------------------------')

# 연습문제 : 역삼각형 모양으로 별 출력하기
# 다음 소스코드를 완성하여 역삼각형 모양으로 별이 출력되게 만드세요

for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

print('----------------------------------------')

# 심사문제 : 산 모양으로 별 출력하기
# 표준 입력으로 삼각혀으이 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요.
# input에서 안내 문자열은 출력하지 않아야 합니다.
# 이때 출력 결과는 예제와 정확히 일치해야 합니다.
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

h = int(input())
for i in range(h):
    for j in reversed(range(h)): # reversed : 리스트의 요소를 뒤집을 때 사용
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(h):
        if i > j:
            print('*', end='')
    print()