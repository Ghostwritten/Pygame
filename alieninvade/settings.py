class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 3
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_diretion为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        self.ship_limit = 3