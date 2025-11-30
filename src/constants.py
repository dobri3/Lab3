from src.factorial import factorial, factorial_recursive
from src.fibo import fibonachi, fibonachi_recursive
from src.sort.bubble_sort import bubble_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.counting_sort import counting_sort
from src.sort.heap_sort import heap_sort
from src.sort.quick_sort import quick_sort
from src.sort.radix_sort import radix_sort


HANDLERS = {
        'factorial': factorial,
        'factorial rec': factorial_recursive,
        'fibo': fibonachi,
        'fibo rec': fibonachi_recursive,
        'bubble sort': bubble_sort,
        'quick sort': quick_sort,
        'counting sort': counting_sort,
        'radix sort': radix_sort,
        'bucket sort': bucket_sort,
        'heap sort': heap_sort
    }
