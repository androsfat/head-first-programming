from tkinter import *


def safe_data():
    file = open("deliveries.txt", "a")
    file.write("Depot:\n%s\nDescription:\n%s\nAddress:\n%s\n"
               % (depot.get(), description.get(), address.get("1.0", END)))
    file.close()
    # Clear entry fields
    depot.set(None)
    description.delete(0, END)
    address.delete("1.0", END)


# Create user interface
app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text="Depot:").pack()
# depot = Entry(app)
# depot.pack()
# Control variable to initialise radio buttons to None
depot = StringVar()
depot.set(None)
Radiobutton(app, variable=depot, text="Cambridge, MA", value="Cambridge, MA").pack()
Radiobutton(app, variable=depot, text="Cambridge, UK", value="Cambridge, UK").pack()
Radiobutton(app, variable=depot, text="Seattle, WA", value="Seattle, WA").pack()
Label(app, text="Description:").pack()
description = Entry(app)
description.pack()
Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save", command=safe_data).pack()

app.mainloop()

