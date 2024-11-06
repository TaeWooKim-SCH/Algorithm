# def bin2(n, k):
#   B = [[0] * (k + 1) for _ in range(n + 1)];
#   for i in range(n + 1):
#     for j in range(min(i, k) + 1):
#       if (j == 0 or j == i):
#         B[i][j] = 1;
#       else:
#         B[i][j] = B[i - 1][j - 1] + B[i - 1][j];
#   return B[n][k];

# for n in range(10):
#   for k in range(n + 1):
#     print(bin2(n, k), end = " ");
#   print();

# def bin3(n, k):
#   if (k > n // 2):
#     k = n - k;
#   B = [0] * (k + 1);
#   B[0] = 1;
#   for i in range(1, n + 1):
#     j = min(n, k);
#     while (j > 0):
#       B[j] += B[j - 1];
#       j -= 1
#   return B[k];

# for n in range(10):
#   for k in range(n + 1):
#     print(bin3(n, k), end = " ");
#   print();

# print(bin3(9, 5));

DP = [0];

def climb_stair(stairs):
  if (len(stairs) == 1):
    DP.append(stairs[0]);
    return;
  elif (len(stairs) == 2):
    DP.append(max(stairs[0], stairs[1]));
    return;

  first = max(stairs[len(stairs) - 1], stairs[len(stairs) - 2]);
  seconde = max(stairs[len(stairs) - 1], stairs[len(stairs) - 3]);
  DP.append(max(first, seconde));

  return climb_stair(stairs[:len(stairs) - 1]);

stairs = [6, 10, 20, 15, 25, 10, 20];

climb_stair(stairs)
print(DP);