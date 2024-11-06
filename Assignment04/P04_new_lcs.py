import time    
import utils

    
def solution(test_case):
    # time check
    start_time = time.time()
    
    ##################### CODE HERE #####################
    # 1. 입력 처리 및 기본 변수 초기화
    X, Y = test_case.split('\n');
    X = ' ' + X;
    Y = ' ' + Y;
    X_len, Y_len = len(X), len(Y);
    dp = [[0 for _ in range(Y_len)] for _ in range(X_len)]; # lcs 길이 테이블
    tracking_dp = [[0 for _ in range(Y_len)] for _ in range(X_len)]; # 역추적 테이블

    # 2. lcs 길이 탐색
    for X_i in range(X_len):
        for Y_i in range(Y_len):
            if (X[X_i] == Y[Y_i]): # 두 문자가 같다면
                dp[X_i][Y_i] = dp[X_i - 1][Y_i - 1] + 1; # 왼쪽 위 대각선 + 1
                tracking_dp[X_i][Y_i] = 1; # 역추적 테이블에 대각선에서 온 경우엔 1로 설정
            else: # 두 문자가 다르다면
                if (dp[X_i][Y_i - 1] >= dp[X_i - 1][Y_i]): # 왼쪽 값이 더 크거나 같으면
                    dp[X_i][Y_i] = dp[X_i][Y_i - 1]; # 왼쪽 값을 가져옴
                    tracking_dp[X_i][Y_i] = 2; # 역추적 테이블에 오른쪽에서 온 경우엔 2로 설정
                else: # 오른쪽 값이 더 크면
                    dp[X_i][Y_i] = dp[X_i - 1][Y_i]; # 오른쪽 값을 가져옴
                    tracking_dp[X_i][Y_i] = 3; # 역추적 테이블에 위쪽에서 온 경우엔 3으로 설정
    
    # 3. lcs 구하기
    lcs_X, lcs_Y = X_len - 1, Y_len - 1; # 뒤에서부터 추적하기 위해 길이 정보를 가져옴
    lcs_list = []; # lcs 문자열 요소들이 담길 리스트

    while (lcs_X > 0 and lcs_Y > 0): # X 또는 Y의 인덱스가 0보다 크면 반복
        if (tracking_dp[lcs_X][lcs_Y] == 3): # 위쪽에서 온 경우
            lcs_X -= 1; # 위로 추적
        elif (tracking_dp[lcs_X][lcs_Y] == 2): # 왼쪽에서 온 경우
            lcs_Y -= 1; # 왼쪽으로 추적
        else: # 대각선에서 온 경우
            lcs_list.append(X[lcs_X]); # lcs 문자열 요소 리스트에 반영
            lcs_X -= 1; # 대각선으로 추적
            lcs_Y -= 1; #  대각선으로 추적

    lcs = ''.join(reversed(lcs_list)); # 거꾸로 탐색했기 때문에 반전시켜줘야 답이 나옴
    lcs_length = len(lcs);
    #####################################################

    # end time
    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.8f} seconds".format(elapsed_time))

    result = f"{lcs} {lcs_length}"

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
        result = solution(test_case)
        utils.write_ouput(args.output, result)
    
    utils.compare_files(args.output)
    
