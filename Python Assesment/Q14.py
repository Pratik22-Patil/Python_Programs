def process_list(data):
    sum = 0  
    concat = " "  
    count = 0  

    for i in data:
        if isinstance(i, (int, float)):  
            sum += i
        elif isinstance(i, str): 
            concat += i
        elif isinstance(i, (list, tuple, dict)):  
            count += len(i)

    return sum, concat, count


data = [1, "two", 3.0, [4, 5], {"five": 5}, (6,)]
l = [12, 'Python', 90.56, 78, 34, 'Is', 65.90, 'Easy']


sum_result, concat_result, count_result = process_list(l)
print("Sum : ", sum_result)
print("Concatenation : ", concat_result)
print("Count:", count_result)
