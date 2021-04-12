class hello_class:
    def __init__(self):
        self.__private_c = self.__calc_private_ab(1, 2)
        self.public_c = self.__private_c
        self.printall()

    def calc_public_ab(self, a, b):
        return a+b
    
    def __calc_private_ab(self, a, b):
        return a+b

    def printall(self):
        print("Hello World3")
        print("c:",self.__private_c)

if __name__=="__main__":
    hello = hello_class()

    # print public calc_ab
    try:
        print("Public_ab:", hello.calc_public_ab(1, 2))
    except Exception as e:
        print(e)

    # print private calc_ab
    try:
        print("Private_ab:", hello.__calc_private_ab(1, 2))
    except Exception as e:
        print(e)

    # ======================================

    # print public c
    try:
        print("Public_c:", hello.public_c)
    except Exception as e:
        print(e)

    # print private c
    try:
        print("Private_c:", hello.__private_c)
    except Exception as e:
        print(e)

    
    