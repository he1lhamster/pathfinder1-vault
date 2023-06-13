---
cssclass: [monsters]
title1: Oni, Void Yai
desc_short: This towering, three-eyed horned giant carries himself with the self-assurance
  of an undefeated champion of countless wars.
title2: Void Yai
CR: 20
sources:
- name: Bestiary 3
  page: 210
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 307200
alignment: LE
size: Huge
type: outsider
subtypes:
- giant
- native
- oni
- shapechanger
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 36
  touch: 9
  flat_footed: 35
  components:
    armor: 9
    dex: 1
    natural: 18
    size: -2
HP:
  HP: 379
  long: 23d10+253
  regeneration: 15
  regeneration_weakness: fire or good spells
saves:
  fort: 24
  ref: 9
  will: 21
immunities:
- cold
SR: 31
speeds:
  base: 40
  other_semicolon: 60 ft., fly 60 ft. without armor
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: mwk greatclub +39/+34/+29/+24 (3d8+25/19-20)
      entries:
      - - damage: 3d8+25
          crit_range: 19-20
      attack: mwk greatclub
      bonus:
      - 39
      - 34
      - 29
      - 24
  - - text: 2 slams +28 (2d6+17)
      entries:
      - - damage: 2d6+17
      count: 2
      attack: slams
      bonus:
      - 28
  ranged:
  - - text: void missile +23 touch (6d6 plus energy drain)
      entries:
      - - damage: 6d6
        - effect: energy drain
      attack: void missile
      bonus:
      - 23
      touch: true
  special:
  - commanding voice
  - energy drain (2 levels, DC 28)
  - void trap
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: Constant
    other: chill shield
  - name: fly
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: gaseous form
    source: default
    freq: At will
    other: self only
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: minor creation
    source: default
    freq: At will
  - name: vision
    source: default
    freq: At will
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 22
  - name: demand
    source: default
    freq: 3/day
    DC: 25
  - name: dominate person
    source: default
    freq: 3/day
    DC: 22
  - name: major creation
    source: default
    freq: 3/day
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 25
  - name: polar ray
    source: default
    freq: 3/day
  - name: teleport object
    source: default
    freq: 3/day
    DC: 24
  - name: implosion
    source: default
    freq: 1/day
    DC: 26
  - name: plane shift
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 44
  DEX: 15
  CON: 32
  INT: 18
  WIS: 23
  CHA: 25
BAB: 23
CMB: 42
CMD: 54
feats:
- name: Awesome Blow
- name: Cleave
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (greatclub)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 17
    when jumping: 25
  Bluff: 30
  Fly: 20
  Intimidate: 30
  Knowledge (arcana): 27
  Knowledge (history): 24
  Knowledge (nobility): 24
  Knowledge (planes): 27
  Perception: 29
  Sense Motive: 29
  Spellcraft: 24
  Use Magic Device: 30
languages:
- Common
- Giant
special_qualities:
- change shape (Large, Huge, or Gargantuan humanoid; giant form II)
- void form
ecology:
  environment: cold or temperate mountains
  organization: solitary
  treasure_type: double
  treasure:
  - masterwork full plate
  - masterwork greatclub
  - other treasure
special_abilities:
  Commanding Voice (Su): A void oni gains a +4 racial bonus on the save DC of any
    charm or compulsion effects it uses against humanoids.
  Void Form (Su): A void yai may become incorporeal as a swift action. In this form,
    it appears as a solid black shadow of its true form. It gains the incorporeal
    subtype and incorporeal defensive ability while in void form. Any gear or armor
    the yai carries becomes incorporeal as well-it loses its AC bonus from armor and
    natural armor, but gains a deflection bonus to its AC equal to its Charisma modifier
    (+7 for most void yai, for an AC of 16). It may still speak while incorporeal
    and can still use its spell-like and special abilities.
  Void Missile (Su): As a swift action, a void yai can launch a bolt of darkness from
    its third eye. Damage caused by this missile is negative energy damage. This attack
    has a range of 180 feet with no range increment.
  Void Trap (Su): When a void oni uses any teleportation effect on itself (including
    its greater teleport and plane shift spell-like abilities, but not its teleport
    object spell-like ability), it can choose to arrive at its destination in void
    form as a free action. When it does so, it leaves behind a temporary lesser sphere
    of annihilation in a square of its choice that was part of its space before it
    teleported. This sphere of annihilation cannot be caused to move by other creatures,
    but the sphere itself moves at a fly speed of 30 feet (perfect) toward the closest
    Tiny or larger creature on the oni's next turn. If no appropriate creature is
    within 30 feet, the sphere does not move that round. If the sphere enters a square
    occupied by a creature (or if a creature touches the sphere), that creature is
    affected as if by a disintegrate spell (CL 20th, DC 23). Once the sphere damages
    a creature with this effect, the sphere vanishes-it also vanishes on its own after
    24 hours in the unlikely event that it never discharges on a creature. The save
    DC is Charisma-based.
desc_long: |-
  The concept of the void is a difficult one for many individuals to grasp, for it encompasses more than just an absence of anything. The concept of “void” as an element also represents the heavens above, the dark places between the stars, the nature of the spiritual world, and even the capacity to create and envision new ideas. The void yai represents all of these possibilities, interpreted in a way that exemplifies the evil of the oni race.

  Unlike lesser oni, the void yai does not represent any single humanoid race-the closest it comes is perhaps the rune giant, and certainly the void yai superficially resembles monsters of legend, with its dark, heavily muscled body, horns, and fangs. A void yai manifests when the combination of an extremely powerful oni spirt and an overwhelmingly evil location intersect at precisely the right time. Rarely, an eldritch transformation spontaneously elevates an existing yai to the vaunted status of void yai-whispers of vile rituals that an oni can perform to quicken this transformation keep some sages awake at night, for if such rituals existed, then all oni could potentially become void yai-a sobering thought indeed, given the void yai's daunting capacity for cruelty. As with almost all oni, the void oni's use of weapons and armor seems like cruel overkill. A void oni is 20 feet tall and weighs 10,000 pounds.

  Void yai turn toward the Material Plane to satisfy their desires, lording over lesser creatures with the aid of the void. A void yai usually claims a huge territory, bringing much larger creatures to heel as servants. As with fire yai, a void yai makes frequent use of lesser oni as its minions, but prefers to surround itself with whatever giant tribe or society it has conquered. Rarely, a void yai commands kingdoms of smaller humanoids, but since the immense void yai has no ability to assume the shape of such small and insignificant creatures, it often feels awkward and out of place. More so than other yai, void yai are ashamed of their true appearance-their vanity is such that most are masters of using their change shape ability to appear as breathtakingly handsome or beautiful giants, and it is in this form they prefer to live. Only when combat begins does their rage take control, causing them to revert to their true, horrific shapes.

---

# Oni, Void Yai
This towering, three-eyed horned giant carries himself with the self-assurance of an undefeated _[[items/Armor Magic Abilities/Champion|champion]]_ of countless wars.
**Source** Bestiary 3 pg. 210
**XP** 307,200

LE Huge outsider (giant, native, oni, shapechanger)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +29

##### Defense

**AC** 36, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+9 armor, +1 Dex, +18 natural, –2 size)
**hp** 379 (23d10+253); _[[universal monster rules/Regeneration|regeneration]]_ 15 (fire or good spells)
**Fort** +24, **Ref** +9, **Will** +21
**Immune** cold; **SR** 31

##### Offense
**Speed** 40 ft., fly 40 ft. (good); 60 ft., fly 60 ft. without armor
**Melee** mwk _[[items/Weapon/Greatclub|greatclub]]_ +39/+34/+29/+24 (3d8+25/19–20) or 2 slams +28 (2d6+17)
**Ranged** void missile +23 touch (6d6 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** commanding voice, _energy drain_ (2 levels, DC 28), void trap
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Fire Shield|fire shield]]_ (chill _[[spells/Shield|shield]]_), fly, _true seeing_
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Gaseous Form|gaseous form]]_ (self only), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Minor Creation|minor creation]]_, _[[spells/Vision|vision]]_
3/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Demand|demand]]_ (DC 25), _[[spells/Dominate Person|dominate person]]_ (DC 22), _[[spells/Major Creation|major creation]]_, mass _[[spells/Charm Monster|charm monster]]_ (DC 25), _[[spells/Polar Ray|polar ray]]_, _[[spells/Teleport Object|teleport object]]_ (DC 24)
1/day—_[[spells/Implosion|implosion]]_ (DC 26), _[[spells/Plane Shift|plane shift]]_ (DC 24)

##### Statistics
**Str** 44, **Dex** 15, **Con** 32, **Int** 18, **Wis** 23, **Cha** 25
**Base Atk** +23; **CMB** +42; **CMD** 54
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greatclub_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +17 (+25 when jumping), Bluff +30, Fly +20, Intimidate +30, Knowledge (arcana) +27, Knowledge (history) +24, Knowledge (nobility) +24, Knowledge (planes) +27, Perception +29, Sense Motive +29, Spellcraft +24, Use Magic Device +30
**Languages** Common, Giant
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Large, Huge, or Gargantuan humanoid; _[[spells/Giant Form II|giant form II]]_), void form

##### Ecology

**Environment** cold or temperate mountains
**Organization** solitary
**Treasure** double (masterwork _[[items/Armor/Full plate|full plate]]_, masterwork _greatclub_, other treasure)

### Special Abilities

**Commanding Voice (Su)** A void oni gains a +4 racial bonus on the save DC of any charm or compulsion effects it uses against humanoids.

**Void Form (Su)** A void yai may become _[[universal monster rules/Incorporeal|incorporeal]]_ as a swift action. In this form, it appears as a solid black _[[items/Armor Magic Abilities/Shadow|shadow]]_ of its _[[spells/True Form|true form]]_. It gains the _incorporeal_ subtype and _incorporeal_ defensive ability while in void form. Any gear or armor the yai carries becomes _incorporeal_ as well—it loses its AC bonus from armor and natural armor, but gains a deflection bonus to its AC equal to its Charisma modifier (+7 for most void yai, for an AC of 16). It may still speak while _incorporeal_ and can still use its spell-like and special abilities.

**Void Missile (Su) **As a swift action, a void yai can launch a bolt of _[[spells/Darkness|darkness]]_ from its _[[items/Wondrous Item/Third Eye|third eye]]_. Damage caused by this missile is negative energy damage. This attack has a range of 180 feet with no range increment.

**Void Trap (Su)** When a void oni uses any teleportation effect on itself (including its greater teleport and _plane shift_ _spell-like abilities_, but not its _teleport object_ spell-like ability), it can choose to arrive at its destination in void form as a free action. When it does so, it leaves behind a temporary lesser _[[items/Wondrous Item/Sphere of Annihilation|sphere of annihilation]]_ in a square of its choice that was part of its space before it teleported. This _sphere of annihilation_ cannot be caused to move by other creatures, but the sphere itself moves at a fly speed of 30 feet (perfect) toward the closest Tiny or larger creature on the oni’s next turn. If no appropriate creature is within 30 feet, the sphere does not move that round. If the sphere enters a square occupied by a creature (or if a creature touches the sphere), that creature is affected as if by a _[[spells/Disintegrate|disintegrate]]_ spell (CL 20th, DC 23). Once the sphere damages a creature with this effect, the sphere vanishes—it also vanishes on its own after 24 hours in the unlikely event that it never discharges on a creature. The save DC is Charisma-based.

##### Description

The concept of the void is a difficult one for many individuals to _[[spells/Grasp|grasp]]_, for it encompasses more than just an absence of anything. The concept of “void” as an element also represents the heavens above, the dark places between the stars, the nature of the spiritual world, and even the capacity to create and envision new ideas. The void yai represents all of these possibilities, interpreted in a way that exemplifies the evil of the oni race.

Unlike lesser oni, the void yai does not represent any single humanoid race—the closest it comes is perhaps the rune giant, and certainly the void yai superficially resembles monsters of legend, with its dark, heavily muscled body, horns, and fangs. A void yai manifests when the combination of an extremely powerful oni spirt and an overwhelmingly evil location intersect at precisely the right time. Rarely, an eldritch _[[spells/Transformation|transformation]]_ spontaneously elevates an existing yai to the vaunted _[[spells/Status|status]]_ of void yai—whispers of vile rituals that an oni can perform to quicken this _transformation_ keep some sages awake at night, for if such rituals existed, then all oni could potentially become void yai—a sobering thought indeed, given the void yai’s daunting capacity for _[[feats/Cruelty|cruelty]]_. As with almost all oni, the void oni’s use of weapons and armor seems like _[[items/Weapon Magic Abilities/Cruel|cruel]]_ overkill. A void oni is 20 feet tall and weighs 10,000 pounds.

Void yai turn toward the Material Plane to satisfy their desires, lording over lesser creatures with the aid of the void. A void yai usually claims a huge territory, bringing much larger creatures to heel as servants. As with fire yai, a void yai makes frequent use of lesser oni as its minions, but prefers to surround itself with whatever giant tribe or society it has conquered. Rarely, a void yai commands kingdoms of smaller humanoids, but since the immense void yai has no ability to assume the shape of such small and insignificant creatures, it often feels awkward and out of place. More so than other yai, void yai are ashamed of their true appearance—their vanity is such that most are masters of using their _change shape_ ability to appear as breathtakingly handsome or beautiful giants, and it is in this form they prefer to live. Only when combat begins does their _[[spells/Rage|rage]]_ take control, causing them to revert to their true, horrific shapes.