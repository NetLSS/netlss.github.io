start = input()
col = ord(start[0]) - ord('a') + 1 # 빼는 순서!
row = int(start[1])

mov_row = [-2,-2,-1,1,2, 2, 1,-1]
mov_col = [-1, 1,2 ,2,1,-1,-2,-2]
cnt = 0

for mov_type in range(len(mov_col)):
    final_row = row + mov_row[mov_type]
    final_col = col + mov_col[mov_type]
    if final_row < 1 or final_row > 8 or final_col < 1 or final_col > 8:
        continue
    cnt+=1
    
print(cnt)
     