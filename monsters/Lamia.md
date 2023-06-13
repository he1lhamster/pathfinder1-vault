---
cssclass: [monsters]
title1: Lamia
desc_short: This creature has the head and upper body of a beautiful woman, the lower
  body of a lion, and long, serpentine tail.
title2: Mythic Lamia
CR: 7
MR: 3
sources:
- name: Mythic Adventures
  page: 205
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 3200
alignment: CE
size: Large
type: monstrous humanoid
subtypes:
- mythic
- shapechanger
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: seduction
  DC: 16
AC:
  AC: 24
  touch: 14
  flat_footed: 19
  components:
    dex: 3
    dodge: 2
    natural: 10
    size: -1
HP:
  HP: 97
  long: 9d10+48
saves:
  fort: 7
  ref: 9
  will: 11
DR:
- amount: 5
  weakness: epic
speeds:
  base: 60
attacks:
  melee:
  - - text: +1 scimitar +13/+8 (1d6+5/18-20)
      entries:
      - - damage: 1d6+5
          crit_range: 18-20
      attack: +1 scimitar
      bonus:
      - 13
      - 8
    - text: 2 claws +12 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: claws
      bonus:
      - 12
    - text: touch +7 (1d4 Wisdom drain)
      entries:
      - - damage: 1d4
          type: Wisdom drain
      attack: touch
      bonus:
      - 7
  special:
  - mythic power (3/day, surge +1d6)
  - pounce
  - Wisdom drain
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
  - name: charm monster
    source: default
    freq: 3/day
    DC: 16
  - name: major image
    source: default
    freq: 3/day
    DC: 15
  - name: mirror image
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 15
  - name: deep slumber
    source: default
    freq: 1/day
    DC: 15
  sources:
  - name: default
    CL: 9
    concentration: 11
spells:
  entries:
  - name: haste
    source: Sorcerer
    level: 3
  - name: death knell
    source: Sorcerer
    level: 2
    DC: 14
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: cure light wounds
    source: Sorcerer
    level: 1
  - name: divine favor
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 12
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 12
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 8
    slots:
      3: 3
      2: 6
      1: 7
      0: at-will
ability_scores:
  STR: 18
  DEX: 16
  CON: 14
  INT: 13
  WIS: 17
  CHA: 15
BAB: 9
CMB: 14
CMD: 28
CMD_other: 32 vs. trip
feats:
- is_mythic: true
  name: Dodge
- name: Great Fortitude
- name: Iron Will
- name: Mobility
- is_mythic: true
  name: Spring Attack
skills:
  Bluff: 10
  Diplomacy: 5
  Disguise: 7
  Intimidate: 11
  Knowledge (religion): 4
  Perception: 15
  Stealth: 15
  Survival: 12
  _racial_mods:
    Bluff:
      _: 4
    Stealth:
      _: 4
languages:
- Abyssal
- Common
special_qualities:
- change shape (giant constrictor snake, lamia matriarch, or lion; polymorph)
- undersized weapons
ecology:
  environment: temperate desert
  organization: solitary, pair, or cult (3-12)
  treasure_type: double
  treasure:
  - +1 scimitar
  - other treasure
special_abilities:
  Aura of Seduction (Su): Any creature within 30 feet of a mythic lamia must succeed
    at a DC 16 Will save or become fascinated. A creature that succeeds at this save
    is immune to the lamia's aura for 24 hours. This is a mind-affecting effect. The
    save DC is Charisma-based.
  Spells: A mythic lamia casts spells as a 6th-level sorcerer, and can cast spells
    from the cleric list as well as those normally available to a sorcerer. Cleric
    spells are considered arcane spells for a mythic lamia.
  Wisdom Drain (Su): A lamia drains 1d4 points of Wisdom each time she hits with her
    melee touch attack. (Unlike with other kinds of ability drain attacks, a lamia
    does not heal any damage when she uses her Wisdom drain.) Lamias try to use this
    power early in an encounter to make foes more susceptible to charm monster and
    suggestion.
desc_long: A mythic lamia dabbled in dark pacts or strange magic in an attempt to
  break the ancient curse that gives her a monstrous form, but instead gained the
  ability to change her shape as well as other magical abilities. Impressed by her
  progress but angered by her lack of complete success, she continues her research
  and plotting.

---

# Lamia
This creature’s upper torso is that of a comely woman with cat’s eyes and sharp fangs, while her lower body is that of a _[[monsters/Lion|lion]]_.
**Source** Pathfinder RPG Bestiary pg. 186
**XP** 2,400
CE Large monstrous humanoid
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 Dex, +1 dodge, +7 natural, –1 size)
**hp** 67 (9d10+18)
**Fort** +7, **Ref** +9, **Will** +11

##### Offense
**Speed** 60 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +13/+8 (1d4+4/19–20), touch +7 (1d4 Wisdom drain), 2 claws +7 (1d4+2)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** Wisdom drain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
At will—_[[spells/Disguise Self|disguise self]]_, _[[spells/Ventriloquism|ventriloquism]]_
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 15), _[[spells/Major Image|major image]]_ (DC 14), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 14)
1/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 14)

##### Statistics
**Str** 18, **Dex** 16, **Con** 14, **Int** 13, **Wis** 17, **Cha** 13
**Base Atk** +9; **CMB** +14; **CMD** 28 (32 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Bluff +9, Diplomacy +4, Disguise +6, Intimidate +10, Knowledge (religion) +4, Perception +15, Stealth +15, Survival +12; **Racial Modifiers** +4 Bluff, +4 Stealth
**Languages** Abyssal, Common
**SQ** _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** temperate deserts
**Organization** solitary, pair, or cult (3–12)
**Treasure** double (+1 _dagger_, other treasure)

### Special Abilities

**_Undersized Weapons_ (Ex)** Although a _[[monsters/Lamia|lamia]]_ is Large, its upper torso is the same size as that of a _[[classes/Medium|Medium]]_ humanoid. As a result, lamias wield weapons as if they were one size category smaller than their actual size (_Medium_ for most lamias).

**Wisdom Drain (Su)** A _lamia_ drains 1d4 points of Wisdom each time it hits with its melee touch attack. (Unlike with other kinds of ability drain attacks, a _lamia_ does not _[[spells/Heal|heal]]_ any damage when it uses its Wisdom drain.) Lamias try to use this power early in an encounter to make foes more susceptible to _charm monster_ and _suggestion_.

##### Description

The hate-filled inheritors of an ancient curse, lamias appear as lean and attractive women from the waist up, while below they possess the bodies of powerful lions. Even their humanoid features bear distinctly feline traits, their eyes slitted and feral and their teeth like predatory fangs. A typical _lamia_ stands over 6 feet tall, measures more than 8 feet long, and weighs upward of 650 pounds.

Lamias are attracted to the ruined and forsaken parts of the world. Crumbling keeps, abandoned cities, and forgotten monuments all satisfy these _[[items/Weapon Magic Abilities/Deadly|deadly]]_ hunters’ _[[items/Weapon Magic Abilities/Cruel|cruel]]_ aesthetic—particularly those in arid or otherwise lifeless environs. Foremost, though, lamias favor decrepit temples. They delight in seeing the shrines of good deities in ruins and go out of their way to bring hardship to thriving holy places.

Lamias look to the eldest female of the group as their leader, mother, and _[[classes/Shaman|shaman]]_, cleaving to her with fanatical reverence. While lamias shun most religious followings—viewing such as the source of the curse that blighted them with bestial forms—_lamia_ elders claim to hear the whispers of the scouring desert winds and know the cold whims of the stars, drawing upon such mystical sources to lead their people.

The lamias presented here are but the most common and least powerful members of this cursed race, with others bearing serpentine, avian, and even more perverse forms.