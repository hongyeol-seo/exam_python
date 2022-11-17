# ---------------------------------
# dict 데이터 타입 전용 메서드
# ---------------------------------

jumsu = {'kor': [98, 99, 78], 'art': [100, 92, 99]}

# 키만 알고 싶다!

print(jumsu.keys(), type(jumsu.keys()))
# 타입은 dict_key! 예전에는 list로 주었었는데,
# view 라는 개념으로 보여주기 식으로 준다. / 뷰객체 / 예전에는 키만 있는 리스트를 주었엇는데, 그럼 보여주겠다고 /  필요하면 list를 생성해자

jumsuKeys = list(jumsu.keys())  # 리스트로 변경한다.

# 'dict_keys' object is not subscriptable / 읽을 수 없었다. / 방법론 배우면 리스트로 빼오는 방법을 안된다.
print(f'jumsu[0] {jumsuKeys[0]}')

print(jumsu.values())

# 키하고 값을 묶어서, 보여주는 ? items?
print(jumsu.items())  # dict_items 키하고 값을 묶어서, (값, 값2) 튜플로 묶어서 보여준다! 이것도 변경하려면 리스트로

jumsu = {'kor': [98, 99, 78], 'art': [100, 92, 99]}
# 과목별 최고점수, 최저점수, 합계 알고싶어요!
print()
# max(jumsu['kor']),max(jumsu['art']),min(jumsu['kor']),min(jumsu['art']),sum(jumsu['kor']),sum(jumsu['art'])

print('국어최고점수 : {}, 미술최고점수 : {}\n 국어최저점수 : {}, 미술최저점수{}\n, 국어합계 : {}, 미술합계 : {}'.format(max(jumsu['kor']), max(
    jumsu['art']), min(jumsu['kor']), min(jumsu['art']), sum(jumsu['kor']), sum(jumsu['art'])))
