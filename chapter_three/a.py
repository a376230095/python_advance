with open("test","w") as a:
    for i in range(1,1000):
        a.write("{}".format(i))
        a.write("\n")