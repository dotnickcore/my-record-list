class MenuService:
    def __init__(self):
        self.options = {}
    
    def add_menu_option(self, option_key, description, func):
        self.options[option_key] = (description, func)
        
    def display_menu(self):
        """Prints the menu options to the console."""
        print("\n--- Main Menu ---")
        for key, (description, _) in self.options.items():
            print(f"{key}: {description}")
        print("Q: Quit")
        print("-----------------")