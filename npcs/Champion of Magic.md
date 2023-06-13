---
cssclass: [monsters]
title1: Champion of Magic
title2: Champion of Magic
CR: 12
sources:
- name: NPC Codex
  page: 222
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Gnome
classes:
- paladin of Torag 2
- sorcerer 7
- eldritch knight 4
alignment: LG
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: -1
senses:
  low-light vision: true
  see invisibility: true
AC:
  AC: 21
  touch: 12
  flat_footed: 21
  components:
    armor: 8
    deflection: 2
    dex: -1
    natural: 1
    size: 1
HP:
  HP: 134
  long: 2d10+7d6+4d10+72
saves:
  fort: 15
  ref: 6
  will: 13
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 130
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 warhammer +14/+9 (1d6+5/×3)
      entries:
      - - damage: 1d6+5
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 14
      - 9
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - smite evil (+3 attack and AC, +2 damage)
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  - name: detect evil
    source: paladin
    freq: At will
  sources:
  - name: default
    CL: 13
    concentration: 16
  - name: paladin
    CL: 2
    concentration: 5
spells:
  entries:
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: resilient sphere
    source: Sorcerer
    level: 4
    DC: 17
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: displacement
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: darkvision
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 15
  - name: comprehend languages
    source: Sorcerer
    level: 1
  - name: enlarge person
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 10
    concentration: 13
    failure_chance: 15%
    slots:
      5: 3
      4: 5
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: arcane
tactics:
  Before Combat: The eldritch knight casts see invisibility and stoneskin.
  During Combat: The eldritch knights separates large groups with a wall of force,
    then attacks opponents outside of the wall before passing through it with dimension
    door to finish off the remainder of his assailants.
  Base Statistics: Without see invisibility and stoneskin, the eldritch knight's statistics
    are Senses low-light vision; DR none.
ability_scores:
  STR: 14
  DEX: 8
  CON: 18
  INT: 12
  WIS: 10
  CHA: 17
BAB: 9
CMB: 10
CMD: 21
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Craft Magic Arms and Armor
- name: Eschew Materials
- name: Extra Lay on Hands
- name: Power Attack
- name: Still Spell
- name: Toughness
- name: Weapon Focus (warhammer)
- name: Weapon Specialization (warhammer)
skills:
  Craft (armor): 10
  Diplomacy: 9
  Heal: 5
  Knowledge (arcana): 9
  Knowledge (religion): 9
  Perception: 12
  Spellcraft: 9
  Use Magic Device: 11
languages:
- Common
- Draconic
- Gnome
- Sylvan
special_qualities:
- arcane bond (+1 warhammer)
- aura
- bloodline arcana (+1 DC for spells augmented by metamagic feats that increase spell
  level)
- code of conduct
- diverse training
- lay on hands (1d6, 6/day)
- metamagic adept (2/day)
desc_long: These eldritch knights seek out evil spellcasters and dispense justice
  for their misdeeds.

---

# Champion of Magic

**Source** NPC Codex pg. 222
**XP** 19,200
Gnome _[[classes/Paladin|paladin]]_ of Torag 2/sorcerer 7/eldritch _[[npcs/Knight|knight]]_ 4

LG Small humanoid (gnome)
**Init** –1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +12

##### Defense

**AC** 21, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+8 armor, +2 deflection, –1 Dex, +1 natural, +1 size)
**hp** 134 (2d10+7d6+4d10+72)
**Fort** +15, **Ref** +6, **Will** +13; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **DR** 10/adamantine (130 points)

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon/Warhammer|warhammer]]_ +14/+9 (1d6+5/×3)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, smite evil (+3 attack and AC, +2 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +16)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Paladin_ _Spell-Like Abilities_** (CL 2nd; concentration +5)
At will—_[[spells/Detect Evil|detect evil]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 10th; concentration +13; arcane spell failure 15%)
5th (3/day)—_[[spells/Wall Of Force|wall of force]]_
4th (5/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Resilient Sphere|resilient sphere]]_ (DC 17), _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, fly, _[[spells/Heroism|heroism]]_
2nd (7/day)—_[[spells/Darkvision|darkvision]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_, _see invisibility_, web (DC 15)
1st (7/day)—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Enlarge Person|enlarge person]]_, _[[spells/Identify|identify]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _dancing lights_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Mending|mending]]_, _prestidigitation_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **arcane

### Tactics

**Before Combat **The eldritch _knight_ casts _see invisibility_ and _stoneskin_.
**During Combat **The eldritch knights separates large groups with a _wall of force_, then attacks opponents outside of the wall before passing through it with _dimension door_ to finish off the remainder of his assailants.
**Base Statistics **Without _see invisibility_ and _stoneskin_, the eldritch _knight_’s statistics are **Senses **_low-light vision_; **DR **none.

##### Statistics
**Str** 14, **Dex** 8, **Con** 18, **Int** 12, **Wis** 10, **Cha** 17
**Base Atk** +9; **CMB** +10; **CMD** 21
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extra Lay On Hands|Extra Lay on Hands]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Still Spell|Still Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_warhammer_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_warhammer_)
**Skills** Craft (armor) +10, Diplomacy +9, _[[spells/Heal|Heal]]_ +5, Knowledge (arcana, religion) +9, Perception +12, Spellcraft +9, Use Magic Device +11
**Languages** Common, Draconic, Gnome, Sylvan
**SQ** arcane bond (+1 _warhammer_), aura, bloodline arcana (+1 DC for spells augmented by metamagic feats that increase spell level), code of conduct, diverse _training_, lay on hands (1d6, 6/day), metamagic adept (2/day)

These eldritch knights seek out evil spellcasters and dispense justice for their misdeeds.