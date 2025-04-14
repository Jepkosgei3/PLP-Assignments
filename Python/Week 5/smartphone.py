class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah, is_waterproof=False):
        """Initialize a new smartphone with basic specifications"""
        self.brand = brand
        self.model = model
        self.storage = storage_gb
        self.battery = battery_mah
        self.is_waterproof = is_waterproof
        self.is_on = False
        self.battery_level = 100
        self.installed_apps = []
    
    def power_on(self):
        """Turn on the smartphone"""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print("Device is already on.")
    
    def power_off(self):
        """Turn off the smartphone"""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print("Device is already off.")
    
    def install_app(self, app_name):
        """Install a new app"""
        if app_name not in self.installed_apps:
            self.installed_apps.append(app_name)
            print(f"App '{app_name}' installed successfully.")
        else:
            print(f"App '{app_name}' is already installed.")
    
    def uninstall_app(self, app_name):
        """Uninstall an app"""
        if app_name in self.installed_apps:
            self.installed_apps.remove(app_name)
            print(f"App '{app_name}' uninstalled successfully.")
        else:
            print(f"App '{app_name}' is not installed.")
    
    def check_battery(self):
        """Check and display battery level"""
        print(f"Battery level: {self.battery_level}%")
    
    def use_battery(self, percent):
        """Simulate battery usage"""
        if self.battery_level - percent >= 0:
            self.battery_level -= percent
            print(f"Used {percent}% battery. Remaining: {self.battery_level}%")
        else:
            print("Warning: Battery critically low!")
            self.battery_level = 0
    
    def charge(self, percent):
        """Charge the battery"""
        if self.battery_level + percent <= 100:
            self.battery_level += percent
            print(f"Charged {percent}%. Battery now at {self.battery_level}%")
        else:
            self.battery_level = 100
            print("Battery fully charged!")
    
    def display_specs(self):
        """Display all specifications of the smartphone"""
        print(f"\n{self.brand} {self.model} Specifications:")
        print(f"Storage: {self.storage}GB")
        print(f"Battery Capacity: {self.battery}mAh")
        print(f"Waterproof: {'Yes' if self.is_waterproof else 'No'}")
        print(f"Installed Apps: {', '.join(self.installed_apps) if self.installed_apps else 'None'}")
        print(f"Current Battery: {self.battery_level}%")
        print(f"Power Status: {'On' if self.is_on else 'Off'}")


# Inheritance example - GamingSmartphone extends Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, gpu_model, cooling_system, refresh_rate_hz):
        """Initialize a gaming smartphone with additional gaming-specific features"""
        super().__init__(brand, model, storage_gb, battery_mah, is_waterproof=True)
        self.gpu_model = gpu_model
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate_hz
        self.game_mode = False
    
    def activate_game_mode(self):
        """Activate gaming optimizations"""
        self.game_mode = True
        print(f"Game mode activated! {self.refresh_rate}Hz refresh rate enabled.")
    
    def deactivate_game_mode(self):
        """Deactivate gaming optimizations"""
        self.game_mode = False
        print("Game mode deactivated.")
    
    def display_specs(self):  # Method overriding
        """Display specs including gaming-specific features"""
        super().display_specs()
        print(f"GPU Model: {self.gpu_model}")
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate}Hz")
        print(f"Game Mode: {'Active' if self.game_mode else 'Inactive'}")


# Demonstration
if __name__ == "__main__":
    print("=== Regular Smartphone ===")
    phone1 = Smartphone("Apple", "iPhone 13", 128, 3095)
    phone1.power_on()
    phone1.install_app("Instagram")
    phone1.install_app("WhatsApp")
    phone1.use_battery(15)
    phone1.display_specs()
    
    print("\n=== Gaming Smartphone ===")
    gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 256, 6000, 
                                  "Adreno 730", "Vapor Chamber", 165)
    gaming_phone.power_on()
    gaming_phone.activate_game_mode()
    gaming_phone.install_app("Genshin Impact")
    gaming_phone.install_app("Call of Duty Mobile")
    gaming_phone.display_specs()
