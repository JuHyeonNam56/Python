file = open('test.txt')
#이 메소드를 통해 파일의 모든 콘텐츠를 읽을 수 있습니다.
#매개변수를 이용하여 특정 개수의 글자를 읽는다
#print(file.read(5))

print(file.readline())
#print(file.read(5))을 같이 쓰면 5번째 글자 이 후 부터 읽어서 혼란을 줄 수 있으니 주의
#readline을 이용하여 한 줄만 읽기

print(file.readline())

file.close()

#print lune 별로 출력