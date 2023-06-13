---
cssclass: [monsters]
title1: Vampire, Vampire Seducer
title2: Vampire Seducer
CR: 6
sources:
- name: Monster Codex
  page: 239
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Human
classes:
- vampire bard 5
alignment: NE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    armor: 4
    dex: 4
    dodge: 1
    natural: 6
HP:
  HP: 61
  long: 5d8+35
  fast_healing: 5
saves:
  fort: 7
  ref: 10
  will: 5
  other: +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: magic and silver
immunities:
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- vampire weaknesses
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +7 (1d4+4 plus energy drain)
      entries:
      - - damage: 1d4+4
        - effect: energy drain
      attack: slam
      bonus:
      - 7
  special:
  - bardic performance 24 rounds/day (countersong, distraction, fascinate [DC 18],
    inspire competence +2, inspire courage +2)
  - blood drain
  - children of the night
  - create spawn
  - dominate (DC 18)
  - energy drain (2 levels, DC 18)
spells:
  entries:
  - name: darkness
    source: Bard
    level: 2
  - name: enthrall
    source: Bard
    level: 2
    DC: 20
  - superscripts:
    - UM
    name: share memory
    source: Bard
    level: 2
    DC: 18
  - name: charm person
    source: Bard
    level: 1
    DC: 19
  - superscripts:
    - UM
    name: ear-piercing scream
    source: Bard
    level: 1
  - name: lesser confusion
    source: Bard
    level: 1
    DC: 19
  - superscripts:
    - APG
    name: memory lapse
    source: Bard
    level: 1
    DC: 19
  - name: daze
    source: Bard
    level: 0
    DC: 18
  - name: detect magic
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: open/close
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
    DC: 16
  - superscripts:
    - APG
    name: unwitting ally
    source: Bard
    level: 0
    DC: 18
  sources:
  - name: Bard
    type: known
    CL: 5
    concentration: 11
    slots:
      2: 4
      1: 6
      0: at-will
tactics:
  During Combat: The vampire seducer uses her dominate ability to make others defend
    her, calls for assistance using her children of the night ability, and attacks
    with her slams. She uses her necklace of fireballs when she can target multiple
    opponents.
ability_scores:
  STR: 18
  DEX: 18
  CON:
  INT: 15
  WIS: 12
  CHA: 22
BAB: 3
CMB: 7
CMD: 22
feats:
- is_bonus: true
  name: Alertness
- name: Combat Casting
- is_bonus: true
  name: Dodge
- name: Extra Performance
- name: Greater Spell Focus (enchantment)
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
- name: Spell Focus (enchantment)
- is_bonus: true
  name: Toughness
skills:
  Bluff: 22
  Diplomacy: 14
  Intimidate: 14
  Knowledge (local): 12
  Knowledge (nobility): 12
  Perception: 19
  Perform (act): 14
  Perform (dance): 14
  Sense Motive: 19
  Stealth: 19
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- Dwarven
- Elven
special_qualities:
- bardic knowledge +2
- change shape (dire bat or wolf, beast shape II)
- gaseous form
- lore master 1/day
- shadowless
- spider climb
- versatile performance (dance)
gear:
  combat:
  - feather token (whip)
  - necklace of fireballs (type I)
  - potion of inflict moderate wounds
  - potion of invisibility
  - scroll of haste
  - wand of disguise self (15 charges)
  - smokesticks (2)
  - thunderstones (2)
  other:
  - mwk chain shirt
  - animated portrait
  - 450 gp
ecology:
  environment: any
desc_long: |-
  A vampire seducer relies on getting others to do her bidding instead of acting in the open herself. Deception, manipulation, and spells are all tools of her trade. This does not mean that such a vampire cannot defend herself in combat-it simply means that she prefers to get others to risk their necks instead of taking matters into her own cold, dead hands.

  Through a blend of natural charm, physical beauty, and supernatural persuasion, the vampire seducer selects her prey from among her admirers and critics, takes her victim back to her home, and convinces them to let her bite them willingly-all part of her game. The vampire might dispose of her victims before they are too obviously aff licted by her unnatural appetites by forcing them to duel rivals for her affection or arranging for mysterious accidents and suicides (usually easily explained as the result of broken hearts).

  If the seducer's true nature is ever discovered, she has no qualms about abandoning the paramours she has acquired and relocating to a new city to begin her plots anew. Some seducers do this many times over the course of their long unlives, if only to stave off the eternal boredom that inevitably afflicts them all.

---

# Vampire, Vampire Seducer

**Source** Monster Codex pg. 239
**XP** 2,400
Human _[[monsters/Vampire|vampire]]_ _[[classes/Bard|bard]]_ 5

NE Medium undead (augmented humanoid, human)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 armor, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 61 (5d8+35); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +7, **Ref** +10, **Will** +5; +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/magic and silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _vampire_ weaknesses

##### Offense
**Speed** 30 ft.
**Melee** slam +7 (1d4+4 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Special Attacks** bardic performance 24 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate [DC 18], inspire competence +2, inspire courage +2), _[[universal monster rules/Blood Drain|blood drain]]_, children of the night, create spawn, dominate (DC 18), _energy drain_ (2 levels, DC 18)
**_Bard_ Spells Known **(CL 5th; concentration +11)
2nd (4/day)—_[[spells/Darkness|darkness]]_, _[[spells/Enthrall|enthrall]]_ (DC 20), _[[spells/Share Memory|share memory]]_ (DC 18)
1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 19), _[[spells/Ear-Piercing Scream|ear-piercing scream]]_, lesser _[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Memory Lapse|memory lapse]]_ (DC 19)
0 (at will)—_[[spells/Daze|daze]]_ (DC 18), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_ (DC 16), _[[spells/Unwitting Ally|unwitting ally]]_ (DC 18)

### Tactics

**During Combat** The _vampire_ seducer uses her dominate ability to make others defend her, calls for assistance using her children of the night ability, and attacks with her slams. She uses her necklace of fireballs when she can target multiple opponents.

##### Statistics
**Str** 18, **Dex** 18, **Con** —, **Int** 15, **Wis** 12, **Cha** 22
**Base Atk** +3; **CMB** +7; **CMD** 22
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Extra Performance|Extra Performance]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Toughness|Toughness]]_
**Skills** Bluff +22, Diplomacy +14, Intimidate +14, Knowledge (local) +12, Knowledge (nobility) +12, Perception +19, Perform (act) +14, Perform (dance) +14, Sense Motive +19, Stealth +19; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Common, Dwarven, Elven
**SQ** bardic knowledge +2, _[[universal monster rules/Change Shape|change shape]]_ (dire bat or _[[monsters/Wolf|wolf]]_, _[[spells/Beast Shape II|beast shape II]]_), _[[spells/Gaseous Form|gaseous form]]_, lore master 1/day, shadowless, _[[spells/Spider Climb|spider climb]]_, versatile performance (dance)
**Combat Gear** feather token (_[[items/Weapon/Whip|whip]]_), necklace of fireballs (type I), potion of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Haste|haste]]_, wand of _[[spells/Disguise Self|disguise self]]_ (15 charges), smokesticks (2), thunderstones (2); **Other Gear** mwk _[[items/Armor/Chain shirt|chain shirt]]_, _[[items/Wondrous Item/Animated Portrait|animated portrait]]_, 450 gp

##### Ecology

**Environment** any

##### Description

A _vampire_ seducer relies on getting others to do her bidding instead of acting in the open herself. Deception, manipulation, and spells are all tools of her trade. This does not mean that such a _vampire_ cannot defend herself in combat—it simply means that she prefers to get others to risk their necks instead of taking matters into her own cold, dead hands.

Through a _[[spells/Blend|blend]]_ of natural charm, physical beauty, and supernatural persuasion, the _vampire_ seducer selects her prey from among her admirers and critics, takes her victim back to her home, and convinces them to let her bite them willingly—all part of her game. The _vampire_ might dispose of her victims before they are too obviously aff licted by her unnatural appetites by forcing them to duel rivals for her affection or arranging for mysterious accidents and suicides (usually easily explained as the result of _[[conditions/Broken|broken]]_ hearts).

If the seducer’s true nature is ever discovered, she has no qualms about abandoning the paramours she has acquired and relocating to a new city to begin her plots anew. Some seducers do this many times over the course of their long unlives, if only to stave off the eternal boredom that inevitably afflicts them all.