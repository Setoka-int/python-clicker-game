# core.py - Все классы игры
class Player:
    def __init__(self):
        self.tokens = 0
        self.tokens_per_click = 1
        self.upgrades = []

    def click(self):
        self.tokens += self.tokens_per_click
        return self.tokens_per_click

    def can_afford(self, price):
        return self.tokens >= price


class Upgrade:
    def __init__(self, name, price, multiplier=2):
        self.name = name
        self.price = price
        self.multiplier = multiplier

    def buy(self, player):
        if player.can_afford(self.price):
            player.tokens -= self.price
            player.tokens_per_click *= self.multiplier
            player.upgrades.append(self)
            return True
        return False

#class market
class Game:
    def __init__(self):
        self.player = Player()
        self.shop = [
            Upgrade("x2 Клик", 50, 2),
            Upgrade("x3 Клик", 200, 3),
            Upgrade("x5 Клик", 1000, 5),
        ]