---
cssclass: [monsters]
title1: Drow Matron
title2: Drow Matron
CR: 15
sources:
- name: Inner Sea NPC Codex
  page: 19
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 51200
race: Drow
classes:
- noble cleric of Nocticula 15
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 4
senses:
  darkvision: 120
AC:
  AC: 22
  touch: 12
  flat_footed: 20
  components:
    armor: 8
    dex: 2
    natural: 2
HP:
  HP: 116
  long: 15d8+45
saves:
  fort: 13
  ref: 14
  will: 18
  other: +2 vs. enchantment
immunities:
- sleep
SR: 26
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk dagger +12/+7/+2 (1d4/19-20 plus poison)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: poison
      attack: mwk dagger
      bonus:
      - 12
      - 7
      - 2
  ranged:
  - - text: mwk hand crossbow +17 (1d4/19-20 plus poison)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: poison
      attack: mwk hand crossbow
      bonus:
      - 17
  special:
  - channel negative energy 6/day (DC 20, 8d6)
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
  - name: divine favor
    source: default
    freq: 1/day
  - name: dispel magic
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 16
  - name: charming smile
    source: domain
    freq: At will
    other: 15 rounds
    DC: 17
  - name: dazing touch
    source: domain
    freq: 9/day
  - name: touch of darkness
    source: domain
    freq: 9/day
    other: 7 rounds
  sources:
  - name: default
    CL: 15
  - name: domain
    CL: 15
    concentration: 21
spells:
  entries:
  - is_domain_spell: true
    name: demand
    source: Cleric
    level: 8
    DC: 24
  - name: summon monster VIII
    source: Cleric
    level: 8
  - name: destruction
    source: Cleric
    level: 7
    DC: 23
  - is_domain_spell: true
    name: power word blind
    source: Cleric
    level: 7
  - name: word of chaos
    source: Cleric
    level: 7
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 22
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: harm
    source: Cleric
    level: 6
    DC: 22
  - name: heal
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: shadow walk
    source: Cleric
    level: 6
    DC: 22
  - name: break enchantment
    source: Cleric
    level: 5
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: charm monster
    source: Cleric
    level: 5
    DC: 21
  - name: dispel good
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 21
  - name: slay living
    source: Cleric
    level: 5
    DC: 21
  - name: air walk
    source: Cleric
    level: 4
  - name: cure critical wounds
    source: Cleric
    level: 4
    count: 2
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: heroism
    source: Cleric
    level: 4
  - name: neutralize poison
    source: Cleric
    level: 4
  - name: bestow curse
    source: Cleric
    level: 3
    count: 2
    DC: 19
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - name: stone shape
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: suggestion
    source: Cleric
    level: 3
    DC: 19
  - name: align weapon
    source: Cleric
    level: 2
  - name: bear's endurance
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: blindness/deafness
    source: Cleric
    level: 2
    DC: 18
    other: only to cause blindness
  - name: death knell
    source: Cleric
    level: 2
    DC: 18
  - name: hold person
    source: Cleric
    level: 2
    DC: 18
  - name: silence
    source: Cleric
    level: 2
    count: 2
    DC: 18
  - name: bless
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: charm person
    source: Cleric
    level: 1
    DC: 17
  - name: command
    source: Cleric
    level: 1
    count: 2
    DC: 17
  - name: detect good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
    count: 2
  - name: bleed
    source: Cleric
    level: 0
    DC: 16
  - name: read magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 15
    concentration: 21
    slots:
      0: at-will
    domains:
    - charm
    - darkness
ability_scores:
  STR: 10
  DEX: 19
  CON: 12
  INT: 10
  WIS: 22
  CHA: 16
BAB: 11
CMB: 11
CMD: 25
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Precise Shot
- name: Quick Draw
- name: Rapid Reload (hand crossbow)
- name: Toughness
- name: Weapon Focus (hand crossbow)
skills:
  Knowledge (religion): 12
  Linguistics: 4
  Perception: 8
  Spellcraft: 13
  Stealth: 10
  _racial_mods:
    Perception:
      _: 2
languages:
- Abyssal
- Elven
- Undercommon
special_qualities:
- aura
- eyes of darkness (7 rounds/day)
- poison use
gear:
  combat:
  - +1 bane bolts (10, various designated foes)
  - +1 icy burst seeking bolts (2)
  - +3 unholy bolts (2)
  - potions of invisibility (2)
  - drow poison (6 doses)
  other:
  - +2 glamered chainmail
  - mwk dagger
  - mwk hand crossbow with 10 bolts
  - amulet of natural armor +2
  - belt of incredible dexterity +2
  - cloak of resistance +3
  - headband of mental prowess +2 (Wis, Cha)
  - 282 gp
desc_long: Among the demon-worshiping dark elves of Sekamina, the drow matrons are
  some of the most dangerous. Not only do they hold considerable influence within
  their matriarchal society, but they must be capable of wicked cunning, incredible
  treachery, and vile deeds to have attained their august rank as leaders of their
  chaotic and conniving kind.

---

# Drow Matron

**Source** Inner Sea NPC Codex pg. 19
**XP** 51,200
_[[monsters/Drow|Drow]]_ noble _[[classes/Cleric|cleric]]_ of Nocticula 15
CE Medium humanoid (elf)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +8

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+8 armor, +2 Dex, +2 natural)
**hp** 116 (15d8+45)
**Fort** +13, **Ref** +14, **Will** +18; +2 vs. enchantment
**Immune** sleep; **SR** 26

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +12/+7/+2 (1d4/19–20 plus poison)
**Ranged** mwk _[[items/Weapon/Hand crossbow|hand crossbow]]_ +17 (1d4/19–20 plus poison)
**Special Attacks** channel negative energy 6/day (DC 20, 8d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th)
Constant—_[[spells/Detect Magic|detect magic]]_ 
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Levitate|levitate]]_
1/day—_[[spells/Divine Favor|divine favor]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Suggestion|suggestion]]_ (DC 16)
**Domain _Spell-Like Abilities_ **(CL 15th; concentration +21)
At will—charming smile (15 rounds, DC 17)
9/day—dazing touch, touch of _[[spells/Darkness|darkness]]_ (7 rounds)
**_Cleric_ Spells Prepared **(CL 15th; concentration +21)
8th—_[[spells/Demand|demand]]_ (DC 24), _[[spells/Summon Monster VIII|summon monster VIII]]_
7th—_[[spells/Destruction|destruction]]_ (DC 23), _[[spells/Power Word Blind|power word blind]]_, _[[spells/Word Of Chaos|word of chaos]]_
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 22), greater _dispel magic_, _[[spells/Harm|harm]]_ (DC 22), _[[spells/Heal|heal]]_, _[[spells/Shadow Walk|shadow walk]]_ (DC 22)
5th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Breath Of Life|breath of life]]_, _[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Dispel Good|dispel good]]_, _[[spells/Flame Strike|flame strike]]_ (DC 21), _[[spells/Slay Living|slay living]]_ (DC 21)
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_ (2), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Heroism|heroism]]_, _[[spells/Neutralize Poison|neutralize poison]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (2, DC 19), _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Stone Shape|stone shape]]_, _suggestion_ (DC 19)
2nd—_[[spells/Align Weapon|align weapon]]_, bear’s _[[feats/Endurance|endurance]]_, blindness/deafness (DC 18, only to cause blindness), _[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Silence|silence]]_ (2, DC 18)
1st—_[[spells/Bless|bless]]_, _[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Command|command]]_ (2, DC 17), _[[spells/Detect Good|detect good]]_, _[[spells/Shield Of Faith|shield of faith]]_ (2)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_
**D **domain spell; **Domains **Charm, _Darkness_

##### Statistics
**Str** 10, **Dex** 19, **Con** 12, **Int** 10, **Wis** 22, **Cha** 16
**Base Atk** +11; **CMB** +11; **CMD** 25
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Rapid Reload|Rapid Reload]]_ (_hand crossbow_), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_hand crossbow_)
**Skills** Knowledge (religion) +12, Linguistics +4, Perception +8, Spellcraft +13, Stealth +10; **Racial Modifiers** +2 Perception
**Languages** Abyssal, Elven, Undercommon
**SQ** aura, eyes of _darkness_ (7 rounds/day), poison use
**Combat Gear** +1 _[[spells/Bane|bane]]_ bolts (10, various designated foes), +1 _[[items/Weapon Magic Abilities/Icy Burst|icy burst]]_ seeking bolts (2), +3 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ bolts (2), potions of _[[spells/Invisibility|invisibility]]_ (2), _[[poisons/Drow poison|drow poison]]_ (6 doses); **Other Gear** +2 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Armor/Chainmail|chainmail]]_, mwk _dagger_, mwk _hand crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Mental Prowess +2|headband of mental prowess +2]]_ (Wis, Cha), 282 gp

Among the demon-worshiping dark elves of Sekamina, the _drow_ matrons are some of the most dangerous. Not only do they hold considerable influence within their matriarchal society, but they must be capable of wicked _[[items/Weapon Magic Abilities/Cunning|cunning]]_, incredible treachery, and vile deeds to have attained their august rank as leaders of their chaotic and conniving kind.