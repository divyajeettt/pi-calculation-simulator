import pygame
import screens
import generator


"""
This is a 'Pi' Calculator Simulation

You will be asked to enter the number of darts to use to calculate pi by the
following algorithm:
    • A SQUARE screen will appear which contains a CIRCLE
    • the diameter of the CIRCLE is exactly equal to the side of the SQUARE
    • the darts will be placed one-by-one (randomly) inside the SQUARE

    • let the total number of darts be Nₜ
    • let the number of darts landing in the CIRCLE be Nₒ
    • ratio Nₒ / Nₜ ∝ Area(CIRCLE) / Area(SQUARE) ≡ π / 4
      when the diameter of the CIRCLE is exactly equal to side of the SQUARE

    • so, 4 * (Nₒ/Nₜ) is a close approximation of pi, which gets better and
      better for higher number of darts (as Nₜ → ∞)

Controls:
    Press Space-Bar to stop at any point of time
    Press P to print the current calculated value of Pi and Percentage Error
    Press A / M to print the average / mean value of Pi over the last 50 terms
        and Percentage Error in it
"""


screens.main()


SIDE: int = 650            # side of main screen and the SQUARE
RADIUS: int = SIDE // 2    # radius of the circle
CENTER: tuple[int, int] = (RADIUS, RADIUS)

WINDOW = pygame.display.set_mode((SIDE, SIDE))
FPS: int = 60

DARTS: int = screens.darts
INSIDE: int = 0

# colors
Color = tuple[int, int, int]
WHITE: Color = (255, 255, 255)
BLACK: Color = (0, 0, 0)
RED: Color = (255, 0, 0)
BLUE: Color = (0, 0, 255)

pygame.display.set_caption("Pi Calculator")


def draw_dart() -> None:
    """draws the darts one-by-one on the screen"""
    global INSIDE

    pair = (x, y) = generator.pair(SIDE)
    if generator.inside(pair, CENTER, RADIUS):
        INSIDE += 1
        pygame.draw.rect(WINDOW, RED, (x, y, 2, 2))
    else:
        pygame.draw.rect(WINDOW, BLUE, (x, y, 2, 2))


def main() -> None:
    total = 0
    clock = pygame.time.Clock()
    cache = []

    WINDOW.fill(WHITE)
    pygame.draw.circle(WINDOW, BLACK, CENTER, RADIUS, width=3)

    pygame.display.update()

    RUN = True
    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    RUN = False
                elif event.key == pygame.K_p:
                    print(f"{total=},",
                        (pi := generator.calculate(INSIDE, total)),
                        generator.error(pi)
                    )
                elif event.key in (pygame.K_a, pygame.K_m):
                    print("avg(π) =",
                        (pi := sum(cache)/len(cache)), generator.error(pi)
                    )

        if RUN and total < DARTS:
            draw_dart()
            if len(cache) > 50:
                cache = cache[1:]
            if total >= 1:
                cache.append(generator.calculate(INSIDE, total))
            total += 1
        else:
            RUN = False
            screens.ending(
                total,
                (pi := generator.calculate(INSIDE, total)), generator.error(pi)
            )

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
