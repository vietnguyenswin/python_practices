class Main(object):
    def __init__(self, num):
        self.nums = list(num)

    def cal(self):
        for i in range(len(self.nums)):
            num = self.nums[i].replace(' ', '')
            sep = [int(x) for x in list(num)]
            sum_z = sum(sep)

            sep_x = [int(y) for y in list(str(sum_z))]
            sum_x = sum(sep_x)

            sep_y = [int(z) for z in list(str(sum_x))]
            sum_y = sum(sep_y)

            print num + " : " + str(sum_z) + " : " + str(sum_x) + " --> " + str(sum_y)


m = Main(["0402 891 112", "0402 890 027", "0402 890 135",\
          "0402 890 281", "0402 890 021", "0402 890 069",\
          "0402 890 269", "0402 890 328"])
m.cal()
