---
cssclass: [monsters]
title1: Saumen Kar
desc_short: This hulking humanoid's dense fur is scored with rune-shaped brands. Skin
  cracked and blackened by frostbite stretches taught over a misshapen skull crowned
  with a pair of ivory horns.
title2: Saumen Kar
CR: 10
sources:
- name: 'Pathfinder #51: The Hungry Storm'
  page: 90
  link: http://paizo.com/pathfinder/v5748btpy8kgv
XP: 9600
alignment: CN
size: Large
type: monstrous humanoid
initiative:
  bonus: 2
senses:
  darkvision: 60
  scent: true
AC:
  AC: 24
  touch: 11
  flat_footed: 22
  components:
    deflection: 4
    dex: 2
    natural: 9
    size: -1
HP:
  HP: 136
  long: 13d10+65
saves:
  fort: 11
  ref: 10
  will: 9
defensive_abilities:
- frostbite brands
immunities:
- cold
resistances:
  fire: 20
speeds:
  base: 40
attacks:
  melee:
  - - text: greataxe +21/+16/+11 (2d6+12/19-20 plus 1d6 cold)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
        - damage: 1d6
          type: cold
      attack: greataxe
      bonus:
      - 21
      - 16
      - 11
    - text: headbutt +15 (1d6+4 plus stun)
      entries:
      - - damage: 1d6+4
        - effect: stun
      attack: headbutt
      bonus:
      - 15
  special:
  - snowstorm (2d6 cold plus 2d6 slashing damage, DC 24)
  - stun (1 round, DC 24)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: wall of ice
    source: default
    freq: 3/day
    DC: 14
  - name: summon nature's ally VI
    source: default
    freq: 1/day
    other: polar bear [dire bear] only
  sources:
  - name: default
    CL: 13
    concentration: 13
ability_scores:
  STR: 26
  DEX: 15
  CON: 20
  INT: 11
  WIS: 12
  CHA: 11
BAB: 13
CMB: 22
CMD: 38
feats:
- name: Alertness
- name: Diehard
- name: Endurance
- name: Great Fortitude
- name: Improved Critical (greataxe)
- name: Self-Sufficient
- name: Weapon Focus (greataxe)
skills:
  Heal: 3
  Knowledge (nature): 13
  Perception: 21
  Sense Motive: 3
  Stealth: 14
    in ice and snow: 18
  Survival: 21
  _racial_mods:
    Stealth:
      in ice and snow: 4
languages:
- Giant
ecology:
  environment: cold plains, hills, or desert
  organization: solitary or family (2-5)
  treasure:
  - greataxe
special_abilities:
  Frostbite Brands (Ex): A saumen kar's brands infuse the creature with intense cold,
    so much that it gains resistance to fire 20 and its touch deals an additional
    1d6 points of cold damage. A saumen kar's metallic weapons also conduct this chill.
    A saumen kar's brands can be removed by the spell erase as though they were magic
    writing with a caster level equal to the saumen kar's Hit Dice. If the brands
    are removed, the saumen kar loses both its fire resistance and its ability to
    do additional cold damage, until the following dawn when the brands re-etch themselves
    upon its body.
  Snowstorm (Su): 'In mimicry of its unforgiving environment, a saumen kar can transform
    into a living snowstorm of lethal power. This ability lasts as long and operates
    like the whirlwind special attack with the following changes: Creatures within
    the area of the snowstorm take 2d6 points of cold damage and 2d6 points of slashing
    damage and take a -20 penalty on Perception checks. A saumen kar gains a fly speed
    of 40 feet (perfect) while in this form.'
  Stun (Ex): While a saumen kar's horns are not large enough for a gore attack, they
    extend under the skin to form a bony plate. A creature struck by a saumen kar's
    headbutt must succeed at a DC 24 Fortitude saving throw or be stunned for 1 round.
desc_long: This leathery-faced creature stands tall and upright, with long, simian
  limbs and a shaggy coat. Intelligent and powerful, saumen kars are not naturally
  aggressive, but the hostility of their environment forces them to defend the land
  that supports them with ferocity, even to the death. Their natural coloration and
  snow-packed fur make saumen kars almost invisible among the drifts of their icy
  homes, leading many arctic races to refer to them as “men of snow.” A longforgotten
  deal made by their race in its infancy still brutally scars the body of each saumen
  kar, marking them with their distinctive frostbite brands-though if this debt is
  already paid, lapsed, or growing ever greater, none can remember. An adult saumen
  kar stands 12 feet tall and weighs almost 2,000 pounds, but the ice and snow matted
  to its fur for both insulation and armor add another 1,000 pounds to its bulk.

---

# Saumen Kar
This hulking humanoid’s dense fur is scored with rune-shaped brands. Skin cracked and blackened by _[[spells/Frostbite|frostbite]]_ stretches taught over a misshapen skull crowned with a pair of ivory horns.
**Source** Pathfinder #51: The Hungry Storm pg. 90
**XP** 9,600

CN Large monstrous humanoid
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +21

##### Defense

**AC** 24, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+4 deflection, +2 Dex, +9 natural, –1 size)
**hp** 136 (13d10+65)
**Fort** +11, **Ref** +10, **Will** +9
**Defensive Abilities** _frostbite_ brands; **Immune** cold; **Resist** fire 20

##### Offense
**Speed** 40 ft.
**Melee** _[[items/Weapon/Greataxe|greataxe]]_ +21/+16/+11 (2d6+12/19–20 plus 1d6 cold), headbutt +15 (1d6+4 plus stun)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** snowstorm (2d6 cold plus 2d6 slashing damage, DC 24), stun (1 round, DC 24)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +13)
3/day—_[[spells/Wall Of Ice|wall of ice]]_ (DC 14)
1/day—_[[universal monster rules/Summon|summon]]_ nature’s ally VI (polar bear [dire bear] only)

##### Statistics
**Str** 26, **Dex** 15, **Con** 20, **Int** 11, **Wis** 12, **Cha** 11
**Base Atk** +13; **CMB** +22; **CMD** 38
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greataxe_), _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greataxe_)
**Skills** _[[spells/Heal|Heal]]_ +3, Knowledge (nature) +13, Perception +21, Sense Motive +3, Stealth +14 (+18 in ice and snow), Survival +21; **Racial Modifiers** +4 Stealth in ice and snow
**Languages** Giant

##### Ecology

**Environment** cold plains, hills, or desert
**Organization** solitary or family (2–5)
**Treasure** _greataxe_

### Special Abilities

**_Frostbite_ Brands (Ex) **A _[[monsters/Saumen Kar|saumen kar]]_’s brands infuse the creature with intense cold, so much that it gains _[[universal monster rules/Resistance|resistance]]_ to fire 20 and its touch deals an additional 1d6 points of cold damage. A _saumen kar_’s metallic weapons also conduct this chill. A _saumen kar_’s brands can be removed by the spell _[[spells/Erase|erase]]_ as though they were magic writing with a caster level equal to the _saumen kar_’s Hit Dice. If the brands are removed, the _saumen kar_ loses both its fire _resistance_ and its ability to do additional cold damage, until the following dawn when the brands re-etch themselves upon its body.
**Snowstorm (Su) **In mimicry of its unforgiving environment, a _saumen kar_ can transform into a living snowstorm of lethal power. This ability lasts as long and operates like the _[[universal monster rules/Whirlwind|whirlwind]]_ special attack with the following changes: Creatures within the area of the snowstorm take 2d6 points of cold damage and 2d6 points of slashing damage and take a –20 penalty on Perception checks. A _saumen kar_ gains a fly speed of 40 feet (perfect) while in this form.
**Stun (Ex) **While a _saumen kar_’s horns are not large enough for a gore attack, they extend under the skin to form a bony plate. A creature struck by a _saumen kar_’s headbutt must succeed at a DC 24 Fortitude saving throw or be _[[conditions/Stunned|stunned]]_ for 1 round.

##### Description

This leathery-faced creature stands tall and upright, with long, simian limbs and a shaggy coat. Intelligent and powerful, saumen kars are not naturally aggressive, but the hostility of their environment forces them to defend the land that supports them with _[[universal monster rules/Ferocity|ferocity]]_, even to the death. Their natural coloration and snow-packed fur make saumen kars almost _[[conditions/Invisible|invisible]]_ among the drifts of their icy homes, leading many arctic races to refer to them as “men of snow.” A longforgotten deal made by their race in its infancy still brutally scars the body of each _saumen kar_, marking them with their distinctive _frostbite_ brands—though if this debt is already paid, lapsed, or _[[items/Weapon Magic Abilities/Growing|growing]]_ ever greater, none can remember. An adult _saumen kar_ stands 12 feet tall and weighs almost 2,000 pounds, but the ice and snow matted to its fur for both insulation and armor add another 1,000 pounds to its bulk.