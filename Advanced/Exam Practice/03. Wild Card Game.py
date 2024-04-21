def draw_cards(*args, **kwargs):
    monster_cards = {}
    spell_cards = {}

    for card_name, card_type in args:
        if card_type == "monster":
            monster_cards[card_name] = card_type
        elif card_type == "spell":
            spell_cards[card_name] = card_type

    for card_name, card_type in kwargs.items():
        if card_type == "monster":
            monster_cards[card_name] = card_type
        elif card_type == "spell":
            spell_cards[card_name] = card_type

    sorted_monster_cards = sorted(monster_cards.keys(), reverse=True)

    sorted_spell_cards = sorted(spell_cards.keys())

    result = ""

    if sorted_monster_cards:
        result += "Monster cards:\n"
        for card_name in sorted_monster_cards:
            result += f"{card_name} - {monster_cards[card_name]}\n"

    if sorted_spell_cards:
        result += "Spell cards:\n"
        for card_name in sorted_spell_cards:
            result += f"{card_name} - {spell_cards[card_name]}\n"

    return result.strip()

