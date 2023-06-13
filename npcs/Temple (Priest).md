---
cssclass: [monsters]
title1: Temple (Priest)
title2: Temple (Priest)
CR: 8
sources:
- name: GameMastery Guide
  page: 305
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 4800
race: Human
classes:
- cleric 9
alignment: LN
size: Medium
type: humanoid
initiative:
  bonus: 1
AC:
  AC: 26
  touch: 11
  flat_footed: 25
  components:
    armor: 11
    dex: 1
    shield: 4
HP:
  HP: 70
  long: 9d8+30
saves:
  fort: 9
  ref: 5
  will: 11
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 merciful morningstar +9/+4 (1d8+3 plus 1d6 nonlethal)
      entries:
      - - damage: 1d8+3
        - damage: 1d6
          type: nonlethal
      attack: +1 merciful morningstar
      bonus:
      - 9
      - 4
  - - text: dagger +8/+3 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 8
      - 3
  ranged:
  - - text: mwk light crossbow +8 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 8
  - - text: dagger +7 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 7
  special:
  - channel positive energy 5/day (DC 14, 5d6)
  - staff of order (4 rounds, 1/day)
spell_like_abilities:
  entries:
  - name: rebuke death
    source: default
    freq: 7/day
  - name: touch of law
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - is_domain_spell: true
    name: breath of life
    source: Cleric
    level: 5
  - name: righteous might
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: order's wrath
    source: Cleric
    level: 4
    DC: 18
  - name: spell immunity
    source: Cleric
    level: 4
  - name: daylight
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against chaos
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - name: bull's strength
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: cure moderate wounds
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: status
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: detect chaos
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
    count: 2
  - is_domain_spell: true
    name: protection from chaos
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 9
    concentration: 13
    slots:
      0: at-will
    domains:
    - healing
    - law
ability_scores:
  STR: 14
  DEX: 12
  CON: 14
  INT: 8
  WIS: 18
  CHA: 10
BAB: 6
CMB: 8
CMD: 19
feats:
- name: Armor Proficiency (heavy)
- name: Craft Magic Arms and Armor
- name: Extra Channel
- name: Shield Focus
- name: Toughness
- name: Vital Strike
skills:
  Diplomacy: 5
  Heal: 10
  Knowledge (religion): 10
  Perception: 8
  Sense Motive: 8
  Spellcraft: 11
languages:
- Common
special_qualities:
- healer's blessing
gear:
  gear:
  - +2 full plate
  - +2 heavy wooden shield
  - +1 merciful morningstar
  - masterwork light crossbow with 10 bolts
  - dagger
  - cloak of resistance +1
  - healer's kit
npc_boon: A priest can accompany PCs or send a patrol of four temple guards to assist
  them for up to 3 days. She can also craft magical arms and armor at a 10% discount.
desc_long: A priest is a leader within his church, spreading the faith by any means
  necessary, even through conversion at swordpoint when argument fails. A priest can
  be a crusader, warpriest, or divine champion. A priest might be advisor to a noble
  (CR 10), or travel with a retinue of a dozen temple guards (CR 10).

---

# Temple (Priest)

**Source** GameMastery Guide pg. 305
**XP** 4,800
Human _[[classes/Cleric|cleric]]_ 9

LN Medium humanoid
**Init** +1; **Senses** Perception +8

##### Defense

**AC** 26, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+11 armor, +1 Dex, +4 _[[spells/Shield|shield]]_)
**hp** 70 (9d8+30)
**Fort** +9, **Ref** +5, **Will** +11

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Merciful|merciful]]_ _[[items/Weapon/Morningstar|morningstar]]_ +9/+4 (1d8+3 plus 1d6 nonlethal) or _[[items/Weapon/Dagger|dagger]]_ +8/+3 (1d4+2/19–20)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d8/19–20) or _dagger_ +7 (1d4+2/19–20)
**Special Attacks** channel positive energy 5/day (DC 14, 5d6), staff of order (4 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th, concentration +13)
7/day—_[[spells/Rebuke|rebuke]]_ death, touch of law
**_Cleric_ Spells Prepared **(CL 9th, concentration +13)
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Righteous Might|righteous might]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Freedom of Movement|freedom of movement]]_, order’s wrath (DC 18), _[[spells/Spell Immunity|spell immunity]]_
3rd—_[[spells/Daylight|daylight]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, _[[spells/Prayer|prayer]]_, _[[spells/Searing Light|searing light]]_
2nd—aid, bull’s strength, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Delay Poison|delay poison]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Status|status]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Divine Favor|divine favor]]_ (2), _[[spells/Protection From Chaos|protection from chaos]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, stabilize
**D** domain spell; **Domains** Healing, Law

##### Statistics
**Str** 14, **Dex** 12, **Con** 14, **Int** 8, **Wis** 18, **Cha** 10
**Base Atk** +6; **CMB** +8; **CMD** 19
**Feats** Armor Proficiency (heavy), _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Shield Focus|Shield Focus]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Diplomacy +5, _[[spells/Heal|Heal]]_ +10, Knowledge (religion) +10, Perception +8, Sense Motive +8, Spellcraft +11
**Languages** Common
**SQ** _[[npcs/Healer|healer]]_’s blessing
**Gear** +2 _[[items/Armor/Full plate|full plate]]_, +2 _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _merciful_ _morningstar_, masterwork _light crossbow_ with 10 bolts, _dagger_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _healer_’s kit

**Boon** A priest can accompany PCs or send a patrol of four temple guards to assist them for up to 3 days. She can also craft magical arms and armor at a 10% discount.

A priest is a leader within his church, spreading the faith by any means necessary, even through conversion at swordpoint when argument fails. A priest can be a crusader, _[[classes/Warpriest|warpriest]]_, or divine _[[items/Armor Magic Abilities/Champion|champion]]_. A priest might be advisor to a noble (CR 10), or travel with a retinue of a dozen temple guards (CR 10).