import time    
import utils

##################### CODE HERE FOR USER-DEFINED FUNCTION #####################   


###############################################################################

def solution(test_case):        
    
    start_time = time.time()
    
    ##################### CODE HERE #####################  
    ############### 풀이 ###############
    # 이 문제는 정렬하지 않고 풀 수 있다.
    # 각 자리수가 0~9이기 때문에
    # 1. 각 자리수가 몇 번 나오는지 카운팅
    # 2. 인풋 길이의 반 만큼 카운팅을 제거
    # 3. 문자열 합치기
    # 위 과정대로 하면 시간 복잡도 O(N)으로 정렬하지 않아도 풀 수 있다.
    result = '';

    # 1. 각 자리수가 몇 번 나오는지 카운팅
    count_list = [0] * 10;
    mid = len(test_case) // 2;

    for num in test_case:
        count_list[int(num)] += 1;
    
    # 2. 인풋 길이의 반 만큼 카운팅을 제거
    search_idx = 0;
    while (mid != 0):
        if (count_list[search_idx] == 0):
            search_idx += 1;
            continue;
        count_list[search_idx] -= 1;
        mid -= 1;
    
    # 3. 문자열 합치기
    for i in range(len(count_list)):
        result += count_list[i] * str(i);
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

    INPUT_PATH = args.input
    OUTPUT_PATH = args.output

    utils.output_checker(args.output)    
    test_cases = utils.read_input(args.input)

    for test_case in test_cases:
        result = solution(test_case)
        utils.write_ouput(OUTPUT_PATH, result)
    
    utils.compare_files(OUTPUT_PATH)
    
