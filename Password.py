class Password(object):

    def validate(self, num):
        value = str(num)

        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                return False

        repeated_counts = {}
        for pos in range(len(value) - 1):
            first = value[pos]
            second = value[pos + 1]

            if first == second:
                if first not in repeated_counts:
                    repeated_counts[first] = 0
                else:
                    repeated_counts[first] += 1

        total = 0
        for number in repeated_counts.values():
            total += number

        if total % 2 is 0 and len(repeated_counts) is not 0:
            return True
        return False

    def check_validate(self, passwords):
        count = 0

        for numbers in passwords:
            if self.validate(numbers):
                count += 1
        return count
