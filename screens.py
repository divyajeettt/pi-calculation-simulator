import tkinter as tk
import tkinter.messagebox as msg


def start() -> None:
    global darts

    if not (darts := box.get()):
        msg.showwarning("Empty Field", "Please enter required Number of darts")
        return
    if (darts := int(darts)) < 1:
        msg.showwarning("Invalid Value", "Number of darts must be > 1")
        return

    root.destroy()


def ending(total: int, calculated: float, error: float) -> None:
    temp = tk.Tk()
    temp.withdraw()
    msg.showinfo(
        title="Pi has been calculated",
        message=(
            f"Calculated value of Pi is: {calculated} \n"
            f"Percentage Error in Calculation: {error}%"
        ),
        parent=temp
    )


def main() -> None:
    global root, box

    root = tk.Tk()
    root.title("Welcome to Pi Calculator Simulation")

    tk.Label(
        text="Enter the number of darts to calculate pi \n(preferably > 1000)",
        font=("consolas", 12, "bold")
    ).pack()

    box = tk.Entry(
        root, width=41, bd=3, font=("consolas", 12, "bold"), validate="key",
        validatecommand=(root.register(lambda s: s.isnumeric() or not s), "%P")
    )
    box.pack()
    box.bind("<Return>", (lambda evt: start()))

    tk.Button(
        root, text="Start", width=41, bd=3, font=("consolas", 12, "bold"),
        command=start
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
    print(darts)