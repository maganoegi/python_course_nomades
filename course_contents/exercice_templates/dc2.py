



from typing import TypeVar, Optional

T = TypeVar("T")

from dataclasses import dataclass

@dataclass
class DoubleLinkedNode:
    data: T
    next: Optional['DoubleLinkedNode']=None
    prev: Optional['DoubleLinkedNode']=None


@dataclass
class DoubleLinkedList:
    root: DoubleLinkedNode
    radius: int
    pi: float
    circumference: Optional[float]=None

    def __post_init__(self) -> None:
        self.circumference = self.pi * self.radius * 2

    @logged
    def add_right(self, node: DoubleLinkedNode) -> None:
        target = self.root
        while target.next != None:
            target = target.next

        node.prev = target
        target.next = node

    @logged
    def add_left(self, node: DoubleLinkedNode) -> None:
        target = self.root
        while target.prev:
            target = target.prev

        node.next = target
        target.prev = node


from myawesomelib import timed, logged, debug

@timed
def addition(a, b):
    return a + b

@timed
@logged
def square_huge_list(size):
    return [x**2 for x in range(size)]


@debug
def is_odd(val) -> bool:
    return val % 2 == 1

if __name__ == '__main__':

    result = square_huge_list(100)

    f = filter(lambda x : is_odd(x), result)
    l = list(f)

    # print(result)


    # dll = DoubleLinkedList(DoubleLinkedNode(data=0), 2, 3.14)
    # print(dll)

    # lst = [1, 2, 3, 4, 5]

    # for v in lst:
    #     dll.add_right(DoubleLinkedNode(data=v))

    # print(dll)
        
