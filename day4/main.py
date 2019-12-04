def valid_password(password, part_one):

    duplicate = False

    for i in range(1, len(password)):

        if password[i] < password[i - 1]:
            return False

        if part_one:
            if password[i] == password[i - 1]:
                duplicate = True
        else:
            # left bound
            if i - 1 == 0:
                if password[i] == password[i - 1] and password[i] != password[i + 1]:
                    duplicate = True
            # right bound
            elif i + 1 == len(password):
                if password[i] == password[i - 1] and password[i] != password[i - 2]:
                    duplicate = True
            # somewhere in between
            else:
                if password[i] == password[i - 1] and password[i] != password[i - 2] and password[i] != password[i + 1]:
                    duplicate = True

    return duplicate

if __name__ == '__main__':

    LB = 130254
    UB = 678275
    part_one = 0
    part_two = 0

    for password in range(LB, UB + 1):
        digit_list = [digit for digit in str(password)]

        if valid_password(digit_list, True):
            part_one += 1
        if valid_password(digit_list, False):
            part_two += 1

    print("p1: " + str(part_one))
    print("p2: " + str(part_two))
