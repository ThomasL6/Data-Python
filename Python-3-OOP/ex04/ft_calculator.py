class calculator:

    @staticmethod
    def dotproduct(v1, v2):
        result = 0
        for x, y in zip(v1, v2):
            result += x * y

        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(v1, v2):
        result = [x + y for x, y in zip(v1, v2)]
        print(f"Addition result is: {result}")
        return result

    @staticmethod
    def sous_vec(v1, v2):
        result = [x - y for x, y in zip(v1, v2)]
        print(f"Subtraction result is: {result}")
        return result
