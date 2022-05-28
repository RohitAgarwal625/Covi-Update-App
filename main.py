def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data

get_covid_data()

root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
r= ("poppins",25,"bold")

banner= tk.PhotoImage(file="C:\Users\acer\Downloads")
bannerlabel = tk.Label(root,image=banner)
bannerlabel.pack()

textfield = tk.Entry(root,width_=_50)
textfield.pack()

mainlabel = tk.Label(root, text=get_covid_data(),font =f)
mainlabel.pack()

rtbn = tk.Button(root, text="Reload",font =f,reielf='solid',command=reload)
rtbn.pack()

root.mainloop()