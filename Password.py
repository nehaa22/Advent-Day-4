class Password(object):

    def validate(self, num):
        value = str(num)

        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                return False

        for i in range(len(value) - 1):
            for i in range(len(value) - 1):
                if value[i] == value[i + 1]:
                    if i > 0 and value[i - 1] == value[i]:
                        continue
                    else:
                        return True

    def check_validate(self, passwords):
        count = 0

        for numbers in passwords:
            if self.validate(numbers):
                count += 1
        return count
