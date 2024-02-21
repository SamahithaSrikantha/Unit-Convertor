from tkinter import *
from tkinter import ttk

root=Tk()


def convert():
    entry_val=float(entry.get())
    selection=int(select.get()[0])

    if selection == 1:
        result_ = entry_val / 30.48
        result.config(text=f"{entry_val} cm is equal to {result_:.2f} feet.")
    elif selection == 2:
        result_= entry_val * 12
        result.config(text=f"{entry_val} feet is equal to {result_:.2f} inches.")
    elif selection == 3:
        result_= entry_val / 10.764
        result.config(text=f"{entry_val} sqft is equal to {result_:.2f} sqm.")
    elif selection == 4:
        hectares = entry_val / 107639.104
        acres = entry_val / 43560
        result.config(text=f"{entry_val} sqft is equal to {hectares:.2f} hectares or {acres:.2f} acres.")
    
    #gui ele
head=Label(root,text="Unit Converter",font="comicsansns 18")
head.pack(pady=10)
a=Frame(root,padx=20,pady=20,bg="grey")
a.pack()

choice=Label(a,text="choose a converstion to be made",font="Arial 14")
choice.grid(row=0, column=0, pady=10, padx=10, sticky="w")

unit_change = {
    1: "Centimeter to Feet",
    2: "Feet to Inches",
    3: "Square Feet to Square Meters",
    4: "Square Feet to Hectares/Acres"
}

dropdown_options = [f"{key}. {value}" for key, value in unit_change.items()]

select =ttk.Combobox(a, values=dropdown_options, state="readonly", width=30, font=("Arial", 14))
select.set(dropdown_options[0])
select.grid(row=0, column=1, pady=10, padx=10)


label_length = ttk.Label(a, text="Enter a number to convert:", font=("Arial", 14), background="#FFFFFF")
label_length.grid(row=1, column=0, pady=10, padx=10, sticky="w")

entry = ttk.Entry(a, font=("Arial", 14), width=10)
entry.grid(row=1, column=1, pady=10, padx=10)

convert_button = ttk.Button(root, text="Convert", command=convert, style="Accent.TButton")
convert_button.pack(pady=15)
r=Label(a,text="Result:",font="comicsansns 12 bold")
r.grid(row=2, column=0, pady=10, padx=10, sticky="w")
result=ttk.Label(a,text="",font="comicsansns 12")
result.grid(row=2, column=1, pady=10, padx=10, sticky="w")
root.mainloop()

