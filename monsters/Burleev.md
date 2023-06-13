---
cssclass: [monsters]
title1: Burleev
desc_short: This creature looks like a humanoid skeleton with a complete set of internal
  organs. A violet glow replaces its missing flesh.
title2: Burleev
CR: 4
sources:
- name: Inner Sea Gods
  page: 299
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 1200
alignment: N
size: Medium
type: outsider
subtypes:
- cold or fire
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 60
  detect magic: true
AC:
  AC: 16
  touch: 10
  flat_footed: 16
  components:
    natural: 6
HP:
  HP: 32
  long: 5d10+5
saves:
  fort: 5
  ref: 3
  will: 5
defensive_abilities:
- frostfire spirit
DR:
- amount: 5
  weakness: magic
immunities:
- cold or fire
SR: 15
weaknesses:
- vulnerable to cold or fire
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 slams +5 (1d6 plus 1d6 cold or fire)
      entries:
      - - damage: 1d6
        - damage: 1d6
          type: cold or fire
      count: 2
      attack: slams
      bonus:
      - 5
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - name: read magic
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: invisibility
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 5
    concentration: 8
spells:
  entries:
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: daze monster
    source: Sorcerer
    level: 2
    DC: 15
  - name: chill touch
    source: Sorcerer
    level: 1
    DC: 14
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 14
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: sleep
    source: Sorcerer
    level: 1
    DC: 14
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 13
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 5
    concentration: 8
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 11
  DEX: 10
  CON: 13
  INT: 10
  WIS: 13
  CHA: 16
BAB: 5
CMB: 5
CMD: 15
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Intimidate: 11
  Knowledge (arcana): 8
  Knowledge (planes): 8
  Perception: 9
  Spellcraft: 8
  Stealth: 4
  Use Magic Device: 11
  _racial_mods:
    Stealth:
      _: 4
languages:
- Abyssal
- Celestial
- Draconic
- Protean
- read magic
ecology:
  environment: any (Maelstrom)
  organization: solitary, pair, or cabal (3-5)
  treasure_type: standard
special_abilities:
  Frostfire Spirit (Su): A burleev is surrounded by either cold or fire energy. The
    burleev can change the energy type as a swift action. When surrounded by fire,
    the burleev has the fire subtype, it adds fire damage to its attacks, and creatures
    striking it with melee weapons, natural attacks, or unarmed strikes take 1d6 points
    of fire damage; when surrounded by cold, it instead gains the cold subtype and
    deals cold damage rather than fire damage. It can also completely dampen its aura
    for 1d6 rounds, but cannot reactivate it until this time has passed.
  Spells: A burleev cast spells as a 5th-level sorcerer.
desc_long: |-
  A burleev is a planar explorer created by the power of Nethys. Some are his mortal petitioners assigned to this role after their death by a deliberate act of the god, whereas others are hapless visitors who were transformed by proximity to Nethys or certain parts of his realm. They serve as his eyes and ears on many planes, using their power to adapt to hostile environments and report their discoveries to his greater servitors. Each has a unique allotment of spells suited for its current task, and a burleev that has completed its service in one inhospitable location might be destroyed and recreated with a different array of arcane talents that suit it better for its next duty. The spells shown above represent those of a typical burleev.

  A burleev's supernatural nimbus burns brightly with cold or heat, making it painfully cold or hot to the touch. As a burleev discovers information useful to the god of magic, the color of its aura increases in intensity. The eldest of these creatures, or those that have travelled far from Nethys's realm in the Maelstrom for the longest, often burn like living pyres. These burleevs sometimes take sorcerer class levels as their magical power grows to match their ever-increasing knowledge. Should it later be crushed and reformed as part of its continuing duties, such a burleev retains much of its brightness and arcane might. A spellcaster whose research interests mirror those of a burleev can keep such an outsider's attention for days, weeks, or longer so long as the mortal continues to make new and exciting discoveries.

  Burleevs stand around 6 feet tall and weigh roughly 80 pounds.

---

# Burleev
This creature looks like a humanoid skeleton with a complete set of internal organs. A violet glow replaces its missing flesh.
**Source** Inner Sea Gods pg. 299
**XP** 1,200

N Medium outsider (cold or fire, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +9

##### Defense

**AC** 16, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 natural)
**hp** 32 (5d10+5)
**Fort** +5, **Ref** +3, **Will** +5
**Defensive Abilities** frostfire spirit; **DR** 5/magic; **Immune** cold or fire; **SR** 15
**Weaknesses** vulnerable to cold or fire

##### Offense
**Speed** 30 ft.
**Melee** 2 slams +5 (1d6 plus 1d6 cold or fire)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
At will—_detect magic_, _[[spells/Read Magic|read magic]]_
3/day—_[[spells/Cure Light Wounds|cure light wounds]]_
1/day—_[[spells/Invisibility|invisibility]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 5th; concentration +8)
2nd (5)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Daze Monster|daze monster]]_ (DC 15)
1st (7)—_[[spells/Chill Touch|chill touch]]_ (DC 14), _[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, sleep (DC 14)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 11, **Dex** 10, **Con** 13, **Int** 10, **Wis** 13, **Cha** 16
**Base Atk** +5; **CMB** +5; **CMD** 15
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Intimidate +11, Knowledge (arcana) +8, Knowledge (planes) +8, Perception +9, Spellcraft +8, Stealth +4, Use Magic Device +11; **Racial Modifiers** +4 Stealth
**Languages** Abyssal, Celestial, Draconic, Protean; _read magic_

##### Ecology

**Environment** any (Maelstrom)
**Organization** solitary, pair, or cabal (3–5)
**Treasure** standard

### Special Abilities

**Frostfire Spirit (Su)** A _[[monsters/Burleev|burleev]]_ is surrounded by either cold or fire energy. The _burleev_ can change the energy type as a swift action. When surrounded by fire, the _burleev_ has the fire subtype, it adds fire damage to its attacks, and creatures striking it with melee weapons, _[[universal monster rules/Natural Attacks|natural attacks]]_, or unarmed strikes take 1d6 points of fire damage; when surrounded by cold, it instead gains the cold subtype and deals cold damage rather than fire damage. It can also completely dampen its aura for 1d6 rounds, but cannot reactivate it until this time has passed.
**Spells **A _burleev_ cast spells as a 5th-level _sorcerer_.

##### Description

A _burleev_ is a _[[items/Weapon Magic Abilities/Planar|planar]]_ _[[feats/Explorer|explorer]]_ created by the power of Nethys. Some are his mortal petitioners assigned to this role after their death by a deliberate act of the god, whereas others are hapless visitors who were transformed by proximity to Nethys or certain parts of his realm. They serve as his eyes and ears on many planes, using their power to adapt to hostile environments and report their discoveries to his greater servitors. Each has a unique allotment of spells suited for its current task, and a _burleev_ that has completed its service in one inhospitable location might be destroyed and recreated with a different array of arcane talents that suit it better for its next duty. The spells shown above represent those of a typical _burleev_.

A _burleev_’s supernatural nimbus burns brightly with cold or _[[universal monster rules/Heat|heat]]_, making it painfully cold or hot to the touch. As a _burleev_ discovers information useful to the god of magic, the color of its aura increases in intensity. The eldest of these creatures, or those that have travelled far from Nethys’s realm in the Maelstrom for the longest, often _[[universal monster rules/Burn|burn]]_ like living pyres. These burleevs sometimes take _sorcerer_ class levels as their magical power grows to match their ever-increasing knowledge. Should it later be crushed and reformed as part of its continuing duties, such a _burleev_ retains much of its brightness and arcane might. A spellcaster whose research interests _[[items/Mundane/Mirror|mirror]]_ those of a _burleev_ can keep such an outsider’s attention for days, weeks, or longer so long as the mortal continues to make new and exciting discoveries.

Burleevs stand around 6 feet tall and weigh roughly 80 pounds.