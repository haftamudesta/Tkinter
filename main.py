import tkinter as tk
import customtkinter as ctk
import re

window = tk.Tk()
window.geometry("280x500")
window.title("Calculator")


def display_input(_input):
    input_box.insert(index=tk.INSERT, string=_input)
    display_result()


def display_result():
    try:
        calculation = input_box.get()
        if re.search(pattern=r'[\%\/\*\-\+]', string=calculation):
            result = eval(calculation)
            result_label.config(text=f'={result}')
        else:
            result_label.config(text='')
    except Exception as error:
        print(error)


def delete_input():
    index = input_box.index(tk.INSERT) - 1
    input_box.delete(index)
    display_result()


def clear_input():
    input_box.delete(0, tk.END)
    result_label.config(text='')
    input_box.config(font=('Bold', 20))
    result_label.config(font=("Bold", 15))


def highlight_result():
    input_box.config(font=('Bold', 15))
    result_label.config(font=("Bold", 30))


def theme_change():
    current_bg = window.cget('bg')
    if current_bg == "SystemButtonFace" or current_bg == "light colors":
        window.tk_setPalette(background='black', foreground='white')
        input_box.configure(bg="black")
        theme_btn.configure(text="☀", bg='black', fg='white')
    else:
        window.tk_setPalette(background='SystemButtonFace', foreground='black')
        theme_btn.configure(text="🌙", bg='SystemButtonFace', fg='black')


input_box = tk.Entry(window, font=("BOLD", 20),
                     justify=tk.RIGHT, bd=0, bg='systemButtonFace')
input_box.place(x=15, y=10, width=250, height=50)
result_label = tk.Label(window, font=("Bold", 15),
                        fg="gray", anchor=tk.E)
result_label.place(x=15, y=75, width=250, height=60)


clear_btn = ctk.CTkButton(master=window, text="C",
                          width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=clear_input)
clear_btn.place(x=15, y=145)
delete_btn = ctk.CTkButton(master=window, text="D",
                           width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=delete_input)
delete_btn.place(x=80, y=145)

percentage_btn = ctk.CTkButton(master=window, text="%",
                               width=40, height=40, font=("Bold", 25), fg_color="#FF7433", corner_radius=8, command=lambda: display_input(_input='%'))
percentage_btn.place(x=145, y=145)

devide_btn = ctk.CTkButton(master=window, text="/",
                           width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=lambda: display_input(_input='/'))
devide_btn.place(x=215, y=145)

btn_7 = ctk.CTkButton(master=window, text="7",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='7'))
btn_7.place(x=15, y=210)

btn_8 = ctk.CTkButton(master=window, text="8",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='8'))
btn_8.place(x=80, y=210)

btn_9 = ctk.CTkButton(master=window, text="9",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='9'))
btn_9.place(x=145, y=210)

multiply_btn = ctk.CTkButton(master=window, text="*",
                             width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=lambda: display_input(_input='*'))
multiply_btn.place(x=215, y=210)


btn_4 = ctk.CTkButton(master=window, text="4",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='4'))
btn_4.place(x=15, y=285)

btn_5 = ctk.CTkButton(master=window, text="5",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='5'))
btn_5.place(x=80, y=285)

btn_6 = ctk.CTkButton(master=window, text="6",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='6'))
btn_6.place(x=145, y=285)

minus_btn = ctk.CTkButton(master=window, text="-",
                          width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=lambda: display_input(_input='-'))
minus_btn.place(x=215, y=285)


btn_1 = ctk.CTkButton(master=window, text="1",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='1'))
btn_1.place(x=15, y=345)

btn_2 = ctk.CTkButton(master=window, text="2",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='2'))
btn_2.place(x=80, y=345)

btn_3 = ctk.CTkButton(master=window, text="3",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='3'))
btn_3.place(x=145, y=345)

add_btn = ctk.CTkButton(master=window, text="+",
                        width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=lambda: display_input(_input='+'))
add_btn.place(x=215, y=345)

theme_btn = ctk.CTkButton(master=window, text="🌙",
                          width=40, height=40, font=("Bold", 20), corner_radius=8, border_width=0, command=theme_change)
theme_btn.place(x=15, y=435)

btn_0 = ctk.CTkButton(master=window, text="0",
                      width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='0'))
btn_0.place(x=80, y=435)

dot_btn = ctk.CTkButton(master=window, text=".",
                        width=40, height=40, font=("Bold", 30), corner_radius=8, command=lambda: display_input(_input='.'))
dot_btn.place(x=145, y=435)

equals_btn = ctk.CTkButton(master=window, text="=",
                           width=40, height=40, font=("Bold", 30), fg_color="#FF7433", corner_radius=8, command=highlight_result)
equals_btn.place(x=215, y=435)


window.mainloop()
