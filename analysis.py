import csv
import statistics
import matplotlib.pyplot as plt

filenames = ["AAPL.csv", "GS.csv" , "IBM.csv" , "INTC.csv" , "JPM.csv"]
for stockticker in filenames:
    stats_data = []
    with open(stockticker, "r") as infile:
        reader = csv.DictReader(infile)
        # save this dictReader object into a list of dictionaries to analyze
        for row in reader:
            stats_data.append(row)


    # get each week of stock data, 5 iterations at a time
    i = 0
    stats_stdev = [] 
    while i < len(stats_data):
        if i + 5 >= len(stats_data):
            break
        day1 = float(stats_data[i]["closing price"])
        day2 = float(stats_data[i + 1]["closing price"])
        day3 = float(stats_data[i + 2]["closing price"])
        day4 = float(stats_data[i + 3]["closing price"])
        day5 = float(stats_data[i + 4]["closing price"])
        x = statistics.pstdev([day1,day2,day3,day4,day5])
        stats_stdev.append(x) 
        i += 5
  

    #Stats_data Visualization 
    plt.plot(stats_stdev)
    plt.xlabel("Weeks")
    plt.ylabel("Standard Deviation of Closing Price")
    plt.title("Weekly Standard Deviation")
    plt.savefig(f"{stockticker}stdev.png")
    plt.clf()


