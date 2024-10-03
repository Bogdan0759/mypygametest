import tkinter as tk
from tkinter import ttk
import random
from anticheat import AntiCheat

class ShooterGame:
    def __init__(self, root):
        self.root = root
        self.version = "1.3.0"
        self.root.title(f"Текстовый шутер - Версия {self.version}")
        self.root.geometry("600x400")
        self.root.configure(bg="#2e2e2e")

        self.style = ttk.Style()
        self.style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.map("TButton", background=[("active", "#5a5a5a")])

        self.player_health = 100
        self.enemies = [
            {"name": "Враг 1", "health": 100, "damage_range": (5, 25), "reward": 10},
            {"name": "Враг 2", "health": 120, "damage_range": (10, 30), "reward": 20},
            {"name": "Враг 3", "health": 150, "damage_range": (15, 35), "reward": 30}
        ]
        self.current_enemy = self.enemies[0]
        self.defending = False
        self.inventory = {"Пистолет": {"урон": 10, "патроны": 10}, "Эликсир здоровья": 1}
        self.current_weapon = "Пистолет"
        self.coins = 50

        self.label = ttk.Label(root, text="Добро пожаловать в текстовый шутер!")
        self.label.pack(pady=10)

        self.health_label = ttk.Label(root, text=f"Ваше здоровье: {self.player_health} | Здоровье {self.current_enemy['name']}: {self.current_enemy['health']}")
        self.health_label.pack(pady=10)

        self.weapon_label = ttk.Label(root, text=f"Текущее оружие: {self.current_weapon} | Патроны: {self.inventory[self.current_weapon]['патроны']}")
        self.weapon_label.pack(pady=10)

        self.attack_button = ttk.Button(root, text="Атака", command=self.attack)
        self.attack_button.pack(pady=10)

        self.defend_button = ttk.Button(root, text="Защита", command=self.defend)
        self.defend_button.pack(pady=10)

        self.use_elixir_button = ttk.Button(root, text="Использовать эликсир", command=self.use_elixir)
        self.use_elixir_button.pack(pady=10)

        self.shop_button = ttk.Button(root, text="Магазин", command=self.open_shop)
        self.shop_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.restart_button = ttk.Button(root, text="Начать заново", command=self.restart)
        self.restart_button.pack(pady=10)
        self.restart_button.pack_forget()  # Скрываем кнопку перезапуска до конца игры

        self.version_label = ttk.Label(root, text=f"Версия игры: {self.version}")
        self.version_label.pack(side=tk.BOTTOM, pady=5)

        self.anti_cheat = AntiCheat(self)
        self.anti_cheat.check_initial_values()

    # Остальные методы игры...

    def restart(self):
        self.player_health = 100
        self.enemies = [
            {"name": "Враг 1", "health": 100, "damage_range": (5, 25), "reward": 10},
            {"name": "Враг 2", "health": 120, "damage_range": (10, 30), "reward": 20},
            {"name": "Враг 3", "health": 150, "damage_range": (15, 35), "reward": 30}
        ]
        self.current_enemy = self.enemies[0]
        self.defending = False
        self.inventory = {"Пистолет": {"урон": 10, "патроны": 10}, "Эликсир здоровья": 1}
        self.current_weapon = "Пистолет"
        self.coins = 50
        self.update_health()
        self.result_label.config(text="")
        self.attack_button.config(state=tk.NORMAL)
        self.defend_button.config(state=tk.NORMAL)
        self.shop_button.config(state=tk.NORMAL)
        self.restart_button.pack_forget()  # Скрываем кнопку перезапуска
        self.anti_cheat.check_initial_values()

    def open_shop(self):
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Магазин")
        shop_window.geometry("300x200")
        shop_window.configure(bg="#2e2e2e")

        ttk.Label(shop_window, text="Магазин", style="TLabel").pack(pady=10)
        ttk.Label(shop_window, text=f"Монеты: {self.coins}", style="TLabel").pack(pady=10)

        ttk.Button(shop_window, text="Купить патроны (10 монет)", command=lambda: self.buy_ammo(shop_window)).pack(pady=5)
        ttk.Button(shop_window, text="Купить новое оружие (50 монет)", command=lambda: self.buy_weapon(shop_window)).pack(pady=5)
        ttk.Button(shop_window, text="Купить эликсир здоровья (30 монет)", command=lambda: self.buy_elixir(shop_window)).pack(pady=5)

    def buy_ammo(self, shop_window):
        if self.coins >= 10:
            self.coins -= 10
            self.inventory[self.current_weapon]["патроны"] += 5
            self.result_label.config(text="Вы купили 5 патронов.")
            shop_window.destroy()
        else:
            self.result_label.config(text="У вас недостаточно монет!")

    def buy_weapon(self, shop_window):
        if self.coins >= 50:
            self.coins -= 50
            self.inventory["Новое оружие"] = {"урон": 20, "патроны": 10}
            self.current_weapon = "Новое оружие"
            self.result_label.config(text="Вы купили новое оружие.")
            shop_window.destroy()
        else:
            self.result_label.config(text="У вас недостаточно монет!")

    def buy_elixir(self, shop_window):
        if self.coins >= 30:
            self.coins -= 30
            self.inventory["Эликсир здоровья"] += 1
            self.result_label.config(text="Вы купили эликсир здоровья.")
            shop_window.destroy()
        else:
            self.result_label.config(text="У вас недостаточно монет!")

    # Остальные методы игры...
