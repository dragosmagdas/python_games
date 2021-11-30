import pygame as pg
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = pg.Rect(0, 0, 800, 600)

def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "images", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

def main(winstyle=0):
    pg.init()

    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # decorate the game window
    pg.display.set_caption("Spy")
    #pg.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = load_image("spy_background.png")
    background = pg.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    # Run our main loop whilst the player is alive.
    while True:
        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()