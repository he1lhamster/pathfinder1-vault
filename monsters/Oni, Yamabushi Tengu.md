---
cssclass: [monsters]
title1: Oni, Yamabushi Tengu
desc_short: This humanoid creature has a fearsome mien, with a cruel red face, glaring
  yellow eyes, a prodigious nose, and large ravenlike wings.
title2: Yamabushi Tengu
CR: 5
sources:
- name: 'Pathfinder #49: The Brinewall Legacy'
  page: 88
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/jadeRegent/v5748btpy8mfv
XP: 1600
alignment: LE
size: Medium
type: outsider
subtypes:
- native
- oni
- shapechanger
- tengu
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    armor: 2
    dex: 4
    natural: 2
HP:
  HP: 57
  long: 6d10+24
  regeneration: 2
  regeneration_weakness: fire or acid
saves:
  fort: 9
  ref: 9
  will: 4
  other: -2 vs. illusion (pattern) spells
SR: 16
weaknesses:
- susceptible to patterns
speeds:
  base: 30
  fly: 30
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 kusarigama +10/+5 (1d6+4/×3)
      entries:
      - - damage: 1d6+4
          crit_multiplier: 3
      attack: +1 kusarigama
      bonus:
      - 10
      - 5
    - text: bite +3 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 3
  ranged:
  - - text: composite longbow +10/+5 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: composite longbow
      bonus:
      - 10
      - 5
  special:
  - steal voice
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: ventriloquism
    source: default
    freq: Constant
    DC: 14
  - name: dimension door
    source: default
    freq: 3/day
  - name: hideous laughter
    source: default
    freq: 3/day
    DC: 15
  - name: ray of enfeeblement
    source: default
    freq: 3/day
    DC: 14
  - name: scorching ray
    source: default
    freq: 3/day
  - name: blur
    source: default
    freq: 1/day
  - name: glitterdust
    source: default
    freq: 1/day
    DC: 15
  sources:
  - name: default
    CL: 5
    concentration: 8
ability_scores:
  STR: 15
  DEX: 19
  CON: 18
  INT: 12
  WIS: 15
  CHA: 16
BAB: 6
CMB: 8
CMD: 22
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Improved Initiative
skills:
  Acrobatics: 13
  Bluff: 12
  Disguise: 12
  Fly: 13
  Knowledge (planes): 10
  Perception: 15
  Stealth: 13
  _racial_mods:
    Perception:
      _: 4
languages:
- Common
- Tengu
- Tien
special_qualities:
- change shape (Medium humanoid, alter self )
- yamabushi weapons
gear:
  gear:
  - leather armor
ecology:
  environment: temperate mountains
  organization: solitary, pair, or patrol (1-2 plus 3-8 tengus or dire corbies)
  treasure_type: double
  treasure:
  - leather armor
  - +1 kusarigama
  - composite longbow [+2 Str] with 20 arrows
  - other treasure
special_abilities:
  Yamabushi Weapons (Ex): A yamabushi tengu is proficient with all monk weapons and
    all swordlike weapons (including katanas and wakizashi), and gains a +1 bonus
    on attack rolls and damage rolls with such weapons. Yamabushi tengus who do not
    use swords favor the kusarigama.
  Steal Voice (Su): Up to three times per day, but no more than once per target, a
    yamabushi tengu can attempt to steal a victim's voice as part of its bite attack.
    When it does so, the creature bitten must make a DC 16 Will save or lose the ability
    to speak aloud. This prevents the use of any spell with verbal components and
    the use of command-word- activated magic items, among other difficulties. The
    yamabushi tengu's voice changes to match the one stolen. The victim's voice remains
    stolen until the oni steals another voice, until the oni agrees to give the stolen
    voice back (a standard action requiring the oni to touch the victim), or until
    the next sunrise. Any effect that removes curses (such as remove curse or break
    enchantment) can restore a stolen voice (DC for success equals the save DC of
    the steal voice ability-DC 16 for most yamabushi tengu), as does the death of
    the oni who stole the voice in the first place. The save DC is Charisma-based.
  Susceptible to Patterns (Ex): A yamabushi tengu takes a -2 penalty on all saving
    throws against illusion spells of the pattern subschool. For 1 round after a yamabushi
    tengu either makes a successful save against a pattern or recovers from the effects
    of a pattern, it is dazzled.
desc_long: |-
  Yamabushi tengus are oni with a predilection toward thievery and trickery, wearing the flesh of wicked, fiendish tengus. When a yamabushi tengu first appears, its first course of action is invariably to seek out a well-hidden nest or other nook to serve as a lair. Despite their ability to fly, most yamabushi tengus are nervous in open areas, since it's easy to be seen in such environs. A yamabushi tengu is more at home indoors or at night, where it can skulk in the shadows when it's unsure of its surroundings.

  A yamabushi tengu is 5 feet tall and weighs 120 pounds.

---

# Oni, Yamabushi Tengu
This humanoid creature has a fearsome mien, with a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ red face, glaring yellow eyes, a prodigious nose, and large ravenlike wings.
**Source** Pathfinder #49: The Brinewall Legacy pg. 88
**XP** 1,600

LE Medium outsider (native, oni, shapechanger, _[[monsters/Tengu|tengu]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +15

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 armor, +4 Dex, +2 natural)
**hp** 57 (6d10+24); _[[universal monster rules/Regeneration|regeneration]]_ 2 (fire or acid)
**Fort** +9, **Ref** +9, **Will** +4; –2 vs. illusion (pattern) spells
**SR** 16
**Weaknesses** susceptible to patterns

##### Offense
**Speed** 30 ft., fly 30 ft. (average)
**Melee** +1 _[[items/Weapon/Kusarigama|kusarigama]]_ +10/+5 (1d6+4/×3), bite +3 (1d4+1)
**Ranged** _[[items/Weapon/Composite longbow|composite longbow]]_ +10/+5 (1d8+2/×3)
**Special Attacks** _[[spells/Steal Voice|steal voice]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
Constant—_see invisibility_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
3/day—_[[spells/Dimension Door|dimension door]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 15), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Scorching Ray|scorching ray]]_
1/day—_[[spells/Blur|blur]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 15)

##### Statistics
**Str** 15, **Dex** 19, **Con** 18, **Int** 12, **Wis** 15, **Cha** 16
**Base Atk** +6; **CMB** +8; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Acrobatics +13, Bluff +12, Disguise +12, Fly +13, Knowledge (planes) +10, Perception +15, Stealth +13; **Racial Modifiers** +4 Perception
**Languages** Common, _Tengu_, Tien
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_Medium_ humanoid, _[[spells/Alter Self|alter self]]_ ), yamabushi weapons
**Gear** _[[items/Armor/Leather armor|leather armor]]_

##### Ecology

**Environment** temperate mountains
**Organization** solitary, pair, or patrol (1–2 plus 3–8 tengus or dire corbies)
**Treasure** double (_leather armor_, +1 _kusarigama_, _composite longbow_ [+2 Str] with 20 arrows, other treasure)

### Special Abilities

**Yamabushi Weapons (Ex) **A yamabushi _tengu_ is proficient with all _[[classes/Monk|monk]]_ weapons and all swordlike weapons (including katanas and _[[items/Weapon/Wakizashi|wakizashi]]_), and gains a +1 bonus on attack rolls and damage rolls with such weapons. Yamabushi tengus who do not use swords favor the _kusarigama_.
**_Steal Voice_ (Su) **Up to three times per day, but no more than once per target, a yamabushi _tengu_ can attempt to steal a victim’s voice as part of its bite attack. When it does so, the creature bitten must make a DC 16 Will save or lose the ability to speak aloud. This prevents the use of any spell with verbal components and the use of command-word- activated magic items, among other difficulties. The yamabushi _tengu_’s voice changes to match the one stolen. The victim’s voice remains stolen until the oni steals another voice, until the oni agrees to give the stolen voice back (a standard action requiring the oni to touch the victim), or until the next sunrise. Any effect that removes curses (such as _[[spells/Remove Curse|remove curse]]_ or _[[spells/Break Enchantment|break enchantment]]_) can restore a stolen voice (DC for success equals the save DC of the _steal voice_ ability—DC 16 for most yamabushi _tengu_), as does the death of the oni who stole the voice in the first place. The save DC is Charisma-based.
**Susceptible to Patterns (Ex) **A yamabushi _tengu_ takes a –2 penalty on all saving throws against illusion spells of the pattern subschool. For 1 round after a yamabushi _tengu_ either makes a successful save against a pattern or recovers from the effects of a pattern, it is _[[conditions/Dazzled|dazzled]]_.

##### Description

Yamabushi tengus are oni with a predilection toward thievery and trickery, wearing the flesh of wicked, fiendish tengus. When a yamabushi _tengu_ first appears, its first course of action is invariably to seek out a well-hidden nest or other nook to serve as a lair. Despite their ability to fly, most yamabushi tengus are nervous in open areas, since it’s easy to be seen in such environs. A yamabushi _tengu_ is more at home indoors or at night, where it can _[[monsters/Skulk|skulk]]_ in the shadows when it’s unsure of its surroundings.

A yamabushi _tengu_ is 5 feet tall and weighs 120 pounds.