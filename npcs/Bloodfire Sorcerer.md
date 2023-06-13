---
cssclass: [monsters]
title1: Bloodfire Sorcerer
title2: Bloodfire Sorcerer
CR: 6
sources:
- name: NPC Codex
  page: 164
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Half-orc
classes:
- sorcerer 7
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 17
  touch: 12
  flat_footed: 16
  components:
    armor: 4
    deflection: 1
    dex: 1
    natural: 1
HP:
  HP: 60
  long: 7d6+33
saves:
  fort: 3
  ref: 3
  will: 7
defensive_abilities:
- orc ferocity
resistances:
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk falchion +7 (2d4+4/18-20)
      entries:
      - - damage: 2d4+4
          crit_range: 18-20
      attack: mwk falchion
      bonus:
      - 7
  ranged:
  - - text: mwk heavy crossbow +5 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 5
spell_like_abilities:
  entries:
  - name: elemental ray
    source: default
    freq: 6/day
    other: 1d6+3 fire
  sources:
  - name: default
    CL: 7
    concentration: 10
spells:
  entries:
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 17
  - name: haste
    source: Sorcerer
    level: 3
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: blur
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 15
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 15
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: magic weapon
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 14
  - name: shield
    source: Sorcerer
    level: 1
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 13
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 14
  - name: light
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
    other: fire
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 10
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
    bloodline: elemental (fire)
tactics:
  Before Combat: The sorcerer casts false life and mage armor.
  During Combat: The sorcerer casts haste before targeting her foes with fireball
    or scorching ray. In melee combat, she casts shield on herself, and magic weapon
    on her falchion.
  Base Statistics: Without false life and mage armor, the sorcerer's statistics are
    AC 13, touch 11, flat-footed 12; hp 48.
ability_scores:
  STR: 16
  DEX: 12
  CON: 13
  INT: 8
  WIS: 10
  CHA: 16
BAB: 3
CMB: 6
CMD: 18
feats:
- name: Combat Casting
- name: Eschew Materials
- name: Iron Will
- name: Power Attack
- name: Spell Focus (evocation)
- name: Toughness
skills:
  Intimidate: 11
  Knowledge (arcana): 3
  Linguistics: 0
  Perception: 7
  Spellcraft: 4
languages:
- Common
- Ignan
- Orc
special_qualities:
- bloodline arcana (change energy damage spells to fire)
- orc blood
- weapon familiarity
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of fly (2)
  other:
  - masterwork falchion
  - masterwork heavy crossbow with 10 bolts
  - amulet of natural armor +1
  - ring of protection +1
  - 225 gp
desc_long: The bloodfire sorcerer withers her enemies with flame and quickens her
  allies with hot-blooded ferocity.

---

# Bloodfire Sorcerer

**Source** NPC Codex pg. 164
**XP** 2,400
Half-orc _[[classes/Sorcerer|sorcerer]]_ 7

NE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +7

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 natural)
**hp** 60 (7d6+33)
**Fort** +3, **Ref** +3, **Will** +7
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Resist** fire 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Falchion|falchion]]_ +7 (2d4+4/18–20)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +5 (1d10/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
6/day—elemental ray (1d6+3 fire)
**_Sorcerer_ Spells Known **(CL 7th; concentration +10)
3rd (5/day)—_[[spells/Fireball|fireball]]_ (DC 17), _[[spells/Haste|haste]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd (7/day)—_[[spells/Blur|blur]]_, _[[spells/False Life|false life]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 15), _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Shield|shield]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), light, _[[spells/Ray of Frost|ray of frost]]_ (fire), _[[spells/Read Magic|read magic]]_
**Bloodline **elemental (fire)

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _mage armor_.
**During Combat **The _sorcerer_ casts _haste_ before targeting her foes with _fireball_ or _scorching ray_. In melee combat, she casts _shield_ on herself, and _magic weapon_ on her _falchion_.
**Base Statistics **Without _false life_ and _mage armor_, the _sorcerer_’s statistics are **AC **13, touch 11, _flat-footed_ 12; **hp **48.

##### Statistics
**Str** 16, **Dex** 12, **Con** 13, **Int** 8, **Wis** 10, **Cha** 16
**Base Atk** +3; **CMB** +6; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_
**Skills** Intimidate +11, Knowledge (arcana) +3, Linguistics +0, Perception +7, Spellcraft +4
**Languages** Common, Ignan, _Orc_
**SQ** bloodline arcana (change energy damage spells to fire), _orc_ blood, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of fly (2); **Other Gear** masterwork _falchion_, masterwork _heavy crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 225 gp

The _[[npcs/Bloodfire Sorcerer|bloodfire sorcerer]]_ withers her enemies with flame and quickens her allies with hot-blooded _ferocity_.