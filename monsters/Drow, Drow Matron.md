---
cssclass: [monsters]
title1: Drow, Drow Matron
title2: Drow Matron
CR: 15
sources:
- name: Monster Codex
  page: 39
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 51200
race: Drow
classes:
- noble cleric (demonic apostle) 15 (Pathfinder RPG Advanced Race Guide 104)
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 6
senses:
  darkvision: 120
AC:
  AC: 24
  touch: 14
  flat_footed: 21
  components:
    armor: 8
    deflection: 4
    dex: 2
    dodge: 1
HP:
  HP: 101
  long: 15d8+30
saves:
  fort: 10
  ref: 7
  will: 18
  other: +2 vs. enchantment
immunities:
- sleep
SR: 26
weaknesses:
- light blindness
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 heavy mace +12/+7/+2 (1d8+1)
      entries:
      - - damage: 1d8+1
      attack: +1 heavy mace
      bonus:
      - 12
      - 7
      - 2
  special:
  - demonic channel 7/day (DC 19, 8d6 plus sicken or special)
  - hand of the acolyte (10/day)
  - scythe of evil (7 rounds, 2/day)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - name: faerie fire
    source: default
    freq: At will
  - name: feather fall
    source: default
    freq: At will
  - name: levitate
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: 1/day
  - name: divine favor
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 15
  - name: Like Abilities
    source: default
    freq: Domain S pell
    CL: 15
    other: concentration +22
  - name: touch of evil
    source: default
    freq: 10/day
    other: 7 rounds
  - name: dispelling touch
    source: default
    freq: 2/day
  sources:
  - name: default
    CL: 15
    concentration: 17
spells:
  entries:
  - name: fire storm
    source: Cleric
    level: 8
    DC: 25
  - is_domain_spell: true
    name: unholy aura
    source: Cleric
    level: 8
    DC: 25
  - is_domain_spell: true
    name: blasphemy
    source: Cleric
    level: 7
    DC: 24
  - name: destruction
    source: Cleric
    level: 7
    DC: 25
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - name: summon monster VII
    source: Cleric
    level: 7
  - name: antilife shell
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: antimagic field
    source: Cleric
    level: 6
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: harm
    source: Cleric
    level: 6
    DC: 24
  - name: heal
    source: Cleric
    level: 6
  - superscripts:
    - UC
    name: communal spell immunity
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: dispel good
    source: Cleric
    level: 5
    DC: 22
  - superscripts:
    - UM
    name: fickle winds
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
  - name: slay living
    source: Cleric
    level: 5
    DC: 23
  - name: wall of stone
    source: Cleric
    level: 5
    DC: 22
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: dimensional anchor
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: imbue with spell ability
    source: Cleric
    level: 4
  - superscripts:
    - UC
    name: summoner conduit
    source: Cleric
    level: 4
    DC: 22
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 21
  - superscripts:
    - UC
    name: chain of perdition
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - name: water breathing
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: evil only
  - name: delay poison
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: dread bolt
    source: Cleric
    level: 2
    DC: 19
  - name: hold person
    source: Cleric
    level: 2
    DC: 19
  - name: lesser restoration
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: protective penumbra
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 19
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 2
  - name: entropic shield
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    count: 2
    DC: 18
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 15
    concentration: 22
    slots:
      0: at-will
    domains:
    - evil
    - magic
ability_scores:
  STR: 10
  DEX: 14
  CON: 12
  INT: 14
  WIS: 24
  CHA: 15
BAB: 11
CMB: 11
CMD: 25
feats:
- name: Combat Casting
- name: Dodge
- name: Extra Channel
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Spell Focus (necromancy)
- name: Toughness
skills:
  Bluff: 10
  Diplomacy: 9
  Intimidate: 12
  Knowledge (arcana): 9
  Knowledge (history): 8
  Knowledge (nobility): 9
  Knowledge (planes): 9
  Knowledge (religion): 15
  Perception: 19
  Sense Motive: 20
  Spellcraft: 13
languages:
- Abyssal
- Common
- Elven
- Undercommon
special_qualities:
- poison use
- quasit familiar
gear:
  combat:
  - potion of displacement
  - potion of invisibility
  - scroll of blade barrier
  - scrolls of cure moderate wounds (2)
  - scroll of mass cure serious wounds
  - scroll of summon monster VII
  other:
  - +2 mithral chainmail
  - +1 heavy mace
  - belt of incredible dexterity +2
  - headband of inspired wisdom +4
  - ring of protection +1
  - reliquary
  - spell component pouch
  - 183 gp
ecology:
  environment: underground
desc_long: Born with unusual powers, the matron has survived coup attempts by countless
  rivals to remain the head of her house.

---

# Drow, Drow Matron

**Source** Monster Codex pg. 39
**XP** 51,200
_[[monsters/Drow|Drow]]_ noble _[[classes/Cleric|cleric]]_ (demonic apostle) 15 (Pathfinder RPG Advanced Race Guide 104)
CE Medium humanoid (elf)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +19

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+8 armor, +4 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 101 (15d8+30)
**Fort** +10, **Ref** +7, **Will** +18; +2 vs. enchantment
**Immune** sleep; **SR** 26
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +12/+7/+2 (1d8+1)
**Special Attacks** demonic channel 7/day (DC 19, 8d6 plus sicken or special), hand of the _[[npcs/Acolyte|acolyte]]_ (10/day), _[[items/Weapon/Scythe|scythe]]_ of evil (7 rounds, 2/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +17)
Constant—_[[spells/Detect Magic|detect magic]]_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Levitate|levitate]]_
1/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Suggestion|suggestion]]_ (DC 15)
Domain S pell-Like Abilities (CL 15th; concentration +22)
10/day—_[[feats/Touch Of Evil|touch of evil]]_ (7 rounds)
2/day—_[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ touch
**_Cleric_ Spells Prepared **(CL 15th; concentration +22)
8th—_[[spells/Fire Storm|fire storm]]_ (DC 25), _[[spells/Unholy Aura|unholy aura]]_ (DC 25)
7th—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Destruction|destruction]]_ (DC 25), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Summon Monster VII|summon monster VII]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Antimagic Field|antimagic field]]_, greater _dispel magic_, _[[spells/Harm|harm]]_ (DC 24), _[[spells/Heal|heal]]_
5th—communal _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Dispel Good|dispel good]]_ (DC 22), _[[spells/Fickle Winds|fickle winds]]_, _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Slay Living|slay living]]_ (DC 23), _[[spells/Wall Of Stone|wall of stone]]_ (DC 22)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Imbue with Spell Ability|imbue with spell ability]]_, _[[spells/Summoner Conduit|summoner conduit]]_ (DC 22)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 21), _[[spells/Chain of Perdition|chain of perdition]]_, _dispel magic_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (evil only), _[[spells/Delay Poison|delay poison]]_, _[[spells/Dread Bolt|dread bolt]]_ (DC 19), _[[spells/Hold Person|hold person]]_ (DC 19), lesser _[[spells/Restoration|restoration]]_, _[[spells/Protective Penumbra|protective penumbra]]_, _[[spells/Sound Burst|sound burst]]_ (DC 19)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Murderous Command|murderous command]]_ (2, DC 18), _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_detect magic_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Evil, Magic

##### Statistics
**Str** 10, **Dex** 14, **Con** 12, **Int** 14, **Wis** 24, **Cha** 15
**Base Atk** +11; **CMB** +11; **CMD** 25
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Toughness|Toughness]]_
**Skills** Bluff +10, Diplomacy +9, Intimidate +12, Knowledge (arcana) +9, Knowledge (history) +8, Knowledge (nobility) +9, Knowledge (planes) +9, Knowledge (religion) +15, Perception +19, Sense Motive +20, Spellcraft +13
**Languages** Abyssal, Common, Elven, Undercommon
**SQ** poison use, quasit familiar
**Combat Gear** potion of _[[spells/Displacement|displacement]]_, potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Blade Barrier|blade barrier]]_, scrolls of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), scroll of mass _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _summon monster VII_; **Other Gear** +2 mithral _[[items/Armor/Chainmail|chainmail]]_, +1 _heavy mace_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, reliquary, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 183 gp

##### Ecology

**Environment** underground

##### Description

Born with unusual powers, the matron has survived coup attempts by countless rivals to remain the head of her house.