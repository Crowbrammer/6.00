answers = dict()
answers[(1, 2)] = "Tom"
if answers[(1,3)] == "y":
    print("Tim")
    print("Tim")


# # with open(my_file.txt) as f:
# #     print(f.read())
# import string
# print(string.__dict__)

#
#
# def coroutine(val = None):
#     result = None
#     while True:
#         line = (yield result)
#         result = chr(line)
#         print("test")
#
# gen = coroutine()
# next(gen)
# gen.send(48)
# for i in range(10):
#     print(chr(61))
#     print(gen.send(61))
# # print(coroutine())
