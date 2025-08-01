def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        reamin: 선택되지 않고 남은 값 목록 
    '''
    # 모든 요소를 선택할 것이니... 나머지가 없을 때까지
    if not remain:
    #if selected(remain)==3: #3개만 선택할 때
        print(selected)
    else: # 아직 선택할 요소가 남아있다면!
        for idx in range(len(remain)): # 그 요소를 모두 순회하면서
            # idx번째의 요소를 선택
            selected_item=remain[idx]
            # 선택된 idx번째를 제외한 remain을 만들자 (진짜 나머지 리스트)
            remain_list=remain[:idx]+remain[idx+1:]
            perm(selected+[selected_item],remain_list)

# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
