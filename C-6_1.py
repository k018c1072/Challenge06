num_1 = int(input('数値1＞ '))
num_2 = int(input('数値2＞ '))


def greatest_common_denominator(a, b):
    over = a % b
    if over == 0:
        return b
    else:
        return greatest_common_denominator(b, over)


print('最大公約数 :', greatest_common_denominator(num_1, num_2))
