import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一个存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编程
    bullets = Group()
    aliens = Group()
    #创建一个外星人
    alien = Alien(ai_settings, screen)
    #创建外星人集群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        #开始游戏循环
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()