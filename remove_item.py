def remove_one(list_input):

      print list_input
      count = 0
      while len(list_input) != count:
              if len(list_input) > (count + 2) and list_input[count]+1 == list_input[count+1] and len(list_input) > (count + 2) and list_input[count+2] == list_input[count] + 2 :
                      list_input.pop(count)
              elif len(list_input) > (count+1) and list_input[count]+1 == list_input[count+1]:
                      list_input.pop(count)
                      list_input.pop(count)
              else:
                      count += 1
      print list_input




def remove_cons_dup(list_input):

      print list_input
      count = 0
      while len(list_input) != count:
              if list_input[count] == list_input[count+1]:
                      list_input.pop(count)
                      count += 1
              else:
                      count += 1
      print list_input
 
