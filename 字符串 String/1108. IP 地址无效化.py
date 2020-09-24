class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = len(address)
        new_str = [''] * (n + 6)
        i = j = 0
        while i < n:
            if address[i] == '.':
                new_str[j] = '['
                j += 1
                new_str[j] = '.'
                j += 1
                new_str[j] = ']'
            else:
                new_str[j] = address[i]
            i += 1
            j += 1
        return ''.join(new_str)

    # def defangIPaddr(self, address: str) -> str:
    #     return address.replace('.', '[.]')


print(Solution().defangIPaddr('1.1.1.1'))
print(Solution().defangIPaddr('255.100.50.0'))
