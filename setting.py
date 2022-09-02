class settings():

    def __init__(self) :
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5
        self.ship_limit=3
        self.alien_speed_factor=1
        self.fleet_droop_speed=10
        self.fleet_direction=1
        self.bullet_speed=3
        self.bullet_width=1100
        self.bullet_high=15
        self.bullet_color=60,60,60
        self.bullet_speed_factor = 1
        self.bullet_allow=3
        self.increace_scale=1.1
        self.aliens_point=50
        self.score_scale=1.5
    def int__dynamic(self):
        self.alien_speed_factor = 1
        self.bullet_speed = 3
        self.ship_speed_factor = 1.5
        self.fleet_direction = 1
    def increace_speed(self):
        self.alien_speed_factor*=self.increace_scale
        self.bullet_speed*=self.increace_scale
        self.ship_speed_factor*=self.increace_scale
        self.aliens_point=int(self.aliens_point*self.score_scale)

