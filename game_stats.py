class Game_stats():
    def __init__(self,ai_setting):
        self.ai_setting=ai_setting
        self.reset_stats()
        self.game_active=False
        self.high_score = 0

        #self.score=0
    def reset_stats(self):
        self.ship_left=self.ai_setting.ship_limit
        self.score=0
        self.level=0