# Текстовый шутер (Text Shooter Game)

A simple text-based shooter game built with Python and tkinter.

## 🎮 Game Description

This is a turn-based text shooter game where you fight against enemies, manage your health and ammunition, and purchase upgrades from the shop. The game features a dark theme interface and includes an anti-cheat system.

## ✨ Features

- **Combat System**: Attack and defend against multiple enemy types
- **Inventory Management**: Manage weapons, ammunition, and health elixirs
- **Shop System**: Purchase ammunition, weapons, and health items with coins
- **Multiple Enemies**: Fight against 3 different enemy types with varying difficulty
- **Anti-cheat Protection**: Built-in anti-cheat system to prevent cheating
- **Dark Theme UI**: Modern dark-themed user interface

## 🎯 Game Mechanics

### Player Stats
- **Health**: 100 HP (starting value)
- **Starting Weapon**: Пистолет (Pistol) with 10 damage and 10 bullets
- **Starting Coins**: 50

### Enemies
1. **Враг 1** (Enemy 1): 100 HP, 5-25 damage, 10 coin reward
2. **Враг 2** (Enemy 2): 120 HP, 10-30 damage, 20 coin reward  
3. **Враг 3** (Enemy 3): 150 HP, 15-35 damage, 30 coin reward

### Shop Items
- **Ammunition**: 5 bullets for 10 coins
- **New Weapon**: 20 damage weapon with 10 bullets for 50 coins
- **Health Elixir**: Restore health for 30 coins

## 🚀 Installation & Running

### Prerequisites
- Python 3.x
- tkinter (usually comes with Python)

### Running the Game
```bash
# Clone the repository
git clone https://github.com/Bogdan0759/mypygametest.git
cd mypygametest

# Run the game
python main.py
```

## 🎮 How to Play

1. **Attack**: Click the "Атака" (Attack) button to damage enemies
2. **Defend**: Click the "Защита" (Defense) button to reduce incoming damage
3. **Use Elixir**: Click "Использовать эликсир" to restore health
4. **Shop**: Click "Магазин" to open the shop and purchase items
5. **Restart**: After game over, click "Начать заново" to restart

## 📁 Project Structure

```
mypygametest/
├── main.py          # Main game file with ShooterGame class
├── anticheat.py     # Anti-cheat system (currently empty)
└── README.md        # This file
```

## 🔧 Technical Details

- **Language**: Python 3.x
- **GUI Framework**: tkinter with ttk styling
- **Game Version**: 1.3.0
- **Architecture**: Object-oriented design with main ShooterGame class

## 🛡️ Anti-cheat System

The game includes an anti-cheat system (`anticheat.py`) that monitors game values to prevent cheating, though the implementation is currently minimal.

## 🎨 UI Features

- Dark theme with #2e2e2e background
- Modern button styling with hover effects
- Real-time health and ammunition display
- Responsive layout with proper spacing

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements. Some areas for enhancement:

- Complete the missing game methods (marked with "# Остальные методы игры...")
- Implement the anti-cheat system
- Add more enemy types and weapons
- Improve the user interface
- Add sound effects
- Implement save/load functionality

## 📝 License

This project is open source. Please check the repository for any license information.

## 🐛 Known Issues

- The main.py file appears to be incomplete (some methods are missing)
- The anticheat.py file is currently empty
- No main execution block (`if __name__ == "__main__":`)

## 📞 Contact

Repository: [https://github.com/Bogdan0759/mypygametest](https://github.com/Bogdan0759/mypygametest)

---

*Note: Despite the repository name suggesting pygame, this project actually uses tkinter for the GUI.*