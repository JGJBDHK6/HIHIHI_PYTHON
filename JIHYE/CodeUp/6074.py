atoz = ord(input()) #ord는 문자 입력을 숫자로 변환 ex) a -> 97
anum = ord('a')     # 비교를 위하여 'a'를 숫자로 변환하여 저장

while anum <= atoz :
  print(chr(anum), end = ' ') # chr은 숫자를 문자로 변환 표현
  anum = anum + 1  # anum += 1 로도 표현 가능
