from tkinter import *
root= Tk()
root.geometry("700x700")
root.title("Sales Profits")

month=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (10000, 20000, 450000, 60000, 70000, 30000, 23400, 68000, 80000, 60800, 50000, 3240)

month_tuple=Label(root)
month_tuple["text"]= str(month)
month_tuple.place(relx=0.5, rely= 0.2, anchor=CENTER)
profits_tuple=Label(root)
profits_tuple["text"] = str(profits)
profits_tuple.place(relx=0.5, rely=0.3, anchor=CENTER)

max_profit_month_lbl=Label(root)
max_profit_month_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
def show_max():
    max_profit=max(profits)
    max_profit_index= profits.index(max_profit)
    max_profit_month=month[max_profit_index]
    max_profit_month_lbl["text"]="Maximum Profit Of "+ str(max_profit) + " Was Recorded In The Month Of " + str(max_profit_month)

max_btn=Button(root, text="Show Max Profit Month", command=show_max)
max_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

min_profit_month_lbl=Label(root)
min_profit_month_lbl.place(relx=0.5, rely=0.6, anchor=CENTER)
def show_min():
    min_profit=min(profits)
    min_profit_index= profits.index(min_profit)
    min_profit_month=month[min_profit_index]
    min_profit_month_lbl["text"]="Minimum Profit Of "+ str(min_profit) + " Was Recorded In The Month Of " + str(min_profit_month)

min_btn=Button(root, text="Show Min Profit Month", command=show_min)
min_btn.place(relx=0.5, rely=0.7, anchor=CENTER)



root.mainloop()
