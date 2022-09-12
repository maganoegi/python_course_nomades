







# revue
# dataclass -> doubly linked list
# precision @property
# decorateurs

from typing import TypeVar, Optional

T = TypeVar("T")

class DoubleLinkedNode:
    
    def __init__(
        self, 
        data: T, 
        next: Optional['DoubleLinkedNode']=None, 
        prev: Optional['DoubleLinkedNode']=None
    ) -> None:
        self._data = data
        self.next = next
        self.prev = prev

    @property
    def data(self) -> T:
        return self._data

    # def __str__(self) -> str:
    #     return f"-|{self.data}|-"


class DoubleLinkedList:
    def __init__(self, node: DoubleLinkedNode) -> None:
        self._root = node

    @property
    def root(self) -> DoubleLinkedNode:
        return self._root

    def add_right(self, node: DoubleLinkedNode) -> None:
        target = self.root
        while target.next != None:
            target = target.next

        node.prev = target
        target.next = node

    def add_left(self, node: DoubleLinkedNode) -> None:
        target = self.root
        while target.prev:
            target = target.prev

        node.next = target
        target.prev = node

    # def __str__(self) -> str:
    #     target = self.root
    #     while target.prev:
    #         target = target.prev

    #     res = str(target)
    #     while target.next:
    #         target = target.next
    #         res += str(target)

    #     return res


if __name__ == '__main__':

    dll = DoubleLinkedList(DoubleLinkedNode(data=0))

    print(dll)
    # lst = [1, 2, 3, 4, 5]

    # for v in lst:
    #     dll.add_right(DoubleLinkedNode(data=v))

    # print(dll)
        



