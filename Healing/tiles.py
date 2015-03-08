import enemies, items, actions, world, random



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves


    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.UsePP())


        return moves


class EmptyCorridor(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the mall. You must forge onwards.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - random.randint(self.enemy.dmg1, self.enemy.dmg2)
            print("You have {} HP and {} stamina remaining.".format(player.hp, player.stamina))
        else:
            print("You have {} HP and {} stamina remaining.".format(player.hp, player.stamina))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class WalkerRoom(EnemyRoom):

    def __init__(self, x, y):
        super().__init__(x, y, enemies.Walker())

    def intro_text(self):
        if self.enemy.is_alive():
            return"""
            A dark room, lit only by thin shafts of light breaking through the dirty, boarded-up windows.
            Broken shelves and piles of smashed junk litter the floor. It might be your head playing tricks on you,
            but you think there might be something moving in there...
            A recently deceased corpse moves towards you!
            """
        else:
            return """
            A corpse is on the ground, rats scurry away from it as you approach.
            """