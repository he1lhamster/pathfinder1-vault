---
cssclass: [monsters]
title1: Healer
title2: Healer
CR: 7
sources:
- name: NPC Codex
  page: 248
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Halfling
classes:
- adept 9
alignment: NG
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 1
AC:
  AC: 16
  touch: 12
  flat_footed: 15
  components:
    armor: 4
    dex: 1
    size: 1
HP:
  HP: 34
  long: 9d6+3
saves:
  fort: 6
  ref: 5
  will: 11
  other: +2 vs. fear
speeds:
  base: 20
attacks:
  melee:
  - - text: quarterstaff +3 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: quarterstaff
      bonus:
      - 3
  ranged:
  - - text: sling +6 (1d3-2)
      entries:
      - - damage: 1d3-2
      attack: sling
      bonus:
      - 6
spells:
  entries:
  - name: remove disease
    source: Adept
    level: 3
  - name: cure moderate wounds
    source: Adept
    level: 2
  - name: delay poison
    source: Adept
    level: 2
  - name: web
    source: Adept
    level: 2
    DC: 14
  - name: cure light wounds
    source: Adept
    level: 1
    count: 2
  - name: endure elements
    source: Adept
    level: 1
  - name: obscuring mist
    source: Adept
    level: 1
  - name: create water
    source: Adept
    level: 0
  - name: read magic
    source: Adept
    level: 0
  - name: stabilize
    source: Adept
    level: 0
  sources:
  - name: Adept
    type: prepared
    CL: 9
    concentration: 11
    slots:
      0: at-will
tactics:
  Before Combat: The adept drinks her potion of mage armor.
  During Combat: The adept catches as many foes as possible in her web, then heals
    her allies or seeks to escape. If she must fight, she prefers her sling.
  Base Statistics: Without mage armor, the adept's statistics are AC 12, touch 12,
    flat-footed 11.
ability_scores:
  STR: 6
  DEX: 13
  CON: 10
  INT: 12
  WIS: 14
  CHA: 12
BAB: 4
CMB: 1
CMD: 12
feats:
- name: Brew Potion
- name: Great Fortitude
- name: Iron Will
- name: Scribe Scroll
- name: Skill Focus (Heal)
skills:
  Acrobatics: 3
    when jumping: -1
  Appraise: 4
  Climb: 0
  Heal: 19
  Knowledge (local): 8
  Knowledge (nature): 13
  Linguistics: 3
  Perception: 4
  Profession (herbalist): 14
  Survival: 8
languages:
- Common
- Elven
- Gnome
- Halfling
- Sylvan
special_qualities:
- summon familiar (toad)
gear:
  combat:
  - potions of cure light wounds (2)
  - potion of cure moderate wounds
  - potions of lesser restoration (2)
  - potion of mage armor
  - restorative ointment
  - scroll of animal trance
  - scroll of cure moderate wounds
  - scroll of neutralize poison (CL 8th)
  - scroll of remove curse (CL 8th)
  - scroll of remove disease
  - wand of cure light wounds (29 charges)
  - holy water
  - tanglefoot bag
  other:
  - quarterstaff
  - sling with 10 bullets
  - antitoxin (2)
  - everburning torch
  - healer's kit
  - spell component pouch
  - wooden holy symbol
  - bit and bridle
  - pony (combat trained)
  - saddle
  - saddlebags
  - 38 gp
desc_long: |-
  This wise woman knows many natural remedies for wounds and ailments, and supports this knowledge with a strange mix of spells, scrolls, and potions. She is midwife to many women, assists in the delivery of livestock, and is trusted for her ability to predict storms and droughts. The healer has a kind heart and hates to see any creature suffer. She is usually able to find alternative ways for poor folk to pay for her services, and as a result is beloved by her community. Once she is provided with sufficient food, water, and household supplies for her needs, she often directs payments above and beyond that to other needy people in the vicinity, creating a web of trust and reliance among the townsfolk or villagers.

  If she helps adventurers with a curse, disease, or terrible injury, she is likely to ask them to build a stone wall, repair a house, or tend to a farmer's livestock in payment. This is the case even if there is a remote threat of monsters nearby, for she understands that the adventurers were likely to chase down that threat anyway, and therefore would be getting a service for free. She believes in generosity and altruism, but likes it when people remain humble and are willing to get their hands dirty doing "real work" that lacks the "glory" of bloodshed.

  Many of her supplies were acquired from years of negotiating and trading, whether directly for the items (such as her wand of cure light wounds) or for rare or exotic materials she can use to make potions and scrolls. If adventurers wish to pay her in the form of these goods (or by questing for them) or offer her minor healing items the adventurers have outgrown but that would still be useful for helping villagers, she gratefully accepts.

  The healer is especially interested in acquiring potions of cure light wounds, as she is not particularly fast on her feet (and is getting slower as the years pass), nor is she a skilled rider, so being able to hand a healing potion (which even a non-spellcaster can administer) to a fast rider or runner might make the difference between life and death for an injured farmer or rancher.

---

# Healer

**Source** NPC Codex pg. 248
**XP** 3,200
Halfling adept 9

NG Small humanoid (halfling)
**Init** +1; **Senses** Perception +4

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 Dex, +1 size)
**hp** 34 (9d6+3)
**Fort** +6, **Ref** +5, **Will** +11; +2 vs. _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +3 (1d4–2)
**Ranged** _[[items/Weapon/Sling|sling]]_ +6 (1d3–2)
**Adept Spells Prepared **(CL 9th; concentration +11)
3rd—_[[spells/Remove Disease|remove disease]]_
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Delay Poison|delay poison]]_, web (DC 14)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Endure Elements|endure elements]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Read Magic|read magic]]_, stabilize

### Tactics

**Before Combat **The adept drinks her potion of _[[spells/Mage Armor|mage armor]]_.
**During Combat **The adept catches as many foes as possible in her web, then heals her allies or seeks to escape. If she must fight, she prefers her _sling_.
**Base Statistics **Without _mage armor_, the adept’s statistics are **AC **12, touch 12, _flat-footed_ 11.

##### Statistics
**Str** 6, **Dex** 13, **Con** 10, **Int** 12, **Wis** 14, **Cha** 12
**Base Atk** +4; **CMB** +1; **CMD** 12
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (_[[spells/Heal|Heal]]_)
**Skills** Acrobatics +3 (–1 when jumping), Appraise +4, _[[universal monster rules/Climb|Climb]]_ +0, _Heal_ +19, Knowledge (local) +8, Knowledge (nature) +13, Linguistics +3, Perception +4, Profession (herbalist) +14, Survival +8
**Languages** Common, Elven, Gnome, Halfling, Sylvan
**SQ** _[[universal monster rules/Summon|summon]]_ familiar (toad)
**Combat Gear** potions of _cure light wounds_ (2), potion of _cure moderate wounds_, potions of lesser _[[spells/Restoration|restoration]]_ (2), potion of _mage armor_, _[[items/Wondrous Item/Restorative Ointment|restorative ointment]]_, scroll of _[[spells/Animal Trance|animal trance]]_, scroll of _cure moderate wounds_, scroll of _[[spells/Neutralize Poison|neutralize poison]]_ (CL 8th), scroll of _[[spells/Remove Curse|remove curse]]_ (CL 8th), scroll of _remove disease_, wand of _cure light wounds_ (29 charges), _[[items/Mundane/Holy water|holy water]]_, _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** _quarterstaff_, _sling_ with 10 bullets, _[[items/Mundane/Antitoxin|antitoxin]]_ (2), _[[items/Mundane/Everburning torch|everburning torch]]_, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Spell component pouch|spell component pouch]]_, wooden holy symbol, _[[items/Mundane/Bit and bridle|bit and bridle]]_, pony (combat trained), saddle, _[[items/Mundane/Saddlebags|saddlebags]]_, 38 gp

This wise woman knows many natural remedies for wounds and ailments, and supports this knowledge with a strange mix of spells, scrolls, and potions. She is midwife to many women, assists in the delivery of livestock, and is trusted for her ability to predict storms and droughts. The _healer_ has a kind heart and hates to see any creature suffer. She is usually able to find alternative ways for poor folk to pay for her services, and as a result is beloved by her community. Once she is provided with sufficient food, water, and household supplies for her needs, she often directs payments above and beyond that to other needy people in the vicinity, creating a web of trust and reliance among the townsfolk or villagers.

If she helps adventurers with a curse, disease, or terrible injury, she is likely to ask them to build a stone wall, repair a house, or tend to a farmer’s livestock in payment. This is the case even if there is a remote threat of monsters nearby, for she understands that the adventurers were likely to chase down that threat anyway, and therefore would be getting a service for free. She believes in generosity and altruism, but likes it when people remain humble and are willing to get their hands dirty doing "real work" that lacks the "glory" of bloodshed.

Many of her supplies were acquired from years of negotiating and trading, whether directly for the items (such as her wand of _cure light wounds_) or for rare or exotic materials she can use to make potions and scrolls. If adventurers _[[spells/Wish|wish]]_ to pay her in the form of these goods (or by questing for them) or offer her minor healing items the adventurers have outgrown but that would still be useful for helping villagers, she gratefully accepts.

The _healer_ is especially interested in acquiring potions of _cure light wounds_, as she is not particularly fast on her feet (and is getting slower as the years pass), nor is she a skilled rider, so being able to hand a healing potion (which even a non-spellcaster can administer) to a fast rider or runner might make the difference between life and death for an injured farmer or rancher.