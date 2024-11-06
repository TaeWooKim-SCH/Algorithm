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
    dp = [[0 for _ in range(Y_len)] for _ in range(X_len)];

    # 2. lcs 길이 탐색
    for X_i in range(X_len):
        for Y_i in range(Y_len):
            if (X[X_i] == Y[Y_i]):
                dp[X_i][Y_i] = dp[X_i - 1][Y_i - 1] + 1;
            else:
                dp[X_i][Y_i] = max(dp[X_i][Y_i - 1], dp[X_i - 1][Y_i]);
    
    # 3. lcs 구하기
    lcs_X, lcs_Y = X_len - 1, Y_len - 1;
    lcs_list = [];

    while(lcs_X >= 0 and lcs_Y >= 0):
        if (dp[lcs_X][lcs_Y] == dp[lcs_X - 1][lcs_Y]):
            lcs_X -= 1;
        elif (dp[lcs_X][lcs_Y] == dp[lcs_X][lcs_Y - 1]):
            lcs_Y -= 1;
        else:
            lcs_list.append(X[lcs_X]);
            lcs_X -= 1;
            lcs_Y -= 1;

    lcs = ''.join(reversed(lcs_list));
    lcs_length = len(lcs);
    print(lcs, lcs_length);
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
    
