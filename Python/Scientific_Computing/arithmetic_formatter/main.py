

# main function
def arithmetic_arranger(list, display_results=True):

    if len(list) > 5: return "Error: Too many problems."

    top_row = f""
    bottom_row = f""
    line = f""
    solutions = f""
    
    for item in list:
        item_list = item.split(' ')
        # error handling
        if item_list[1] != '-' and item_list[1] != '+' or item_list[1] == '/' : return "Error: Operator must be '+' or '-'."
        try:
          int(item_list[0])
          int(item_list[2])
        except:
          return "Error: Numbers must only contain digits."
      
        if len(item_list[0]) > 4 or len(item_list[2]) > 4: return 'Error: Numbers cannot be more than four digits.'

        spaces_req = max(len(item_list[0]) , len(item_list[2]))
        longest_item = str( max( int(item_list[0]) , int(item_list[2])) )

        bottom_line = '-' * (len(longest_item) + 2)
        top_row += f"{item_list[0].rjust(spaces_req + 6)}"
        bottom_row += f"{item_list[1].rjust(5) + ' ' + item_list[2].rjust(spaces_req)}"
        line += f"{' ' * 4}{bottom_line}" 
        # ahh yes ... readability

        if item_list[1] == '+':
            sum = int(item_list[0]) + int(item_list[2])
            solutions += f"{str(sum).rjust(spaces_req + 6)}"  
        elif item_list[1] == '-':
            sum = int(item_list[0]) - int(item_list[2])
            solutions += f"{str(sum).rjust(spaces_req + 6)}"
        
    if display_results:
        return '\n'.join((top_row[4:], bottom_row[4:],line[4:],solutions[4:]))   
    else:
        return '\n'.join((top_row[4:], bottom_row[4:],line[4:]))

