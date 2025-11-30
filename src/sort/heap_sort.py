import typer
from src.validation.sort_int_validation import sort_int_validation


def heap_sort()->None:
    """
    работает в режиме сортировки кучей

    :return: None
    """
    while (n:= input("Heap sort mode>> ")) not in ["back", 'b', 'q']:
            n_list = n.split()
            valid, message = sort_int_validation(n_list)
            if valid:
                print(*heap(list(map(int, n_list))))
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
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[i] < a[left]:
        largest = left

    if right < n and a[largest] < a[right]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]

        to_heap(a, n, largest)
