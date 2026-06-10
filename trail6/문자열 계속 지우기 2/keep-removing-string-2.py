# 이 프로그램은 문자열 A에서 문자열 B를 반복적으로 찾아 삭제하는 문제를 해결합니다.
# 이 때 KMP 알고리즘의 실패함수를 활용하여 반복적인 탐색을 효율적으로 수행하는 방법을 사용합니다.

# 최대 문자열 길이를 고려하여 충분한 크기의 배열을 선언합니다.
MAX_SIZE = 200005

# 실패함수 배열을 선언합니다.
failureArray = [0] * MAX_SIZE

# 문자열을 스택처럼 다루기 위해 인덱스와 현재까지의 매칭 길이를 기록하는 두 개의 배열을 선언합니다.
indexStack = [0] * MAX_SIZE
matchLengthStack = [0] * MAX_SIZE

# 스택에 들어있는 요소의 개수를 기록하는 변수입니다.
stackSize = 0

# 각 위치의 문자가 삭제되었는지를 기록하는 배열입니다. true이면 삭제된 상태를 나타냅니다.
isRemoved = [False] * MAX_SIZE

# 문자열 B의 실패함수를 만드는 함수입니다.
# 실패함수는 패턴 내에서 자기 자신과 일치하는 접두사의 길이를 저장합니다.
def buildFailureFunction():
    global failureArray, B, Blen
    # 인덱스 0의 실패값을 -1로 초기화합니다.
    failureArray[0] = -1

    for i in range(1, Blen + 1):
        # 이전의 실패값을 가져옵니다.
        j = failureArray[i - 1]
        # 현재 문자와 j+1번째 문자가 일치하지 않는 동안 j를 갱신합니다.
        # 패턴 내에서 가능한 한 긴 접두사와 접미사가 일치하는 부분을 찾습니다.
        while j >= 0 and B[j + 1] != B[i]:
            j = failureArray[j]
        # 실패함수의 현재 위치의 값을 j+1로 설정합니다.
        failureArray[i] = j + 1

# 이 함수는 문자열 A를 순회하면서 문자열 B와의 매칭을 시도하고,
# 매칭된 경우 스택을 이용하여 해당 부분을 삭제하는 과정을 수행합니다.
def removeBOccurrences():
    global stackSize, indexStack, matchLengthStack, isRemoved, A, B, Alen, Blen, failureArray
    # 스택을 초기화하기 위해 더미 상태를 스택에 넣습니다.
    # 스택의 첫번째 요소는 0번째 인덱스를 의미하며, 매칭 길이도 0으로 설정합니다.
    indexStack[stackSize] = 0
    matchLengthStack[stackSize] = 0
    stackSize += 1

    # 현재까지의 매칭 길이를 저장하는 변수를 초기화합니다.
    currentMatchLength = 0

    # 문자열 A의 각 위치를 순회하면서 문자를 처리합니다.
    # pos 변수는 문자열 A 상의 현재 문자 위치를 나타냅니다.
    for pos in range(1, Alen + 1):
        # 현재 매칭 길이를 조정하기 위해서 KMP 실패함수를 사용합니다.
        # 만약 문자열 B의 다음 문자가 문자열 A의 현재 문자와 일치하지 않으면
        # 이전에 매칭된 부분을 기반으로 현재 매칭 길이를 조정합니다.
        while currentMatchLength >= 0 and B[currentMatchLength + 1] != A[pos]:
            currentMatchLength = failureArray[currentMatchLength]
        # 현재 문자가 문자열 B와 일치하였으므로 매칭 길이를 1 증가시킵니다.
        currentMatchLength += 1

        # 현재 문자열 A의 위치와 매칭 길이를 스택에 저장합니다.
        # 이는 나중에 문자열 B와 완전히 매칭되었을 때, 해당 위치들을 손쉽게 제거하기 위함입니다.
        indexStack[stackSize] = pos
        matchLengthStack[stackSize] = currentMatchLength
        stackSize += 1

        # 만약 현재까지 매칭된 문자의 수가 문자열 B의 전체 길이와 같다면
        # 문자열 B가 문자열 A 내에서 완전히 매칭된 것입니다.
        if currentMatchLength == Blen:
            # 패턴 길이만큼 스택에서 요소들을 제거하여 해당 부분이 삭제되도록 합니다.
            for k in range(Blen):
                # 스택의 가장 최상단에 있는 위치 인덱스를 가져옵니다.
                removedPos = indexStack[stackSize - 1]
                # 해당 위치의 문자를 삭제된 것으로 표시합니다.
                isRemoved[removedPos] = True
                # 스택에서 해당 요소를 제거하기 위해 스택 사이즈를 감소시킵니다.
                stackSize -= 1
            # 스택의 현재 최상단에 저장된 매칭 길이를 현재 매칭 길이로 복원합니다.
            currentMatchLength = matchLengthStack[stackSize - 1]

# 문자열 A를 입력받습니다.
A = input()
# 문자열 B를 입력받습니다.
B = input()

# A와 B의 길이를 저장합니다.
Alen = len(A)
Blen = len(B)

# 인덱스 1부터 시작할 수 있도록 앞에 빈 문자열을 추가합니다.
A = " " + A
B = " " + B

# 패턴에 대한 실패함수를 만듭니다.
buildFailureFunction()

# 문제의 핵심인, 문자열 B를 계속 찾아 지우는 것을 반복하는 함수입니다.
removeBOccurrences()

# 텍스트의 전체 문자 중 삭제되지 않은 문자들을 순서대로 출력합니다.
for pos in range(1, Alen + 1):
    # 만약 해당 위치가 삭제되지 않은 문자라면 출력을 수행합니다.
    if not isRemoved[pos]:
        print(A[pos], end = "")
