# pi-calculation-simulator

# About pi-calculation-simulator

pi-calculation-simulator is a simple project containing different simulations of calculating the mathematical constant **[pi](https://en.wikipedia.org/wiki/Pi)**, which is built using [`pygame`](https://www.pygame.org/docs/) in Python. It is a graphical-user interface based project. 

*Date of creation:* `07 August, 2021`

This project includes the following two methods of calculating pi:
- *Throwing* darts 
- [Infinite Series](https://en.wikipedia.org/wiki/Series_(mathematics))

## *Throwing* darts

Darts are *thrown*/placed on a screen containing a cricle inscribed in a square. The darts are drawn randomly from a uniform distribution. For larger and larger number of darts, the ratio

```python
4 * (darts_in_circle / total_darts)
```

[approaches](https://en.wikipedia.org/wiki/Limit_(mathematics)) the value of pi. A formal proof of working of the algorithm can be found in [`proof.pdf`](https://github.com/divyajeettt/pi-calculation-simulator/blob/main/proof.pdf).

### Features

- The darts landing inside the circle are marked RED.
- The darts landing ourside the circle are marked BLUE.
- Percentage error in the approximation of pi.
- Ability to view the approximation at any given moment.

### Controls

- Spacebar: Stop/end the simulation and view the final result
- P: Print the current approximation (and error)
- A/M: Print the average/mean of the 50 latest approximations and its error

### Module: `graph_darts`

A separate module allows the user to run the simulation without the GUI. Using this, a live-plot of the calculation is displayed, where the calculation is performed by throwing darts. The number of simulations to run can also be changed. To change the number of simulations, change [Line 6](https://github.com/divyajeettt/pi-calculation-simulator/blob/b8e529b344a79ffefd7dbaacd06f0b2c82c84706/graph_darts.py#L6) of `graph_darts.py` to 

```python
SIMULATIONS: int = X
```

where `X` is your desired number of simulations.

## Infinite Series

The user can select one of (currently) three infinite series that [converge to](https://en.wikipedia.org/wiki/Convergent_series) pi. A live-plot of the calculation is displayed. To select a seires, change [Line 14](https://github.com/divyajeettt/pi-calculation-simulator/blob/b8e529b344a79ffefd7dbaacd06f0b2c82c84706/graph_series.py#L14) of `graph_series.py` to

```python
SERIES: Callable[[int], series.GeneratorType] = series.seriesX()
```

where `X` should be a number from 1, 2, or 3.

### Module: `series`

`series.py` is a module, which can also be used independently of the project. It contains (currently) three generators, that yield values that get closer and closer to pi. It is currently used in `graph_series.py`, but may also be used as a separate module.

## Run

Clone the repository on your device and navigate to the folder.

To run the simulation of calculating pi by throwing darts and view it in real-time using the GUI, run:

```
python3 darts.py
```

To run the simulation(s) of calculating pi by throwing darts and view the approximations and errors in real-time on a plot, run:

```
python3 graph_darts.py
```

To run the simulation of calculating pi by infinite series and view the approximations and errors in real-time on a plot, run:

```
python3 graph_series.py
```

## References

- [Calculating Pi with Darts (YouTube)](https://www.youtube.com/watch?v=M34TO71SKGk)
- [Computing PI by throwing darts](https://www.cs.wustl.edu/~cytron/cs101/Lectures/5.html)
