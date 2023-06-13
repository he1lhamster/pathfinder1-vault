---
cssclass: [monsters]
title1: Troll, Troll Elder Matron
title2: Troll Elder Matron
CR: 10
sources:
- name: Monster Codex
  page: 230
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 9600
race: Troll
classes:
- witch 10 (Pathfinder RPG Advanced Player's Guide 65)
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 18
  touch: 11
  flat_footed: 16
  components:
    armor: 2
    dex: 2
    natural: 5
    size: -1
HP:
  HP: 200
  long: 6d8+10d6+138
  HD: 16
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 17
  ref: 8
  will: 12
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +12 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: bite
      bonus:
      - 12
    - text: 2 claws +12 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 12
  special:
  - hexes (agony [10 rounds], cackle, evil eye [-4, 6 rounds], misfortune [2 rounds],
    slumber [10 rounds], water lung)
  - rend (2 claws, 1d6+7)
space: 10
reach: 10
spells:
  entries:
  - name: flame strike
    source: Witch
    level: 5
    DC: 20
  - superscripts:
    - APG
    name: mass pain strike
    source: Witch
    level: 5
    DC: 18
  - name: confusion
    source: Witch
    level: 4
    DC: 17
  - name: enervation
    source: Witch
    level: 4
  - name: wall of ice
    source: Witch
    level: 4
    DC: 17
  - name: fireball
    source: Witch
    level: 3
    count: 2
    DC: 18
  - name: ray of exhaustion
    source: Witch
    level: 3
    DC: 16
  - superscripts:
    - APG
    name: screech
    source: Witch
    level: 3
    DC: 16
  - name: bull's strength
    source: Witch
    level: 2
  - superscripts:
    - APG
    name: burning gaze
    source: Witch
    level: 2
    DC: 17
  - name: enthrall
    source: Witch
    level: 2
    DC: 15
  - name: flaming sphere
    source: Witch
    level: 2
    DC: 17
  - name: touch of idiocy
    source: Witch
    level: 2
  - name: burning hands
    source: Witch
    level: 1
    DC: 16
  - name: cause fear
    source: Witch
    level: 1
    DC: 14
  - name: ray of enfeeblement
    source: Witch
    level: 1
    DC: 14
  - name: reduce person
    source: Witch
    level: 1
    DC: 14
  - name: bleed
    source: Witch
    level: 0
    DC: 13
  - name: detect magic
    source: Witch
    level: 0
  - name: purify food and drink
    source: Witch
    level: 0
  - name: touch of fatigue
    source: Witch
    level: 0
    DC: 13
  sources:
  - name: Witch
    type: prepared
    CL: 10
    concentration: 13
    slots:
      0: at-will
    patron: elements
tactics:
  During Combat: The troll elder matron attacks with flame strike or mass pain strike.
    She then adjusts her strategy to suit her opponents, usually choosing the misfortune
    or evil eye hex and using Split Hex to apply it to the two enemies who would be
    most hindered by it.
ability_scores:
  STR: 19
  DEX: 14
  CON: 27
  INT: 16
  WIS: 11
  CHA: 8
BAB: 9
CMB: 14
CMD: 26
feats:
- name: Combat Casting
- name: Craft Wondrous Item
- superscripts:
  - APG
  name: Elemental Focus (fire)
- superscripts:
  - APG
  name: Greater Elemental Focus (fire)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Split Hex
skills:
  Bluff: 7
  Intimidate: 14
  Knowledge (arcana): 14
  Knowledge (nature): 11
  Perception: 16
  Sense Motive: 8
  Spellcraft: 11
  Stealth: 8
  Survival: 8
  Swim: 9
languages:
- Abyssal
- Giant
- Goblin
- Orc
special_qualities:
- witch's familiar (bat)
gear:
  combat:
  - dust of disappearance
  other:
  - bracers of armor +2
  - cloak of resistance +1
  - headband of vast intelligence +4
  - 500 gp
ecology:
  environment: cold mountains
desc_long: A troll elder matron serves her tribe as the fount of all magical knowledge.
  She is both her tribemates' fiercest protector and their harshest critic, doling
  out punishments to those who fail to achieve the (sometimes cryptic) goals she sets
  for them. Female trolls benefit from a matron's teachings almost exclusively, though
  she might set a promising young male on the path toward becoming a ranger. The matron
  often lives or travels with females nearing adulthood who are struggling with their
  studies; those she rejects as unworthy rejoin their sisters and never speak of the
  strange things they experienced while apprenticed to the matron. Even a troll monarch
  listens to an elder matron's counsel, for she has outlived many monarchs and watched
  generations of trolls be born, grow, and die.

---

# Troll, Troll Elder Matron

**Source** Monster Codex pg. 230
**XP** 9,600
_[[monsters/Troll|Troll]]_ _[[classes/Witch|witch]]_ 10 (Pathfinder RPG Advanced Player’s Guide 65)
CE Large humanoid (giant)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +16

##### Defense

**AC** 18, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 armor, +2 Dex, +5 natural, –1 size)
**hp** 200 (16 HD; 6d8+10d6+138); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +17, **Ref** +8, **Will** +12

##### Offense
**Speed** 30 ft.
**Melee** bite +12 (1d8+4), 2 claws +12 (1d6+4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** hexes (agony [10 rounds], cackle, evil eye [–4, 6 rounds], misfortune [2 rounds], slumber [10 rounds], water lung), _[[universal monster rules/Rend|rend]]_ (2 claws, 1d6+7)
**_Witch_ Spells Prepared **(CL 10th; concentration +13)
5th—_[[spells/Flame Strike|flame strike]]_ (DC 20), mass _[[spells/Pain Strike|pain strike]]_ (DC 18)
4th—_[[spells/Confusion|confusion]]_ (DC 17), _[[spells/Enervation|enervation]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 17)
3rd—_[[spells/Fireball|fireball]]_ (2, DC 18), _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 16), _[[spells/Screech|screech]]_ (DC 16)
2nd—bull’s strength, _[[spells/Burning Gaze|burning gaze]]_ (DC 17), _[[spells/Enthrall|enthrall]]_ (DC 15), _[[spells/Flaming Sphere|flaming sphere]]_ (DC 17), _[[spells/Touch of Idiocy|touch of idiocy]]_
1st—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Reduce Person|reduce person]]_ (DC 14)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 13)
**Patron **elements

### Tactics

**During Combat** The _troll_ elder matron attacks with _flame strike_ or mass _pain strike_. She then adjusts her strategy to suit her opponents, usually choosing the misfortune or evil eye hex and using _[[feats/Split Hex|Split Hex]]_ to apply it to the two enemies who would be most hindered by it.

##### Statistics
**Str** 19, **Dex** 14, **Con** 27, **Int** 16, **Wis** 11, **Cha** 8
**Base Atk** +9; **CMB** +14; **CMD** 26
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Elemental Focus|Elemental Focus]]_ (fire), _[[feats/Greater Elemental Focus|Greater Elemental Focus]]_ (fire), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _Split Hex_
**Skills** Bluff +7, Intimidate +14, Knowledge (arcana) +14, Knowledge (nature) +11, Perception +16, Sense Motive +8, Spellcraft +11, Stealth +8, Survival +8, Swim +9
**Languages** Abyssal, Giant, _[[monsters/Goblin|Goblin]]_, _[[monsters/Orc|Orc]]_
**SQ** _witch_’s familiar (bat)
**Combat Gear** _[[items/Wondrous Item/Dust of Disappearance|dust of disappearance]]_; **Other Gear** _[[items/Wondrous Item/Bracers of Armor +2|bracers of armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +4|headband of vast intelligence +4]]_, 500 gp

##### Ecology

**Environment** cold mountains

##### Description

A _troll_ elder matron serves her tribe as the fount of all magical knowledge. She is both her tribemates’ fiercest protector and their harshest critic, doling out punishments to those who fail to achieve the (sometimes cryptic) goals she sets for them. Female trolls benefit from a matron’s teachings almost exclusively, though she might set a promising young male on the path toward becoming a _[[classes/Ranger|ranger]]_. The matron often lives or travels with females nearing adulthood who are struggling with their studies; those she rejects as unworthy rejoin their sisters and never speak of the strange things they experienced while apprenticed to the matron. Even a _troll_ monarch listens to an elder matron’s counsel, for she has outlived many monarchs and watched generations of trolls be born, grow, and die.