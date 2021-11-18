class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(llist):
    cur = llist.head
    while cur:
        print(str(cur.data), end=' ')
        cur = cur.next


def mergeLists(head1, head2):
    tmp_list = SinglyLinkedList()

    while head1 and head2:
        if head1.data <= head2.data:
            tmp_list.insert_node(head1.data)
            head1 = head1.next
        else:
            tmp_list.insert_node(head2.data)
            head2 = head2.next

    while head1:
        tmp_list.insert_node(head1.data)
        head1 = head1.next
    while head2:
        tmp_list.insert_node(head2.data)
        head2 = head2.next

    return tmp_list


if __name__ == "__main__":
    # 1. List1 초기화
    llist1_count = int(input())
    llist1 = SinglyLinkedList()
    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)

    # 2. List2 초기화
    llist2_count = int(input())
    llist2 = SinglyLinkedList()
    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    # 3. List3 초기화 및 출력
    llist3 = mergeLists(llist1.head, llist2.head)
    print_singly_linked_list(llist3)