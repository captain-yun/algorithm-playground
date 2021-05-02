def reorder_logfiles(logs: list):
    # order
    # 1. characters precede number
    # 2. when the containing strings are same, identifiers would be used as a second factor to make an order.
    # 3. Among number logs, the order would be just as their order coming in.

    ptr_str = 0
    ptr_num = 0
    # 1. identify whether it's a number or string log.

    num_list = []
    str_list = []
    for log in logs:
        id, data = log.split(' ')[0], log.split(' ')[1:]
        if log.split(' ')[1].isdigit():
            num_list.append(log)
        else:
            # if [[x.spilt[0], str_list.index(x)] for x in str_list if x.split(x[1:]) == data]:
                # Compare identifiers
                str_list.append(log)
                for l in str_list:
                    if l.split()[1:] == data:
                        if  l.split()[0] > id:
                            str_list.insert(str_list.index(l), log)
                            break
                        else:
                            str_list.append(log)
                            break
    reorder_logs = str_list + num_list
    print(reorder_logs)

    # 2. if it's num, let it place to the index upon its pointer.
    # 3. if it's string, check if there's exacly the same data to it.
        # if 'yes', compare those identifiers and get a priority.
        # if 'no', just let it place to the index upon its pointer.

def reorder_logfiles(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # *** first key : data, second key : identifier
    return letters + digits
if __name__ == "__main__":
    reorder_logfiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])