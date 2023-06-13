---
cssclass: [monsters]
title1: Zuvembie
desc_short: This withered old corpse has a feral glint in her eyes and clasps a rusty
  axe in her yellow-nailed hands.
title2: Zuvembie
CR: 4
sources:
- name: Bestiary 3
  page: 289
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1200
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 13
  flat_footed: 12
  components:
    dex: 2
    dodge: 1
    natural: 2
HP:
  HP: 37
  long: 5d8+15
saves:
  fort: 3
  ref: 3
  will: 6
defensive_abilities:
- channel resistance +4
DR:
- amount: 5
  weakness: piercing
immunities:
- cold
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: battleaxe +4 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: battleaxe
      bonus:
      - 4
    - text: claw -1 (1d4)
      entries:
      - - damage: 1d4
      attack: claw
      bonus:
      - -1
  - - text: 2 claws +4 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 2
      attack: claws
      bonus:
      - 4
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  - name: ghoul touch
    source: default
    freq: 3/day
  - name: scare
    source: default
    freq: 3/day
    DC: 14
  - name: animate dead
    source: default
    freq: 1/day
  - name: ray of exhaustion
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: bat
      amount: 1d3
    - name: bird swarms [use the same stats]
    - name: constrictor snakes
      amount: 1d2
    - name: venomous snakes
      amount: 1d3
    - name: wolves
      amount: 1d4
  sources:
  - name: default
    CL: 4
    concentration: 6
ability_scores:
  STR: 13
  DEX: 14
  CON:
  INT: 11
  WIS: 14
  CHA: 15
BAB: 3
CMB: 4
CMD: 17
feats:
- name: Ability Focus (corpse call)
- name: Dodge
- name: Toughness
skills:
  Bluff: 7
  Knowledge (arcana): 8
  Perception: 10
  Stealth: 14
  _racial_mods:
    Stealth:
      _: 4
languages:
- Common (can't speak)
ecology:
  environment: any land
  organization: solitary
  treasure_type: standard
  treasure:
  - battleaxe
special_abilities:
  Corpse Call (Su): Zuvembies cannot speak, but their strange calls and whistles captivate
    the minds of those who hear them. Once per day, a zuvembie may call out, and all
    living creatures with an Intelligence score of 3 or higher within a 100-foot spread
    must succeed at a DC 16 Will save or move toward the zuvembie using the most direct
    means possible. If this path leads them into a dangerous area such as through
    fire or off a cliff, the creatures receive a second saving throw to end the effect
    before moving into peril. Captivated creatures can take no actions other than
    to defend themselves. A victim within 5 feet of the zuvembie simply stands and
    offers no resistance to the zuvembie's attacks. This effect continues for as long
    as the zuvembie continues its call as a standard action each round. This is a
    sonic mind-affecting charm effect, and has no effect on deaf creatures. The save
    DC is Charisma-based.
desc_long: |-
  Tied to the dark forces of nature and unholy magic, zuvembies employ fear and the wild creatures of the land to take their vengeance upon the living. Zuvembies appear to be withered, animate corpses but possess ruthless minds and blasphemous vigor. Revenge fuels a zuvembie, a hatefulness directed toward those who wronged it in life. Yet even when the last one who maligned it lies dead, its rage remains, turning against all who live, especially the relatives of the target of its original hate.

  Most zuvembies willingly performed the vile rituals to attain vengeance through unlife, but the transformation can also be wrought upon a helpless victim. The method of transforming into a zuvembie involves the creation and consumption of a vial of oil of animate dead, plus the performance of additional dark rites that take a day to perform and cost 3,000 gp. The ritual kills the target, who must make a DC 20 Will save. Failure results in the victim's death, while success means it reanimates as a free-willed zuvembie.

  Zuvembies stand between 5 and 6 feet tall and rarely weigh over 100 pounds.

---

# Zuvembie
This withered old corpse has a feral glint in her eyes and clasps a rusty axe in her yellow-nailed hands.
**Source** Bestiary 3 pg. 289
**XP** 1,200

NE Medium undead
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 15, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 37 (5d8+15)
**Fort** +3, **Ref** +3, **Will** +6
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 5/piercing; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Battleaxe|battleaxe]]_ +4 (1d8+1/×3), claw –1 (1d4) or 2 claws +4 (1d4+1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
At will—_[[spells/Darkness|darkness]]_
3/day—_[[spells/Ghoul touch|ghoul touch]]_, _[[spells/Scare|scare]]_ (DC 14)
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1d3 bat or bird swarms [use the same stats], 1d2 constrictor snakes, 1d3 venomous snakes, or 1d4 wolves)

##### Statistics
**Str** 13, **Dex** 14, **Con** —, **Int** 11, **Wis** 14, **Cha** 15
**Base Atk** +3; **CMB** +4; **CMD** 17
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (corpse call), _Dodge_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +7, Knowledge (arcana) +8, Perception +10, Stealth +14; **Racial Modifiers** +4 Stealth
**Languages** Common (can’t speak)

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** standard (_battleaxe_)

### Special Abilities

**Corpse Call (Su)** Zuvembies cannot speak, but their strange calls and whistles captivate the minds of those who hear them. Once per day, a _[[monsters/Zuvembie|zuvembie]]_ may _[[feats/Call Out|call out]]_, and all living creatures with an Intelligence score of 3 or higher within a 100-foot spread must succeed at a DC 16 Will save or move toward the _zuvembie_ using the most direct means possible. If this path leads them into a dangerous area such as through fire or off a cliff, the creatures receive a second saving throw to end the effect before moving into peril. Captivated creatures can take no actions other than to defend themselves. A victim within 5 feet of the _zuvembie_ simply stands and offers no _[[universal monster rules/Resistance|resistance]]_ to the _zuvembie_’s attacks. This effect continues for as long as the _zuvembie_ continues its call as a standard action each round. This is a sonic mind-affecting charm effect, and has no effect on deaf creatures. The save DC is Charisma-based.

##### Description

Tied to the dark forces of nature and _[[items/Weapon Magic Abilities/Unholy|unholy]]_ magic, zuvembies employ _[[universal monster rules/Fear|fear]]_ and the wild creatures of the land to take their _[[feats/Vengeance|vengeance]]_ upon the living. Zuvembies appear to be withered, animate corpses but possess ruthless minds and blasphemous _[[spells/Vigor|vigor]]_. Revenge fuels a _zuvembie_, a hatefulness directed toward those who wronged it in life. Yet even when the last one who maligned it lies dead, its _[[spells/Rage|rage]]_ remains, turning against all who live, especially the relatives of the target of its original hate.

Most zuvembies willingly performed the vile rituals to attain _vengeance_ through unlife, but the _[[spells/Transformation|transformation]]_ can also be wrought upon a _[[conditions/Helpless|helpless]]_ victim. The method of transforming into a _zuvembie_ involves the creation and _[[feats/Consumption|consumption]]_ of a _[[items/Mundane/Vial|vial]]_ of oil of _animate dead_, plus the performance of additional dark rites that take a day to perform and cost 3,000 gp. The ritual kills the target, who must make a DC 20 Will save. Failure results in the victim’s death, while success means it reanimates as a free-willed _zuvembie_.

Zuvembies stand between 5 and 6 feet tall and rarely weigh over 100 pounds.