def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, mode='r', encoding='utf-8') as file:

        k=0
      for line in file:
         if len(line)>7:
               k+=1
      return k