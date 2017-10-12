x = [10, 2, 30, 4, 50]


class avgFil2(object):
    def __init__(self):
        self.avg = 0
        self.k = 1.0

    def __call__(self, x):
        alpha = (self.k - 1.0) / self.k
        self.avg = alpha * self.avg + (1 - alpha) * x
        self.k += 1
        return self.avg


def simpleTest(x=x):
    average = []
    avg = avgFil2()  # new variable and creation of instance (all initialisation)
    for i in range(len(x)):
        print('input %f' % x[i])
        print('before change avg.avg=%f, k=%f' % (avg.avg, avg.k))
        average.append(avg(x[i]))  # class is called here, so all changes going on
        print('after change avg.avg=%f, k=%f' % (avg.avg, avg.k))
        print('The output average is %f' % average[i])


simpleTest()
