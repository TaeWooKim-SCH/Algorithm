import time    
import utils

##################### CODE HERE FOR USER-DEFINED FUNCTION #####################
def case_leftBuy_rightSell(daily_changes, buy_idx, mid_idx, sell_idx):
    # 왼쪽에서 매수 시점 탐색
    left_acc = 0;
    left_max = float('-inf'); # 최대 이익이 -인 부분을 고려
    left_max_idx = mid_idx;
    for buy_idx in range(mid_idx, buy_idx - 1, -1): # 이익이 최대가 될 때 매수 시점을 찾아야 하기 때문에 중간부터 누적합을 하며 탐색
        left_acc += daily_changes[buy_idx];
        if (left_acc > left_max):
            left_max = left_acc;
            left_max_idx = buy_idx;

    # 오른쪽에서 매도 시점 탐색
    right_acc = 0;
    right_max = float('-inf'); # 최대 이익이 -인 부분을 고려
    right_max_idx = mid_idx + 1;
    for sell_idx in range(mid_idx + 1, sell_idx + 1):
        right_acc += daily_changes[sell_idx];
        if (right_acc > right_max):
            right_max = right_acc;
            right_max_idx = sell_idx;

    return (left_max_idx, right_max_idx, left_max + right_max);

def max_profit_subarray(daily_changes, buy_idx, sell_idx):
    if (sell_idx == buy_idx):
        return (buy_idx, sell_idx, daily_changes[buy_idx]);
        
    mid_idx = (buy_idx + sell_idx) // 2;
    
    # 왼쪽에서 매수, 매도가 모두 발생할 때
    left_buy_idx, left_sell_idx, left_sum = max_profit_subarray(daily_changes, buy_idx, mid_idx);
    
    # 오른쪽에서 매수, 매도가 모두 발생할 때
    right_buy_idx, right_sell_idx, right_sum = max_profit_subarray(daily_changes, mid_idx + 1, sell_idx);
    
    # 왼쪽에서 매수가 일어나고 오른쪽에서 매도가 일어날 때
    cross_buy_idx, cross_sell_idx, cross_sum = case_leftBuy_rightSell(daily_changes, buy_idx, mid_idx, sell_idx);

    # 3가지 경우를 비교하고 최대의 이익이 되는 경우를 반환
    if (left_sum >= right_sum and left_sum >= cross_sum):
        return (left_buy_idx, left_sell_idx, left_sum);
    elif (right_sum >= left_sum and right_sum >= cross_sum):
        return (right_buy_idx, right_sell_idx, right_sum);
    else:
        return (cross_buy_idx, cross_sell_idx, cross_sum);
###############################################################################


def solution(test_case):  
    
    start_time = time.time()
    
    ##################### CODE HERE #####################
    ##################### 문제 풀이 #####################
    # 매수: B 매도: S 최대이익: M
    # B + S + M
    # 입력: 1일부터 N일 간의 주식의 종가 리스트
    # 현재 시점과 이전 시점의 차이를 이용해 변동률 리스트를 만든 후 누적합을 이용
    # 1. 분할 과정을 통해 왼쪽과 오른쪽 리스트를 나눔
    # 2. 분할이 끝나면 정복 과정에서 누적합을 이용해 이익이 최대가 되는 인덱스와 이익을 반환
    # 3. 이때 3가지 경우가 존재 -> 왼쪽에서 매도/매수가 모두 일어날 때, 오른쪽에서 매도/매수가 모두 일어날 때, 왼쪽에서 매수 후 오른쪽에서 매도할 때
    # 4. 3가지 경우를 비교해 가장 큰 이익일 때를 반환

    result = 0;
    ################# 입력처리 #################
    input = list(map(int, test_case.split(' ')));
    daily_changes = [input[i + 1] - input[i] for i in range(len(input) - 1)]; # 변동률 리스트 생성
    buy_idx = 0; # 매수 인덱스
    sell_idx = len(daily_changes) - 1;
    buy_idx, sell_idx, max_profit = max_profit_subarray(daily_changes, buy_idx, sell_idx);
    result = (buy_idx + 1) + (sell_idx + 2) + max_profit; # 인덱스가 0부터 시작하는 특성 때문에 실제 날짜는 1씩 더해줘야 하고, 매도 날짜는 변동률 리스트를 만들며 사라진 1만큼 추가를 해줌
    #####################################################

    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.8f} seconds".format(elapsed_time))

    return result

###################### DO NOT TOUCH BE0LOW ######################
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
    
