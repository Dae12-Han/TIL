'''
학생들의 이름과 점수를 딕셔너리에 저장하시오.
모든 학생의 평균 점수를 계산하여 출력하시오.
80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.

학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.
students={'Alice':85,'Bob':78,'Charlie':92,'David':88,'Eve':95}
score_avg=sum(students.values())/len(students)
students_sort = sorted(students.items(), key=lambda x: x[1], reverse=True)

print(f"1. 학생들의 이름과 점수를 딕셔너리에 저장")
print(f"students type: {type(students)}")
print(f"학생들의 이름과 점수: {students}")

print(f"2. 모든 학생들의 평균 점수: {score_avg:.2f}")

over_avg = [name for name, score in students.items() if score >= 80]
print("3. 기준 점수(80점) 이상을 받은 학생 수: ", over_avg)

print("4. 점수 순으로 정렬: ")
for name,score in students_sort:
   print(f"{name}: {score}")

print(f"5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {max(students.values())-min(students.values())}")
print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for name,score in students.items():
   if score>=score_avg:
      print(f"{name} 학생의 점수({score})는 평균 이상입니다.")
   else:
      print(f"{name} 학생의 점수({score})는 평균 이하입니다.")
