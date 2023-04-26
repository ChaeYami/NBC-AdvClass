# 파스칼의 삼각형


# 정리한 2차 풀이 (리스트 컴프리헨션, 리스트에 연산자 사용하기)

def pascal(n):
    m = n - 1 # 리스트 인덱스는 0부터 시작하므로 맞춰주기
    if m == 0: # 0번째 리스트, 즉 1번 줄
        return [1]
    
    else:
        before = pascal(n-1) #  이전 리스트
        return [1] + [before[i-1] + before[i] for i in range(1, m)] + [1]

print(pascal(8)) # [1, 7, 21, 35, 35, 21, 7, 1]



# 1차 풀이

# def pascal(n):
#     m = n - 1 # 리스트 인덱스는 0부터 시작하므로 맞춰주기
#     if m == 0: # 0번째 리스트, 즉 1번 줄
#         return [1]
    
#     else:
#         before = pascal(n-1) #  이전 리스트
        
#         p = [1] # 가장 앞에 1
        
#         for i in range(1,m):
#             p.append(before[i-1] + before[i]) 
            
#         p.append(1) # 마지막에 1
        
#         return p

# print(pascal(8)) # [1, 7, 21, 35, 35, 21, 7, 1]

