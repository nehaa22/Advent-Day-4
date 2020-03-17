class Password(object):

    def validate(self, num):
        value = str(num)

        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                return False

        for i in range(len(value) - 1):
            for i in range(len(value) - 1):
                if value[i] == value[i + 1]:
                    if (i > 0 and value[i - 1] == value[i]) or (
                            i < len(value) - 2 and value[i + 2] == value[i + 1]):
                        continue
                    else:
                        return True


# my_list = list(range(1, 1001))
