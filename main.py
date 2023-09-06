# from library import greet


def main():
    float_variable = 5.0
    integer_variable = 55

    print(f'the sum of {float_variable} and {integer_variable} is: '
          f'{float_variable + integer_variable}')
    print(f'the sum of {integer_variable} and {integer_variable} '
          f'converted to integer is: {int(float_variable + integer_variable)}')


if __name__ == '__main__':
    main()

# the sum of 5.0 and 55 is: 60.0
# 55 and 55 converted to integer is: 60
