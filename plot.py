def plot():
    import matplotlib.pyplot as plt
    import pandas as pd
    file_name = str(input("Enter the file name: "))
    df = pd.read_excel(f"{file_name}.xlsx")
    x = str(input("Enter the name of X axis: "))
    x_value = df[x]
    y = str(input("Enter the name of Y axis: "))
    y_value = df[y]
    paint_x = str(input("Enter X axis label color: "))
    paint_x = paint_x.lower()
    paint_y = str(input("Enter Y axis label color: "))
    paint_y = paint_y.lower()
    title = str(input("Enter a title for your graph: "))

    plt.title(title, fontsize = 25, color = "black")
    plt.plot(x_value,y_value, linestyle = "--" ,marker = "o" ,color = "magenta")
    plt.xlabel(f"{x}",fontsize = 14, color = paint_x)
    plt.ylabel(f"{y}",fontsize = 14, color = paint_y)

    plt.show()
    
def main():
    while 1:
        x = int(input("Press 1 to plot and 0 to exit: "))
        if x == 1:
            plot()
        if x == 0:
            break
main()