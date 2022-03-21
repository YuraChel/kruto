import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('700x350')

    label1 = tk.Label(text="Введите строку").pack()
    string_entry = tk.Entry(window, width=80)
    string_entry.pack()

    def Submit():
        text_box.delete(0.0, tk.END)
        s = string_entry.get()

        s = s.replace('!','')
        s = s.replace('*','')
        s = s.replace('%','')
        s = s.replace('.','')
        #s = s.replace(',','')
        s = s[0:-1] + '.' #добавление точки в конец предложения
        lst = s.split()
        newList = [x for x in lst if len(x) >= 2] # убрал одиночные символы
        for index, word in enumerate(newList):      # сократил подряд идущие запятые до одной
            if ",," in word:
                idx = word.find(',')
                word = word[0:idx+1]
                newList[index] = word

        text_box.insert(tk.END, newList)

    btn_submit = tk.Button(text="Редактровать",command=Submit).pack()

    text_box = tk.Text(window)
    text_box.pack()

    window.mainloop()
