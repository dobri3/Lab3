import typer
from src.sort.quick_sort import quick
from src.validation.sort_float_validation import sort_float_validation


def bucket_sort()->None:
    """
    работает в режиме карманной сортировки

    :return: None
    """
    while (n:= input("Bucket sort mode>> ")) not in ["back", 'b', 'q']:
            n_list = n.split()
            buckets = input("How many buckets: ")
            if buckets == "" or int(buckets)<=0:
                typer.secho("Buckets must be greater than 0", fg=typer.colors.RED)
                break
            valid, message = sort_float_validation(list(map(float, n_list)))
            if valid:
                print(*bucket(list(map(float, n_list)), int(buckets)))
            else:
                typer.secho(message, fg=typer.colors.RED)


def bucket(a:list[float],  buckets: int) -> list[float]:
    """
    осуществляем карманную cортировку

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """

    answer = []
    if len(a)<=1:
        return a
    buckets_list: list[list[float]] = [[] for _ in range(buckets)]
    max_el = max(a)
    min_el = min(a)
    range_of_list = max_el-min_el
    for i in range(len(a)):
        index = int((a[i] - min_el) * (buckets-1) / range_of_list)
        buckets_list[index].append(a[i])
    for i in range(buckets):
        buckets_list[i] = quick(buckets_list[i])
    for i in range(buckets):
        for k in range(len(buckets_list[i])):
            answer.append(buckets_list[i][k])
    return answer
