# Python-Rider-Game-Slots-Backend
Backend for selecting a random car with slots. Intended to be similar to the slots in the mobile game ["Rider"](https://play.google.com/store/apps/details?id=com.ketchapp.rider&hl=en_ZA&gl=US).

##### Fun 60 min project i did the previous day.


## Config

```py

common_chance = 50  # 
rare_chance = 30    # Chances to get an epic, rare and common car.
epic_chance = 20    #
coins = 2000 # Starter coins
required_amount_for_spin = 200 # How much coins does the first spin cost.
new_spin_amount = 50 # Amount to be added to required_amount_for_spin each spin.
admin = True # Special testing setting

"""
The Possible Choices:
"""
common = ["Toyota RAV4", "Subaru Impreza", "Ford Explorer", "7 Toyota Corolla", "Ford Focus", "Chevrolet Impala", "Honda Civic", "Chevrolet Malibu"]
rare = ["Lancia Stratos", "Land Rover Defende", "Lamborghini Miura", "Mini", "Lotus Esprit", "Porsche 911", "Audi Quattro", "McLaren F1"]
epic = ["Lamborghini Veneno", "Koenigsegg CCXR Trevita", "Bugatti Divo", "Mercedes-Maybach Exeleo", "Bugatti Centodieci", "Bugatti La Voiture Noire", "Rolls-Royce Boat Tail"]

```
