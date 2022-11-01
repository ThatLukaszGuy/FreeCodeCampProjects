# not working btw
mylist = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


# main function
def arithmetic_arranger(list, display_results=False):

    if len(list) > 5: return "Error: Too many problems."

    output = f""

    for item in list:
        item_list = item.split(' ')
        # error handling
        if item_list[1] != '-' and item_list[1] != '+' : return "Error: Operator must be '+' or '-'"
        if len(item_list[0]) > 4 or len(item_list[2]) > 4: return 'Error: Numbers cannot be more than four digits.'

        spaces_req = max(len(item_list[0]) , len(item_list[2]))
        longest_item = str( max( int(item_list[0]) , int(item_list[2])) )

        if display_results:
            sum = item_list[0] + item_list[2]
            print(sum)
        else:
            bottom_line = '-' * (len(longest_item) + 2)
            full_string = f"{item_list[0].rjust(spaces_req + 6)}\n{item_list[1].rjust(5) + ' ' + item_list[2].rjust(spaces_req)}\n{' ' * 4}{bottom_line}" # ahh yes ... readability
            output += full_string









arithmetic_arranger(mylist)