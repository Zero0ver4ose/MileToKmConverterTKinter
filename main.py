import tkinter


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(200,100)
window.config(padx=30,pady=30)

def calculated_result():
    result = input.get()
    resulted = round(float(result) * 1.60934)
    calculated = label_result.config(text=resulted)
    return calculated

#input
input = tkinter.Entry(text="0", width=10)
input.grid(column=1, row=0)
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

#Text
text = tkinter.Label(text="is equal to")
text.grid(column=0,row=1)
km = tkinter.Label(text="Km")
km.grid(column=2,row=1)

#Button
button = tkinter.Button(text="Calculate",command=calculated_result)
button.grid(column=1, row=3)

#result
label_result = tkinter.Label(text="0")
label_result.grid(column=1,row=1)

window.mainloop()