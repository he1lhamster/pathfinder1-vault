---
cssclass: [monsters]
title1: Cannibal Zealot
desc_short: Crude designs painted in what can only be dried blood cake the face and
  the hide clothing of this rugged-looking human, whose grinning mouth is filled with
  sharp, filed teeth.
title2: Cannibal Zealot
CR: 6
sources:
- name: Tombs of Golarion
  page: 61
  link: http://paizo.com/products/btpy98yu?Pathfinder-Campaign-Setting-Tombs-of-Golarion
XP: 2400
race: Human
classes:
- barbarian 3
- inquisitor 4
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    armor: 4
    dex: 1
    dodge: 1
    shield: 1
HP:
  HP: 54
  long: 4d8+3d12+11
  HD: 7
saves:
  fort: 8
  ref: 3
  will: 8
defensive_abilities:
- trap sense +1
- uncanny dodge
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk light flail +10/+5 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: mwk light flail
      bonus:
      - 10
      - 5
  - - text: spear +9/+4 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: spear
      bonus:
      - 9
      - 4
  special:
  - judgment 2/day
  - rage (14 rounds/day)
  - rage power (animal fury)
spell_like_abilities:
  entries:
  - superscripts:
    - UM
    name: decompose corpse
    source: default
    freq: 1/day
  - name: detect alignment
    source: inquisitor
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 7
  - name: inquisitor
    CL: 4
    concentration: 7
spells:
  entries:
  - name: hold person
    source: Inquisitor
    level: 2
    DC: 15
  - superscripts:
    - APG
    name: weapon of awe
    source: Inquisitor
    level: 2
    DC: 15
  - name: command
    source: Inquisitor
    level: 1
    DC: 14
  - name: cure light wounds
    source: Inquisitor
    level: 1
  - name: shield of faith
    source: Inquisitor
    level: 1
  - superscripts:
    - APG
    name: wrath
    source: Inquisitor
    level: 1
  - name: bleed
    source: Inquisitor
    level: 0
    DC: 13
  - name: create water
    source: Inquisitor
    level: 0
  - name: daze
    source: Inquisitor
    level: 0
    DC: 13
  - name: guidance
    source: Inquisitor
    level: 0
  - name: light
    source: Inquisitor
    level: 0
  - name: stabilize
    source: Inquisitor
    level: 0
  sources:
  - name: Inquisitor
    type: known
    CL: 4
    concentration: 7
    slots:
      2: 2
      1: 4
      0: at-will
    inquisition: anger
ability_scores:
  STR: 16
  DEX: 13
  CON: 12
  INT: 8
  WIS: 16
  CHA: 10
BAB: 6
CMB: 9
CMD: 21
feats:
- name: Cleave
- name: Dodge
- name: Intimidating Prowess
- name: Polytheistic Blessing (Sar-Gorog pantheon; see the sidebar on page 63)
- name: Power Attack
- superscripts:
  - APG
  name: Precise Strike
skills:
  Craft (traps): 5
  Heal: 9
  Intimidate: 15
  Knowledge (nature): 5
  Perception: 9
  Sense Motive: 11
  Stealth: 9
  Survival: 13
languages:
- Polyglot
special_qualities:
- hateful retort
- monster lore +3
- solo tactics
- stern gaze +2
- track +2
gear:
  combat:
  - potion of cure light wounds
  - potion of invisibility
  - tanglefoot bag
  other:
  - mwk hide armor
  - mwk light wooden shield
  - mwk light flail
  - spears (4)
  - artisan's tools
  - silk rope (50 ft.)
desc_long: |-
  These Koboto cannibals have lived in the harsh, rain-scoured jungles of the Sodden Lands their entire lives. From a young age, these warriors have been indoctrinated into the worship of Sar-Gorog, the Three Feasters of Koboto lore. Worship of this pantheon, they believe, is all that protects their people from devastation by monsters and weather. Cannibalism is a sacred rite in the worship of the Three Feasters, and the Koboto believe that consuming the flesh of their enemies grants them strength and power. These warriors rarely rush into combat without some consideration and preparation. They prefer to cast preparatory spells such as shield of faith and weapon of awe if time permits. Their preferred method of combat is ambush; they use Stealth and attempt to approach their enemies undetected. The cannibals prefer to incapacitate their enemies using hold person or tanglefoot bags so they can tie up and eventually cook and eat their victims; a living prisoner spoils less quickly than a decaying corpse. If open combat becomes necessary, these zealots let the ferocious rage of the Three Feasters overtake them and don't back down until they or their enemies are dead.

  These zealots follow Jitikai out of habit rather than slavish devotion. Jitikai increasingly favors her juju zombies over her living followers, and has forbidden the zealots from consuming any corpses in Mifutu's tomb. The zealots are starting to discuss-in hushed tones-whether perhaps they ought to desert Jitikai and find another witch doctor to serve.

---

# Cannibal Zealot
Crude designs painted in what can only be dried blood cake the face and the hide clothing of this rugged-looking human, whose grinning mouth is filled with sharp, filed teeth.
**Source** Tombs of Golarion pg. 61
**XP** 2,400
Human _[[classes/Barbarian|barbarian]]_ 3/inquisitor 4

NE Medium humanoid (human)
**Init** +4; **Senses** Perception +9

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +1 _[[spells/Shield|shield]]_)
**hp** 54 (7 HD; 4d8+3d12+11)
**Fort** +8, **Ref** +3, **Will** +8
**Defensive Abilities** trap sense +1, uncanny _dodge_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Light flail|light flail]]_ +10/+5 (1d8+3) or _[[items/Weapon/Spear|spear]]_ +9/+4 (1d8+4/×3)
**Special Attacks** judgment 2/day, _[[spells/Rage|rage]]_ (14 rounds/day), _rage_ power (animal fury)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +7)
1/day—_[[spells/Decompose Corpse|decompose corpse]]_
**_[[classes/Inquisitor|Inquisitor]]_ _Spell-Like Abilities_** (CL 4th; concentration +7)
At will—detect alignment
**_Inquisitor_ Spells Known **(CL 4th; concentration +7)
2nd (2/day)—_[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Weapon of Awe|weapon of awe]]_ (DC 15)
1st (4/day)—_[[spells/Command|command]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Shield Of Faith|shield of faith]]_, wrath
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Create Water|create water]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Guidance|guidance]]_, light, stabilize
**Inquisition** Anger

##### Statistics
**Str** 16, **Dex** 13, **Con** 12, **Int** 8, **Wis** 16, **Cha** 10
**Base Atk** +6; **CMB** +9; **CMD** 21
**Feats** _[[feats/Cleave|Cleave]]_, _Dodge_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Polytheistic Blessing|Polytheistic Blessing]]_ (Sar-Gorog pantheon; see the sidebar on page 63), _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Strike|Precise Strike]]_
**Skills** Craft (traps) +5, _[[spells/Heal|Heal]]_ +9, Intimidate +15, Knowledge (nature) +5, Perception +9, Sense Motive +11, Stealth +9, Survival +13
**Languages** Polyglot
**SQ** hateful _[[items/Mundane/Retort|retort]]_, monster lore +3, solo tactics, stern _[[universal monster rules/Gaze|gaze]]_ +2, track +2
**Combat Gear** potion of _cure light wounds_, potion of _[[spells/Invisibility|invisibility]]_, _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** mwk _[[items/Armor/Hide armor|hide armor]]_, mwk _[[items/Shield/Light wooden shield|light wooden shield]]_, mwk _light flail_, spears (4), artisan’s tools, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.)

These Koboto cannibals have lived in the harsh, rain-scoured jungles of the Sodden Lands their entire lives. From a young age, these warriors have been indoctrinated into the worship of Sar-Gorog, the Three Feasters of Koboto lore. Worship of this pantheon, they believe, is all that protects their people from devastation by monsters and weather. Cannibalism is a _[[items/Weapon Magic Abilities/Sacred|sacred]]_ rite in the worship of the Three Feasters, and the Koboto believe that consuming the flesh of their enemies grants them strength and power. These warriors rarely rush into combat without some consideration and preparation. They prefer to cast preparatory spells such as _shield of faith_ and _weapon of awe_ if time permits. Their preferred method of combat is ambush; they use Stealth and attempt to approach their enemies undetected. The cannibals prefer to incapacitate their enemies using _hold person_ or tanglefoot bags so they can tie up and eventually cook and eat their victims; a living prisoner spoils less quickly than a decaying corpse. If open combat becomes necessary, these zealots let the ferocious _rage_ of the Three Feasters overtake them and don’t back down until they or their enemies are dead.

These zealots follow Jitikai out of habit rather than slavish devotion. Jitikai increasingly favors her juju zombies over her living followers, and has forbidden the zealots from consuming any corpses in Mifutu’s tomb. The zealots are starting to discuss—in hushed tones—whether perhaps they ought to desert Jitikai and find another _[[classes/Witch|witch]]_ doctor to serve.