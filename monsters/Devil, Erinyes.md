---
cssclass: [monsters]
title1: Devil, Erinyes
desc_short: Some calamity has befallen this angelic warrior. Wings stained black shear
  the air as her merciless eyes search for a target.
title2: Erinyes
CR: 8
sources:
- name: Pathfinder RPG Bestiary
  page: 75
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 4800
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 6
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
AC:
  AC: 23
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    dodge: 1
    natural: 6
HP:
  HP: 94
  long: 9d10+45
saves:
  fort: 11
  ref: 12
  will: 7
DR:
- amount: 5
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 19
speeds:
  base: 30
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 longsword +15/+10 (1d8+8/19-20)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 15
      - 10
  ranged:
  - - text: +1 flaming composite longbow +14/+14/+9 (1d8+6/×3 plus 1d6 fire)
      entries:
      - - damage: 1d8+6
          crit_multiplier: 3
        - damage: 1d6
          type: fire
      attack: +1 flaming composite longbow
      bonus:
      - 14
      - 14
      - 9
  - - text: rope +15 touch (entangle)
      entries:
      - - effect: entangle
      attack: rope
      bonus:
      - 15
      touch: true
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: fear
    source: default
    freq: At will
    other: single target
    DC: 19
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: minor image
    source: default
    freq: At will
    DC: 17
  - name: unholy blight
    source: default
    freq: At will
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: bearded devils
      amount: 2
      chance: 50%
  sources:
  - name: default
    CL: 12
ability_scores:
  STR: 20
  DEX: 23
  CON: 21
  INT: 14
  WIS: 18
  CHA: 21
BAB: 9
CMB: 14
CMD: 31
feats:
- name: Combat Reflexes
- is_bonus: true
  name: Dodge
- is_bonus: true
  name: Mobility
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Shot on the Run
skills:
  Acrobatics: 18
  Bluff: 17
  Diplomacy: 14
  Escape Artist: 12
  Fly: 19
  Intimidate: 17
  Knowledge (planes): 8
  Knowledge (religion): 8
  Perception: 16
  Sense Motive: 10
  Stealth: 15
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary or trio
  treasure_type: triple
  treasure:
  - +1 longsword
  - +1 flaming composite longbow [+5 Str bonus]
  - rope
special_abilities:
  Entangle (Su): Each erinyes carries a 50-foot-long rope that entangles opponents
    of any size as an animate rope spell (CL 16th, DC 20). An erinyes can hurl its
    rope 30 feet with no range penalty. An erinyes's rope functions only for the erinyes
    who made it and no other. The save DC is Dexterity-based.
desc_long: |-
  Known by many names-the Fallen, the Ash Wings, and the Furies-the devils called erinyes mock the form of the angelic hosts in their exaction of vengeance and bloody justice. Executioners, not judges, erinyes alight upon the bladed eaves of Dis, Hell's cosmopolitan second layer, ever attentive for chances to soar into battle, whether in defense of Hell, on the whims of diabolical masters, or at the impassioned summons of jilted mortal summoners. All erinyes weave deadly living ropes from their own hair, which they use in battle to lift their foes into the air, mocking and condemning their victims for their transgressions before dropping them from great heights.

  Erinyes appear as darkly beautiful angels, augmenting their sensuality with deliberate bruises and scars. Yet despite their beauty, erinyes are not seducers-they lack the subtlety and patience required for such fine emotional manipulations, and instead vastly prefer to solve their problems with swift and excruciating violence. Often, an erinyes will stay her hand before attempting to slay a foe simply so she can draw out the victim's suffering. Death is usually the only way to escape an erinyes's not-so-tender attentions, and the most powerful of these devils excel at keeping their enemies alive but helpless so as to extend their torment-many going as far as to keep their victims alive with magic. Rumors hold that the most powerful erinyes torturers have skills that allow their torment to continue even after their subject has died from their attentions.

  Most erinyes stand just under 6 feet tall and weigh approximately 140 pounds, even with their black- feathered wings that stretch over 10 feet wide.

---

# Devil, Erinyes
Some calamity has befallen this angelic warrior. Wings stained black shear the air as her merciless eyes search for a target.
**Source** Pathfinder RPG Bestiary pg. 75
**XP** 4,800

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +16

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 94 (9d10+45)
**Fort** +11, **Ref** +12, **Will** +7
**DR** 5/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 50 ft. (good)
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +15/+10 (1d8+8/19–20)
**Ranged** +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Composite longbow|composite longbow]]_ +14/+14/+9 (1d8+6/×3 plus 1d6 fire) or rope +15 touch (_[[spells/Entangle|entangle]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
Constant—_true seeing_
At will—_[[universal monster rules/Fear|fear]]_ (single target, DC 19), greater teleport (self plus 50 lbs. of objects only), _[[spells/Minor Image|minor image]]_ (DC 17), _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
1/day—_[[universal monster rules/Summon|summon]]_ (level 3, 2 bearded devils, 50%)

##### Statistics
**Str** 20, **Dex** 23, **Con** 21, **Int** 14, **Wis** 18, **Cha** 21
**Base Atk** +9; **CMB** +14; **CMD** 31
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_
**Skills** Acrobatics +18, Bluff +17, Diplomacy +14, Escape Artist +12, Fly +19, Intimidate +17, Knowledge (planes) +8, Knowledge (religion) +8, Perception +16, Sense Motive +10, Stealth +15
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary or trio
**Treasure** triple (+1 _longsword_, +1 _flaming_ _composite longbow_ [+5 Str bonus], rope)

### Special Abilities

**_Entangle_ (Su)** Each erinyes carries a 50-foot-long rope that entangles opponents of any size as an _[[spells/Animate Rope|animate rope]]_ spell (CL 16th, DC 20). An erinyes can hurl its rope 30 feet with no range penalty. An erinyes’s rope functions only for the erinyes who made it and no other. The save DC is Dexterity-based.

##### Description

Known by many names—the _[[monsters/Fallen|Fallen]]_, the Ash Wings, and the Furies—the devils _[[items/Weapon Magic Abilities/Called|called]]_ erinyes mock the form of the angelic hosts in their exaction of _[[feats/Vengeance|vengeance]]_ and bloody justice. Executioners, not judges, erinyes alight upon the bladed eaves of Dis, Hell’s _[[feats/Cosmopolitan|cosmopolitan]]_ second layer, ever attentive for chances to soar into battle, whether in defense of Hell, on the whims of diabolical masters, or at the impassioned summons of jilted mortal summoners. All erinyes weave _[[items/Weapon Magic Abilities/Deadly|deadly]]_ living ropes from their own hair, which they use in battle to lift their foes into the air, mocking and condemning their victims for their transgressions before dropping them from great heights.

Erinyes appear as darkly beautiful angels, augmenting their sensuality with deliberate bruises and scars. Yet despite their beauty, erinyes are not seducers—they lack the subtlety and patience required for such fine emotional manipulations, and instead vastly prefer to solve their problems with swift and excruciating violence. Often, an erinyes will stay her hand before attempting to slay a foe simply so she can draw out the victim’s suffering. Death is usually the only way to escape an erinyes’s not-so-tender attentions, and the most powerful of these devils excel at keeping their enemies alive but _[[conditions/Helpless|helpless]]_ so as to extend their torment—many going as far as to keep their victims alive with magic. Rumors hold that the most powerful erinyes torturers have skills that allow their torment to continue even after their subject has died from their attentions.

Most erinyes stand just under 6 feet tall and weigh approximately 140 pounds, even with their black- feathered wings that stretch over 10 feet wide.