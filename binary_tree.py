# 클래스와 함수 선언
class Node():
    def __init__(self):
        self.data = None # 노드의 데이터 값
        self.left = None # 자식의 왼쪽 노드
        self.right = None # 자식의 오른쪽 노드

class BST:

    def __init__(self):
        self.root = None
        
    # 노드 삽입
    def insertNode(self, new_data):

        newNode = Node() # 노드 생성
        newNode.data = new_data # 노드 데이터 입력

        if self.root == None: # root값이 None이면 
            self.root = newNode # 새로운 노드를 root값을 줌
            return

        current = self.root # 근노값을 root변수에 줌

        while True:
            parent = current
            if new_data < current.data: # 현재 노드의 값이 새로운 노드의 값보다 크면
                current = current.left # root에 root 왼쪽 자식노드의 값을 줌 
                if current == None: # root값이 None이면 
                    parent.left = newNode # 현재 노드의 왼쪽 자식노드에 새 노드 삽입
                    break 

            elif new_data > current.data: # 현재 노드의 값이 새로운 노드의 값보다 작으면
                current = current.right # root에 root 오른쪽 자식노드의 값을 줌 
                if current == None: # root값이 None이면 
                    parent.right = newNode # 현재 노드의 오른쪽 자식노드에 새 노드 삽입
                    break

    # 노드 탐색        
    def find(self, find_data):
        current = self.root # current에 근노드 값을 줌

        while True:
            if current == None: # current값이 None이면 
                print("찾는 자료가 없습니다!!")
                return None

            if current.data > find_data: # current값이 찾는 값보다 크면
                current = current.left # current 값에 current의 왼쪽 자식노드를 줌

            elif current.data < find_data: # current값이 찾는 값보다 작으면
                current = current.right # current 값에 current의 오른쪽 자식노드를 줌

            else: # 찾는 자료값이 있으면
                print("찾는 자료: " + current.data)
                print("찾는 자료가 있습니다!!")
                return current

    # 전위순회            
    def preorder(self, node):

        if node != None: #node값이 None이 아니면 
            print(node.data, end = ' ') # node값을 출력
            self.preorder(node.left) # 재귀함수를 통해 노드의 왼쪽 자식 노드를 출력
            self.preorder(node.right) # 재귀함수를 통해 노드의 오른쪽 자식 노드를 출력
        

            
                
## 메인 코드 부분 ##
if __name__ == "__main__" :
    bst = BST()
    
    while True:
        print()
        print("==================================================\n")
        print(" [0: 종료] [1: 삽입] [2: 탐색] [3: preorder] \n")
        print("==================================================\n")
        menu = int(input("메뉴 입력: "))

        # 종료
        if menu == 0:
            quit()
            
        # insertNode(삽입)
        elif menu == 1:
            add_data = (input('입력할 자료: '))
            bst.insertNode(add_data)
            
            
        # find(탐색)
        elif menu == 2:
            find_data = (input('찾는 자료: '))
            bst.find(find_data)      

        # 출력
        elif menu == 3:
            bst.preorder(bst.root)

        # 오류
        else:
            print("[Error]다시 입력!!")
        
