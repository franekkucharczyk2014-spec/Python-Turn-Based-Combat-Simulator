# Python Turn-Based Combat Simulator

Welcome to the **Python Turn-Based Combat Simulator**! This is a lightweight, text-based RPG combat game built entirely in Python. The game features strategic decision-making, a risk-versus-reward mechanic, and two distinct gameplay modes: challenging single-player battles against an AI with multiple difficulty scaling tiers, and a local head-to-head two-player duel.

---

## 🎮 Game Modes

The game offers two primary modes selectable from the main menu:

1. **Single Player Mode:** Pit your tactical skills against an AI-controlled opponent. Choose from four distinct difficulty levels, each featuring unique starting attributes, custom scaling, and distinct AI damage profiles.
2. **Two-Player Mode:** Duel a friend in local turn-based combat. Each player manages their own health pool, limited healing resources, and high-risk stun abilities.

---

## ⚙️ Gameplay Mechanics

### ⚔️ Basic Combat
* **Attack Action:** In both game modes, standard attacks deal a randomized damage range of **10 to 20** to the opponent.

---

### 🛡️ Single-Player Mechanics

In Single-Player, the player starts with **100 HP** and faces an enemy whose health and damage scale with the chosen difficulty. On each turn, you can choose one of three actions:

1. **Attack:** Deals **10–20 damage** to the enemy.
2. **Heal:** Consumes one healing charge (if available) to attempt to restore **20 HP** (capped at 100 HP). 
   * **Success Rate:** Base success rate is **50%**.
   * **Tactical Advantage:** A successful heal **prevents the enemy from attacking** you during that turn. A failed heal fails to restore HP, consumes the charge, and leaves you open to an enemy counterattack.
3. **Run (Escape):** Attempt to immediately escape the battle and end the run. The base escape chance depends entirely on your chosen difficulty level.
   * **The Cost of Failure (Severe Scaling Penalty):** If your escape attempt fails, the enemy becomes significantly more dangerous:
     * The enemy's current and maximum health is **increased by 50%** (rounded to the nearest whole number).
     * Your overall escape chance is permanently **divided by 1.5** for subsequent attempts.
     * Your success chance for healing is **increased by 10%** (multiplied by 1.1) as a defensive compensation.
     * The enemy immediately attacks you.

---

### 🤼 Two-Player Duel Mechanics

In local PvP mode, both players start with **100 HP** and **6 healing charges**. On your turn, you can select one of three actions:

1. **Attack:** Deals **10–20 damage** to the opponent.
2. **Heal:** Consumes one healing charge to attempt to restore **20 HP** (capped at 100 HP) with a **50% success rate**. 
3. **Stun:** A high-risk, high-reward tactical move with a **25% success rate**.
   * **On Success:** The opponent is stunned, completely skipping their upcoming turn.
   * **On Failure (Backfire):** The opponent is rewarded for your failed attempt: they instantly regain **10 HP** (capped at 100 HP) and receive **+1 extra healing charge**.

---

## 📊 Difficulty Matrix (Single Player)

The game features four difficulty levels that determine the starting enemy attributes, your resources, and escape probabilities:

| Difficulty Level | Enemy Starting & Max HP | Enemy Attack Damage Range | Player Healing Charges | Base Escape Chance |
| :--- | :---: | :---: | :---: | :---: |
| **Easy** | 100 HP | 10 – 20 | 0 | 50% |
| **Medium** | 150 HP | 12 – 22 | 6 | 25% |
| **Hard** | 200 HP | 15 – 25 | 8 | 25% |
| **Impossible** | 250 HP | 20 – 30 | 10 | 0% (Cannot Escape) |

*Design Note:* On **Easy**, you cannot heal (0 heals), but the enemy is weaker and you have the highest chance to run away. On **Impossible**, escaping is completely disabled (0% chance), and the enemy hits incredibly hard with 250 HP, but you are compensated with 10 healing charges to survive.

---

## 🚀 How to Run

### Prerequisites
* **Python 3.x** installed on your system.
* Standard Python libraries (uses the built-in `random` module, no external dependencies required).

### Execution
1. Clone or download this repository.
2. Open your terminal or command prompt in the directory containing the `battle.py` file.
3. Run the script depending on your operating system:
   * **On Windows:**
     ```cmd
     python battle.py
     ```
   * **On Mac / Linux:**
     (Make sure to append `3` to the command)
     ```bash
     python3 battle.py
     ```
4. Follow the on-screen prompts to select your game mode and enter combat actions!
