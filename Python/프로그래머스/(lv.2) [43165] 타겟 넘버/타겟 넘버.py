def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하는 경우 + 빼는 경우를 합산하여 반환
        return dfs(index + 1, current_sum + numbers[index]) + \
               dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)