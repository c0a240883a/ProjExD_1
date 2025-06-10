import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/3.png")
    bg_img2 = pg.transform.flip(bg_img2,True,False)
    kk_rct = bg_img2.get_rect()
    kk_rct.center = 300,200
    bg_img3 = pg.transform.flip(bg_img,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr
        if x==3199:
            tmr=0
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img3, [-x+1600, 0])
        screen.blit(bg_img, [-x, 0])
        key_lis = pg.key.get_pressed()
        if key_lis[pg.K_UP]:
            kk_rct.move_ip((0,-1))
        elif key_lis[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        elif key_lis[pg.K_RIGHT]:
            kk_rct.move_ip((1,0))
        elif key_lis[pg.K_DOWN]:
            kk_rct.move_ip((0,1))
        screen.blit(bg_img2, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()