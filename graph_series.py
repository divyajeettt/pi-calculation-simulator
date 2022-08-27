from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from typing import Callable
import generator
import series


number: int = 0

TERMS: list[int] = []
ESTIMATES: list[float] = []
ERRORS: list[float] = []

SERIES: Callable[[int], series.GeneratorType] = series.series1()


def plot(n: int) -> None:
    global number

    for ax in (ax1, ax2):
        ax.cla()
        ax.plot(0, 0, color="black", linewidth=3, marker="o")
        ax.axhline(y=0, color="black", linewidth=3)
        ax.axvline(x=0, color="black", linewidth=3)

    ax1.axhline(
        y=series.math.pi, color="red", linewidth=2,
        linestyle="--", label="y = π"
    )

    ax1.plot(TERMS, ESTIMATES)
    ax2.plot(TERMS, ERRORS)

    ax1.set_ylabel("Value of Pi")
    ax2.set_ylabel("Percentage Error in Calculation")
    ax2.set_xlabel("Number of Terms")

    ax1.grid(True)
    ax2.grid(True)
    ax1.legend(loc="lower right")

    TERMS.append(number := number + 1)
    ESTIMATES.append(pi := next(SERIES))
    ERRORS.append(generator.error(pi))


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
animate = FuncAnimation(fig, plot, interval=1)

if __name__ == "__main__":
    plt.show()