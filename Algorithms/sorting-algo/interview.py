# def find_empty(bo):
#     for i in range(len(bo)):
#         for j in range(len(bo[0])):
#             if bo[i][j] == 0:
#                 return (i, j)
#
#     return None
#
# def solve(bo):
#     pos = find_empty(bo)
#     if not pos:
#         return True
#     else:
#         row, col = pos
#     for i in range(1, 10):
#         if valid(bo, i, (row, col)):
#             bo[row][col] = i
#             if solve(bo):
#                 return True
#             bo[row][col] = 0
#
# def valid(bo, num, pos):
#     # check row
#     for i in range(len(bo[0])):
#         if bo[pos[0]][i] == num and pos[1] != i:
#             return False
#
#     # check column
#     for i in range(len(bo)):
#         if bo[i][pos[1]] == num and pos[0] != i:
#             return False
#
#     # check box
#     box_x = pos[1] // 3
#     box_y = pos[0] // 3
#
#     for i in range(box_y * 3, box_y * 3 + 1):
#         for j in range(box_x * 3, box_x * 3 + 1):
#             if bo[i][j] == num and (i, j) != pos:
#                 return False
#
#     return True
#
# def print_board(bo):
#     for num in bo:
#         print(' '.join(map(str, num)))
#
#
bo = [[0, 9, 5, 0, 2, 0, 0, 6, 0],
      [0, 0, 7, 1, 0, 3, 9, 0, 2],
      [6, 0, 0, 0, 0, 5, 3, 0, 4],
      [0, 4, 0, 0, 1, 0, 6, 0, 7],
      [5, 0, 0, 2, 0, 7, 0, 0, 9],
      [7, 0, 3, 0, 9, 0, 0, 2, 0],
      [0, 0, 9, 8, 0, 0, 0, 0, 6],
      [8, 0, 6, 3, 0, 2, 1, 0, 5],
      [0, 5, 0, 0, 7, 0, 2, 8, 3]]
# solve(bo)
# print_board(bo)
















