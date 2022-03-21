import math
import tkinter as tk
import tkinter.messagebox as mb

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x350')

    label1 = tk.Label(text="Введите коэффициенты для уравнения").pack()
    label2 = tk.Label(text="ax^2 + bx + c = 0:").pack()

    label3 = tk.Label(text="A = ").pack()
    a_entry = tk.Entry(window, width=30)
    a_entry.pack()

    label4 = tk.Label(text="B = ").pack()
    b_entry = tk.Entry(window, width=30)
    b_entry.pack()

    label5 = tk.Label(text="C = ").pack()
    c_entry = tk.Entry(window, width=30)
    c_entry.pack()


    def Submit():
        file = open("file.txt", "a")
        text_box.delete(0.0, tk.END)

        if len(a_entry.get()) == 0:
            mb.showinfo(title="Ошибка", message="Введите A")
            file.write("\nПользователь не ввел A")
            return
        else:
            a = float(a_entry.get())
        if len(b_entry.get()) == 0:
            mb.showinfo(title="Ошибка", message="Введите B")
            file.write("\nПользователь не ввел B")
            return
        else:
            b = float(b_entry.get())
        if len(c_entry.get()) == 0:
            mb.showinfo(title="Ошибка", message="Введите C")
            file.write("\nПользователь не ввел C")
            return
        else:
            c = float(c_entry.get())

        file.write("\nПользователь ввел: A="+str(a)+" B="+str(b)+" C="+str(c))
        discr = b ** 2 - 4 * a * c
        print("Дискриминант D = %.2f" % discr)
        text_box.insert(tk.END, "Дискриминант D = %.2f " % discr)
        file.write(" Дискриминант D = %.2f " % discr)

        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
            text_box.insert(tk.END,"\nx1 = %.2f \nx2 = %.2f" % (x1, x2))
            file.write(" ОТВЕТ: x1 = %.2f x2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -b / (2 * a)
            print("x = %.2f" % x)
            text_box.insert(tk.END, "\nx = %.2f" % x)
            file.write(" ОТВЕТ: x = %.2f" % x)
        else:
            print("Корней нет")
            text_box.insert(tk.END, "Корней нет")
            file.write(" ОТВЕТ: Корней нет")
        file.close()


    btn_submit = tk.Button(text="Считать",command=Submit).pack()

    answer_label = tk.Label(text='Ответ: ').pack()
    text_box = tk.Text(window)
    text_box.pack()

    window.mainloop()
