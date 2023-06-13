---
cssclass: [monsters]
title1: Yah-Thelgaad
desc_short: A writhing forest of tendrils extends from one end of this chitincovered
  creature's body, while from the other lashes a pincer-tipped tail. Six transparent
  blisters adorn its back, each containing a brain floating in thick green fluid.
title2: Yah-Thelgaad
CR: 14
sources:
- name: 'Pathfinder #88: Valley of the Brain Collectors'
  page: 90
  link: http://paizo.com/products/btpy99sg?Pathfinder-Adventure-Path-88-Valley-of-the-Brain-Collectors
XP: 38400
alignment: CE
size: Large
type: aberration
initiative:
  bonus: 8
senses:
  darkvision: 60
  diagnose disease: true
  true seeing: true
AC:
  AC: 30
  touch: 25
  flat_footed: 26
  components:
    dex: 4
    insight: 12
    natural: 5
    size: -1
HP:
  HP: 200
  long: 16d8+128
saves:
  fort: 13
  ref: 11
  will: 17
defensive_abilities:
- carapace
DR:
- amount: 10
  weakness: magic and adamantine
immunities:
- disease
- mind-affecting effects
resistances:
  cold: 10
  fire: 10
SR: 25
speeds:
  base: 20
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: claw +22 (3d6+11 plus poison)
      entries:
      - - damage: 3d6+11
        - effect: poison
      attack: claw
      bonus:
      - 22
    - text: 2 tentacles +22 (1d8+11 plus grab)
      entries:
      - - damage: 1d8+11
        - effect: grab
      count: 2
      attack: tentacles
      bonus:
      - 22
  special:
  - command disease
  - mind storm
  - powerful tentacles
  - spellstrike
space: 10
reach: 10
spell_like_abilities:
  entries:
  - superscripts:
    - UM
    name: diagnose disease
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 12
    concentration: 20
spells:
  entries:
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 21
  - name: sending
    source: Sorcerer
    level: 5
  - superscripts:
    - APG
    name: suffocation
    source: Sorcerer
    level: 5
    DC: 22
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 19
  - name: contagion
    source: Sorcerer
    level: 4
    DC: 21
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: clairaudience/clairvoyance
    source: Sorcerer
    level: 3
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: slow
    source: Sorcerer
    level: 3
    DC: 18
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 17
  - name: ghoul touch
    source: Sorcerer
    level: 2
    DC: 19
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: spectral hand
    source: Sorcerer
    level: 2
  - name: chill touch
    source: Sorcerer
    level: 1
    DC: 18
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 18
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 15
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 15
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 17
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 32
    slots:
      6: 4
      5: 6
      4: 8
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 32
  DEX: 18
  CON: 26
  INT: 23
  WIS: 25
  CHA: 21
BAB: 12
CMB: 24
CMD: 50
CMD_other: 62 vs. trip
feats:
- name: Arcane Strike
- name: Combat Casting
- name: Combat Expertise
- is_bonus: true
  name: Eschew Materials
- name: Greater Spell Focus (necromancy)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Spell Focus (necromancy)
- name: Vital Strike
skills:
  Bluff: 21
  Diplomacy: 13
  Fly: 21
  Intimidate: 24
  Knowledge (arcana): 37
  Knowledge (engineering): 37
  Knowledge (geography): 37
  Knowledge (planes): 37
  Perception: 26
  Spellcraft: 25
  Use Magic Device: 21
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Infernal
- Protean
- Undercommon
- telepathy 100 ft.
special_qualities:
- brain collection
- strange knowledge
ecology:
  environment: any
  organization: solitary
  treasure_type: double
special_abilities:
  Brain Collection (Ex): A yah-thelgaad can store up to six brains of Small or Medium
    creatures and use them to enhance its knowledge and power. Each stored brain grants
    a yah-thelgaad a cumulative +2 insight bonus to AC, concentration checks, and
    Knowledge checks. A yah-thelgaad can extract a brain from a helpless opponent
    with a coup de grace attack, or as a standard action from a body that has been
    dead for no more than 1 minute. A yah-thelgaad that has fewer than six collected
    brains gains two negative levels for each missing brain. These negative levels
    never become permanent, and can only be removed by replacing one of the yah-thelgaad's
    collected brains. The statistics presented here assume a yah-thelgaad with a full
    collection.
  Carapace (Ex): The spikes on a yah-thelgaad's carapace make melee attacks against
    it hazardous. Any opponent attempting to attack a yah-thelgaad with a light weapon,
    unarmed strike, touch attack, or natural attack must succeed at a DC 22 Reflex
    save or take 1d6 points of bleed damage from these bristling barbs. Bleed damage
    from multiple failed Reflex saves does not stack. The save DC is Dexterity-based.
  Command Disease (Su): As a swift action, a yah-thelgaad can cause a disease or infection
    currently afflicting a creature within 30 feet to quicken and activate, forcing
    the afflicted creature to immediately attempt a saving throw against the disease's
    effects. Those who fail immediately suffer the disease's effects. These additional
    saving throws count against those one must succeed at to recover from a disease,
    so it's possible for a victim to be cured by succeeding at enough saving throws.
    Any creature that has been affected by a yah-thelgaad's command disease ability
    (whether or not the creature succeeded at the saving throw this ability triggered)
    takes a -2 penalty against any mind-affecting spell or effect generated by the
    yah-thelgaad in the next minute.
  Mind Storm (Su): As a standard action once every 1d4 rounds, a yah-thelgaad can
    employ its own brain as well as any brains kept in its blisters to create a powerful
    psychic vortex. When the creature activates this ability, all creatures within
    a 40-foot radius must succeed at DC 23 Will save or become confused for 1d4 rounds.
    When a yah-thelgaad activates this ability, it can choose to absorb one of its
    brains as a swift action to cause one creature within the area of effect that
    has succumbed to the confusion effect to instead become stunned for 1d4 rounds.
    A creature stunned in this manner is confused for 1d4 rounds after the stun effect
    ends. A yah-thelgaad generally saves this tactic for when it's faced with a particularly
    dangerous foe, since the stun effect forces the yah-thelgaad to lose one of its
    stored brains and gain 2 negative levels. This is a mind-affecting confusion effect.
    The save DC is Charisma-based.
  Poison (Ex): Claw-injury; save Fort DC 26; frequency 1/round for 6 rounds; effect
    1d4 Strength damage and nauseated for 1 round; cure 2 consecutive saves. The save
    DC is Constitution-based.
  Powerful Tentacles (Ex): A yah-thelgaad's tentacles are primary attacks.
  Spells (Su): A yah-thelgaad casts spells as a 12th-level sorcerer. Its caster level
    is reduced by 2 for each negative level it gains from missing brains. A yah-thelgaad
    with no collected brains can't cast any of its spells.
  Spellstrike (Su): Whenever a yah-thelgaad casts a spell with a range of “touch,”
    it can deliver the spell through its claw attack as part of a melee attack. Instead
    of the free melee touch attack normally allowed to deliver the spell, the yahthelgaad
    can make one free melee attack with its claw as part of casting the spell. If
    successful, this claw attack deals its normal damage (including poison) as well
    as the effects of the spell.
  Strange Knowledge (Ex): All knowledge skills are class skills for yah-thelgaads.
desc_long: |-
  When a neh-thalggu has absorbed a critical mass of thoughts and memories from an unknown number of humanoid brains, its body undergoes a horrific transformation. The creature enters a state of torpor, its body curling into a tight ball as it consumes the oldest of its seven stored brains to trigger the metamorphosis. Over the course of several days of selfconsumption, the neh-thalggu bursts from the shell of its old body into its new incarnation as a yah-thelgaad.

  While the yah-thelgaad shares many of the features of its less powerful progenitor, it is in every way a more powerful creature than it was before. While the capacity to store one fewer brain than a neh-thalggu presents some disadvantage, the yah-thelgaad gains twice as much power from a collected brain as its lesser kin does. In addition, these creatures need not limit their harvest to the brains of humanoids-any Small or Medium creature's brain will do.

  Yah-thelgaads are zealously devoted to the inscrutable causes of the Dominion of the Black, but they are also notoriously devout believers in that alliance's weird theology, worshiping a concept they refer to as the “Ineffable Void,” among other cryptic mysteries. It is not uncommon for yahthelgaads of high rank to also possess inquisitor or oracle levels, lording their authority and fanatical faith over those in their charge-the most powerful yah-thelgaads often take levels in mystic theurge to combine their class-based mastery of the divine with their stolen brains' arcane lore.

  Yah-thelgaads often supervise the Dominion of the Black's surgical and genetic engineers on major projects, pushing those agents to attempt greater and more horrific procedures. For all their legendary cruelty, however, yah-thelgaads don't appear to gain pleasure from such experiments. Indeed, they don't seem to feel any emotions at all on their own, but rather experience such sensations vicariously through the memories of the brains they've collected. In this way, the creatures know lust, fear, hatred, and pride without exposing their own minds to the disadvantages of being susceptible to mind-affecting effects.

---

# Yah-Thelgaad
A writhing forest of tendrils extends from one end of this chitincovered creature’s body, while from the other lashes a pincer-tipped tail. Six transparent blisters adorn its back, each containing a brain floating in thick green fluid.
**Source** Pathfinder #88: Valley of the Brain Collectors pg. 90
**XP** 38,400
CE Large aberration
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Diagnose Disease|diagnose disease]]_, _[[spells/True Seeing|true seeing]]_; Perception +26

##### Defense

**AC** 30, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 Dex, +12 insight, +5 natural, –1 size)
**hp** 200 (16d8+128)
**Fort** +13, **Ref** +11, **Will** +17
**Defensive Abilities** carapace; **DR** 10/magic and adamantine; **Immune** disease, mind-affecting effects; **Resist** cold 10, fire 10; **SR** 25

##### Offense
**Speed** 20 ft., fly 40 ft. (perfect)
**Melee** claw +22 (3d6+11 plus poison), 2 tentacles +22 (1d8+11 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Command|command]]_ disease, mind storm, powerful tentacles, spellstrike
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +20)
Constant—_diagnose disease_, _true seeing_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 12th; concentration +32)
6th (4/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 21)
5th (6/day)—_[[spells/Sending|sending]]_, _[[spells/Suffocation|suffocation]]_ (DC 22)
4th (8/day)—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Contagion|contagion]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_
3rd (8/day)—clairaudience/clairvoyance, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Slow|slow]]_ (DC 18), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Ghoul touch|ghoul touch]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Spectral Hand|spectral hand]]_
1st (8/day)—_[[spells/Chill Touch|chill touch]]_ (DC 18), _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 18), _[[spells/Shocking Grasp|shocking grasp]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 15), _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 17)

##### Statistics
**Str** 32, **Dex** 18, **Con** 26, **Int** 23, **Wis** 25, **Cha** 21
**Base Atk** +12; **CMB** +24; **CMD** 50 (62 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (necromancy), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +21, Diplomacy +13, Fly +21, Intimidate +24, Knowledge (arcana) +37, Knowledge (engineering) +37, Knowledge (geography) +37, Knowledge (planes) +37, Perception +26, Spellcraft +25, Use Magic Device +21
**Languages** Abyssal, Aklo, Common, Draconic, Infernal, Protean, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** brain collection, strange knowledge

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double

### Special Abilities

**Brain Collection (Ex)** A _[[monsters/Yah-Thelgaad|yah-thelgaad]]_ can store up to six brains of Small or Medium creatures and use them to enhance its knowledge and power. Each stored brain grants a _yah-thelgaad_ a cumulative +2 insight bonus to AC, concentration checks, and Knowledge checks. A _yah-thelgaad_ can extract a brain from a _[[conditions/Helpless|helpless]]_ opponent with a coup de _[[spells/Grace|grace]]_ attack, or as a standard action from a body that has been dead for no more than 1 minute. A _yah-thelgaad_ that has fewer than six collected brains gains two negative levels for each missing brain. These negative levels never become permanent, and can only be removed by replacing one of the _yah-thelgaad_’s collected brains. The statistics presented here assume a _yah-thelgaad_ with a full collection.

**Carapace (Ex)** The spikes on a _yah-thelgaad_’s carapace make melee attacks against it hazardous. Any opponent attempting to attack a _yah-thelgaad_ with a light weapon, unarmed strike, touch attack, or natural attack must succeed at a DC 22 Reflex save or take 1d6 points of _[[universal monster rules/Bleed|bleed]]_ damage from these bristling barbs. _Bleed_ damage from multiple failed Reflex saves does not stack. The save DC is Dexterity-based.

**_Command_ Disease (Su)** As a swift action, a _yah-thelgaad_ can cause a disease or infection currently afflicting a creature within 30 feet to quicken and activate, forcing the afflicted creature to immediately attempt a saving throw against the disease’s effects. Those who fail immediately suffer the disease’s effects. These additional saving throws count against those one must succeed at to recover from a disease, so it’s possible for a victim to be cured by succeeding at enough saving throws. Any creature that has been affected by a _yah-thelgaad_’s _command_ disease ability (whether or not the creature succeeded at the saving throw this ability triggered) takes a –2 penalty against any mind-affecting spell or effect generated by the _yah-thelgaad_ in the next minute.

**Mind Storm (Su)** As a standard action once every 1d4 rounds, a _yah-thelgaad_ can employ its own brain as well as any brains kept in its blisters to create a powerful _[[classes/Psychic|psychic]]_ _[[spells/Vortex|vortex]]_. When the creature activates this ability, all creatures within a 40-foot radius must succeed at DC 23 Will save or become _[[conditions/Confused|confused]]_ for 1d4 rounds. When a _yah-thelgaad_ activates this ability, it can choose to absorb one of its brains as a swift action to cause one creature within the area of effect that has succumbed to the _confusion_ effect to instead become _[[conditions/Stunned|stunned]]_ for 1d4 rounds. A creature _stunned_ in this manner is _confused_ for 1d4 rounds after the stun effect ends. A _yah-thelgaad_ generally saves this tactic for when it’s faced with a particularly dangerous foe, since the stun effect forces the _yah-thelgaad_ to lose one of its stored brains and gain 2 negative levels. This is a mind-affecting _confusion_ effect. The save DC is Charisma-based.

**Poison (Ex)** Claw—injury; save Fort DC 26; frequency 1/round for 6 rounds; effect 1d4 Strength damage and _[[conditions/Nauseated|nauseated]]_ for 1 round; cure 2 consecutive saves. The save DC is Constitution-based.

**Powerful Tentacles (Ex)** A _yah-thelgaad_’s tentacles are primary attacks.
**Spells (Su)** A _yah-thelgaad_ casts spells as a 12th-level _sorcerer_. Its caster level is reduced by 2 for each negative level it gains from missing brains. A _yah-thelgaad_ with no collected brains can’t cast any of its spells.
**Spellstrike (Su)** Whenever a _yah-thelgaad_ casts a spell with a range of “touch,” it can deliver the spell through its claw attack as part of a melee attack. Instead of the free melee touch attack normally allowed to deliver the spell, the yahthelgaad can make one free melee attack with its claw as part of casting the spell. If successful, this claw attack deals its normal damage (including poison) as well as the effects of the spell.
**Strange Knowledge (Ex)** All knowledge skills are class skills for yah-thelgaads.

##### Description

When a _[[monsters/Neh-Thalggu|neh-thalggu]]_ has absorbed a critical mass of thoughts and memories from an _[[monsters/Unknown|unknown]]_ number of humanoid brains, its body undergoes a horrific _[[spells/Transformation|transformation]]_. The creature enters a state of torpor, its body curling into a tight ball as it consumes the oldest of its seven stored brains to trigger the metamorphosis. Over the course of several days of selfconsumption, the _neh-thalggu_ bursts from the shell of its old body into its new incarnation as a _yah-thelgaad_.

While the _yah-thelgaad_ shares many of the features of its less powerful progenitor, it is in every way a more powerful creature than it was before. While the capacity to store one fewer brain than a _neh-thalggu_ presents some disadvantage, the _yah-thelgaad_ gains twice as much power from a collected brain as its lesser kin does. In addition, these creatures need not limit their harvest to the brains of humanoids—any Small or _Medium_ creature’s brain will do.

Yah-thelgaads are zealously devoted to the inscrutable causes of the Dominion of the Black, but they are also notoriously devout believers in that alliance’s _[[spells/Weird|weird]]_ theology, worshiping a concept they refer to as the “Ineffable Void,” among other cryptic mysteries. It is not uncommon for yahthelgaads of high rank to also possess _[[classes/Inquisitor|inquisitor]]_ or _[[classes/Oracle|oracle]]_ levels, lording their authority and fanatical faith over those in their charge—the most powerful yah-thelgaads often take levels in mystic theurge to combine their class-based mastery of the divine with their stolen brains’ arcane lore.

Yah-thelgaads often supervise the Dominion of the Black’s surgical and genetic engineers on major projects, pushing those agents to attempt greater and more horrific procedures. For all their legendary _[[feats/Cruelty|cruelty]]_, however, yah-thelgaads don’t appear to gain pleasure from such experiments. Indeed, they don’t seem to feel any emotions at all on their own, but rather experience such sensations vicariously through the memories of the brains they’ve collected. In this way, the creatures know lust, _[[universal monster rules/Fear|fear]]_, hatred, and pride without exposing their own minds to the disadvantages of being susceptible to mind-affecting effects.