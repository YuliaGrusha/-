# sort.py - функции сортировки

def bin_insertion_sort(items, key_funcs):
    """
    Сортировка бинарными вставками по составному ключу.
    key_funcs - список кортежей (функция_ключа, обратный_порядок)
    """
    for idx in range(1, len(items)):
        current = items[idx]
        left, right = 0, idx
        
        while left < right:
            mid = (left + right) // 2
            is_less = True
            
            for key_func, reverse in key_funcs:
                mid_key = key_func(items[mid])
                current_key = key_func(current)
                
                if mid_key < current_key:
                    is_less = not reverse
                    break
                elif mid_key > current_key:
                    is_less = reverse
                    break
            
            if is_less:
                left = mid + 1
            else:
                right = mid
        
        if left != idx:
            items.pop(idx)
            items.insert(left, current)
    
    return items