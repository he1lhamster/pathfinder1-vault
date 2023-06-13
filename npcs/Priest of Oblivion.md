---
cssclass: [monsters]
title1: Priest of Oblivion
title2: Priest of Oblivion
CR: 18
sources:
- name: NPC Codex
  page: 60
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Human
classes:
- cleric of Zon-Kuthon 19
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
AC:
  AC: 31
  touch: 14
  flat_footed: 31
  components:
    armor: 13
    deflection: 4
    natural: 2
    shield: 2
HP:
  HP: 184
  long: 19d8+95
saves:
  fort: 16
  ref: 7
  will: 18
speeds:
  base: 20
attacks:
  melee:
  - - text: +4 spiked chain +23/+18/+13 (2d4+10/19-20)
      entries:
      - - damage: 2d4+10
          crit_range: 19-20
      attack: +4 spiked chain
      bonus:
      - 23
      - 18
      - 13
  special:
  - channel negative energy 7/day (DC 23, 12d6)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 9/day
    other: 9 rounds
  - name: touch of darkness
    source: default
    freq: 9/day
    other: 9 rounds
  sources:
  - name: default
    CL: 19
    concentration: 25
spells:
  entries:
  - name: energy drain
    source: Cleric
    level: 9
    DC: 25
  - name: etherealness
    source: Cleric
    level: 9
  - name: implosion
    source: Cleric
    level: 9
    DC: 25
  - is_domain_spell: true
    name: wail of the banshee
    source: Cleric
    level: 9
    DC: 25
  - name: antimagic field
    source: Cleric
    level: 8
  - is_domain_spell: true
    name: create greater undead
    source: Cleric
    level: 8
  - name: earthquake
    source: Cleric
    level: 8
  - name: fire storm
    source: Cleric
    level: 8
    DC: 24
  - name: blasphemy
    source: Cleric
    level: 7
    count: 2
    DC: 23
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: power word blind
    source: Cleric
    level: 7
  - name: repulsion
    source: Cleric
    level: 7
    DC: 23
  - name: antilife shell
    source: Cleric
    level: 6
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 22
  - name: harm
    source: Cleric
    level: 6
    count: 2
    DC: 22
  - is_domain_spell: true
    name: shadow walk
    source: Cleric
    level: 6
    DC: 22
  - name: word of recall
    source: Cleric
    level: 6
  - name: greater command
    source: Cleric
    level: 5
    DC: 21
  - name: insect plague
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: slay living
    source: Cleric
    level: 5
    count: 2
  - name: unhallow
    source: Cleric
    level: 5
  - name: wall of stone
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: death ward
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
  - name: neutralize poison
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 20
  - is_domain_spell: true
    name: deeper darkness
    source: Cleric
    level: 3
    count: 2
  - name: dispel magic
    source: Cleric
    level: 3
    count: 2
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: darkness
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
    DC: 18
  - name: desecrate
    source: Cleric
    level: 2
  - name: gentle repose
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 18
  - name: shield other
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 17
  - name: bless
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 17
  - name: deathwatch
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 17
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 19
    concentration: 25
    slots:
      0: at-will
    domains:
    - darkness
    - death
tactics:
  Before Combat: The cleric casts air walk, freedom of movement, greater magic weapon,
    and magic vestment.
  During Combat: The cleric uses melee attacks and channeled energy against close
    opponents. Against ranged opponents, he uses spells to divide, blind, and kill.
  Base Statistics: Without greater magic weapon and magic vestment, the cleric's statistics
    are AC 28, touch 14, flat-footed 28; Melee +1 spiked chain +20/+15/+10 (2d4+7/19-20).
ability_scores:
  STR: 18
  DEX: 10
  CON: 18
  INT: 8
  WIS: 22
  CHA: 14
BAB: 14
CMB: 18
CMD: 32
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Command Undead
- name: Critical Focus
- name: Extra Channel
- name: Heavy Armor Proficiency
- name: Improved Channel
- name: Improved Critical (spiked chain)
- name: Improved Initiative
- name: Selective Channeling
- name: Vital Strike
- name: Weapon Focus (spiked chain)
skills:
  Knowledge (local): 4
  Knowledge (religion): 12
  Perception: 21
  Sense Motive: 17
languages:
- Common
special_qualities:
- aura
- death's embrace
- eyes of darkness (9 rounds/day)
gear:
  gear:
  - +1 full plate
  - +1 spiked chain
  - javelin of lightning
  - amulet of natural armor +2
  - belt of physical might +4 (Str, Con)
  - cloak of resistance +1
  - headband of mental prowess +2 (Wis, Cha)
  - phylactery of negative channeling
  - ring of force shield
  - ring of protection +4
  - silver unholy symbol
  - unholy water
  - materials for unhallow (worth 1,000 gp)
  - onyx gems (worth 1,500 gp each)
  - platinum rings for shield other (worth 100 gp)
  - silver dust for desecrate (worth 25 gp)
  - 3,450 gp
desc_long: The priest of oblivion wishes to drown all creatures in darkness and despair,
  then defile their bodies and raise them as undead.

---

# Priest of Oblivion

**Source** NPC Codex pg. 60
**XP** 153,600
Human _[[classes/Cleric|cleric]]_ of Zon-Kuthon 19

NE Medium humanoid (human)
**Init** +4; **Senses** Perception +21

##### Defense

**AC** 31, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+13 armor, +4 _[[spells/Deflection|deflection]]_, +2 natural, +2 _[[spells/Shield|shield]]_)
**hp** 184 (19d8+95)
**Fort** +16, **Ref** +7, **Will** +18

##### Offense
**Speed** 20 ft.
**Melee** +4 _[[items/Weapon/Spiked chain|spiked chain]]_ +23/+18/+13 (2d4+10/19–20)
**Special Attacks** channel negative energy 7/day (DC 23, 12d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +25)
9/day—bleeding touch (9 rounds), touch of _[[spells/Darkness|darkness]]_ (9 rounds)
**_Cleric_ Spells Prepared **(CL 19th; concentration +25)
9th—_[[universal monster rules/Energy Drain|energy drain]]_ (DC 25), _[[spells/Etherealness|etherealness]]_, _[[spells/Implosion|implosion]]_ (DC 25), wail of the bansheeD (DC 25)
8th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Create Greater Undead|create greater undead]]_, _[[spells/Earthquake|earthquake]]_, _[[spells/Fire Storm|fire storm]]_ (DC 24)
7th—_[[spells/Blasphemy|blasphemy]]_ (2, DC 23), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Repulsion|repulsion]]_ (DC 23)
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Blade Barrier|blade barrier]]_ (DC 22), _[[spells/Harm|harm]]_ (2, DC 22), _[[items/Armor Magic Abilities/Shadow|shadow]]_ walkD (DC 22), _[[spells/Word of Recall|word of recall]]_
5th—greater _[[spells/Command|command]]_ (DC 21), _[[spells/Insect Plague|insect plague]]_, slay livingD (2), _[[spells/Unhallow|unhallow]]_, _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3rd—deeper darknessD (2), _[[spells/Dispel Magic|dispel magic]]_ (2), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_
2nd—_darkness_, _[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/Desecrate|desecrate]]_, _[[spells/Gentle Repose|gentle repose]]_, _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Shield Other|shield other]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 17), _[[spells/Bless|bless]]_, cause fearD (DC 17), _[[spells/Deathwatch|deathwatch]]_, _[[spells/Doom|doom]]_ (DC 17), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **_Darkness_, Death

### Tactics

**Before Combat **The _cleric_ casts _air walk_, _freedom of movement_, greater _magic weapon_, and _magic vestment_.
**During Combat **The _cleric_ uses melee attacks and channeled energy against close opponents. Against ranged opponents, he uses spells to divide, blind, and kill.
**Base Statistics **Without greater _magic weapon_ and _magic vestment_, the _cleric_’s statistics are **AC **28, touch 14, _flat-footed_ 28; **Melee** +1 _spiked chain_ +20/+15/+10 (2d4+7/19–20).

##### Statistics
**Str** 18, **Dex** 10, **Con** 18, **Int** 8, **Wis** 22, **Cha** 14
**Base Atk** +14; **CMB** +18; **CMD** 32
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Critical|Improved Critical]]_ (_spiked chain_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spiked chain_)
**Skills** Knowledge (local) +4, Knowledge (religion) +12, Perception +21, Sense Motive +17
**Languages** Common
**SQ** aura, death’s embrace, eyes of _darkness_ (9 rounds/day)
**Gear** +1 _[[items/Armor/Full plate|full plate]]_, +1 _spiked chain_, _[[items/Wondrous Item/Javelin of Lightning|javelin of lightning]]_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Mental Prowess +2|headband of mental prowess +2]]_ (Wis, Cha), _[[items/Wondrous Item/Phylactery of Negative Channeling|phylactery of negative channeling]]_, _[[items/Ring/Ring of Force Shield|ring of force shield]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, _unholy_ water, materials for _unhallow_ (worth 1,000 gp), onyx gems (worth 1,500 gp each), platinum rings for _shield other_ (worth 100 gp), silver dust for _desecrate_ (worth 25 gp), 3,450 gp

The _[[npcs/Priest of Oblivion|priest of oblivion]]_ wishes to drown all creatures in _darkness_ and despair, then defile their bodies and raise them as undead.