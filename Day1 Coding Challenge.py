def list_addup(check_list: list, num: int) -> bool:
  """
  Takes a list and a int as paramenters 
  and checks if 2 of its unique members sums up to the
  supplied number parameter and return a boolean if, the 
  sum is possible
  """
  for i in check_list:
    for j in check_list:
      if i + j == num and check_list.index(i) != check_list.index(j):
        return True

  return False
    
print(sum_of_list([10, 15, 3, 7], 17))
            
