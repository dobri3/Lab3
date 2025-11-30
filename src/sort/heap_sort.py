import typer
from src.validation.sort_int_validation import sort_int_validation


def heap_sort()->None:
    """
    работает в режиме сортировки кучей

    :return: None
    """
    while (n:= input("Heap sort mode>> ")) not in ["back", 'b', 'q']:
            n = n.split()
            valid, message = sort_int_validation(n)
            if valid:
                n = list(map(int, n))
                print(*heap(n))
            else:  
                typer.secho(message, fg=typer.colors.RED)


def heap(a:list[int]) -> list[int]:
    """
    осуществляем cортировку кучей

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """
    n = len(a)
    for i in range(n, -1, -1):
        to_heap(a, n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i] 
        to_heap(a, i, 0)

    return a

def to_heap(a, n, i):
    largest = i 
    l = 2 * i + 1   
    r = 2 * i + 2   

    if l < n and a[i] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]

        to_heap(a, n, largest)