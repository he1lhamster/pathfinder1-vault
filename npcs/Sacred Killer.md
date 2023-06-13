---
cssclass: [monsters]
title1: Sacred Killer
title2: Sacred Killer
CR: 8
sources:
- name: NPC Codex
  page: 208
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Half-orc
classes:
- cleric of Norgorber 1
- rogue 6
- assassin 2
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 16
  flat_footed: 14
  components:
    armor: 4
    dex: 5
    dodge: 1
HP:
  HP: 68
  long: 1d8+6d8+2d8+24
saves:
  fort: 7
  ref: 11
  will: 6
  other: +1 vs. poison
defensive_abilities:
- evasion
- improved uncanny dodge
- orc ferocity
- trap sense +2
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 short sword +12 (1d6+1/19-20 plus poison)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
        - effect: poison
      attack: +1 short sword
      bonus:
      - 12
  ranged:
  - - text: mwk dagger +11 (1d4/19-20 plus poison)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: poison
      attack: mwk dagger
      bonus:
      - 11
  special:
  - channel negative energy 2/day (DC 9, 1d6)
  - death attack (DC 14)
  - sneak attack +4d6
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 4/day
  - name: copycat
    source: default
    freq: 4/day
  sources:
  - name: default
    CL: 1
    concentration: 2
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: disguise self
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 11
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    concentration: 2
    slots:
      0: at-will
    domains:
    - death
    - trickery
tactics:
  Before Combat: The assassin attempts to cast his scroll of invisibility and coats
    his short sword with greenblood oil.
  During Combat: The assassin begins combat by studying his foe for a death attack.
    When making this attack, he uses Channel Smite and Vital Strike to do as much
    damage as possible.
ability_scores:
  STR: 10
  DEX: 20
  CON: 14
  INT: 14
  WIS: 12
  CHA: 8
BAB: 5
CMB: 5
CMD: 21
feats:
- name: Channel Smite
- name: Dodge
- name: Step Up
- name: Vital Strike
- name: Weapon Finesse
- name: Weapon Focus (short sword)
skills:
  Bluff: 11
  Climb: 8
  Disguise: 7
  Intimidate: 9
  Knowledge (local): 10
  Knowledge (nobility): 10
  Knowledge (religion): 10
  Perception: 13
  Sense Motive: 13
  Sleight of Hand: 13
  Spellcraft: 10
  Stealth: 17
languages:
- Common
- Dwarven
- Orc
special_qualities:
- aura
- orc blood
- poison use
- rogue talents (bleeding attack +4, finesse rogue, surprise attack)
- trapfinding +3
- weapon familiarity
gear:
  combat:
  - potion of cure serious wounds
  - scroll of invisibility
  - black adder venom (2)
  - giant wasp poison (2)
  - greenblood oil (2)
  other:
  - +1 studded leather
  - +1 short sword
  - masterwork dagger
  - belt of incredible dexterity +2
  - 303 gp
desc_long: Most evil temples and cults use sacred killers to enforce their twisted
  will or to eliminate annoying enemies.

---

# Sacred Killer

**Source** NPC Codex pg. 208
**XP** 4,800
Half-orc _[[classes/Cleric|cleric]]_ of Norgorber 1/rogue 6/assassin 2

NE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13

##### Defense

**AC** 20, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +5 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 68 (1d8+6d8+2d8+24)
**Fort** +7, **Ref** +11, **Will** +6; +1 vs. poison
**Defensive Abilities** evasion, improved uncanny _dodge_, _orc_ _[[universal monster rules/Ferocity|ferocity]]_, trap sense +2

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Short sword|short sword]]_ +12 (1d6+1/19–20 plus poison)
**Ranged** mwk _[[items/Weapon/Dagger|dagger]]_ +11 (1d4/19–20 plus poison)
**Special Attacks** channel negative energy 2/day (DC 9, 1d6), death attack (DC 14), sneak attack +4d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +2)
4/day—bleeding touch, copycat
**_Cleric_ Spells Prepared **(CL 1st; concentration +2)
1st—_[[spells/Bless|bless]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Divine Favor|divine favor]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 11), _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_
**D **Domain spell; **Domains **Death, Trickery

### Tactics

**Before Combat **The assassin attempts to cast his scroll of _[[spells/Invisibility|invisibility]]_ and coats his _short sword_ with _[[poisons/Greenblood Oil|greenblood oil]]_.
**During Combat **The assassin begins combat by studying his foe for a death attack. When making this attack, he uses _[[feats/Channel Smite|Channel Smite]]_ and _[[feats/Vital Strike|Vital Strike]]_ to do as much damage as possible.

##### Statistics
**Str** 10, **Dex** 20, **Con** 14, **Int** 14, **Wis** 12, **Cha** 8
**Base Atk** +5; **CMB** +5; **CMD** 21
**Feats** _Channel Smite_, _Dodge_, _[[feats/Step Up|Step Up]]_, _Vital Strike_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_short sword_)
**Skills** Bluff +11, _[[universal monster rules/Climb|Climb]]_ +8, Disguise +7, Intimidate +9, Knowledge (local, nobility, religion) +10, Perception +13, Sense Motive +13, Sleight of Hand +13, Spellcraft +10, Stealth +17
**Languages** Common, Dwarven, _Orc_
**SQ** aura, _orc_ blood, poison use, _[[classes/Rogue|rogue]]_ talents (bleeding attack +4, finesse _rogue_, surprise attack), trapfinding +3, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _invisibility_, _[[poisons/Black Adder Venom|black adder venom]]_ (2), _[[poisons/Giant Wasp Poison|giant wasp poison]]_ (2), _greenblood oil_ (2); **Other Gear** +1 studded leather, +1 _short sword_, masterwork _dagger_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, 303 gp

Most evil temples and cults use _[[items/Weapon Magic Abilities/Sacred|sacred]]_ killers to enforce their twisted will or to eliminate annoying enemies.