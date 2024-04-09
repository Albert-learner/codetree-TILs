product, code = input().split()

class PRODUCT:
    def __init__(self, prod = "codetree", code = 50):
        self.prod = prod
        self.code = code

    def print_info(self):
        print("product", self.code, "is " + self.prod)

product_inst = PRODUCT()
product_inst.print_info()
product_inst = PRODUCT(product, code)
product_inst.print_info()