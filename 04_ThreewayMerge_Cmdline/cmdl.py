import readline
import shlex
import cmd

class Monster:
    def __init__(self, name, hp, x, y):
        self.name = name
        self.hp = int(hp)
        self.x = int(x)
        self.y = int(y)

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

class game(cmd.Cmd):
    prompt = "> "
    monsters = []
    player = Player()
    cnt = 0

    def do_add(self, arg):
        args = shlex.split(arg)
        name = args[2]
        hp = args[4]
        x = args[6]
        y = args[7]
        for monster in self.monsters:
            if monster.x == x and monster.y == y and monster.name == name:
                monster.hp = hp
                return
        self.monsters.append(Monster(name, hp, x, y))

    def do_show(self, arg):
        for monster in self.monsters:
            print(f"{monster.name} at ({monster.x} {monster.y}) hp {monster.hp}")

    def do_move(self, arg):
        args = shlex.split(arg)
        phrase = "cannot move"
        if args[0] == "up":
            if self.player.y < 9:
                self.player.y += 1
                phrase = ""
        elif args[0] == "down":
            if self.player.y > 0:
                self.player.y -= 1
                phrase = ""
        elif args[0] == "right":
            if self.player.x < 9:
                self.player.x += 1
                phrase = ""
        elif args[0] == "left":
            if self.player.x > 0:
                self.player.x -= 1
                phrase = ""

        if phrase:
            print(phrase)
        else:
            print(f"player at {self.player.x} {self.player.y}")
            monsters_in_field = []
            for monster in self.monsters:
                if monster.x == self.player.x and monster.y == self.player.y:
                    monsters_in_field.append(f"{monster.name} {monster.hp} hp")
            if len(monsters_in_field):
                print("encountered:", ','.join(monsters_in_field))
        
    def do_atack(self, arg):
        args = shlex.split(arg)
        for monster in self.monsters:
            if monster.x == self.player.x and monster.y == self.player.y and monster.name == args[0]:
                monster.hp -= 10
                if monster.hp <= 0:
                    print(f"{monster.name} dies")
                    self.monsters.remove(monster)
                else:
                    print(f"monster {monster.name} lost 10 hp, now has {monster.hp} hp")
                return
        print(f"no {args[0]} here")

    def complete_move(self, prefix, allcommand, beg, end):
        directions = ["up", "down", "left", "right"]
        return [s for s in directions if s.startswith(prefix)]
    
    def do_exit(self, arg):
        return True

game().cmdloop()
