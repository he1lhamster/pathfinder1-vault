---
cssclass: [monsters]
title1: Demon, Schir
desc_short: This goat-headed humanoid is covered in a mangy gray hide that only partly
  covers its gaunt but muscled frame.
title2: Schir
CR: 4
sources:
- name: Bestiary 3
  page: 74
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1200
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 2
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 19
  touch: 12
  flat_footed: 17
  components:
    dex: 2
    natural: 7
HP:
  HP: 37
  long: 5d10+10
saves:
  fort: 6
  ref: 3
  will: 3
DR:
- amount: 5
  weakness: cold iron or good
immunities:
- disease
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 15
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk halberd +10 (1d10+4/×3 plus disease)
      entries:
      - - damage: 1d10+4
          crit_multiplier: 3
        - effect: disease
      attack: mwk halberd
      bonus:
      - 10
    - text: gore +3 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: gore
      bonus:
      - 3
  - - text: gore +8 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: gore
      bonus:
      - 8
  special:
  - powerful charge (gore, 3d6+4)
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: arcane lock
    source: default
    freq: 3/day
  - name: expeditious retreat
    source: default
    freq: 3/day
  - name: protection from good
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 2
    summons:
    - name: schirs
      amount: 1d3
      chance: 20%
  sources:
  - name: default
    CL: 6
    concentration: 4
ability_scores:
  STR: 17
  DEX: 14
  CON: 15
  INT: 8
  WIS: 5
  CHA: 6
BAB: 5
CMB: 8
CMD: 20
feats:
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (halberd)
skills:
  Acrobatics: 10
    jumping: 18
  Climb: 11
  Intimidate: 6
  Perception: 13
  Survival: 2
  _racial_mods:
    Acrobatics:
      when jumping: 8
    Perception:
      _: 8
languages:
- Abyssal
- telepathy 100 ft.
- tongues
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or pack (2-8)
  treasure_type: standard
  treasure:
  - masterwork halberd
  - other treasure
special_abilities:
  Disease (Ex): |-
    A schir gnaws constantly at the ends of its halberd. This infuses the blades with disease from the demon's filthy spittle. Any creature struck by a schir's halberd must succeed at a DC 14 Fortitude save or contract gray pox-a frightening disease that causes weakness, gray splotches on the skin, and eventual catatonia. The save DC is Constitution-based.

    Gray Pox: Halberd-injury; save Fort DC 14; onset 1 day; frequency 1/day; effect 1d6 Str damage; cure 2 consecutive saves.
desc_long: |-
  A schir resembles a tall, muscular humanoid with the head and hooves of a demonic goat. A ragged hide covers patches of a schir's body, usually around the forearms and lower legs, with a crestlike patch running down from the creature's crown to the nape of its neck. Schir demons are 7 feet tall, though they usually stoop and so appear shorter, and weigh 300 pounds.

  Also known as spite demons, schirs are among the most violent and vile-tempered inhabitants of the Abyss. Schirs are formed from the souls of mortals who either committed or framed others for heinous crimes-acts committed for the sole purpose of petty retribution. Despite such origins, schirs occupy one of the lowest orders in the demonic hierarchy, often serving as front-line infantry in demonic armies or as guards for minor demonic commanders.

  Although not especially intelligent, schirs are cunning warriors and able sentries. Although they prefer to charge into combat, a schir's natural jumping ability makes it a nimble enemy, capable of using its surroundings astutely. A schir will often jump on top of rocks, crumbling walls, or any other high place to hack with its disease-ridden halberd. For all of schirs' capabilities, their spitefulness makes them distrustful of any creature that has not proven its greater power and strength numerous times.

  A schir set loose upon the Material Plane quickly seeks to set itself up as a leader of its own army-often, schirs seek out tribes of savage humanoids and attempt to replace the current leaders. They are particularly fond of infiltrating gnoll tribes.

---

# Demon, Schir
This goat-headed humanoid is covered in a mangy _[[monsters/Gray|gray]]_ hide that only partly covers its gaunt but muscled frame.
**Source** Bestiary 3 pg. 74
**XP** 1,200
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +13

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +7 natural)
**hp** 37 (5d10+10)
**Fort** +6, **Ref** +3, **Will** +3
**DR** 5/cold iron or good; **Immune** disease, electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 15

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Halberd|halberd]]_ +10 (1d10+4/×3 plus disease), gore +3 (1d6+1) or gore +8 (1d6+4)
**Special Attacks** _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 3d6+4)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +4)
Constant—_see invisibility_, _[[spells/Tongues|tongues]]_
3/day—_[[spells/Arcane Lock|arcane lock]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Protection From Good|protection from good]]_
1/day—_[[universal monster rules/Summon|summon]]_ (level 2, 1d3 schirs 20%)

##### Statistics
**Str** 17, **Dex** 14, **Con** 15, **Int** 8, **Wis** 5, **Cha** 6
**Base Atk** +5; **CMB** +8; **CMD** 20
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_halberd_)
**Skills** Acrobatics +10 (+18 jumping), _[[universal monster rules/Climb|Climb]]_ +11, Intimidate +6, Perception +13, Survival +2; **Racial Modifiers** +8 Acrobatics when jumping, +8 Perception
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., _tongues_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or pack (2–8)
**Treasure** standard (masterwork _halberd_, other treasure)

### Special Abilities

**Disease (Ex)** A schir gnaws constantly at the ends of its _halberd_. This infuses the blades with disease from the demon’s filthy spittle. Any creature struck by a schir’s _halberd_ must succeed at a DC 14 Fortitude save or contract _gray_ pox—a frightening disease that causes weakness, _gray_ splotches on the skin, and eventual _[[spells/Catatonia|catatonia]]_. The save DC is Constitution-based.

_Gray_ Pox: _Halberd_—injury; save Fort DC 14; onset 1 day; frequency 1/day; effect 1d6 Str damage; cure 2 consecutive saves.

##### Description

A schir resembles a tall, muscular humanoid with the head and hooves of a demonic goat. A ragged hide covers patches of a schir’s body, usually around the forearms and lower legs, with a crestlike patch running down from the creature’s crown to the nape of its neck. Schir demons are 7 feet tall, though they usually stoop and so appear shorter, and weigh 300 pounds.

Also known as _[[spells/Spite|spite]]_ demons, schirs are among the most violent and vile-tempered inhabitants of the Abyss. Schirs are formed from the souls of mortals who either committed or framed others for heinous crimes—acts committed for the sole purpose of petty _[[spells/Retribution|retribution]]_. Despite such origins, schirs occupy one of the lowest orders in the demonic hierarchy, often serving as front-line infantry in demonic armies or as guards for minor demonic commanders.

Although not especially intelligent, schirs are _[[items/Weapon Magic Abilities/Cunning|cunning]]_ warriors and able sentries. Although they prefer to charge into combat, a schir’s natural jumping ability makes it a nimble enemy, capable of using its surroundings astutely. A schir will often _[[spells/Jump|jump]]_ on top of rocks, crumbling walls, or any other high place to hack with its disease-ridden _halberd_. For all of schirs’ capabilities, their spitefulness makes them distrustful of any creature that has not proven its greater power and strength numerous times.

A schir set loose upon the Material Plane quickly seeks to set itself up as a leader of its own army—often, schirs seek out tribes of savage humanoids and attempt to replace the current leaders. They are particularly fond of infiltrating _[[monsters/Gnoll|gnoll]]_ tribes.