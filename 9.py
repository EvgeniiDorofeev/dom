def create_file_with_numbers(n: int) -> None:
    my_file = open(f'range_{n}.txt', mode='w', encoding='utf-8')
    for i in range(1,n+1):
        my_file.write(str(i)+ '\n')
    #print(my_file.read())
n=int(input())
create_file_with_numbers(n)