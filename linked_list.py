#node 구조 생성
class Node:
    def __init__(self, data):
        self.data = data    # node를 생성할 때 입력값은 data로 저장
        self.next = None    # node에는 다음 node를 연결할 수 있는 변수 next가 존재
'''
head = Node(5)          #head를 생성, data = 5
next_node = Node(12)    #next_node를 생성, data = 12
head.next = next_node   #head에 next_node를 연결
'''

#single linked list 생성
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1
    
    #첫 번째 노드 삽입(head 교체)
    def insertFirst(self, data):
        new_node = Node(data)       # new_node 생성
        tmp_node = self.head        # tmp_node에 head 저장
        self.head = new_node        # head에 new_node 저장
        self.head.next = tmp_node   # head.next와 tmp_node 연결
        self.list_size += 1         # list_size 1 증가

    #노드 선택
    def selectNode(self, num):
        if self.list_size < num:    # 오버플로우
            return 
        node = self.head            # node에 head 저장
        count = 0                   # count 0으로 초기화
        while count < num:          # count가 num을 가리킬때까지 반복
            node = node.next
            count += 1
        return node
    
    #중간 노드 삽입
    def insertMiddle(self, num, data):
        if self.head.next == None:  # 만약 연결리스트에 head만 존재한다면
            self.insertLast(data)        # 메서드 insertLast()를 실행
            return
        node = self.selectNode(num) # node에 입력된 num의 인덱스에 해당하는 node를 저장
        new_node = Node(data)       # new_node에 새로운 node를 생성
        tmp_next = node.next        # tmp_next에 가져온 node의 다음 node를 저장
        node.next = new_node        # 다음 node 자리에는 새로운 node를 저장
        new_node.next = tmp_next    # 새로운 node의 다음 자리에 tmp_next에 저장해둔 node를 연결
        self.list_size += 1         # list_size 1 증가
        
    #마지막 노드 삽입
    def insertLast(self, data):
        node = self.head            # node에 head 저장
        while True:                 # 다음 링크가 없을 때까지 이동
            if node.next == None:
                break
            node = node.next        
        new_node = Node(data)       # new_node 생성
        node.next = new_node        # new_node 연결
        self.list_size += 1         # list_size 1 증가

    #노드 삭제
    def deleteNode(self, num):
        if self.list_size < 1:      # 언더플로우
            return                  
        elif self.list_size < num:  # 오버플로우
            return
        if num == 0:                # num이 0, 즉 head를 가리킨다면 deleteHead() 실행
            self.deleteHead()
            return
        node = self.selectNode(num-1)# node에 삭제할 노드의 전 node를 저장
        node.next = node.next.next  # node.next에 다다음 node를 연결
        del_node = node.next        # del_node에 삭제할 노드를 저장
        del del_node                # 삭제

    #헤드 삭제
    def deleteHead(self):   # 배열이 아니므로 전부 한칸씩 당길 필요가 없음!!
        node = self.head            # node에 head 저장
        self.head = node.next       # head에 다음 노드 저장
        del node                    # node(head) 삭제

