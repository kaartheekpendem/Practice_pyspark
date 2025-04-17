class Solution:
    def cals(num):
        if num not in range(-2147483648, 2147483648):
            return 0
        return num

    def reverse(self, x: int) -> int:
        b = list(str(x))[::-1]
        x = []
        if '-' in b:

            x = int(''.join(['-'] + b[:-1]))
        elif '0' in b and len(b) == 0:
            b.remove('0')
            x = int(''.join(b))
        elif len(b) == 0:
            x = 0
        else:
            x = int(''.join(b))

        return Solution.cals(x)


a=Solution()
print(a.reverse(234))