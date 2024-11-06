import time    
import utils

def solution(test_case):
    start_time = time.time()

    ##################### CODE HERE #####################

    # python P01_body_guard.py --input C:\Users\bigda\Downloads\Assignment01-1\Assignment01\input --output C:\Users\bigda\Downloads\Assignment01-1\Assignment01\output
    ####### 출력 변수 선언 #######
    result: int = 0;

    ######### 입력처리 ###########
    split_input: list = test_case.split('\n'); # 인풋을 줄바꿈 기준으로 분리
    N, M = map(int, split_input[0].split(' ')); # 철수의 집 크기 (N, M)
    board: list[list[str]] = split_input[1:]; # 현재 배치된 보디가드의 위치를 나타내는 행렬

    for i in range(len(board)): # 맨 끝에 줄바꿈이 있는 입력도 있어 빈 리스트 발생 처리
        if (len(board[i]) == 0):
            board.pop();

    ########## 문제풀이 ###########
    # 최소 보디가드 수만 생각하면 되기 때문에
    # 각 행과 열 별로 or 연산 후
    # False인 행, 열을 카운팅하고 더 큰 결과만 리턴하면 됨
    # 해당 문제에선 메모리의 연산과 효율성을 위해 모두 불리언 값으로 처리 후 시작

    # 1. 'O/X로 이루어진 문자열을 다루기 쉽도록 True 또는 False 조합의 배열로 치환 -> X=0 O=1
    board: list[list[bool]] = [list(map(lambda x: True if x == 'O' else False, row)) for row in board];

    # 2. 행, 열이 모두 불린 값으로 이루어져 있기 때문에 행, 열 별로 or 연산한 리스트 생성
    #   - rows_count: 각각 행의 or 연산. 만약 False이면 해당 인덱스의 행은 보디가드 배치 필요
    #   - cols_count: 각각 열의 or 연산. 만약 False이면 해당 인덱스의 열은 보디가드 배치 필요
    nec_row_count: int = 0;
    nec_col_count: int = 0;
    
    for row_i in range(N): # 행에 대한 탐색
        if (any(board[row_i]) == False): # or 연산
            nec_row_count += 1;
    
    for col_i in range(M): # 열에 대한 탐색
        for row_i in range(N):
            if (board[row_i][col_i]):
                break; # 더 이상 탐색할 필요 없음. 해당 열은 이미 보디가드가 존재하기 떄문
            if ((board[row_i][col_i] == False) and (row_i == len(board) - 1)):
                nec_col_count += 1;

    result = max(nec_row_count, nec_col_count);
    #####################################################

    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.8f} seconds".format(elapsed_time))

    return result

###################### DO NOT TOUCH BELOW ######################
if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description = 'Argument parser')
    parser.add_argument('--input', '-i', default = './input', help = 'Input file path')
    parser.add_argument('--output', '-o', default = './output', help = 'Output file path')
    args = parser.parse_args()

    utils.output_checker(args.output)    
    test_cases = utils.read_input(args.input)

    for test_case in test_cases:
        result = solution(test_case) # solution function call here.
        utils.write_ouput(args.output, result)
    
    utils.compare_files(args.output)  
