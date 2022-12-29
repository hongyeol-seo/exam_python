datas = {"과목" : ["국어","수학","윤리","국사"],"베트맨":[90,89,98,99],"마징가":[82,73,71,91],"피오나":[78,99,91,83]}

arrKeys = list(datas.keys())

s1 = datas["베트맨"]
batHight = s1.index(max(datas[arrKeys[1]])) #3
batrow = s1.index(min(datas[arrKeys[1]])) #3

s2 = datas["마징가"]
maHight = s2.index(max(datas[arrKeys[2]])) #3
marow = s2.index(min(datas[arrKeys[2]])) #3

s3 = datas["피오나"]
PHight = s3.index(max(datas[arrKeys[3]])) #3
Prow = s3.index(min(datas[arrKeys[3]])) #3

sub = datas["과목"]

print(f"{arrKeys[1]} 최고점수 {max(datas[arrKeys[1]])},{sub[batHight]}, 최저점수{min(datas[arrKeys[1]])},{sub[batrow]}")
print(f"{arrKeys[2]} 최고점수 {max(datas[arrKeys[2]])},{sub[maHight]}, 최저점수{min(datas[arrKeys[2]])},{sub[marow]}")
print(f"{arrKeys[3]} 최고점수 {max(datas[arrKeys[3]])},{sub[PHight]}, 최저점수{min(datas[arrKeys[3]])},{sub[Prow]}")

#1 

# i = 5
# result = [{i} * {j} = {i*j} for j in range(1,10) for i in range(2,10)]

# print(result)

# gugudan = [({x} + (y),(x*y)) for x in range(8) for y in range(9)]
# print(gugudan)



