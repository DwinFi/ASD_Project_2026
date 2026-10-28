def beadsort(input_list):
    if not input_list:
        return []
    if min(input_list) < 0:
        return "Ошибка: Beadsort не поддерживает отрицательные числа."
        
    return_list = []
    transposed_list = [0] * max(input_list)
    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
    for i in range(len(input_list)):
        return_list.append(sum(n > i for n in transposed_list))
    return return_list