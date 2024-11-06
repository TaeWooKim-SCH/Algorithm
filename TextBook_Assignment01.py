# n개의 수로 구성된 리스트에서 m개의 가장 작은 수를 찾는 알고리즘을 작성하시오.
n_list = list(map(int, input().split(" ")));
m = int(input());

# def quick_sort(list):
#   if (len(list) <= 1):
#     return list;
#   pivot = list[len(list) // 2];
#   less_list, equal_list, greater_list = [], [], [];
#   for num in list:
#     if (num < pivot):
#       less_list.append(num);
#     elif (num > pivot):
#       greater_list.append(num);
#     else:
#       equal_list.append(num);
#   return quick_sort(less_list) + equal_list + quick_sort(greater_list);

# def solution(n_list, m):
#   if (len(n_list) < m):
#     return "인덱스 범위 초과";
#   sorted_list = quick_sort(n_list);
#   return sorted_list[:m];

# print(solution(n_list, m));

# def solution(n_list, m):
#   result = [];

#   for _ in range(m):
#     temp = n_list[0];
#     for num in n_list[1:]:
#       if (num < temp):
#         temp = num;
#     result.append(temp);
#     n_list.remove(temp);

#   return result;

# # 정수 2개의 최대공약수를 구하는 알고리즘을 작성하시오
# a, b = map(int, input().split(" "));
# while (b > 0):
#   a, b = b, a % b;