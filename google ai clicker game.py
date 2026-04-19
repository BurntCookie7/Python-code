import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Clicker")
        self.root.geometry("300x400")

        # Game Variables
        self.score = 0
        self.multiplier = 1
        self.upgrade_cost = 10
        self.cps = 0

        # UI Elements
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 24))
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(root, text="CLICK ME!", font=("Arial", 16), 
                                      bg="gold", command=self.on_click)
        self.click_button.pack(pady=10, ipadx=20, ipady=10)

        self.upgrade_button = tk.Button(root, text=f"Buy Auto-Clicker ({self.upgrade_cost})", 
                                        command=self.buy_upgrade)
        self.upgrade_button.pack(pady=20)

        self.cps_label = tk.Label(root, text=f"CPS: {self.cps}")
        self.cps_label.pack()

        # Start the background auto-clicker loop
        self.auto_click()

    def on_click(self):
        """Increases score when user clicks the button."""
        self.score += self.multiplier
        self.update_ui()

    def buy_upgrade(self):
        """Increases CPS if the user has enough score."""
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.cps += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Increase price
            self.upgrade_button.config(text=f"Buy Auto-Clicker ({self.upgrade_cost})")
            self.update_ui()

    def auto_click(self):
        """Background loop that adds CPS to score every second."""
        self.score += self.cps
        self.update_ui()
        # Schedule this function to run again in 1000ms (1 second)
        self.root.after(1000, self.auto_click)

    def update_ui(self):
        """Refreshes the labels on the screen."""
        self.score_label.config(text=f"Score: {self.score}")
        self.cps_label.config(text=f"CPS: {self.cps}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
