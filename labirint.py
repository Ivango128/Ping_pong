from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x,size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
      
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
              self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0: 
            for p in platforms_touched:
              self.rect.left = max(self.rect.left, p.rect.right) 
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0  
                self.rect.top = max(self.rect.top, p.rect.bottom) 
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)
    
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
    def update(self):
        if self.rect.x <= 420:
            self.side = "right"
        if self.rect.x >= 800 - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy1(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
  
    def update(self):
        if self.rect.x <= 800 + 50:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    
    
    def update(self):
        if self.rect.x <= 650 + 50: 
            self.side = "right"
        if self.rect.x >= 1000 - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
class Enemy3(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
    def update(self):
        if self.rect.x <= 200 + 50: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= 600:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy4(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
    def update(self):
        if self.rect.x <= 1100 - 50: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 50:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 
  
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()
 

win_width = 1400
win_height = 800
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (152,251,152)
 
barriers = sprite.Group()
 
bullets = sprite.Group()
 
monsters = sprite.Group()
 

w1 = GameSprite('wall.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('wall.png', 370, 100, 50, 400)
w3 = GameSprite('wall.png', 800, 50, 50, 400)
w4 = GameSprite('wall.png', 650, 500, 50, 400)
w5 = GameSprite('wall.png', 200, 550, 50, 400)
w5 = GameSprite('wall.png', 200, 550, 50, 400)
w6 = GameSprite('wall.png', 1000, 400, 50, 300) 

barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)


packman = Player('rabbit.png.png', 5, win_height - 80, 80, 80, 0, 0)
final_sprite = GameSprite('rabbit.png.png', win_width - 85, win_height - 800, 80, 80)
 
monster1 = Enemy('wolf.png', 800- 80, 150, 80, 80, 5)
monster2 = Enemy('wolf.png', 800 - 80, 230, 80, 80, 5)
monster3 = Enemy1('wolf.png', 800 + 50, 230, 80, 80, 5)
monster4 = Enemy2('wolf.png', 800 + 50, 600, 80, 80, 5)
monster5 = Enemy3('wolf.png', 200 + 50, 600, 80, 80, 5)
monster6 = Enemy4('wolf.png', 1100 + 50, 600, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4) 
monsters.add(monster5) 
monsters.add(monster6)

finish = False

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()
 
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
 

    if not finish:
        window.fill(back)

        packman.update()
        bullets.update()

        packman.reset()

        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)


        if sprite.spritecollide(packman, monsters, False):
            finish = True
            img = image.load('game-over.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = image.load('you-win.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    display.update()
    display.update()

