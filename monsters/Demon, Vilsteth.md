---
cssclass: [monsters]
title1: Demon, Vilsteth
desc_short: This fiend seems carved from weathered ivory, and runes and symbols of
  power cover its pale flesh. Its eyes glow an eerie yellow, and horns curl from its
  eerie, mouthless head.
title2: Vilsteth
CR: 16
sources:
- name: 'Pathfinder #77: Herald of the Ivory Labyrinth'
  page: 86
  link: http://paizo.com/products/btpy92lh?Pathfinder-Adventure-Path-77-Herald-of-the-Ivory-Labyrinth
XP: 76800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 30
  touch: 14
  flat_footed: 26
  components:
    dex: 4
    natural: 16
HP:
  HP: 225
  long: 18d10+126
saves:
  fort: 18
  ref: 10
  will: 14
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- electricity
- mind-affecting effects
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 27
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +24 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: claws
      bonus:
      - 24
    - text: gore +24 (2d6+6 plus 1d4 Wis)
      entries:
      - - damage: 2d6+6
        - damage: 1d4
          type: Wis
      attack: gore
      bonus:
      - 24
    - text: tail slap +19 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: tail slap
      bonus:
      - 19
  special:
  - idolatry
  - labyrinthine mindtrap
  - mindrender
  - powerful charge (gore, 4d6+12)
  - rend (2 claws, 2d6+9)
  - unspeakable truth
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - superscripts:
    - APG
    name: enter image
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: meld into stone
    source: default
    freq: At will
  - superscripts:
    - UM
    name: possess object
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
    DC: 17
  - name: charm monster
    source: default
    freq: 3/day
    DC: 20
  - name: quickened dominate person
    source: default
    freq: 3/day
    DC: 21
  - name: stone shape
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: vengeful outrage
    source: default
    freq: 3/day
    DC: 22
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 22
  - name: statue
    source: default
    freq: 1/day
  - superscripts:
    - AP75
    name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: shachath
      amount: 1
    - name: succubi
      amount: 1d3
      chance: 50%
  - name: symbol of persuasion
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 22
  DEX: 19
  CON: 24
  INT: 23
  WIS: 16
  CHA: 23
BAB: 18
CMB: 24
CMD: 38
feats:
- name: Alertness
- name: Combat Casting
- name: Deceitful
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Vital Strike
- name: Persuasive
- name: Quicken Spell-Like Ability (dominate person)
- name: Vital Strike
skills:
  Bluff: 31
  Craft (sculpture): 18
  Craft (stonemasonry): 18
  Diplomacy: 31
  Disguise: 31
  Intimidate: 31
  Knowledge (engineering): 15
  Knowledge (history): 15
  Knowledge (local): 15
  Knowledge (nobility): 15
  Knowledge (religion): 15
  Perception: 36
  Perform (oratory): 15
  Sense Motive: 28
  Spellcraft: 16
  Stealth: 25
  Use Magic Device: 14
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- can't speak
- telepathy 100 ft.
special_qualities:
- change shape (Medium humanoid; polymorph)
- no breath
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or conspiracy (3-12)
  treasure_type: standard
special_abilities:
  Idolatry (Su): When a vilsteth uses enter image, meld into stone, possess object,
    or statue to assume the appearance of a public or religious monument (either by
    entering or controlling an existing object or by taking the semblance of one),
    it can make itself an object of worship and adoration. This functions as sympathy
    (DC 25, CL 18th) upon either a single creature within 30 feet or all creatures
    of the chosen type or alignment within 30 feet. Any creature that fails its saving
    throw against this effect must attempt an additional DC 25 Will save after spending
    24 hours within 30 feet of the object of worship. If the targeted creature fails
    this second save, it's affected as if under a permanent mind fog effect with respect
    to the vilsteth. This is a curse effect and cannot be dispelled (although dispel
    chaos or dispel evil can remove this effect, as does break enchantment).
  Labyrinthine Mindtrap (Su): Whenever a vilsteth is targeted with a divination or
    mind-affecting effect, including effects that simply facilitate mental communication,
    the caster's mind is entrapped within the twisted corridors and pathways of the
    vilsteth's intellect, causing the caster to become dazed (Will DC 25 negates).
    Each round on the victim's turn, it can attempt a new saving throw to escape this
    mind trap, ending its turn, but each failed save deals 1 point of Intelligence,
    Wisdom, and Charisma drain to the creature. A creature that successfully saves
    against this effect is immune to the same vilsteth's labyrinthine mindtrap for
    24 hours.
  Mindrender (Su): When a vilsteth hits with both claw attacks and rends its target,
    it gains a +4 profane bonus on its gore attack for that turn. In addition, if
    the vilsteth's gore attack hits, the target is affected by the vilsteth's labyrinthine
    mindtrap ability, even if the targeted creature already successfully saved against
    that ability in the last 24 hours.
  Unspeakable Truth (Su): A vilsteth is surrounded by a mantle of misinformation.
    Creatures within 30 feet are affected by a curse that manifests the next time
    they attempt to share information about the vilsteth, including things they have
    observed the demon saying or doing. This curse affects the creature as fumbletongueUM
    (Will DC 25 negates). A successful save negates the curse, but if the target fails
    the save, this curse manifests every time that target attempts to talk about the
    vilsteth. This curse is a mind-affecting compulsion effect and can't be dispelled
    or suppressed with protection from evil. A vilsteth can order creatures affected
    by charm or compulsion effects that it creates to share information about it without
    triggering the curse.
desc_long: Vilsteth demons, also known as corruption demons, are calved from the essence
  of the demon lord Baphomet's realm of the Ivory Labyrinth. Vilsteths form from the
  souls of corrupt and deceitful politicians, priests, and power brokers-those who
  in life abused and misused whatever ephemeral power they wielded. The defining sin
  of these souls was pride, fueled by vanity and a desire for adulation and ever-greater
  authority to be wielded in whatever selfish way they saw fit, coupled with a furious
  envy of anyone more beloved, respected, or feared than they. Vilsteths epitomize
  these traits, and can often be found lurking in monuments dedicated to important
  political figures or disguised within statues of prominent saints and heroes. In
  their natural form, vilsteths are over 7 feet tall and weigh 400 pounds.

---

# Demon, Vilsteth
This fiend seems carved from weathered ivory, and runes and symbols of power cover its pale flesh. Its eyes glow an eerie yellow, and horns curl from its eerie, mouthless head.
**Source** Pathfinder #77: Herald of the Ivory Labyrinth pg. 86
**XP** 76,800
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +36

##### Defense

**AC** 30, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 Dex, +16 natural)
**hp** 225 (18d10+126)
**Fort** +18, **Ref** +10, **Will** +14
**DR** 10/cold iron and good; **Immune** electricity, mind-affecting effects, poison; **Resist** acid 10, cold 10, fire 10; **SR** 27

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +24 (2d6+6), gore +24 (2d6+6 plus 1d4 Wis), tail slap +19 (1d8+3)
**Special Attacks** idolatry, labyrinthine mindtrap, mindrender, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d6+12), _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+9), unspeakable truth
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_see invisibility_
At will—_[[spells/Enter Image|enter image]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Possess Object|possess object]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 17)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 20), quickened _[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Stone Shape|stone shape]]_, _[[spells/Vengeful Outrage|vengeful outrage]]_ (DC 22)
1/day—mass _[[spells/Suggestion|suggestion]]_ (DC 22), _[[spells/Statue|statue]]_, _[[universal monster rules/Summon|summon]]_ (level 7, 1 shachath or 1d3 succubi 50%), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 22)

##### Statistics
**Str** 22, **Dex** 19, **Con** 24, **Int** 23, **Wis** 16, **Cha** 23
**Base Atk** +18; **CMB** +24; **CMD** 38
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +31, Craft (sculpture, stonemasonry) +18, Diplomacy +31, Disguise +31, Intimidate +31, Knowledge (engineering, history, local, nobility, religion) +15, Perception +36, Perform (oratory) +15, Sense Motive +28, Spellcraft +16, Stealth +25, Use Magic Device +14; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; can’t speak, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_Medium_ humanoid; _[[spells/Polymorph|polymorph]]_), _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or conspiracy (3–12)
**Treasure** standard

### Special Abilities

**Idolatry (Su)** When a vilsteth uses _enter image_, _meld into stone_, _possess object_, or _statue_ to assume the appearance of a public or religious monument (either by entering or controlling an existing object or by taking the semblance of one), it can make itself an object of worship and _[[spells/Adoration|adoration]]_. This functions as _[[spells/Sympathy|sympathy]]_ (DC 25, CL 18th) upon either a single creature within 30 feet or all creatures of the chosen type or alignment within 30 feet. Any creature that fails its saving throw against this effect must attempt an additional DC 25 Will save after spending 24 hours within 30 feet of the object of worship. If the targeted creature fails this second save, it’s affected as if under a permanent _[[spells/Mind Fog|mind fog]]_ effect with respect to the vilsteth. This is a curse effect and cannot be dispelled (although _[[spells/Dispel Chaos|dispel chaos]]_ or _[[spells/Dispel Evil|dispel evil]]_ can remove this effect, as does _[[spells/Break Enchantment|break enchantment]]_).

**Labyrinthine Mindtrap (Su)** Whenever a vilsteth is targeted with a _[[spells/Divination|divination]]_ or mind-affecting effect, including effects that simply facilitate mental communication, the caster’s mind is entrapped within the twisted corridors and pathways of the vilsteth’s intellect, causing the caster to become _[[conditions/Dazed|dazed]]_ (Will DC 25 negates). Each round on the victim’s turn, it can attempt a new saving throw to escape this mind trap, ending its turn, but each failed save deals 1 point of Intelligence, Wisdom, and Charisma drain to the creature. A creature that successfully saves against this effect is immune to the same vilsteth’s labyrinthine mindtrap for 24 hours.

**Mindrender (Su)** When a vilsteth hits with both claw attacks and rends its target, it gains a +4 profane bonus on its gore attack for that turn. In addition, if the vilsteth’s gore attack hits, the target is affected by the vilsteth’s labyrinthine mindtrap ability, even if the targeted creature already successfully saved against that ability in the last 24 hours.

**Unspeakable Truth (Su)** A vilsteth is surrounded by a mantle of misinformation. Creatures within 30 feet are affected by a curse that manifests the next time they attempt to share information about the vilsteth, including things they have observed the demon saying or doing. This curse affects the creature as _[[spells/Fumbletongue|fumbletongue]]_ (Will DC 25 negates). A successful save negates the curse, but if the target fails the save, this curse manifests every time that target attempts to talk about the vilsteth. This curse is a mind-affecting compulsion effect and can’t be dispelled or suppressed with _[[spells/Protection From Evil|protection from evil]]_. A vilsteth can order creatures affected by charm or compulsion effects that it creates to share information about it without triggering the curse.

##### Description

Vilsteth demons, also known as corruption demons, are calved from the essence of the demon lord Baphomet’s realm of the Ivory Labyrinth. Vilsteths form from the souls of corrupt and _deceitful_ politicians, priests, and power brokers—those who in life abused and misused whatever ephemeral power they wielded. The defining sin of these souls was pride, fueled by vanity and a desire for adulation and ever-greater authority to be wielded in whatever selfish way they _[[items/Mundane/Saw|saw]]_ fit, coupled with a _[[items/Weapon Magic Abilities/Furious|furious]]_ envy of anyone more beloved, respected, or feared than they. Vilsteths epitomize these traits, and can often be found lurking in monuments dedicated to important political figures or disguised within statues of prominent saints and heroes. In their natural form, vilsteths are over 7 feet tall and weigh 400 pounds.