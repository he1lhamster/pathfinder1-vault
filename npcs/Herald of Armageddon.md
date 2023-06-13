---
cssclass: [monsters]
title1: Herald of Armageddon
title2: Herald of Armageddon
CR: 16
sources:
- name: NPC Codex
  page: 58
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Human
classes:
- cleric of Rovagug 17
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 26
  touch: 13
  flat_footed: 25
  other: +2 deflection vs. good
  components:
    armor: 12
    deflection: 2
    dex: 1
    natural: 1
HP:
  HP: 131
  long: 17d8+51
saves:
  fort: 13
  ref: 7
  will: 16
  other: +1 vs. good
speeds:
  base: 20
attacks:
  melee:
  - - text: +2 greataxe +18/+13/+8 (1d12+6/19-20/×3)
      entries:
      - - damage: 1d12+6
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 greataxe
      bonus:
      - 18
      - 13
      - 8
  special:
  - channel negative energy 6/day (DC 23, 9d6)
  - scythe of evil (8 rounds, 3/day)
  - weapon master (17 rounds/day)
spell_like_abilities:
  entries:
  - name: battle rage
    source: default
    freq: 8/day
    other: +8 damage
  - name: touch of evil
    source: default
    freq: 8/day
    other: 8 rounds
  sources:
  - name: default
    CL: 17
    concentration: 22
spells:
  entries:
  - is_domain_spell: true
    name: power word kill
    source: Cleric
    level: 9
  - name: storm of vengeance
    source: Cleric
    level: 9
  - name: earthquake
    source: Cleric
    level: 8
  - name: fire storm
    source: Cleric
    level: 8
    DC: 23
  - is_domain_spell: true
    name: power word stun
    source: Cleric
    level: 8
  - is_domain_spell: true
    name: blasphemy
    source: Cleric
    level: 7
    DC: 22
  - name: destruction
    source: Cleric
    level: 7
    count: 2
    DC: 22
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: blade barrier
    source: Cleric
    level: 6
    DC: 21
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: harm
    source: Cleric
    level: 6
    DC: 21
  - name: heal
    source: Cleric
    level: 6
  - name: mass bull's strength
    source: Cleric
    level: 6
  - name: dispel good
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: flame strike
    source: Cleric
    level: 5
    DC: 20
  - name: righteous might
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    count: 2
    DC: 20
  - name: spell resistance
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 19
  - name: death ward
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: divine power
    source: Cleric
    level: 4
  - name: poison
    source: Cleric
    level: 4
    DC: 19
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: cure serious wounds
    source: Cleric
    level: 3
  - name: deeper darkness
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: meld into stone
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: bull's strength
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 17
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 17
  - is_domain_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 16
  - name: cause fear
    source: Cleric
    level: 1
    count: 2
    DC: 16
  - name: divine favor
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: entropic shield
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 17
    concentration: 22
    slots:
      0: at-will
    domains:
    - evil
    - war
tactics:
  Before Combat: The cleric casts air walk and magic circle against good.
  During Combat: Depending on her estimation of her opponents, the cleric might attack
    with spells or use divine power and righteous might to improve her melee abilities.
ability_scores:
  STR: 16
  DEX: 12
  CON: 14
  INT: 8
  WIS: 20
  CHA: 16
BAB: 12
CMB: 15
CMD: 28
feats:
- name: Bleeding Critical
- name: Combat Casting
- name: Critical Focus
- name: Heavy Armor Proficiency
- name: Improved Channel
- name: Improved Critical (greataxe)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Vital Strike
- name: Weapon Focus (greataxe)
skills:
  Knowledge (arcana): 11
  Sense Motive: 16
  Spellcraft: 19
  Perception: 5
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of invisibility
  other:
  - +3 light fortification full plate
  - +2 greataxe
  - amulet of natural armor +1
  - belt of physical perfection +2
  - boots of speed
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +2
  - cold iron holy symbol (worth 500 gp)
  - 4,230 gp
desc_long: The herald of armageddon serves the god of wrath and destruction. She brings
  misery, ruin, and death.

---

# Herald of Armageddon

**Source** NPC Codex pg. 58
**XP** 76,800
Human _[[classes/Cleric|cleric]]_ of Rovagug 17
CE Medium humanoid (human)
**Init** +5; **Senses** Perception +5

##### Defense

**AC** 26, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+12 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +1 natural); +2 _deflection_ vs. good
**hp** 131 (17d8+51)
**Fort** +13, **Ref** +7, **Will** +16; +1 vs. good

##### Offense
**Speed** 20 ft.
**Melee** +2 _[[items/Weapon/Greataxe|greataxe]]_ +18/+13/+8 (1d12+6/19–20/×3)
**Special Attacks** channel negative energy 6/day (DC 23, 9d6), _[[items/Weapon/Scythe|scythe]]_ of evil (8 rounds, 3/day), weapon master (17 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +22)
8/day—battle _[[spells/Rage|rage]]_ (+8 damage), _[[feats/Touch Of Evil|touch of evil]]_ (8 rounds)
**_Cleric_ Spells Prepared **(CL 17th; concentration +22)
9th—_[[spells/Power Word Kill|power word kill]]_, _[[spells/Storm Of Vengeance|storm of vengeance]]_
8th—_[[spells/Earthquake|earthquake]]_, _[[spells/Fire Storm|fire storm]]_ (DC 23), _[[spells/Power Word Stun|power word stun]]_
7th—blasphemyD (DC 22), _[[spells/Destruction|destruction]]_ (2, DC 22), _[[spells/Ethereal Jaunt|ethereal jaunt]]_
6th—blade barrierD (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Harm|harm]]_ (DC 21), _[[spells/Heal, Mass|heal, mass]]_ bull’s strength
5th—_[[spells/Dispel Good|dispel good]]_, flame strikeD (DC 20), _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (2, DC 20), _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Chaos Hammer|chaos hammer]]_ (DC 19), _[[spells/Death Ward|death ward]]_, _[[spells/Divine Power|divine power]]_, poison (DC 19), _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _dispel magic_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Prayer|prayer]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, bull’s strength, _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (2, DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 16), _[[spells/Cause Fear|cause fear]]_ (2, DC 16), _[[spells/Divine Favor|divine favor]]_, _[[spells/Doom|doom]]_ (DC 16), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domains **Evil, War

### Tactics

**Before Combat **The _cleric_ casts _air walk_ and _magic circle against good_.
**During Combat **Depending on her estimation of her opponents, the _cleric_ might attack with spells or use _divine power_ and _righteous might_ to improve her melee abilities.

##### Statistics
**Str** 16, **Dex** 12, **Con** 14, **Int** 8, **Wis** 20, **Cha** 16
**Base Atk** +12; **CMB** +15; **CMD** 28
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greataxe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greataxe_)
**Skills** Knowledge (arcana) +11, Sense Motive +16, Spellcraft +19
**Languages** Common
**SQ** aura
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** +3 light _[[universal monster rules/Fortification|fortification]]_ _[[items/Armor/Full plate|full plate]]_, +2 _greataxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Physical Perfection +2|belt of physical perfection +2]]_, _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, cold iron holy symbol (worth 500 gp), 4,230 gp

The _[[npcs/Herald of Armageddon|herald of armageddon]]_ serves the god of wrath and _destruction_. She brings misery, ruin, and death.