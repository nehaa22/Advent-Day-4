class Password(object):

    def validate(self, num):
        value = str(num)

        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                return False

        pos = 0
        is_repeated = False

        while pos < len(value) - 1:
            if value[pos] == value[pos + 1]:
                pos += 2
                is_repeated = True
                continue
            pos += 1

        return is_repeated

    def check_validate(self, passwords):
        count = 0

        for numbers in passwords:
            if self.validate(numbers):
                count += 1
        return count
