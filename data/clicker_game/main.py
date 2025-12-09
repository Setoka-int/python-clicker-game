# main.py - Запуск игры и GUI
import tkinter as tk
from core import Game


class ClickerApp:
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("SergToken Clicker")
        self.setup_ui()

    def setup_ui(self):
        # Кнопка клика
        self.click_btn = tk.Button(
            self.root,
            text="КЛИКНУТЬ!",
            font=("Arial", 20),
            command=self.on_click,
            bg="lightblue",
            width=15,
            height=3
        )
        self.click_btn.pack(pady=20)

        # Баланс
        self.balance_label = tk.Label(
            self.root,
            text=f"SergToken: {self.game.player.tokens}",
            font=("Arial", 16)
        )
        self.balance_label.pack()

        # Сила клика
        self.power_label = tk.Label(
            self.root,
            text=f"Сила клика: {self.game.player.tokens_per_click}",
            font=("Arial", 12)
        )
        self.power_label.pack()

        # Кнопка магазина
        self.shop_btn = tk.Button(
            self.root,
            text="Магазин",
            command=self.open_shop,
            font=("Arial", 14)
        )
        self.shop_btn.pack(pady=10)

    def on_click(self):
        self.game.player.click()
        self.update_display()

    def open_shop(self):
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Магазин")

        for upgrade in self.game.shop:
            btn = tk.Button(
                shop_window,
                text=f"{upgrade.name}\nЦена: {upgrade.price}",
                command=lambda u=upgrade: self.buy_upgrade(u),
                width=20
            )
            btn.pack(pady=5)

    def buy_upgrade(self, upgrade):
        if upgrade.buy(self.game.player):
            self.update_display()

    def update_display(self):
        self.balance_label.config(text=f"SergToken: {self.game.player.tokens}")
        self.power_label.config(text=f"Сила клика: {self.game.player.tokens_per_click}")

    def run(self):
        self.root.mainloop()


# Запуск игры
if __name__ == "__main__":
    app = ClickerApp()
    app.run()