class Monster():
    #  attributes for the monster
    def __init__(self, name, hp=20):
        self.exp = 0
        self.name = name
        self.type = "normal"
        self.current_hp = hp
        self.max_hp = hp
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack": 1,
                                 "slash": 2,
                                 "ice_storm": 3,
                                 "fire_storm": 3,
                                 "whirlwind": 3,
                                 "thunder_storm": 3,
                                 "earthquake": 2,
                                 "double_hit": 4,
                                 "tornado": 4,
                                 "wait": 0
                                 }

    def add_attack(self, attack_name):
        if attack_name not in self.possible_attacks.keys():
            return False

        # max attack = 4, if more weakest dropped (alphabetically)
        if len(self.attacks) == 4:
            small = 5
            smallest_key = ""
            for key, value in self.attacks.items():
                if value < small:
                    small = value
                    smallest_key = key
                elif value == small and key[0] < smallest_key[0]:
                    smallest_key = key
            del (self.attacks[smallest_key])

        self.attacks[attack_name] = self.possible_attacks[attack_name]
        return True

    def remove_attack(self, attack_name):
        if attack_name not in self.attacks.keys():
            return False
        del (self.attacks[attack_name])
        if len(self.attacks) < 1:
            self.attacks["wait"] = self.possible_attacks["wait"]
        return True

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.current_hp = self.max_hp
        self.exp += 1


def monster_fight(monster1, monster2):
    only_wait = ["wait"]
    if list(monster1.attacks.keys()) == only_wait and list(monster2.attacks.keys()) == only_wait:
        return -1, None, None
    rounds = 0
    m1_moves = []
    m2_moves = []

    m1 = sorted(monster1.attacks.items(), key=lambda x: (-x[1], x[0]))
    m2 = sorted(monster2.attacks.items(), key=lambda x: (-x[1], x[0]))

    while True:
        monster2.current_hp -= m1[rounds % len(m1)][1]
        m1_moves.append(m1[rounds % len(m1)][0])
        monster1.current_hp -= m2[rounds % len(m2)][1]
        m2_moves.append(m2[rounds % len(m2)][0])

        rounds += 1

        if monster1.current_hp <= 0:
            monster2.win_fight()
            monster1.lose_fight()
            return rounds, monster2, m2_moves
        elif monster2.current_hp <= 0:
            monster1.win_fight()
            monster2.lose_fight()
            return rounds, monster1, m1_moves

