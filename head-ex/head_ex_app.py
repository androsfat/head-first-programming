from tkinter import *
import tkinter.messagebox


def safe_data():
    try:
        file = open("deliveries.txt", "a")
        file.write("Depot:\n%s\nDescription:\n%s\nAddress:\n%s\n"
                   % (depot.get(), description.get(), address.get("1.0", END)))
        file.close()
        # Clear entry fields
        depot.set(None)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)


# Read contents of a file and return a list
def read_depots(file):
    depots = []
    depots_f = open(file)
    for each_line in depots_f:
        depots.append(each_line.strip())
    return depots


# Create user interface
app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text="Depot:").pack()
# Control variable to initialise radio buttons to None
depot = StringVar()
depot.set(None)
# Call the function passing in the name of the file to read the data from
options = read_depots("depots.txt")
# This * means "Take the rest of the parameters from this list and insert them here"
# Use the data to build the option menu
OptionMenu(app, depot, *options).pack()
Label(app, text="Description:").pack()
description = Entry(app)
description.pack()
Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save", command=safe_data).pack()

app.mainloop()

