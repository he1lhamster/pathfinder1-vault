---
cssclass: [monsters]
title1: Lizardfolk, Lizardfolk Clutch Mother
title2: Lizardfolk Clutch Mother
CR: 13
sources:
- name: Monster Codex
  page: 147
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 25600
race: Lizardfolk
classes:
- druid (ancient guardian) 12 (see page 140)
alignment: N
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 4
AC:
  AC: 22
  touch: 11
  flat_footed: 22
  components:
    armor: 6
    deflection: 1
    natural: 5
HP:
  HP: 95
  long: 14d8+32
saves:
  fort: 15
  ref: 7
  will: 16
  other: +4 vs. enchantments
immunities:
- poison
speeds:
  base: 20
  swim: 25
attacks:
  melee:
  - - text: +1 spear +11/+6 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 11
      - 6
    - text: bite +5 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - 5
  - - text: 2 claws +10 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 10
    - text: bite +5 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - 5
  ranged:
  - - text: mwk sling +11 (1d4)
      entries:
      - - damage: 1d4
      attack: mwk sling
      bonus:
      - 11
  special:
  - dispel hostility
  - undo artifice
  - wild shape 5/day
spells:
  entries:
  - is_domain_spell: true
    name: antimagic field
    source: Druid
    level: 6
  - name: mass cure light wounds
    source: Druid
    level: 6
  - name: wall of stone
    source: Druid
    level: 6
    DC: 21
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 20
  - name: commune with nature
    source: Druid
    level: 5
  - name: death ward
    source: Druid
    level: 5
  - is_domain_spell: true
    name: spell resistance
    source: Druid
    level: 5
  - name: wall of thorns
    source: Druid
    level: 5
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: scrying
    source: Druid
    level: 4
    DC: 19
  - is_domain_spell: true
    name: spell immunity
    source: Druid
    level: 4
  - name: call lightning
    source: Druid
    level: 3
    DC: 18
  - name: cure moderate wounds
    source: Druid
    level: 3
    count: 2
  - is_domain_spell: true
    name: protection from energy
    source: Druid
    level: 3
  - superscripts:
    - UM
    name: spit venom
    source: Druid
    level: 3
    DC: 18
  - name: animal messenger
    source: Druid
    level: 2
  - name: barkskin
    source: Druid
    level: 2
  - name: delay poison
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
    count: 2
  - is_domain_spell: true
    name: shield other
    source: Druid
    level: 2
  - name: calm animals
    source: Druid
    level: 1
    DC: 16
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: entangle
    source: Druid
    level: 1
    DC: 16
  - is_domain_spell: true
    name: sanctuary
    source: Druid
    level: 1
    DC: 16
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect poison
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 12
    concentration: 17
    slots:
      0: at-will
    domains:
    - protection
tactics:
  During Combat: The clutch mother uses spells and weapons to defend first the clutch
    and then the tribe.
ability_scores:
  STR: 10
  DEX: 11
  CON: 12
  INT: 12
  WIS: 20
  CHA: 15
BAB: 10
CMB: 10
CMD: 21
feats:
- name: Alertness
- name: Brew Potion
- name: Improved Initiative
- name: Natural Spell
- name: Skill Focus (Diplomacy)
- name: Toughness
- superscripts:
  - UM
  name: Wild Speech
skills:
  Acrobatics: 2
  Diplomacy: 23
  Handle Animal: 11
  Heal: 14
  Knowledge (nature): 13
  Linguistics: 2
  Perception: 22
  Perform (oratory): 15
  Sense Motive: 27
  Spellcraft: 11
  Survival: 16
  Swim: 15
  _racial_mods:
    Acrobatics:
      _: 4
languages:
- Common
- Draconic
- Druidic
- Sylvan
special_qualities:
- ancient ways
- hold breath
- nature bond (Protection domain)
- nature sense
- patience of nature
gear:
  combat:
  - scroll of charm animal
  - scroll of resist energy
  - wand of cure light wounds (15 charges)
  other:
  - +2 hide armor
  - +1 spear
  - mwk sling with 12 bullets
  - druid's vestments
  - headband of inspired wisdom +2
  - pearl of power (2nd)
  - ring of protection +1
  - healer's kit (9 uses)
  - 38 gp
ecology:
  environment: temperate swamps
desc_long: |-
  The clutch mother seeks only to protect her ways and her kind. She faces the onslaught of civilization with diplomacy, reason, and patience.

  While other races might see guarding the children as a waste of one's best warriors, lizardfolk inherently value defense over offense. They think warm-blooded races are insane for sending all their capable combatants off to fight in distant wars, leaving only the aged and infirm to protect the children. Clutch mother (or occasionally clutch father) is a position of prominence and prestige, and many lizardfolk warriors compete eagerly to prove themselves worthy of this great responsibility.

---

# Lizardfolk, Lizardfolk Clutch Mother

**Source** Monster Codex pg. 147
**XP** 25,600
_[[monsters/Lizardfolk|Lizardfolk]]_ _[[classes/Druid|druid]]_ (ancient _[[items/Weapon Magic Abilities/Guardian|guardian]]_) 12 (see page 140)

N Medium humanoid (reptilian)
**Init** +4; **Senses** Perception +22

##### Defense

**AC** 22, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +5 natural)
**hp** 95 (14d8+32)
**Fort** +15, **Ref** +7, **Will** +16; +4 vs. enchantments
**Immune** poison

##### Offense
**Speed** 20 ft., swim 25 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +11/+6 (1d8+1/×3), bite +5 (1d4) or 2 claws +10 (1d4), bite +5 (1d4)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +11 (1d4)
**Special Attacks** dispel hostility, undo artifice, wild shape 5/day
**_Druid_ Spells Prepared **(CL 12th; concentration +17)
6th—_[[spells/Antimagic Field|antimagic field]]_, mass _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Wall Of Stone|wall of stone]]_ (DC 21)
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Commune with Nature|commune with nature]]_, _[[spells/Death Ward|death ward]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Scrying|scrying]]_ (DC 19), _[[spells/Spell Immunity|spell immunity]]_
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 18), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Spit Venom|spit venom]]_ (DC 18)
2nd—_[[spells/Animal Messenger|animal messenger]]_, _[[spells/Barkskin|barkskin]]_, _[[spells/Delay Poison|delay poison]]_, lesser _[[spells/Restoration|restoration]]_ (2), _[[spells/Shield Other|shield other]]_
1st—_[[spells/Calm Animals|calm animals]]_ (DC 16), _cure light wounds_ (2), _[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Sanctuary|sanctuary]]_ (DC 16), _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_
**D** domain spell; **Domain** Protection

### Tactics

**During Combat** The clutch mother uses spells and weapons to defend first the clutch and then the tribe.

##### Statistics
**Str** 10, **Dex** 11, **Con** 12, **Int** 12, **Wis** 20, **Cha** 15
**Base Atk** +10; **CMB** +10; **CMD** 21
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Diplomacy), _[[feats/Toughness|Toughness]]_, _[[feats/Wild Speech|Wild Speech]]_
**Skills** Acrobatics +2, Diplomacy +23, Handle Animal +11, _[[spells/Heal|Heal]]_ +14, Knowledge (nature) +13, Linguistics +2, Perception +22, Perform (oratory) +15, Sense Motive +27, Spellcraft +11, Survival +16, Swim +15; **Racial Modifiers** +4 Acrobatics
**Languages** Common, Draconic, Druidic, Sylvan
**SQ** ancient ways, _[[universal monster rules/Hold Breath|hold breath]]_, nature bond (Protection domain), nature sense, patience of nature
**Combat Gear** scroll of _[[spells/Charm Animal|charm animal]]_, scroll of _[[spells/Resist Energy|resist energy]]_, wand of _cure light wounds_ (15 charges); **Other Gear** +2 _[[items/Armor/Hide armor|hide armor]]_, +1 _spear_, mwk _sling_ with 12 bullets, _druid_’s vestments, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, pearl of power (2nd), _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[npcs/Healer|healer]]_’s kit (9 uses), 38 gp

##### Ecology

**Environment** temperate swamps

##### Description

The clutch mother seeks only to protect her ways and her kind. She faces the _[[feats/Onslaught|onslaught]]_ of civilization with diplomacy, reason, and patience.

While other races might see _[[items/Armor Magic Abilities/Guarding|guarding]]_ the children as a waste of one’s best warriors, _lizardfolk_ inherently value defense over offense. They think warm-blooded races are insane for _[[spells/Sending|sending]]_ all their capable combatants off to fight in distant wars, leaving only the aged and infirm to protect the children. Clutch mother (or occasionally clutch father) is a position of prominence and prestige, and many _lizardfolk_ warriors compete eagerly to prove themselves worthy of this great responsibility.