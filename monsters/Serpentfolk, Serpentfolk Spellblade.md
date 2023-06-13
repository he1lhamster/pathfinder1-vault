---
cssclass: [monsters]
title1: Serpentfolk, Serpentfolk Spellblade
title2: Serpentfolk Spellblade
CR: 13
sources:
- name: Monster Codex
  page: 206
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 25600
race: Advanced
classes:
- serpentfolk magus 9 (Pathfinder RPG Ultimate Magic 9)
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 26
  touch: 15
  flat_footed: 22
  components:
    armor: 7
    deflection: 1
    dex: 3
    dodge: 1
    natural: 4
HP:
  HP: 160
  long: 5d10+9d8+93
  HD: 14
saves:
  fort: 15
  ref: 14
  will: 12
immunities:
- mind-affecting effects
- paralysis
- poison
SR: 24
speeds:
  base: 20
attacks:
  melee:
  - - text: +2 corrosive scimitar +17/+12/+7 (1d6+5/15-20 plus 1d6 acid)
      entries:
      - - damage: 1d6+5
          crit_range: 15-20
        - damage: 1d6
          type: acid
      attack: +2 corrosive scimitar
      bonus:
      - 17
      - 12
      - 7
    - text: bite +9 (1d6+1 plus poison)
      entries:
      - - damage: 1d6+1
        - effect: poison
      attack: bite
      bonus:
      - 9
  ranged:
  - - text: mwk composite longbow +19/+14/+9 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 19
      - 14
      - 9
  special:
  - improved spell combat
  - spell combat (-2 attack, +2 concentration)
  - spellstrike
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
    DC: 14
    other: humanoid form only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 14
  - name: blur
    source: default
    freq: 1/day
  - name: dominate person
    source: default
    freq: 1/day
    DC: 18
  - name: major image
    source: default
    freq: 1/day
    DC: 16
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 19
  - name: mirror image
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 16
  - name: teleport
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 7
spells:
  entries:
  - name: dispel magic
    source: Magus
    level: 3
  - name: displacement
    source: Magus
    level: 3
  - name: vampiric touch
    source: Magus
    level: 3
    count: 2
  - name: acid arrow
    source: Magus
    level: 2
  - superscripts:
    - UM
    name: defensive shock
    source: Magus
    level: 2
  - superscripts:
    - UM
    name: frigid touch
    source: Magus
    level: 2
  - name: invisibility
    source: Magus
    level: 2
  - name: web
    source: Magus
    level: 2
    DC: 17
  - name: burning hands
    source: Magus
    level: 1
    DC: 16
  - name: chill touch
    source: Magus
    level: 1
    DC: 16
  - superscripts:
    - UM
    name: corrosive touch
    source: Magus
    level: 1
  - name: magic missile
    source: Magus
    level: 1
  - name: ray of enfeeblement
    source: Magus
    level: 1
    DC: 16
  - name: shocking grasp
    source: Magus
    level: 1
  - name: arcane mark
    source: Magus
    level: 0
  - name: detect magic
    source: Magus
    level: 0
  - name: mage hand
    source: Magus
    level: 0
  - name: prestidigitation
    source: Magus
    level: 0
    DC: 15
  - name: read magic
    source: Magus
    level: 0
  sources:
  - name: Magus
    type: prepared
    CL: 9
    concentration: 14
    slots:
      0: at-will
tactics:
  Before Combat: A spellblade casts defensive shock if it expects battle, often following
    with displacement and invisibility to pursue a chosen target more freely.
  During Combat: A spellblade combines arcane power and mental mastery with the deadly,
    sinuous grace of the blade. It uses its hasted assault ability whenever possible,
    and uses spell combat and spellstrike whenever it has appropriate spells available.
    It prefers to weaken opponents with poisoned bites and spells like chill touch,
    ray of enfeeblement, and vampiric touch.
ability_scores:
  STR: 16
  DEX: 23
  CON: 21
  INT: 20
  WIS: 13
  CHA: 16
BAB: 11
CMB: 14
CMD: 32
feats:
- name: Combat Expertise
- name: Craft Magic Arms and Armor
- name: Dodge
- name: Great Fortitude
- name: Improved Critical (scimitar)
- name: Improved Initiative
- name: Toughness
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 10
    when jumping: 6
  Climb: 10
  Craft (alchemy): 13
  Disguise: 9
  Escape Artist: 19
  Intimidate: 15
  Knowledge (arcana): 18
  Knowledge (dungeoneering): 12
  Knowledge (history): 8
  Knowledge (nobility): 6
  Perception: 18
  Sense Motive: 8
  Spellcraft: 16
  Stealth: 15
  Survival: 8
  Swim: 4
  Use Magic Device: 15
  _racial_mods:
    Escape Artist:
      _: 8
    Use Magic Device:
      _: 4
languages:
- Aklo
- Common
- Draconic
- Undercommon
- telepathy 100 ft.
special_qualities:
- arcane pool (9 points, +3)
- knowledge pool
- magus arcana (hasted assault, pool strike +4d6, spell shield)
- medium armor proficiency
- spell recall
gear:
  combat:
  - potions of cure serious wounds (2)
  - scroll of force hook charge
  - scroll of gaseous form
  - scroll of greater invisibility
  - scroll of protection from energy
  - acid (4)
  other:
  - +2 glamered scale mail
  - +2 corrosive scimitar
  - mwk composite longbow with 20 +1 arrows
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - ring of protection +1
  - spellbook
  - 449 gp
ecology:
  environment: any land (usually jungles or underground)
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 2 saves. The save DC is Constitution-based.
desc_long: Spellblades mix the brute power of degenerate serpentfolk with the skill
  and magic of purecastes. An enigma even among their own kind, spellblades are respected
  by all.

---

# Serpentfolk, Serpentfolk Spellblade

**Source** Monster Codex pg. 206
**XP** 25,600
Advanced _[[monsters/Serpentfolk|serpentfolk]]_ _[[classes/Magus|magus]]_ 9 (Pathfinder RPG Ultimate Magic 9)

NE Medium monstrous humanoid
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +18

##### Defense

**AC** 26, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 160 (14 HD; 5d10+9d8+93)
**Fort** +15, **Ref** +14, **Will** +12
**Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison; **SR** 24

##### Offense
**Speed** 20 ft.
**Melee** +2 _[[items/Weapon Magic Abilities/Corrosive|corrosive]]_ _[[items/Weapon/Scimitar|scimitar]]_ +17/+12/+7 (1d6+5/15–20 plus 1d6 acid), bite +9 (1d6+1 plus poison)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +19/+14/+9 (1d8+4/×3)
**Special Attacks** improved spell combat, spell combat (–2 attack, +2 concentration), spellstrike
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +7)
At will—_[[spells/Disguise Self|disguise self]]_ (DC 14, humanoid form only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
1/day—_[[spells/Blur|blur]]_, _[[spells/Dominate Person|dominate person]]_ (DC 18), _[[spells/Major Image|major image]]_ (DC 16), mass _[[spells/Suggestion|suggestion]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_, _suggestion_ (DC 16), teleport
**_Magus_ Spells Prepared **(CL 9th; concentration +14)
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Vampiric Touch|vampiric touch]]_ (2)
2nd—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Defensive Shock|defensive shock]]_, _[[spells/Frigid Touch|frigid touch]]_, _[[spells/Invisibility|invisibility]]_, web (DC 17)
1st—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Chill Touch|chill touch]]_ (DC 16), _[[spells/Corrosive Touch|corrosive touch]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_ (DC 15), _[[spells/Read Magic|read magic]]_

### Tactics

**Before Combat** A spellblade casts _defensive shock_ if it expects battle, often following with _displacement_ and _invisibility_ to pursue a chosen target more freely.
 **During Combat** A spellblade combines arcane power and mental mastery with the _[[items/Weapon Magic Abilities/Deadly|deadly]]_, sinuous _[[spells/Grace|grace]]_ of the blade. It uses its hasted assault ability whenever possible, and uses spell combat and spellstrike whenever it has appropriate spells available. It prefers to weaken opponents with poisoned bites and spells like _chill touch_, _ray of enfeeblement_, and _vampiric touch_.

##### Statistics
**Str** 16, **Dex** 23, **Con** 21, **Int** 20, **Wis** 13, **Cha** 16
**Base Atk** +11; **CMB** +14; **CMD** 32
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scimitar_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +10 (+6 when jumping), _[[universal monster rules/Climb|Climb]]_ +10, Craft (alchemy) +13, Disguise +9, Escape Artist +19, Intimidate +15, Knowledge (arcana) +18, Knowledge (dungeoneering) +12, Knowledge (history) +8, Knowledge (nobility) +6, Perception +18, Sense Motive +8, Spellcraft +16, Stealth +15, Survival +8, Swim +4, Use Magic Device +15; **Racial Modifiers** +8 Escape Artist, +4 Use Magic Device
**Languages** Aklo, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** arcane pool (9 points, +3), knowledge pool, _magus_ arcana (hasted assault, pool strike +4d6, spell _[[spells/Shield|shield]]_), _[[feats/Medium Armor Proficiency|medium armor proficiency]]_, spell recall
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scroll of _[[spells/Force Hook Charge|force hook charge]]_, scroll of _[[spells/Gaseous Form|gaseous form]]_, scroll of greater _invisibility_, scroll of _[[spells/Protection from Energy|protection from energy]]_, acid (4); **Other Gear** +2 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Armor/Scale mail|scale mail]]_, +2 _corrosive_ _scimitar_, mwk _composite longbow_ with 20 +1 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 449 gp

##### Ecology

**Environment** any land (usually jungles or underground)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Str; cure 2 saves. The save DC is Constitution-based.

##### Description

Spellblades mix the brute power of degenerate _serpentfolk_ with the skill and magic of purecastes. An enigma even among their own kind, spellblades are respected by all.