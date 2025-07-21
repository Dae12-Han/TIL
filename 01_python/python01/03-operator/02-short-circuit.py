vowels = 'aeiou'
print(('a' and 'b') in vowels)  # False -> 'a'가 True로 평가되지만 'b'는 vowels에 없으므로 False
print(('b' and 'a') in vowels)  # True -> 'b'가 True로 평가되지만 'a'는 vowels에 있으므로 True
print(3 and 5)  # 5 -> 3가 True로 평가되므로 5를 반환
print(3 and 0)  # 0 -> 3가 True로 평가되지만 0은 False로 평가되므로 0을 반환
print(0 and 3)  # 0
print(0 and 0)  # 0
print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
