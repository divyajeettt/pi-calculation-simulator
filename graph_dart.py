from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import generator


SIMULATIONS: int = 1
TOTAL: int = 1

INSIDE: list[int] = [0  for _ in range(SIMULATIONS)]
DARTS: list[list[int]] = [[] for _ in range(SIMULATIONS)]

ESTIMATES: list[list[float]] = [[] for _ in range(SIMULATIONS)]
ERRORS: list[list[float]] = [[] for _ in range(SIMULATIONS)]


def calculate(n: int) -> None:
    global TOTAL

    for ax in (ax1, ax2):
        ax.cla()
        ax.plot(0, 0, color="black", linewidth=3, marker="o")
        ax.axhline(y=0, color="black", linewidth=3)
        ax.axvline(x=0, color="black", linewidth=3)

    ax1.axhline(
        y=generator.math.pi, color="red", linewidth=2,
        linestyle="--", label="y = π"
    )

    for i in range(SIMULATIONS):
        x, y = generator.pair(side=1)
        if generator.inside((x, y), center=(0, 0), radius=1):
            INSIDE[i] += 1

        DARTS[i].append(TOTAL)
        ESTIMATES[i].append(pi := generator.calculate(INSIDE[i], TOTAL))
        ERRORS[i].append(generator.error(pi))

        ax1.plot(DARTS[i], ESTIMATES[i], label=f"Simulation: {i+1}")
        ax2.plot(DARTS[i], ERRORS[i], label=f"Simulation: {i+1}")

    ax1.set_ylabel("Value of Pi")
    ax2.set_ylabel("Percentage Error in Calculation")
    ax2.set_xlabel("Total number of DARTS")

    ax1.grid(True)
    ax2.grid(True)
    ax1.legend(loc="lower right")
    ax2.legend(loc="lower right")

    TOTAL += 1


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
animate = FuncAnimation(fig, calculate, interval=1)

if __name__ == "__main__":
    plt.show()