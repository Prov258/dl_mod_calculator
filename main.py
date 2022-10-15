import math
import random
import tkinter as tk


def calc_handler(a, power, mod, res_label):
    a = int(a)
    mod = int(mod)

    if (power):
        power = int(power)
        a = change_base(a, power, mod)

    res = findMod(a, mod)

    res_label["text"] = str(res)


def equation_handler(a, b, mod, res_label):
    a = int(a)
    b = int(b)
    mod = int(mod)

    power_of_a = eyler_func(mod) - 1

    a = change_base(a, power_of_a, mod)

    res_label["text"] = str(findMod(a * b, mod))


def generate_handler(a, b, res_label):
    a = int(a)
    if (a == 1):
        a += 1
    b = int(b)

    for i in range(a, b):
        if (is_number_simple(i)):
            res_label["text"] = str(i)
            return

    res_label["text"] = "There is no simple number in this range"


def is_number_simple(p):
    for _ in range(10):
        a = random.randrange(1, p)
        a = change_base(a, p - 1, p)
        if (findMod(a, p) != findMod(1, p)):
            return False

    return True


def eyler_func(n):
    total = 0

    for i in range(1, n):
        if greatest_common_divisor(n, i) == 1:
            total += 1

    return total


def greatest_common_divisor(a, b):
    temp = a - b

    while temp > 0:
        if temp >= b:
            temp -= b
        else:
            temp, b = b, temp

    return b


def destruct_pow(power):
    destruct_power = []

    binary = binary_from_decimal(power)[::-1]

    for i in range(len(binary)):
        decimal = 2**i * int(binary[i])
        if decimal != 0:
            destruct_power += [decimal]

    return destruct_power


def binary_from_decimal(decimal):
    binary = ""

    while (decimal / 2 != 0):
        if (decimal % 2 == 0):
            binary = binary + "0"
            decimal = decimal / 2
        else:
            binary = binary + "1"
            decimal = (decimal - 1) / 2

    binary = binary[::-1]

    return binary


def findMod(m, mod):
    return m - math.floor(m / mod) * mod


def change_base(base, power, mod):
    destructed_power = destruct_pow(power)
    total = 1

    for i in pow_loop(1, max(destructed_power)):
        base = findMod(base**2, mod) if i > 1 else findMod(base, mod)

        if i in destructed_power:
            total *= base

    return total


def pow_loop(i, end):
    while i <= end:
        yield i
        i *= 2


def init_gui():
    window = tk.Tk()
    window.title("Calculator")
    window.resizable(width=False, height=False)

    # Calc mod

    frm_calc = tk.Frame(master=window)

    ent_calc_a = tk.Entry(master=frm_calc)
    lbl_calc_power = tk.Label(master=frm_calc, text="^")
    ent_calc_power = tk.Entry(master=frm_calc)
    lbl_calc_mod = tk.Label(master=frm_calc, text="mod")
    ent_calc_mod = tk.Entry(master=frm_calc)
    lbl_calc_x = tk.Label(master=frm_calc, text="= x")

    ent_calc_a.grid(row=0, column=0)
    lbl_calc_power.grid(row=0, column=1)
    ent_calc_power.grid(row=0, column=2)
    lbl_calc_mod.grid(row=0, column=3)
    ent_calc_mod.grid(row=0, column=4)
    lbl_calc_x.grid(row=0, column=5)

    btn_calc_result = tk.Button(master=frm_calc, text="Solve", command=lambda: calc_handler(
        ent_calc_a.get(), ent_calc_power.get(), ent_calc_mod.get(), lbl_calc_result))

    btn_calc_result.grid(row=1, column=0)

    lbl_calc_result_text = tk.Label(master=frm_calc, text="x = ")
    lbl_calc_result = tk.Label(master=frm_calc, text="0")

    lbl_calc_result_text.grid(row=2, column=0)
    lbl_calc_result.grid(row=2, column=1)

    frm_calc.grid(row=0, column=0, pady=5, sticky='w')

    # Calc mod with equation

    frm_equation = tk.Frame(master=window)

    ent_equation_a = tk.Entry(master=frm_equation)
    lbl_equation_x = tk.Label(master=frm_equation, text=" * x ≡ ")
    ent_equation_b = tk.Entry(master=frm_equation)
    lbl_equation_mod = tk.Label(master=frm_equation, text="mod")
    ent_equation_mod = tk.Entry(master=frm_equation)

    ent_equation_a.grid(row=0, column=0)
    lbl_equation_x.grid(row=0, column=1)
    ent_equation_b.grid(row=0, column=2)
    lbl_equation_mod.grid(row=0, column=3)
    ent_equation_mod.grid(row=0, column=4)

    btn_equation_result = tk.Button(master=frm_equation, text="Solve", command=lambda: equation_handler(
        ent_equation_a.get(), ent_equation_b.get(), ent_equation_mod.get(), lbl_equation_result))

    btn_equation_result.grid(row=1, column=0)

    lbl_equation_result_text = tk.Label(master=frm_equation, text="x =")
    lbl_equation_result = tk.Label(master=frm_equation, text="0")

    lbl_equation_result_text.grid(row=2, column=0)
    lbl_equation_result.grid(row=2, column=1)

    frm_equation.grid(row=1, column=0, pady=5, sticky='w')

    # Generate simple number in range

    frm_generate = tk.Frame(master=window)

    lbl_generate_title = tk.Label(
        master=frm_generate, text="Generate simple number in range")
    lbl_generate_from = tk.Label(master=frm_generate, text="from: ")
    ent_generate_a = tk.Entry(master=frm_generate)
    lbl_generate_to = tk.Label(master=frm_generate, text="to: ")
    ent_generate_b = tk.Entry(master=frm_generate)

    lbl_generate_title.grid(row=0, column=0)
    lbl_generate_from.grid(row=0, column=1)
    ent_generate_a.grid(row=0, column=2)
    lbl_generate_to.grid(row=0, column=3)
    ent_generate_b.grid(row=0, column=4)

    btn_generate_result = tk.Button(master=frm_generate, text="Generate", command=lambda: generate_handler(
        ent_generate_a.get(), ent_generate_b.get(), lbl_generate_result))

    btn_generate_result.grid(row=1, column=0)

    lbl_generate_result_text = tk.Label(
        master=frm_generate, text="Number is: ")
    lbl_generate_result = tk.Label(master=frm_generate, text="0")

    lbl_generate_result_text.grid(row=2, column=0)
    lbl_generate_result.grid(row=2, column=1)

    frm_generate.grid(row=2, column=0, pady=5, sticky='w')

    window.mainloop()


init_gui()
