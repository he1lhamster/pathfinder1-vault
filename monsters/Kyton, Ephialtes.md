---
cssclass: [monsters]
title1: Kyton, Ephialtes
desc_short: Amid a roiling cloud of deepest dark, the rattle of chains and heavy footfalls
  announce a being of immense size. An infernal, gasping hiss draws the darkness back,
  revealing a tortured, four-legged fiend of exposed bone and ragged flesh draped
  in chains. Barbs and hooks hang from these wrought iron bands, matching the fiend's
  tail as they writhe like snakes in search of prey.
title2: Ephialtes
CR: 16
sources:
- name: 'Pathfinder #30: The Twice-Damned Prince'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8d54
XP: 76800
alignment: LE
size: Huge
type: outsider
subtypes:
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 6
senses:
  darkvision: 60
auras:
- name: frightful presence
  radius: 30
  DC: 22
AC:
  AC: 30
  touch: 10
  flat_footed: 28
  components:
    armor: 8
    dex: 2
    natural: 12
    size: -2
HP:
  HP: 243
  long: 18d10+144
  regeneration: 5
  regeneration_weakness: good weapons and spells, silver weapons
saves:
  fort: 14
  ref: 13
  will: 14
defensive_abilities:
- chain armor
DR:
- amount: 10
  weakness: silver or good
immunities:
- cold
- fear
- poison
resistances:
  acid: 10
  fire: 10
SR: 27
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +24 (2d6+8)
      entries:
      - - damage: 2d6+8
      attack: bite
      bonus:
      - 24
    - text: 2 chains +25 (2d8+8/19-20)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
      count: 2
      attack: chains
      bonus:
      - 25
    - text: 2 claws +24 (1d8+8)
      entries:
      - - damage: 1d8+8
      count: 2
      attack: claws
      bonus:
      - 24
    - text: tail +19 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: tail
      bonus:
      - 19
  special:
  - breath weapon (50-ft. cone, 2d8+8 piercing damage plus grab, Reflex DC 27 for
    half, usable every 1d4 rounds)
  - dancing chains
  - entrapping chains
  - pull (breath weapon, 10 feet)
  - rend (2 chains, 2d8+12)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: At will
    other: self only
  - name: dimensional anchor
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: shadow walk
    source: default
    freq: 3/day
    DC: 19
  - name: silence
    source: default
    freq: 3/day
    DC: 15
  - name: discern location
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
ability_scores:
  STR: 26
  DEX: 14
  CON: 26
  INT: 10
  WIS: 12
  CHA: 16
BAB: 18
CMB: 28
CMB_other: +32 grapple or pull
CMD: 40
CMD_other: 44 vs. trip
feats:
- name: Alertness
- name: Bleeding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Critical (chains)
- name: Improved Initiative
- name: Iron Will
- name: Stand Still
- name: Weapon Focus (chains)
skills:
  Bluff: 12
  Climb: 15
  Escape Artist: 13
  Intimidate: 24
  Knowledge (planes): 13
  Perception: 24
  Sense Motive: 18
  Stealth: 15
  Survival: 22
languages:
- Infernal
ecology:
  environment: any (Shadow Plane)
  organization: solitary or team (2-8)
  treasure_type: standard
special_abilities:
  Breath Weapon (Su): |-
    As a full-round action, an ephialtes kyton may exhale a spread of barbed, grappling chains anchored within its massive maw, targeting up to six creatures in a 50-foot cone. Those failing a DC 27 Reflex save suffer 2d8+8 points of piercing damage and the kyton may make a combat maneuver check as an immediate action to grapple each victim with the animate chains. A successful save cuts the damage in half and avoids the grapple opportunity. Those successfully grappled by the chains become subject to the kyton's pull ability. A kyton cannot use its breath weapon again while it is grappling or pulling creatures with its breath weapon chains. Otherwise, it may use the breath weapon once every 1d4 rounds. The save DC is Constitution-based.

    An ephialtes kyton's chains (hardness 10, hp 10, Break DC 26) can be broken, or attacked by making a sunder attempt. If the chain is currently grappling a target, the attacker gains a +4 circumstance bonus on the CMB check to sunder. Severing a chain deals no damage to a kyton.
  Chain Armor (Ex): The chains that adorn an ephialtes kyton grant it a +8 armor bonus,
    but are not treated as armor for the purpose of arcane spell failure, armor check
    penalties, maximum Dexterity, weight, or proficiency.
  Dancing Chains (Su): An ephialtes kyton can control up to four chains within 30
    feet as a standard action, making the chains dance or move as it wishes. In addition,
    the kyton can increase these chains' length by up to 15 feet and cause them to
    sprout razor-sharp barbs. The chains attack as effectively as the kyton itself.
    If a chain is in another creature's possession, the creature can attempt a DC
    22 Will save to break the ephialtes kyton's power over that chain. If the save
    is successful, the kyton cannot attempt to control that particular chain again
    for 24 hours or until the chain leaves the other creature's possession. An ephialtes
    kyton can climb chains it controls at its normal speed without making Climb checks.
    The save DC is Charisma-based.
  Entrapping Chains (Su): With a successful combat maneuver check, an ephialtes kyton
    may transfer an adjacent creature grappled by the kyton's breath weapon chains
    to the chains adorning its body, giving the target the pinned condition while
    the kyton deals with remaining foes. The kyton does not retain the grappled condition
    while pinning such creatures. Pinned victims can free themselves with a combat
    maneuver check to break the pin or an Escape Artist check. Other creatures can
    attempt to free pinned victims by making a sunder attempt (hardness 10, hp 10).
    An ephialtes kyton may entrap 1 Large, 2 Medium, 8 Small, 32 Tiny, or 128 Diminutive
    or smaller opponents.
  Pull (Ex): An ephialtes kyton has a +4 racial bonus on CMB checks made using its
    pull special attack.
desc_long: |-
  Sadistic hunters and tormentors of all living souls, ephialtes kytons usually roam the planes in service to the lords of Hell and Shadow, but occasionally in pursuit of their own fell interests. They ruthlessly abduct the innocent and retrieve the damned, dragging their victims into the fires of Hell or the gnashing, wailing dark of the Plane of Shadow. They have no fear, tracking their chosen prey regardless of distance or challenge, and shackle dragons, giants, and humanoids alike for their eternal torturous rewards.

  Ephialtes kytons travel in silent grace while cloaked in darkness, but drop their stealthy veils when ready to intimidate those they've come to collect or punish. Then, their frightening gaze matches the deadly intent of the chains piercing their flesh. These animated, wrought iron bands serve as protection and weapons in the hands or claws of all kytons, but may also bind and lash their victims to the ephialtes' ever-bleeding hide to carry them into the Great Beyond. A typical ephialtes stands 25 feet tall and weighs over 15 tons with the combined burden of their deadly chains.

---

# Kyton, Ephialtes
Amid a roiling cloud of deepest dark, the rattle of chains and heavy footfalls announce a being of immense size. An infernal, gasping hiss draws the _[[spells/Darkness|darkness]]_ back, revealing a tortured, four-legged fiend of exposed bone and ragged flesh draped in chains. Barbs and hooks hang from these wrought iron bands, matching the fiend’s tail as they writhe like snakes in search of prey.
**Source** Pathfinder #30: The Twice-Damned Prince pg. 86
**XP** 76,800

LE Huge outsider (evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +24
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 22)

##### Defense

**AC** 30, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+8 armor, +2 Dex, +12 natural, -2 size)
**hp** 243 (18d10+144); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons and spells, silver weapons)
**Fort** +14, **Ref** +13, **Will** +14
**Defensive Abilities** chain armor; **DR** 10/silver or good; **Immune** cold, _[[universal monster rules/Fear|fear]]_, poison; **Resist** acid 10, fire 10; **SR** 27

##### Offense
**Speed** 30 ft.
**Melee** bite +24 (2d6+8), 2 chains +25 (2d8+8/19-20), 2 claws +24 (1d8+8), tail +19 (1d8+4)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 2d8+8 piercing damage plus _[[universal monster rules/Grab|grab]]_, Reflex DC 27 for half, usable every 1d4 rounds), _[[items/Weapon Magic Abilities/Dancing|dancing]]_ chains, entrapping chains, _[[universal monster rules/Pull|pull]]_ (_breath weapon_, 10 feet), _[[universal monster rules/Rend|rend]]_ (2 chains, 2d8+12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th)
At will - _[[spells/Blur|blur]]_ (self only), _[[spells/Dimensional Anchor|dimensional anchor]]_
3/day - _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Shadow Walk|shadow walk]]_ (DC 19), _[[spells/Silence|silence]]_ (DC 15)
1/day - _[[spells/Discern Location|discern location]]_

##### Statistics
**Str** 26, **Dex** 14, **Con** 26, **Int** 10, **Wis** 12, **Cha** 16
**Base Atk** +18; **CMB** +28 (+32 grapple or _pull_); **CMD** 40 (44 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (chains), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (chains)
**Skills** Bluff +12, _[[universal monster rules/Climb|Climb]]_ +15, Escape Artist +13, Intimidate +24, Knowledge (planes) +13, Perception +24, Sense Motive +18, Stealth +15, Survival +22
**Languages** Infernal

##### Ecology

**Environment** any (_[[items/Armor Magic Abilities/Shadow|Shadow]]_ Plane)
**Organization** solitary or team (2-8)
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Su)** As a full-round action, an ephialtes _kyton_ may exhale a spread of barbed, grappling chains anchored within its massive maw, targeting up to six creatures in a 50-foot cone. Those failing a DC 27 Reflex save suffer 2d8+8 points of piercing damage and the _kyton_ may make a combat maneuver check as an immediate action to grapple each victim with the animate chains. A successful save cuts the damage in half and avoids the grapple opportunity. Those successfully _[[conditions/Grappled|grappled]]_ by the chains become subject to the _kyton_’s _pull_ ability. A _kyton_ cannot use its _breath weapon_ again while it is grappling or pulling creatures with its _breath weapon_ chains. Otherwise, it may use the _breath weapon_ once every 1d4 rounds. The save DC is Constitution-based.

An ephialtes _kyton_’s chains (hardness 10, hp 10, Break DC 26) can be _[[conditions/Broken|broken]]_, or attacked by making a sunder attempt. If the chain is currently grappling a target, the attacker gains a +4 circumstance bonus on the CMB check to sunder. Severing a chain deals no damage to a _kyton_.

**Chain Armor (Ex)** The chains that adorn an ephialtes _kyton_ grant it a +8 armor bonus, but are not treated as armor for the purpose of arcane spell failure, armor check penalties, maximum Dexterity, weight, or proficiency.

**_Dancing_ Chains (Su)** An ephialtes _kyton_ can control up to four chains within 30 feet as a standard action, making the chains dance or move as it wishes. In addition, the _kyton_ can increase these chains’ length by up to 15 feet and cause them to sprout razor-sharp barbs. The chains attack as effectively as the _kyton_ itself. If a chain is in another creature’s _[[spells/Possession|possession]]_, the creature can attempt a DC 22 Will save to break the ephialtes _kyton_’s power over that chain. If the save is successful, the _kyton_ cannot attempt to control that particular chain again for 24 hours or until the chain leaves the other creature’s _possession_. An ephialtes _kyton_ can _climb_ chains it controls at its normal speed without making _Climb_ checks. The save DC is Charisma-based.

**Entrapping Chains (Su)** With a successful combat maneuver check, an ephialtes _kyton_ may transfer an adjacent creature _grappled_ by the _kyton_’s _breath weapon_ chains to the chains adorning its body, giving the target the _[[conditions/Pinned|pinned]]_ condition while the _kyton_ deals with remaining foes. The _kyton_ does not retain the _grappled_ condition while pinning such creatures. _Pinned_ victims can free themselves with a combat maneuver check to break the pin or an Escape Artist check. Other creatures can attempt to free _pinned_ victims by making a sunder attempt (hardness 10, hp 10). An ephialtes _kyton_ may _[[universal monster rules/Entrap|entrap]]_ 1 Large, 2 Medium, 8 Small, 32 Tiny, or 128 Diminutive or smaller opponents.

**_Pull_ (Ex)** An ephialtes _kyton_ has a +4 racial bonus on CMB checks made using its _pull_ special attack.

##### Description

Sadistic hunters and tormentors of all living souls, ephialtes kytons usually roam the planes in service to the lords of Hell and _Shadow_, but occasionally in pursuit of their own fell interests. They ruthlessly abduct the innocent and retrieve the _[[feats/Damned|damned]]_, dragging their victims into the fires of Hell or the gnashing, wailing dark of the Plane of _Shadow_. They have no _fear_, tracking their chosen prey regardless of distance or challenge, and _[[spells/Shackle|shackle]]_ dragons, giants, and humanoids alike for their eternal torturous rewards.

Ephialtes kytons travel in silent _[[spells/Grace|grace]]_ while cloaked in _darkness_, but drop their _[[feats/Stealthy|stealthy]]_ veils when ready to intimidate those they’ve come to collect or punish. Then, their frightening _[[universal monster rules/Gaze|gaze]]_ matches the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ intent of the chains piercing their flesh. These _[[items/Armor Magic Abilities/Animated|animated]]_, wrought iron bands serve as protection and weapons in the hands or claws of all kytons, but may also bind and lash their victims to the ephialtes’ ever-bleeding hide to carry them into the Great Beyond. A typical ephialtes stands 25 feet tall and weighs over 15 tons with the combined burden of their _deadly_ chains.