import time    
import utils

##################### CODE HERE FOR USER-DEFINED FUNCTION #####################   
def merge(left, right):
    i, j = 0, 0;
    sorted_list = [];

    while ((i < len(left)) & (j < len(right))):
        if (left[i] < right[j]):
            sorted_list.append(left[i]);
            i += 1;
        else:
            sorted_list.append(right[j]);
            j += 1;
    
    sorted_list.extend(left[i:]);
    sorted_list.extend(right[j:]);

    return sorted_list;

def merge_sort(unsorted_list):
    if (len(unsorted_list) <= 1):
        return unsorted_list;

    mid = len(unsorted_list) // 2;
    left = unsorted_list[:mid];
    right = unsorted_list[mid:];

    merge_left = merge_sort(left);
    merge_right = merge_sort(right);

    return merge(merge_left, merge_right);

###############################################################################

def solution(test_case):        
    
    start_time = time.time()
    
    ##################### CODE HERE #####################   
    result: str = ''; 
    input_list: list[int] = list(map(int, test_case));
    input_sorted: list[int] = merge_sort(input_list);
    result = ''.join(map(str, input_sorted[len(input_sorted) // 2:]));
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
    
