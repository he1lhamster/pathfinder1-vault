---
cssclass: [monsters]
title1: Sylvan Protector
title2: Sylvan Protector
CR: 2
sources:
- name: NPC Codex
  page: 63
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 600
race: Gnome
classes:
- druid 3
alignment: CN
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 18
  touch: 13
  flat_footed: 16
  components:
    armor: 3
    dex: 2
    shield: 2
    size: 1
HP:
  HP: 24
  long: 3d8+7
saves:
  fort: 5
  ref: 3
  will: 5
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: sickle +1 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: sickle
      bonus:
      - 1
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
spell_like_abilities:
  entries:
  - name: lightning arc
    source: default
    freq: 5/day
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
  sources:
  - name: default
    CL: 3
    concentration: 5
spells:
  entries:
  - name: flaming sphere
    source: Druid
    level: 2
    DC: 14
  - name: summon swarm
    source: Druid
    level: 2
  - is_domain_spell: true
    name: wind wall
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 12
  - name: light
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  - name: virtue
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 3
    concentration: 5
    slots:
      0: at-will
    domains:
    - air
tactics:
  During Combat: The druid casts spider climb and hides, then casts obscuring mist.
ability_scores:
  STR: 6
  DEX: 14
  CON: 15
  INT: 10
  WIS: 15
  CHA: 14
BAB: 2
CMB: -1
CMD: 11
feats:
- name: Augment Summoning
- name: Spell Focus (conjuration)
skills:
  Handle Animal: 7
  Heal: 6
  Knowledge (nature): 6
  Perception: 8
  Spellcraft: 6
  Stealth: 8
  Survival: 10
languages:
- Common
- Druidic
- Gnome
special_qualities:
- nature bond (Air domain)
- nature sense
- wild empathy +5
- woodland stride
- trackless step
gear:
  combat:
  - scrolls of cure light wounds (3)
  - scroll of spider climb
  - tanglefoot bags (2)
  other:
  - +1 leather armor
  - masterwork heavy wooden shield
  - sickle
  - holly and mistletoe
  - spell component pouch
  - 95 gp
desc_long: There is no description for this NPC.

---

# Sylvan Protector

**Source** NPC Codex pg. 63
**XP** 600
Gnome _[[classes/Druid|druid]]_ 3

CN Small humanoid (gnome)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 armor, +2 Dex, +2 _[[spells/Shield|shield]]_, +1 size)
**hp** 24 (3d8+7)
**Fort** +5, **Ref** +3, **Will** +5; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 dodge bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Sickle|sickle]]_ +1 (1d4–2)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +5)
5/day—_[[spells/Lightning Arc|lightning arc]]_
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Druid_ Spells Prepared **(CL 3rd; concentration +5)
2nd—_[[spells/Flaming Sphere|flaming sphere]]_ (DC 14), _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Obscuring Mist|obscuring mist]]_, _speak with animals_
0 (at will)—_[[spells/Flare|flare]]_ (DC 12), light, stabilize, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domain **Air

### Tactics

**During Combat **The _druid_ casts _[[spells/Spider Climb|spider climb]]_ and hides, then casts _obscuring mist_.

##### Statistics
**Str** 6, **Dex** 14, **Con** 15, **Int** 10, **Wis** 15, **Cha** 14
**Base Atk** +2; **CMB** –1; **CMD** 11
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration)
**Skills** Handle Animal +7, _[[spells/Heal|Heal]]_ +6, Knowledge (nature) +6, Perception +8, Spellcraft +6, Stealth +8, Survival +10
**Languages** Common, Druidic, Gnome
**SQ** nature bond (Air domain), nature sense, wild _[[feats/Empathy|empathy]]_ +5, woodland stride, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step
**Combat Gear** scrolls of _cure light wounds_ (3), scroll of _spider climb_, tanglefoot bags (2); **Other Gear** +1 _[[items/Armor/Leather armor|leather armor]]_, masterwork _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, _sickle_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 95 gp

There is no description for this NPC.