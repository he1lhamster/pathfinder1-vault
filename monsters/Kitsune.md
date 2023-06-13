---
cssclass: [monsters]
title1: Kitsune
desc_short: This elegantly dressed woman has the head and bushy tail of well-groomed
  fox.
title2: Kitsune
CR: 1/2
sources:
- name: Bestiary 4
  page: 175
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 200
race: Female
classes:
- kitsune sorcerer 1
alignment: N
size: Medium
type: humanoid
subtypes:
- kitsune
- shapechanger
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 13
  touch: 13
  flat_footed: 10
  components:
    dex: 2
    dodge: 1
HP:
  HP: 5
  long: 1d6-1
saves:
  fort: -1
  ref: 2
  will: 4
speeds:
  base: 30
attacks:
  melee:
  - - text: bite -1 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: bite
      bonus:
      - -1
    - text: mwk quarterstaff -5 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: mwk quarterstaff
      bonus:
      - -5
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 3/day
  - name: laughing touch
    source: bloodline
    freq: 6/day
  sources:
  - name: default
    CL: 1
    concentration: 4
  - name: bloodline
    CL: 1
    concentration: 4
spells:
  entries:
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 15
  - name: sleep
    source: Sorcerer
    level: 1
    DC: 17
  - name: daze
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 4
      0: at-will
    bloodline: fey
ability_scores:
  STR: 8
  DEX: 15
  CON: 8
  INT: 12
  WIS: 14
  CHA: 17
BAB: 0
CMB: -1
CMD: 12
feats:
- name: Dodge
- name: Eschew Materials
skills:
  Acrobatics: 4
  Bluff: 7
  Perception: 3
  Spellcraft: 5
  Stealth: 3
  _racial_mods:
    Acrobatics:
      _: 2
languages:
- Common
- Elven
- Sylvan
special_qualities:
- bloodline arcana (+2 DC for compulsion spells)
- change shape
- kitsune magic
ecology:
  environment: temperate forests, hills, or mountains
  organization: solitary, pair, or gang (3-8)
  treasure_type: NPC Gear
  treasure:
  - potion of cure light wounds
  - mwk quarterstaff
  - other treasure
special_abilities:
  Change Shape (Su): A kitsune can assume the appearance of a specific single human
    form of the same sex. The kitsune always takes this specific form when she uses
    this ability. A kitsune in human form cannot use her bite attack, but gains a
    +10 racial bonus on Disguise checks made to appear human. This ability otherwise
    functions as alter self, except that the kitsune does not adjust her ability scores.
  Kitsune Magic (Ex/Sp): 'Kitsune add 1 to the DC of any saving throws of enchantment
    spells they cast. Kitsune with a Charisma score of 11 or higher gain the following
    spell-like ability: 3/day-dancing lights.'
desc_long: |-
  Wily but noble, kitsune are a race of shapechanging foxfolk. Each Kitsune has two shapes-a slender and attractive human form and its true form of an anthropomorphic fox. In either form, it displays physical grace and natural beauty. Most kitsune have ruddy, auburn fur and salient amber or pale blue eyes, though some are born with black, gray, or even white fur. White-furred kitsune are revered for their close connection to their spirit ancestors and typically raised as oracles.

  Quick-witted and nimble, kitsune delight in the creative arts, particularly riddles, storytelling, pranks, and tall tales, and have garnered a well-deserved reputation and duplicitous tricksters. They are a good-natured folk and greatly value friendship.

  When encountered outside human settlements, kitsune tend to live in small and remote villages run by elders of ancestral clans. In human settlements, kitsune usually remain in human form to avoid conflict.

---

# Kitsune
This elegantly dressed woman has the head and bushy tail of well-groomed fox.
**Source** Bestiary 4 pg. 175
**XP** 200
Female _[[monsters/Kitsune|kitsune]]_ _[[classes/Sorcerer|sorcerer]]_ 1

N Medium humanoid (_kitsune_, shapechanger)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +3

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 10 (+2 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 5 (1d6–1)
**Fort** –1, **Ref** +2, **Will** +4

##### Offense
**Speed** 30 ft.
**Melee** bite –1 (1d4–1), mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ –5 (1d6–1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +4)
3/day—_[[spells/Dancing Lights|dancing lights]]_
**Bloodline _Spell-Like Abilities_** (CL 1st; concentration +4)
6/day—laughing touch
**_Sorcerer_ Spells Known **(CL 1st; concentration +4)
1st (4/day)—_[[spells/Charm Person|charm person]]_ (DC 15), sleep (DC 17)
0 (at will)—_[[spells/Daze|daze]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_
**Bloodline** fey

##### Statistics
**Str** 8, **Dex** 15, **Con** 8, **Int** 12, **Wis** 14, **Cha** 17
**Base Atk** +0; **CMB** –1; **CMD** 12
**Feats** _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_
**Skills** Acrobatics +4, Bluff +7, Perception +3, Spellcraft +5, Stealth +3; **Racial Modifiers** +2 Acrobatics
**Languages** Common, Elven, Sylvan
**SQ** bloodline arcana (+2 DC for compulsion spells), _[[universal monster rules/Change Shape|change shape]]_, _kitsune_ magic

##### Ecology

**Environment** temperate forests, hills, or mountains
**Organization** solitary, pair, or gang (3–8)
**Treasure** NPC gear (potion of _[[spells/Cure Light Wounds|cure light wounds]]_, mwk _quarterstaff_, other treasure)

### Special Abilities

**_Change Shape_ (Su)** A _kitsune_ can assume the appearance of a specific single human form of the same sex. The _kitsune_ always takes this specific form when she uses this ability. A _kitsune_ in human form cannot use her bite attack, but gains a +10 racial bonus on Disguise checks made to appear human. This ability otherwise functions as _[[spells/Alter Self|alter self]]_, except that the _kitsune_ does not adjust her ability scores.

**_Kitsune_ Magic (Ex/Sp)** _Kitsune_ add 1 to the DC of any saving throws of enchantment spells they cast. _Kitsune_ with a Charisma score of 11 or higher gain the following spell-like ability: 3/day—_dancing lights_.

##### Description

Wily but noble, _kitsune_ are a race of shapechanging foxfolk. Each _Kitsune_ has two shapes—a slender and attractive human form and its _[[spells/True Form|true form]]_ of an anthropomorphic fox. In either form, it displays physical _[[spells/Grace|grace]]_ and natural beauty. Most _kitsune_ have ruddy, auburn fur and salient amber or pale blue eyes, though some are born with black, _[[monsters/Gray|gray]]_, or even white fur. White-furred _kitsune_ are revered for their close connection to their spirit ancestors and typically raised as oracles.

Quick-witted and nimble, _kitsune_ delight in the creative arts, particularly riddles, storytelling, pranks, and tall tales, and have garnered a well-deserved reputation and duplicitous tricksters. They are a good-natured folk and greatly value friendship.

When encountered outside human settlements, _kitsune_ tend to live in small and remote villages run by elders of ancestral clans. In human settlements, _kitsune_ usually remain in human form to avoid conflict.