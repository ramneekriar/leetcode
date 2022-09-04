def solution(N):
    # write your code in Python 3.6
    br = str(bin(N))[2:]
    
    br_group = False
    br_highest = 0
    bin_zero_counter = 0

    for char in br:
        if char == '1':
             if br_highest < bin_zero_counter:
                 br_highest = bin_zero_counter
             br_group = True
             bin_zero_counter = 0
        elif br_group:
             bin_zero_counter += 1
    return br_highest