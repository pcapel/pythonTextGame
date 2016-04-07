from character_classes import Player

Commands = {
    'assign skill points': Player.assign_skill_points,
    'quit': Player.quit,
    'help': Player.help,
    'status': Player.status,
    'rest': Player.rest,
    'explore': Player.explore,
    'location': Player.locate,
    'inventory': Player.view_items,
    'use': Player.specify,
    'view bestiary': Player.view_bestiary,
  }

Battle_Commands = {
    'attack': Player.attack,
    'status': Player.status,
    'probe': Player.probe,
    'use': Player.specify,
    'flee': Player.flee,
    'inventory': Player.view_items,
    'help': Player.help,
    'view bestiary': Player.view_bestiary,
    'quit': Player.quit,
  }