import csv
import matplotlib.pyplot as plt

with open('data.csv', mode='r') as CSV_file:  # Opening the file
    fCSV = csv.reader(CSV_file)  # Reading the file

    stats = open("stats.txt", "w")
    writing_lines = []

    bar_x = []
    bar_y = []

    data_2021 = []
    data_2022 = []
    data_month = []
    for line in fCSV:
        print(line)

        if (line[1]).isnumeric():
            line = [int(x) for x in line]

            total = sum(line[1:13])

            s = "Vehicles sold in " + str(line[0]) + ": " + str(total) + "\n"


            writing_lines.append(s)


            bar_x.append(line[0])
            bar_y.append(total)

            if line[0] == 2021:
                data_2021 = line
            elif line[0] == 2022:
                data_2022 = line

        else:
            data_month = line


    plt.figure(1)
    plt.bar(bar_x, bar_y)

    plt.title("Yearly Vehicles Sold")
    plt.xlabel("Year")
    plt.ylabel("Vehicles sold")

    a = sum(data_2022[1:7])
    b = sum(data_2021[1:7])
    SGR = (a - b) / b


    writing_lines.append("Calculated Sales Growth rate: " + str(SGR) + "\n")


    estd_2022_sales = []
    estd_2022_months = data_month[7:13]
    for x in range(7, 13):
        val = data_2021[x] + data_2021[x] * SGR
        estd_2022_sales.append(val)
        s = "Estimated sales in " + data_month[x] + " 2022: " + str(val) + "\n"


        writing_lines.append(s)


    stats.writelines(writing_lines)
    stats.close()

    # second bar plot (horizontal)
    plt.figure(2)
    plt.barh(estd_2022_months, estd_2022_sales)

    plt.title("Estimated Sales")
    plt.ylabel("Month")
    plt.xlabel("Sales")
    plt.grid()

    # Visually show all plots in 'plt'
    plt.show()
