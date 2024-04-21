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

    result = ""

    if monster_cards:
        result += "Monster cards:\n"
        for card_name in sorted(monster_cards.keys(), reverse=True):
            result += f"  ***{card_name}\n"

    if spell_cards:
        result += "Spell cards:\n"
        for card_name in sorted(spell_cards.keys()):
            result += f"  $$${card_name}\n"

    return result.strip()
