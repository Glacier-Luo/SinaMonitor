from sqlite import select
import time, datetime
import matplotlib.pyplot

def show():
    # names = ['realtimehot', 'relevant_topic', 'users', 'words']
    # for name in names:
        # data = select(name)
        # print(data)
        # for key in data.keys():
        #     dateArray = datetime.datetime.utcfromtimestamp(key)
        #     otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        #     print(otherStyleTime + ":" + str(data[key]))

    # data = select("topic")


    data = select("realtimehot")
    time = []
    numbers = {}
    for key in data.keys():
        dateArray = datetime.datetime.utcfromtimestamp(key)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        time.append(otherStyleTime)
        for item in data[key].keys():
            # numbers[item] = []
            try:
                numbers[item][0].append(otherStyleTime)
                numbers[item][1].append(data[key][item])
            except KeyError:
                numbers[item] = [[], []]
                numbers[item][0].append(otherStyleTime)
                numbers[item][1].append(data[key][item])
            # print(item)
            # print(data[key][item])
    print(time)
    print(numbers)
    matplotlib.pyplot.title = "Realtimehot"
    matplotlib.pyplot.xlabel = "Time"
    matplotlib.pyplot.ylabel = "Clicks"
    # matplotlib.pyplot.rcParams['figure.dpi'] = 300
    # matplotlib.pyplot.rcParams['figure.figsize'] = (8.0, 4.0)
    for key in numbers.keys():
        print(numbers[key][0])
        print(numbers[key][1])
        matplotlib.pyplot.plot(numbers[key][0], numbers[key][1], label=key)
        # break
    matplotlib.pyplot.show()



show()