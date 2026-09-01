from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        common_denominator = 2520

        if expression[0].isdigit():
            expression = '+' + expression

        index = 0
        expression_length = len(expression)

        while index < expression_length:
            sign = -1 if expression[index] == '-' else 1
            index += 1

            fraction_end = index
            while fraction_end < expression_length and expression[fraction_end] not in '+-':
                fraction_end += 1

            fraction_string = expression[index:fraction_end]
            fraction_numerator, fraction_denominator = fraction_string.split('/')

            numerator += sign * int(fraction_numerator) * common_denominator // int(fraction_denominator)

            index = fraction_end

        greatest_common_divisor = gcd(numerator, common_denominator)
        numerator //= greatest_common_divisor
        common_denominator //= greatest_common_divisor

        return f'{numerator}/{common_denominator}'