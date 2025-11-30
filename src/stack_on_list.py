class Stack():

    def __init__(self, arr:list|None = None) -> None:
        if arr is None:
            self.arr: list[int] = []
        else:
            self.arr = arr.copy()
        return None

    def __len__(self)->int:
        return len(self.arr)

    def peek(self)->int:
        return self.arr[-1]

    def min(self)->int:
        min_el = 10**10
        if len(self.arr)>0:
            for i in self.arr:
                if i<min_el:
                    min_el = i
        else:
            raise Exception("Stack is empty")
        return min_el

    def is_empty(self)->bool:
        return len(self.arr)==0

    def pop(self) -> int:
        if len(self.arr)!=0:
            return self.arr.pop()
        else:
            raise Exception("Stack is empty")

    def push(self, n:int)-> None:
        self.arr.append(n)
        return None
