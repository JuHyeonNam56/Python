# file = open('test.txt')
# file.close()
#위 방법 보다 더 간단하고 자동으로 읽고 닫는 방법
#파일을 읽고 모든 줄을 리스트에 저장 그 다음 리스트 뒤집기를 해서 전체 줄을 반전시키고
#리스트를 뒤집고 나서 리스트를 파일에다시 쓰는 예제
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
                writer.write(line)
#읽기모드일 경우 'r' / 쓰기모드일 경우 'w'