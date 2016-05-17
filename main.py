import character_classes, commands_dicts

def make_player():
  p = character_classes.Player()
  p.name = raw_input("What is your character's name? ")
  print "(type help to get a list of actions)\n"
  print "You enter a dark cave, searching for adventure.  Having heard that there is both great treasure, and great challenge, you enter seeking your destiny.  But be wary, young %s, for the way is dark, and the challenge that you face may be your last..." % p.name
  while(p.health > 0):
    line = raw_input("> ")
    args = line.split()
    if len(args) > 0:
      command_found = False
      if p.state == 'normal':
        for c in commands_dicts.Commands.keys():
          if args[0] == c[:len(args[0])]:
            commands_dicts.Commands[c](p)
            command_found = True
            break
      elif p.state == 'fight':
        for c in commands_dicts.Battle_Commands.keys():
          if args[0] == c[:len(args[0])]:
            commands_dicts.Battle_Commands[c](p)
            command_found = True
            break
      if not command_found:
        print "%s doesn't understand the suggestion." % p.name


if __name__ == "__main__":
  make_player()
