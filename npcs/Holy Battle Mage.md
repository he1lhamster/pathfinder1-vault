---
cssclass: [monsters]
title1: Holy Battle Mage
title2: Holy Battle Mage
CR: 19
sources:
- name: NPC Codex
  page: 231
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Dwarf
classes:
- cleric of Torag 5
- wizard 5
- mystic theurge 10
alignment: NG
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 30
  touch: 14
  flat_footed: 30
  components:
    armor: 11
    deflection: 5
    dex: -1
    natural: 5
HP:
  HP: 237
  long: 5d8+5d6+10d6+159
saves:
  fort: 16
  ref: 6
  will: 23
  other: +6 vs. poison, +4 vs. fear, +2 vs. spells and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- 20% miss chance
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
immunities:
- electricity (120 points)
- fire (120 points)
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 holy warhammer +13/+8 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 holy warhammer
      bonus:
      - 13
      - 8
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - channel positive energy 5/day (DC 12, 3d6)
  - hand of the apprentice (9/day)
  - spell synthesis
spell_like_abilities:
  entries:
  - name: artificer's touch
    source: default
    freq: 10/day
    other: 1d6+2
  - name: resistant touch
    source: default
    freq: 10/day
  sources:
  - name: default
    CL: 5
    concentration: 12
spells:
  entries:
  - name: greater spell immunity
    source: Cleric
    level: 8
  - is_domain_spell: true
    name: mind blank
    source: Cleric
    level: 8
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - name: holy word
    source: Cleric
    level: 7
    count: 2
    DC: 25
  - is_domain_spell: true
    name: repulsion
    source: Cleric
    level: 7
    DC: 24
  - name: harm
    source: Cleric
    level: 6
    DC: 23
  - name: heal
    source: Cleric
    level: 6
    count: 2
  - name: heroes' feast
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: major creation
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: disrupting weapon
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 23
  - name: righteous might
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: spell resistance
    source: Cleric
    level: 5
  - name: true seeing
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: neutralize poison
    source: Cleric
    level: 4
    count: 2
  - is_domain_spell: true
    name: spell immunity
    source: Cleric
    level: 4
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: meld into stone
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
    count: 2
  - name: remove curse
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: stone shape
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - name: bull's strength
    source: Cleric
    level: 2
    count: 2
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 19
  - is_domain_spell: true
    name: wood shape
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: animate rope
    source: Cleric
    level: 1
  - name: bless
    source: Cleric
    level: 1
    count: 2
  - name: divine favor
    source: Cleric
    level: 1
    count: 2
  - name: shield of faith
    source: Cleric
    level: 1
    count: 2
  - name: detect magic
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  - name: prismatic wall
    source: Wizard
    level: 8
  - name: giant form I
    source: Wizard
    level: 7
  - name: prismatic spray
    source: Wizard
    level: 7
  - name: chain lightning
    source: Wizard
    level: 6
    count: 2
    DC: 23
  - name: disintegrate
    source: Wizard
    level: 6
    DC: 22
  - name: transformation
    source: Wizard
    level: 6
  - name: cloudkill
    source: Wizard
    level: 5
    DC: 21
  - name: hold monster
    source: Wizard
    level: 5
    count: 2
    DC: 21
  - name: wall of stone
    source: Wizard
    level: 5
    count: 2
  - name: arcane eye
    source: Wizard
    level: 4
  - name: dimension door
    source: Wizard
    level: 4
  - name: greater invisibility
    source: Wizard
    level: 4
    count: 2
  - name: stoneskin
    source: Wizard
    level: 4
  - name: fireball
    source: Wizard
    level: 3
    DC: 20
  - name: haste
    source: Wizard
    level: 3
    count: 2
  - name: heroism
    source: Wizard
    level: 3
  - name: suggestion
    source: Wizard
    level: 3
    DC: 19
  - name: acid arrow
    source: Wizard
    level: 2
  - name: invisibility
    source: Wizard
    level: 2
  - name: see invisibility
    source: Wizard
    level: 2
    count: 2
  - name: web
    source: Wizard
    level: 2
    count: 2
    DC: 18
  - name: charm person
    source: Wizard
    level: 1
    DC: 17
  - name: magic missile
    source: Wizard
    level: 1
    count: 3
  - name: shield
    source: Wizard
    level: 1
    count: 2
  - name: detect poison
    source: Wizard
    level: 0
  - name: disrupt undead
    source: Wizard
    level: 0
  - name: mage hand
    source: Wizard
    level: 0
  - name: message
    source: Wizard
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 15
    concentration: 22
    slots:
      0: at-will
    domains:
    - artifice
    - protection
  - name: Wizard
    type: prepared
    CL: 15
    concentration: 21
    failure_chance: 20%
    slots:
      0: at-will
tactics:
  Before Combat: The mystic theurge casts heroes' feast, protection from energy (electricity,
    fire), see invisibility, and stoneskin.
  During Combat: The mystic theurge uses spells to foil opponents and bolster allies.
    If entering melee combat, he casts righteous might and transformation.
  Base Statistics: Without heroes' feast, protection from energy, and stoneskin, the
    mystic theurge's statistics are hp 223; Will +22; +2 vs. poison, spells, and spell-like
    abilities; DR none; Immune none; Melee +1 holy warhammer +12/+7 (1d8+1/×3).
ability_scores:
  STR: 10
  DEX: 8
  CON: 22
  INT: 22
  WIS: 24
  CHA: 11
BAB: 10
CMB: 10
CMD: 24
CMD_other: 28 vs. bull rush or trip
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Extra Channel
- name: Forge Ring
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (evocation)
- name: Spell Penetration
- name: Toughness
- name: Weapon Focus (warhammer)
skills:
  Craft (armor): 14
  Craft (weapons): 14
  Diplomacy: 13
  Heal: 20
  Knowledge (arcana): 29
  Knowledge (religion): 29
  Knowledge (dungeoneering): 19
  Knowledge (engineering): 19
  Knowledge (planes): 19
  Knowledge (history): 14
  Knowledge (local): 14
  Perception: 27
    to notice unusual stonework: 29
  Sense Motive: 20
  Spellcraft: 19
  Use Magic Device: 10
languages:
- Aklo
- Celestial
- Common
- Draconic
- Dwarven
- Elven
- Giant
- Undercommon
special_qualities:
- aura
- arcane bond (+1 holy warhammer)
- combined spells (5th)
gear:
  combat:
  - potions of bull's strength (2)
  - wand of cure serious wounds (20 charges)
  - holy water (5)
  other:
  - +5 mithral chainmail
  - +1 holy warhammer
  - amulet of natural armor +5
  - belt of mighty constitution +6
  - minor cloak of displacement
  - ring of protection +5
  - diamond dust (worth 500 gp)
  - eye ointment (worth 250 gp)
  - pair of canine statuettes (worth 50 gp)
  - 1,863 gp
desc_long: These master theurges mix support for allies with offensive might.

---

# Holy Battle Mage

**Source** NPC Codex pg. 231
**XP** 204,800
Dwarf _[[classes/Cleric|cleric]]_ of Torag 5/wizard 5/mystic theurge 10

NG Medium humanoid (dwarf)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +27

##### Defense

**AC** 30, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+11 armor, +5 _[[spells/Deflection|deflection]]_, –1 Dex, +5 natural)
**hp** 237 (5d8+5d6+10d6+159)
**Fort** +16, **Ref** +6, **Will** +23; +6 vs. poison, +4 vs. _[[universal monster rules/Fear|fear]]_, +2 vs. spells and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants), 20% miss chance; **DR** 10/adamantine (150 points); **Immune** electricity (120 points), fire (120 points)

##### Offense
**Speed** 20 ft.
**Melee** +1 holy _[[items/Weapon/Warhammer|warhammer]]_ +13/+8 (1d8+1/×3)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, channel positive energy 5/day (DC 12, 3d6), hand of the apprentice (9/day), spell synthesis
**_Spell-Like Abilities_** (CL 5th; concentration +12)
10/day—artificer’s touch (1d6+2), resistant touch
**_Cleric_ Spells Prepared **(CL 15th; concentration +22)
8th—greater _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Mind Blank|mind blank]]_
7th—_[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Holy Word|holy word]]_ (2, DC 25), _[[spells/Repulsion|repulsion]]_ (DC 24)
6th—_[[spells/Harm|harm]]_ (DC 23), _[[spells/Heal|heal]]_ (2), heroes’ feast, _[[spells/Major Creation|major creation]]_
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Disrupting Weapon|disrupting weapon]]_, _[[spells/Flame Strike|flame strike]]_ (DC 23), _[[spells/Righteous Might|righteous might]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Neutralize Poison|neutralize poison]]_ (2), _spell immunity_
3rd—_[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_ (2), _[[spells/Remove Curse|remove curse]]_, _[[spells/Stone Shape|stone shape]]_
2nd—aid, bull’s strength (2), _[[spells/Hold Person|hold person]]_ (2, DC 19), _[[spells/Wood Shape|wood shape]]_
1st—_[[spells/Animate Rope|animate rope]]_, _[[spells/Bless|bless]]_ (2), _[[spells/Divine Favor|divine favor]]_ (2), _[[spells/Shield Of Faith|shield of faith]]_ (2)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D **Domain spell; **Domains **Artifice, Protection
**_[[classes/Wizard|Wizard]]_ Spells Prepared **(CL 15th; concentration +21; arcane spell failure 20%)
8th—_[[spells/Prismatic Wall|prismatic wall]]_
7th—_[[spells/Giant Form I|giant form I]]_, _[[spells/Prismatic Spray|prismatic spray]]_
6th—_[[spells/Chain Lightning|chain lightning]]_ (2, DC 23), _[[spells/Disintegrate|disintegrate]]_ (DC 22), _[[spells/Transformation|transformation]]_
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 21), _[[spells/Hold Monster|hold monster]]_ (2, DC 21), _[[spells/Wall Of Stone|wall of stone]]_ (2)
4th—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_ (2), _[[spells/Stoneskin|stoneskin]]_
3rd—_[[spells/Fireball|fireball]]_ (DC 20), _[[spells/Haste|haste]]_ (2), _[[spells/Heroism|heroism]]_, _[[spells/Suggestion|suggestion]]_ (DC 19)
2nd—_[[spells/Acid Arrow|acid arrow]]_, _invisibility_, _[[spells/See Invisibility|see invisibility]]_ (2), web (2, DC 18)
1st—_[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Magic Missile|magic missile]]_ (3), _[[spells/Shield|shield]]_ (2)
0 (at will)—_[[spells/Detect Poison|detect poison]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_

### Tactics

**Before Combat **The mystic theurge casts heroes’ feast, _protection from energy_ (electricity, fire), _see invisibility_, and _stoneskin_.
**During Combat **The mystic theurge uses spells to foil opponents and bolster allies. If entering melee combat, he casts _righteous might_ and _transformation_.
**Base Statistics **Without heroes’ feast, _protection from energy_, and _stoneskin_, the mystic theurge’s statistics are **hp **223; **Will **+22; +2 vs. poison, spells, and _spell-like abilities_; **DR **none; **Immune **none; **Melee **+1 holy _warhammer_ +12/+7 (1d8+1/×3).

##### Statistics
**Str** 10, **Dex** 8, **Con** 22, **Int** 22, **Wis** 24, **Cha** 11
**Base Atk** +10; **CMB** +10; **CMD** 24 (28 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_warhammer_)
**Skills** Craft (armor, weapons) +14, Diplomacy +13, _Heal_ +20, Knowledge (arcana, religion) +29, Knowledge (dungeoneering, engineering, planes) +19, Knowledge (history, local) +14, Perception +27 (+29 to notice unusual stonework), Sense Motive +20, Spellcraft +19, Use Magic Device +10
**Languages** Aklo, Celestial, Common, Draconic, Dwarven, Elven, Giant, Undercommon
**SQ** aura, arcane bond (+1 holy _warhammer_), combined spells (5th)
**Combat Gear** potions of bull’s strength (2), wand of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (20 charges), _[[items/Mundane/Holy water|holy water]]_ (5); **Other Gear** +5 mithral _[[items/Armor/Chainmail|chainmail]]_, +1 holy _warhammer_, _[[items/Wondrous Item/Amulet of Natural Armor +5|amulet of natural armor +5]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +6|belt of mighty constitution +6]]_, minor cloak of _[[spells/Displacement|displacement]]_, _[[items/Ring/Ring of Protection +5|ring of protection +5]]_, diamond dust (worth 500 gp), eye ointment (worth 250 gp), pair of canine statuettes (worth 50 gp), 1,863 gp

These master theurges mix support for allies with offensive might.