import shlex
import cmd
import readline
import pynames 

from collections import defaultdict

class interpreter(cmd.Cmd):
    prompt = "> "
    lang = 'native'
    races = defaultdict(dict)

    for race_part in pynames.utils.get_all_generators():
        races[race_part.__module__.split('.')[2]][race_part.__name__] = race_part

    def do_language(self, arg):
        args = shlex.split(arg)
        self.lang = args[0]

    def do_generate(self, arg):
        args = shlex.split(arg)
        race = args[0]

        if len(args) < 3:
            args.append(None)
            args.append(None)
            args.append(None)

        if args[1][0] in pynames.GENDER.ALL:
            gender = args[1][0]
            race_part = args[2]
        elif args[2][0] in pynames.GENDER.ALL:
            gender = args[2][0]
            race_part = args[1]
        else:
            gender = None
            race_part = args[1]

        if race_part is None:
            G = next(iter(self.races.values()))
        else:
            G = self.races[race][race_part]
        

        gen = G()

        try:
            print(gen.get_name_simple(gender, self.language))
        except:
            print(gen.get_name_simple(gender, 'native'))

    def complete_language(self, prefix, s, start_prefix, end_prefix):
        return [l for l in LANGUAGE.ALL if l.startswith(prefix)]

    def do_info(self, arg):
        args = shlex.split(arg)
        race = self.races[args[0]]

        print(' '.join(race[args[1]].languages))

interpreter().cmdloop()
