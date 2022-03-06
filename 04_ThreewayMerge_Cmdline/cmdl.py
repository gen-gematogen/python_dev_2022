import readline
import shlex
import cmd

class Monster:
    def __init__(self, name, hp, x, y):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

class game(cmd.Cmd):
    prompt = "> "
    monsters = []
    player = Player()

    def do_add(self, arg):
        args = shlex.split(arg)
        name = args[3]
        hp = args[5]
        x = args[7]
        y = args[8]
        for monster in monsters:
            if monster.x == x and monster.y == y and monster.name == name:
                monster.hp = hp
                return
        monsters.append(Monster(name, hp, x, y))

    def do_show(self, arg):
        for monster in monsters:
            print(f"{monster.name} at ({monster.x} {monster.y}) hp {monster.hp}")

    def do_move(self, arg):
        args = shlex.split(arg)
        phrase = "cannot move"
        if args[1] == "up":
            if player.y < 9:
                player.y += 1
                phrase = ""
        elif args[1] == "down":
            if player.y > 0:
                player.y -= 1
                phrase = ""
        elif args[1] == "right":
            if player.x < 9:
                player.x += 1
                phrase = ""
        elif args[1] == "left":
            if player.x > 0:
                player.x -= 1
                phrase = ""

        if phrase:
            print(phrase)
        else:
            print(f"player at {player.x} {player.y}")
            print(f"encountered: {monster.name} {monster.hp} hp".join(',') for monster in monsters if monster.x == player.x and monster.y == player.y)
        
    def do_atack(self, arg):
        for monster in monsters:
            if monster.x == player.x and monster.y == player.y and monster.name == args[1]:
                monster.hp -= 10
                if monster.hp <= 0:
                    print(f"{monster.name} dies")
                    monsters.remove(monster)
                else:
                    print(f"monster {monster.name} lost 10 hp, now has {monster.hp} hp")
                return
        print(f"no {args[1]} here")

    def complete_perform(self, prefix, allcommand, beg, end):
        return [s for s in ("sing", "show") if s.startswith(prefix)]
        
    def do_exit(self, arg):
        return True

game().cmdloop()
