class Password(object):

    def validate(self, num):
        value = str(num)

        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                return False
        return True

