import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    abg_img = pg.transform.flip(bg_img,True,False)
    three_img = pg.image.load("ex01/fig/3.png")
    three_img = pg.transform.flip(three_img , True , False)
    onethree_img = pg.transform.rotate(three_img , 1)
    twothree_img = pg.transform.rotate(three_img , 2)
    santhree_img = pg.transform.rotate(three_img , 3)
    yonthree_img = pg.transform.rotate(three_img , 4)
    fivethree_img = pg.transform.rotate(three_img , 5)
    sixthree_img = pg.transform.rotate(three_img , 6)
    seventhree_img = pg.transform.rotate(three_img , 7)
    eightthree_img = pg.transform.rotate(three_img , 8)
    ninethree_img = pg.transform.rotate(three_img , 9)
    tenthree_img = pg.transform.rotate(three_img , 10)

    tori_list=[three_img,twothree_img,santhree_img,yonthree_img,fivethree_img,sixthree_img,seventhree_img,eightthree_img,ninethree_img,tenthree_img,ninethree_img,eightthree_img,seventhree_img,sixthree_img,fivethree_img,yonthree_img,santhree_img,twothree_img,onethree_img,three_img]
    tmr_img = 0
    tmr2_img=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        tmr_img -= 1

        if tmr_img ==3200:
            tmr2_img=0
        screen.blit(bg_img, [tmr_img, 0])
        screen.blit(abg_img, [1600+tmr_img, 0])
        screen.blit(bg_img, [3200+tmr_img, 0])
        screen.blit(tori_list[tmr_img%20], [300, 200])
        pg.display.update()
        clock.tick(300)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()