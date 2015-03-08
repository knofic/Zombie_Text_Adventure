import random
import items, world

class Player:
    inventory = [items.Knife(), items.ProPlus()]
    hp = 100
    stamina = 50
    location_x, location_y = (0, 1)
    victory = False

    def is_alive(self):
        return self.hp > 0

    def view_inventory(self):
        print("\n=====\nYou have {} hit points and {} stamina left.\n=====\n".format(self.hp, self.stamina),"\nYou are currently carrying:\n")
        for item in self.inventory:
            print(item)

    """def use_consumables(self):
        print("\nChoose an an item to use:")
        consumables = []
        if items.ProPlus(self.inventory):
            consumables.append(actions_usePP)
        if items.FirstAidKit(self.inventory):
            consumables.append(actions_useFAK)
        return consumables"""

    """def use_fak(self):"""

    def use_pp(self):
        for items.ProPlus(self.inventory):
            if self.stamina <= 100:
                self.stamina = self.stamina + ProPlus.stamina
                print("\nYou now have {} stamina.".format(self.stamina))
            else:
                print("\nYou have {} stamina.".format(self.stamina), "You're as pumped as you are gonna get!")



    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        used_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.dmg2 > max_dmg:
                    max_dmg = i.dmg2
                    used_weapon = i

        print("You use your {} against the {}!".format(used_weapon.name, enemy.name))
        enemy.hp -= random.randint(used_weapon.dmg1, used_weapon.dmg2)
        self.stamina -= used_weapon.stamina
        if not enemy.is_alive():
            print("You killed the {}!".format(enemy.name))
        else:
            print("{} has {} HP's left.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

