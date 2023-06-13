import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    three_img = pg.image.load("ex01/fig/3.png")
    three_img = pg.transform.flip(three_img , True , False)
    tenthree_img = pg.transform.rotate(three_img , 10)
    tori_list=[three_img, tenthree_img]
    tmr_img = 0
    tmr2_img=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0+tmr2_img, 0])
        screen.blit(tori_list[tmr_img%2], [300, 200])
        pg.display.update()
        tmr_img += 15
        tmr2_img -=10
        if tmr2_img>1599:
            continue    
        if tmr2_img <= 1599:
            screen.blit(bg_img,[0,0])
            clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()