---
cssclass: [monsters]
title1: Devil, Mnemor
desc_short: This ghoulish figure wears a tattered robe and stares with milky-white
  eyes, a proboscis-like tongue snaking out over its distended jaw.
title2: Mnemor
CR: 5
sources:
- name: Occult Bestiary
  page: 21
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 1600
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect magic: true
  detect thoughts: true
  see in darkness: true
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    dex: 4
    natural: 4
HP:
  HP: 57
  long: 6d10+24
saves:
  fort: 6
  ref: 9
  will: 7
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 16
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +11 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 11
    - text: proboscis +10 touch (memory siphon)
      entries:
      - - effect: memory siphon
      attack: proboscis
      bonus:
      - 10
      touch: true
  special:
  - memory siphon
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 15
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: bearded devil
      amount: 1
    - name: lemures
      amount: 6
      chance: 50%
  sources:
  - name: default
    CL: 6
    concentration: 9
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: aversion
    PE: 2
    DC: 15
  - name: calm emotions
    PE: 2
    DC: 15
  - name: confusion
    PE: 4
    DC: 17
  - superscripts:
    - OA
    name: deja vu
    PE: 1
  - name: invisibility
    PE: 2
  sources:
  - name: default
    CL: 6
    concentration: 9
  PE: 16
ability_scores:
  STR: 18
  DEX: 18
  CON: 18
  INT: 17
  WIS: 15
  CHA: 17
BAB: 6
CMB: 10
CMD: 24
feats:
- name: Improved Initiative
- name: Power Attack
- name: Weapon Focus (claw)
skills:
  Bluff: 12
  Diplomacy: 12
  Knowledge (religion): 11
  Knowledge (planes): 16
  Knowledge (all others): 8
  Perception: 11
  Sense Motive: 11
  Spellcraft: 12
  Stealth: 13
  Use Magic Device: 9
  _racial_mods:
    Knowledge:
      _: 4
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- easily forgotten
ecology:
  environment: any (Hell)
  organization: solitary
  treasure_type: incidental
special_abilities:
  Easily Forgotten (Su): A mnemor devil's appearance and presence are difficult to
    fix in one's mind. Once a mnemor devil moves out of line of sight of a creature
    (or otherwise becomes unseen), that creature must succeed at a DC 16 Will save
    or be unable recall the last known location or direction of the devil. Such a
    creature cannot recall the details or nature of their encounter with the devil,
    though it retains a vague recollection that the encounter occurred. The mnemor
    can choose to suppress this ability.
  Memory Siphon (Sp): A creature struck by a mnemor devil's proboscis suffers the
    effect of the memory lapseAPG spell with no saving throw. Additionally, the mnemor
    devil can choose to attempt to affect the creature as with the repress memoryOA
    spell (DC 16 Will save negates)-the spell targets the creature struck, rather
    than the mnemor devil itself, and spell resistance applies. If the target is a
    willing creature, the mnemor devil may alter memories of any length, as if through
    multiple applications of repress memoryOA.
desc_long: |-
  Some memories are too traumatic to bear; some secrets are too dangerous to keep. When mortals need their memories stripped away, their desperation sometimes drives them to seek out the aid of mnemor devils, creatures that steal and bestow memories in the service of their infernal lords. While memory devils always keep their bargains, those who anger them may find that their altered memories cause more trouble than the originals. Mnemor devils are particularly skilled in the subtle manipulation of memory to drive mortals' actions in destructive directions or even trick them into making the same bargain again and again as the mortal unearths the unbearable secret on her own, paying the devil each time. The most skilled among them subtly alter the false memories they grant to those who would bargain with them in ways that cast the subjects' true memories in a different light, making memories of affectionate smiles seem to take on smirking undertones, or adding sly malice to memories of innocent comments. The bargainer finds himself driven into maddening doubt about the intentions of everyone he thought he knew, suspicion tainting all his interactions.

  Mnemor devils themselves possess eidetic memories, and can recall with perfect clarity any memory they have bought or stolen from a mortal, making them valuable repositories of eclectic knowledge. Those seeking such knowledge might be tempted to seek a deal of their own, and mnemor devils are more than happy to trade one memory for another-though those who strike such bargains find that the mnemor devil nearly always comes out ahead.

  A mnemor devil stands approximately 6 feet tall and weighs 170 pounds.

---

# Devil, Mnemor
This ghoulish figure wears a tattered robe and stares with milky-white eyes, a proboscis-like tongue snaking out over its distended jaw.
**Source** Occult Bestiary pg. 21
**XP** 1,600

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Thoughts|detect thoughts]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +11

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 Dex, +4 natural)
**hp** 57 (6d10+24)
**Fort** +6, **Ref** +9, **Will** +7
**Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 16

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +11 (1d6+4), proboscis +10 touch (memory siphon)
**Special Attacks** memory siphon
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
Constant—_detect magic_, _detect thoughts_
At will—greater teleport, _[[spells/Suggestion|suggestion]]_ (DC 15)
1/day—_[[universal monster rules/Summon|summon]]_ (level 3, 1 bearded devil or 6 lemures 50%)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 6th; concentration +9)
16 PE—_[[spells/Aversion|aversion]]_ (2 PE, DC 15), _[[spells/Calm Emotions|calm emotions]]_ (2 PE, DC 15), _[[spells/Confusion|confusion]]_ (4 PE, DC 17), _[[spells/Deja Vu|deja vu]]_ (1 PE), _[[spells/Invisibility|invisibility]]_ (2 PE)

##### Statistics
**Str** 18, **Dex** 18, **Con** 18, **Int** 17, **Wis** 15, **Cha** 17
**Base Atk** +6; **CMB** +10; **CMD** 24
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Bluff +12, Diplomacy +12, Knowledge (religion) +11, Knowledge (planes) +16, Knowledge (all others) +8, Perception +11, Sense Motive +11, Spellcraft +12, Stealth +13, Use Magic Device +9; **Racial Modifiers** +4 Knowledge
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** easily forgotten

##### Ecology

**Environment** any (Hell)
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Easily Forgotten (Su)** A mnemor devil’s appearance and presence are difficult to fix in one’s mind. Once a mnemor devil moves out of line of sight of a creature (or otherwise becomes _[[items/Weapon Magic Abilities/Unseen|unseen]]_), that creature must succeed at a DC 16 Will save or be unable recall the last known location or direction of the devil. Such a creature cannot recall the details or nature of their encounter with the devil, though it retains a vague recollection that the encounter occurred. The mnemor can choose to suppress this ability.

**Memory Siphon (Sp)** A creature struck by a mnemor devil’s proboscis suffers the effect of the _[[spells/Memory Lapse|memory lapse]]_ spell with no saving throw. Additionally, the mnemor devil can choose to attempt to affect the creature as with the _[[spells/Repress Memory|repress memory]]_ spell (DC 16 Will save negates)—the spell targets the creature struck, rather than the mnemor devil itself, and _[[universal monster rules/Spell Resistance|spell resistance]]_ applies. If the target is a willing creature, the mnemor devil may alter memories of any length, as if through multiple applications of _repress memory_.

##### Description

Some memories are too traumatic to bear; some secrets are too dangerous to keep. When mortals need their memories stripped away, their desperation sometimes drives them to seek out the aid of mnemor devils, creatures that steal and bestow memories in the service of their infernal lords. While memory devils always keep their bargains, those who anger them may find that their altered memories cause more trouble than the originals. Mnemor devils are particularly skilled in the subtle manipulation of memory to drive mortals’ actions in destructive directions or even trick them into making the same bargain again and again as the mortal unearths the unbearable secret on her own, paying the devil each time. The most skilled among them subtly alter the false memories they grant to those who would bargain with them in ways that cast the subjects’ true memories in a different light, making memories of affectionate smiles seem to take on smirking undertones, or adding sly malice to memories of innocent comments. The bargainer finds himself driven into maddening doubt about the intentions of everyone he thought he knew, suspicion tainting all his interactions.

Mnemor devils themselves possess eidetic memories, and can recall with perfect _[[items/Weapon/Clarity|clarity]]_ any memory they have bought or stolen from a mortal, making them valuable repositories of _[[feats/Eclectic|eclectic]]_ knowledge. Those seeking such knowledge might be tempted to seek a deal of their own, and mnemor devils are more than happy to trade one memory for another—though those who strike such bargains find that the mnemor devil nearly always comes out ahead.

A mnemor devil stands approximately 6 feet tall and weighs 170 pounds.