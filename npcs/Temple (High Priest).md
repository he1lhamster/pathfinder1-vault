---
cssclass: [monsters]
title1: Temple (High Priest)
title2: Temple (High Priest)
CR: 12
sources:
- name: GameMastery Guide
  page: 305
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 19200
race: Human
classes:
- cleric 13
alignment: LN
size: Medium
type: humanoid
initiative:
  bonus: 0
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    armor: 3
    shield: 2
HP:
  HP: 90
  long: 13d8+32
saves:
  fort: 13
  ref: 7
  will: 18
defensive_abilities:
- unity (2/day)
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +8 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 8
  ranged:
  - - text: light crossbow +9 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 9
  special:
  - channel positive energy 5/day (DC 18, 7d6)
spell_like_abilities:
  entries:
  - name: calming touch
    source: default
    freq: 10/day
  - name: inspiring word
    source: default
    freq: 10/day
    other: 6 rounds
  sources:
  - name: default
    CL: 13
    concentration: 20
spells:
  entries:
  - name: dictum
    source: Cleric
    level: 7
    DC: 24
  - is_domain_spell: true
    name: repulsion
    source: Cleric
    level: 7
    DC: 24
  - name: summon monster VII
    source: Cleric
    level: 7
  - name: banishment
    source: Cleric
    level: 6
    DC: 23
  - name: heal
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: heroes' feast
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
  - name: summon monster V
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: telepathic bond
    source: Cleric
    level: 5
  - name: true seeing
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: dimensional anchor
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: discern lies
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
  - name: order's wrath
    source: Cleric
    level: 4
    DC: 21
  - name: tongues
    source: Cleric
    level: 4
  - name: create food and water
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
    count: 2
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 19
  - is_domain_spell: true
    name: enthrall
    source: Cleric
    level: 2
    DC: 19
  - name: hold person
    source: Cleric
    level: 2
    DC: 19
  - name: sound burst
    source: Cleric
    level: 2
    DC: 19
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: status
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    DC: 18
  - name: comprehend languages
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: divine favor
    source: Cleric
    level: 1
  - name: hide from undead
    source: Cleric
    level: 1
    DC: 18
  - name: protection from chaos
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 18
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 13
    concentration: 20
    slots:
      0: at-will
    domains:
    - community
    - nobility
ability_scores:
  STR: 8
  DEX: 10
  CON: 15
  INT: 12
  WIS: 24
  CHA: 14
BAB: 9
CMB: 8
CMD: 18
feats:
- name: Augment Summoning
- name: Craft Rod
- name: Craft Wand
- name: Craft Wondrous Item
- name: Leadership
- name: Selective Channeling
- name: Spell Focus (conjuration)
- name: Spell Penetration
- name: Turn Undead
skills:
  Diplomacy: 11
  Heal: 11
  Knowledge (arcana): 6
  Knowledge (local): 10
  Knowledge (nobility): 10
  Knowledge (religion): 16
  Linguistics: 10
  Perception: 15
  Sense Motive: 15
  Spellcraft: 16
languages:
- Aquan
- Auran
- Celestial
- Common
- Ignan
- Infernal
- Sylvan
- Terran
gear:
  combat:
  - lesser metamagic rods (extend, silent)
  - wand of eagle's splendor (50 charges)
  - wand of silence (50 charges)
  other:
  - masterwork studded leather
  - +1 buckler
  - cold iron dagger
  - light crossbow with 10 cold iron bolts
  - belt of mighty constitution +2
  - cloak of resistance +3
  - eyes of the eagle
  - headband of inspired wisdom +4
  - incense of meditation
npc_boon: A high priest may cast a spell at no cost (except for material components)
  or craft a magical item at a 10% discount. He may also be able to secure the PCs
  an audience with a ruler.
desc_long: ''

---

# Temple (High Priest)

**Source** GameMastery Guide pg. 305
**XP** 19,200
Human _[[classes/Cleric|cleric]]_ 13

LN Medium humanoid
**Init** +0; **Senses** Perception +15

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 armor, +2 _[[spells/Shield|shield]]_)
**hp** 90 (13d8+32)
**Fort** +13, **Ref** +7, **Will** +18
**Defensive Abilities** unity (2/day)

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +8 (1d4–1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +9 (1d8/19–20)
**Special Attacks** channel positive energy 5/day (DC 18, 7d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +20)
10/day—_[[items/Armor Magic Abilities/Calming|calming]]_ touch, inspiring word (6 rounds)
**_Cleric_ Spells Prepared **(CL 13th; concentration +20)
7th—_[[spells/Dictum|dictum]]_ (DC 24), _[[spells/Repulsion|repulsion]]_ (DC 24), _[[spells/Summon Monster VII|summon monster VII]]_
6th—_[[spells/Banishment|banishment]]_ (DC 23), _[[spells/Heal|heal]]_, heroes’ feast, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Summon Monster V|summon monster V]]_, _[[spells/Telepathic Bond|telepathic bond]]_, _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Discern Lies|discern lies]]_, greater _[[spells/Magic Weapon|magic weapon]]_, order’s wrath (DC 21), _[[spells/Tongues|tongues]]_
3rd—_[[spells/Create Food and Water|create food and water]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Vestment|magic vestment]]_ (2), _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Searing Light|searing light]]_
2nd—aid, _[[spells/Calm Emotions|calm emotions]]_ (DC 19), _[[spells/Enthrall|enthrall]]_ (DC 19), _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Sound Burst|sound burst]]_ (DC 19), _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Status|status]]_
1st—_[[spells/Command|command]]_ (DC 18), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Hide from Undead|hide from undead]]_ (DC 18), _[[spells/Protection From Chaos|protection from chaos]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Community, Nobility

##### Statistics
**Str** 8, **Dex** 10, **Con** 15, **Int** 12, **Wis** 24, **Cha** 14
**Base Atk** +9; **CMB** +8; **CMD** 18
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Craft Rod|Craft Rod]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Leadership|Leadership]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Turn Undead|Turn Undead]]_
**Skills** Diplomacy +11, _Heal_ +11, Knowledge (arcana) +6, Knowledge (local) +10, Knowledge (nobility) +10, Knowledge (religion) +16, Linguistics +10, Perception +15, Sense Motive +15, Spellcraft +16
**Languages** Aquan, Auran, Celestial, Common, Ignan, Infernal, Sylvan, Terran
**Combat Gear** lesser metamagic rods (extend, silent), wand of _[[monsters/Eagle|eagle]]_’s splendor (50 charges), wand of _[[spells/Silence|silence]]_ (50 charges); **Other Gear** masterwork studded leather, +1 _[[items/Armor/Buckler|buckler]]_, cold iron _dagger_, _light crossbow_ with 10 cold iron bolts, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Eyes of the Eagle|eyes of the eagle]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Wondrous Item/Incense of Meditation|incense of meditation]]_

**Boon** A high priest may cast a spell at no cost (except for material components) or craft a magical item at a 10% discount. He may also be able to secure the PCs an audience with a ruler.