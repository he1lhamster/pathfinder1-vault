---
cssclass: [monsters]
title1: Oni, Nogitsune
desc_short: This fox-headed humanoid has a sleek, feminine form that moves with seductive
  grace. As she steps into a defensive posture, a mass of bushy tails flicks at the
  air above her back and she reveals teeth flecked with blood.
title2: Nogitsune
CR: 7
sources:
- name: 'Pathfinder #50: Night of Frozen Shadows'
  page: 86
  link: http://paizo.com/pathfinder/v5748btpy8jrr
XP: 3200
alignment: NE
size: Medium
type: outsider
subtypes:
- kitsune
- native
- oni
- shapechanger
initiative:
  bonus: 7
senses:
  darkvision: 60
  scent: true
AC:
  AC: 21
  touch: 18
  flat_footed: 13
  components:
    dex: 7
    dodge: 1
    natural: 3
HP:
  HP: 80
  long: 7d10+42
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 8
  ref: 12
  will: 8
defensive_abilities:
- evasion
SR: 18
speeds:
  base: 50
  climb: 50
attacks:
  melee:
  - - text: bite +14 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: bite
      bonus:
      - 14
    - text: 2 claws +14 (1d4+2 plus poison)
      entries:
      - - damage: 1d4+2
        - effect: poison
      count: 2
      attack: claws
      bonus:
      - 14
  ranged:
  - - text: mwk dart +15/+10 (1d4+4 plus poison)
      entries:
      - - damage: 1d4+4
        - effect: poison
      attack: mwk dart
      bonus:
      - 15
      - 10
  special:
  - contagious whisper
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 16
  - name: feather fall
    source: default
    freq: At will
  - name: jump
    source: default
    freq: At will
  - name: obscuring mist
    source: default
    freq: At will
  - name: displacement
    source: default
    freq: 1/day
  - name: haste
    source: default
    freq: 1/day
  - name: shadow walk
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 11
ability_scores:
  STR: 18
  DEX: 25
  CON: 22
  INT: 17
  WIS: 16
  CHA: 19
BAB: 7
CMB: 11
CMD: 29
feats:
- name: Dodge
- name: Mobility
- name: Spring Attack
- name: Weapon Finesse
skills:
  Acrobatics: 17
    jump: 25
  Appraise: 5
  Bluff: 14
  Climb: 16
  Diplomacy: 7
  Disable Device: 16
  Disguise: 13
  Escape Artist: 17
  Knowledge (arcana): 5
  Knowledge (local): 6
  Perception: 13
  Sense Motive: 11
  Sleight of Hand: 10
  Stealth: 17
  Swim: 5
languages:
- Common
- Draconic
- Fey
- Giant
special_qualities:
- change shape (Small or Medium humanoid or animal, alter self or beast shape I)
- fleet distraction
- poison use
ecology:
  environment: any urban
  organization: solitary
  treasure_type: double
  treasure:
  - four masterwork darts
  - 5 doses of blue whinnis poison
  - other treasure
special_abilities:
  Contagious Whisper (Su): As a standard action, a nogitsune can influence a target
    she speaks to as per the spell suggestion. The target must succeed at a DC 17
    Will save or be affected by this effect. In addition to being subject to suggestion's
    normal effects, any creature affected by the contagious whisper can pass the enchantment
    on to other targets. Doing so requires the target to communicate the nogitsune's
    suggestion, forcing the new target to save as if it were the initial target. If
    such a secondary target resists the contagious whisper, it is unaffected, but
    this does not remove the suggestion from the initial target. Failing the save
    puts another creature under the nogitsune's compulsion. Newly affected creatures
    are also able to spread the suggestion. A nogitsune's compelling whisper can affect
    a number of creatures equal to the its Hit Dice and lasts for a number of hours
    equal to its Hit Dice. Creatures that successfully save versus the nogitsune's
    compelling whisper (as a primary or secondary target) cannot be affected by that
    particular nogitsune's compelling whisper for 24 hours. The save DC is Charisma-based.
  Fleet Distraction (Su): A nogitsune can make a Bluff check or use its obscuring
    mist spell-like ability as a swift action in any round in which it moves up to
    half its base land speed.
  Poison Use (Ex): |-
    Nogitsune are skilled in the use of poison and never risk accidentally poisoning themselves. Their aptitude is such that they often paint their weapons and nails with blue whinnis.

    Blue Whinnis: injury; save Fort DC 14; frequency 1/round for 2 rounds; initial effect 1 Con damage; secondary effect unconsciousness for 1d3 hours; cure 1 save
desc_long: |-
  Nogitsune are created when oni spirits take over the bodies of kitsune (sagacious humanoid fox-creatures). The resultant possession creates a creature with the kitsune's foxlike grace and cunning and infuses it with the destructive power of an oni (Note from Nethys: This bolded information is not entirely correct and has been further clarified here). Nogitsune are always female, and resemble shapely humans with a covering of fur and a fox's head. A nogitsune's fur color varies and can be orange and white, grey, pure white, or even black. Whenever nogitsune use their shapechanging abilities to assume a humanoid form, they still evince somewhat pointed, vulpine features. In addition, any hair on their assumed form betrays the natural coloration of their pelts. Nogitsune stand between 5 and 5-1/2 feet tall and weigh just over 100 pounds.

  More details on kitsune can be found in Pathfinder Campaign Setting: Dragon Empires Gazetteer.

---

# Oni, Nogitsune
This fox-headed humanoid has a sleek, feminine form that moves with seductive _[[spells/Grace|grace]]_. As she steps into a defensive posture, a mass of bushy tails flicks at the air above her back and she reveals teeth flecked with blood.
**Source** Pathfinder #50: Night of Frozen Shadows pg. 86
**XP** 3,200

NE Medium outsider (_[[monsters/Kitsune|kitsune]]_, native, oni, shapechanger)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +13

##### Defense

**AC** 21, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 80 (7d10+42); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +8, **Ref** +12, **Will** +8
**Defensive Abilities** evasion; **SR** 18

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** bite +14 (1d6+4), 2 claws +14 (1d4+2 plus poison)
**Ranged** mwk _[[items/Weapon/Dart|dart]]_ +15/+10 (1d4+4 plus poison)
**Special Attacks** contagious whisper, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +11)
Constant—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16)
At will—_[[spells/Feather Fall|feather fall]]_, _[[spells/Jump|jump]]_, _[[spells/Obscuring Mist|obscuring mist]]_
1/day—_[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_, _[[spells/Shadow Walk|shadow walk]]_

##### Statistics
**Str** 18, **Dex** 25, **Con** 22, **Int** 17, **Wis** 16, **Cha** 19
**Base Atk** +7; **CMB** +11; **CMD** 29
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +17 (+25 _jump_), Appraise +5, Bluff +14, _Climb_ +16, Diplomacy +7, Disable Device +16, Disguise +13, Escape Artist +17, Knowledge (arcana) +5, Knowledge (local) +6, Perception +13, Sense Motive +11, Sleight of Hand +10, Stealth +17, Swim +5
**Languages** Common, Draconic, Fey, Giant
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or _Medium_ humanoid or animal, _[[spells/Alter Self|alter self]]_ or _[[spells/Beast Shape I|beast shape I]]_), _[[feats/Fleet|fleet]]_ _[[universal monster rules/Distraction|distraction]]_, poison use

##### Ecology

**Environment** any urban
**Organization** solitary
**Treasure** double (four masterwork darts, 5 doses of _[[poisons/Blue Whinnis|blue whinnis]]_ poison, other treasure)

### Special Abilities

**Contagious Whisper (Su) **As a standard action, a nogitsune can influence a target she speaks to as per the spell _[[spells/Suggestion|suggestion]]_. The target must succeed at a DC 17 Will save or be affected by this effect. In addition to being subject to _suggestion_’s normal effects, any creature affected by the contagious whisper can pass the enchantment on to other targets. Doing so requires the target to communicate the nogitsune’s _suggestion_, forcing the new target to save as if it were the initial target. If such a secondary target resists the contagious whisper, it is unaffected, but this does not remove the _suggestion_ from the initial target. Failing the save puts another creature under the nogitsune’s compulsion. Newly affected creatures are also able to spread the _suggestion_. A nogitsune’s compelling whisper can affect a number of creatures equal to the its Hit Dice and lasts for a number of hours equal to its Hit Dice. Creatures that successfully save versus the nogitsune’s compelling whisper (as a primary or secondary target) cannot be affected by that particular nogitsune’s compelling whisper for 24 hours. The save DC is Charisma-based.

**_Fleet_ _Distraction_ (Su) **A nogitsune can make a Bluff check or use its _obscuring mist_ spell-like ability as a swift action in any round in which it moves up to half its base land speed.

**Poison Use (Ex) **Nogitsune are skilled in the use of poison and never risk accidentally _[[items/Armor Magic Abilities/Poisoning|poisoning]]_ themselves. Their aptitude is such that they often paint their weapons and nails with _blue whinnis_.

_Blue Whinnis_: injury; save Fort DC 14; frequency 1/round for 2 rounds; initial effect 1 Con damage; secondary effect unconsciousness for 1d3 hours; cure 1 save

##### Description

**Nogitsune are created when oni spirits take over the bodies of _kitsune_ (sagacious humanoid fox-creatures). The resultant _[[spells/Possession|possession]]_ creates a creature with the _kitsune_’s foxlike _grace_ and _[[items/Weapon Magic Abilities/Cunning|cunning]]_ and infuses it with the destructive power of an oni** (Note from Nethys: This bolded information is not entirely correct and has been further clarified here). Nogitsune are always female, and resemble shapely humans with a covering of fur and a fox’s head. A nogitsune’s fur color varies and can be orange and white, grey, pure white, or even black. Whenever nogitsune use their shapechanging abilities to assume a humanoid form, they still evince somewhat pointed, vulpine features. In addition, any hair on their assumed form betrays the natural coloration of their pelts. Nogitsune stand between 5 and 5-1/2 feet tall and weigh just over 100 pounds.

More details on _kitsune_ can be found in Pathfinder Campaign Setting: Dragon Empires Gazetteer.