# pi-calculation-simulator

# About pi-calculation-simulator

pi-calculation-simulator is a simple simulation of calculating the mathematical constant [pi](https://en.wikipedia.org/wiki/Pi), which is built using [`pygame`](https://www.pygame.org/docs/) in Python. It is a graphical-user interface based project. 

*Date of creation:* `07 August, 2021`

## The methods

This project includes the following two methods of calculating pi:
- *Throwing* darts 
- [Infinite Series](https://en.wikipedia.org/wiki/Series_(mathematics))

### *Throwing* darts

Pi is calculated using the following algorithm:
- A SQUARE screen will appear which contains a CIRCLE
- the diameter of the CIRCLE is exactly equal to the side of the SQUARE
- the darts will be placed one-by-one (randomly) inside the SQUARE
- let the total number of darts be Nₜ
- let the number of darts landing in the CIRCLE be Nₒ
- ratio Nₒ / Nₜ ∝ Area(CIRCLE) / Area(SQUARE) ≡ π / 4 when the diameter of the CIRCLE is exactly equal to side of the SQUARE
- so, 4 * (Nₒ/Nₜ) is a close approximation of pi, which gets better and
- better for higher number of darts (as Nₜ → ∞)
