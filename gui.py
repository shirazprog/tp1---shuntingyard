import tkinter as tk
from shunting_yard import tokenize, infix_to_postfix, evaluate_postfix, ExpressionError


def on_calculate():
    expr = entry_expr.get()

    try:
        tokens = tokenize(expr)
        postfix = infix_to_postfix(tokens)
        result = evaluate_postfix(postfix)

        entry_postfix.delete(0, tk.END)
        entry_postfix.insert(0, " ".join(postfix))

        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))

        entry_error.delete(0, tk.END)
        entry_error.insert(0, "")

    except ExpressionError as e:
        entry_error.delete(0, tk.END)
        entry_error.insert(0, str(e))


root = tk.Tk()
root.title("Shunting-yard TP1")

tk.Label(root, text="Expression (infix):").grid(row=0, column=0, sticky="w")
entry_expr = tk.Entry(root, width=40)
entry_expr.grid(row=0, column=1)

btn = tk.Button(root, text="Calculer", command=on_calculate)
btn.grid(row=1, column=1, sticky="w")

tk.Label(root, text="Postfix:").grid(row=2, column=0, sticky="w")
entry_postfix = tk.Entry(root, width=40)
entry_postfix.grid(row=2, column=1)

tk.Label(root, text="Résultat:").grid(row=3, column=0, sticky="w")
entry_result = tk.Entry(root, width=40)
entry_result.grid(row=3, column=1)

tk.Label(root, text="Erreur:").grid(row=4, column=0, sticky="w")
entry_error = tk.Entry(root, width=40)
entry_error.grid(row=4, column=1)

root.mainloop()