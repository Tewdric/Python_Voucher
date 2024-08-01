def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        if next_number > n:
            break
        
    return sequence

n = int(input("Digite um numero: "))
result = fibonacci(n)
print(result)