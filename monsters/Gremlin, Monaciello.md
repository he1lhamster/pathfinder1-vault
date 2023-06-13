---
cssclass: [monsters]
title1: Gremlin, Monaciello
desc_short: Dressed in red robes like those of a monk, this little monster displays
  a sharp-toothed smile and flips a gold coin in its hand.
title2: Monaciello
CR: 1
sources:
- name: Bestiary 4
  page: 144
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 400
alignment: CE
size: Small
type: fey
initiative:
  bonus: 2
senses:
  low-light vision: true
auras:
- name: stymie channeling
  radius: 20
  DC: 12
AC:
  AC: 13
  touch: 13
  flat_footed: 11
  components:
    dex: 2
    size: 1
HP:
  HP: 14
  long: 2d6+7
saves:
  fort: 2
  ref: 5
  will: 4
  other: +4 vs. divine magic
DR:
- amount: 5
  weakness: cold iron
SR: 12
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +4 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: bite
      bonus:
      - 4
    - text: dagger +4 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 4
spell_like_abilities:
  entries:
  - name: prestidigitation
    source: default
    freq: At will
  - superscripts:
    - APG
    name: putrefy food and drink
    source: default
    freq: At will
    DC: 11
  - name: ghost sound
    source: default
    freq: At will
    DC: 12
  - name: silent image
    source: default
    freq: At will
    DC: 12
  - name: glitterdust
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 3
    concentration: 4
ability_scores:
  STR: 6
  DEX: 15
  CON: 14
  INT: 11
  WIS: 12
  CHA: 13
BAB: 1
CMB: -2
CMD: 10
feats:
- name: Skill Focus (Stealth)
- is_bonus: true
  name: Toughness
- is_bonus: true
  name: Weapon Finesse
skills:
  Bluff: 6
  Disable Device: 8
  Escape Artist: 7
  Perception: 6
  Sense Motive: 6
  Stealth: 18
    when moving: 14
  _racial_mods:
    Disable Device:
      _: 4
    Stealth:
      _: 4
      when moving: 0
languages:
- Aklo
special_qualities:
- compression
- magic bag
ecology:
  environment: any urban
  organization: solitary, pair, congregation (3-12), or infestation (13-20 plus 1-3
    sorcerers of 1st-3rd level, 1 rogue leader of 2nd-4th level, 2-14 trained dire
    rats, 2-5 trained venomous snakes, and 1-3 rat swarms)
  treasure_type: double
  treasure:
  - always gold coins
special_abilities:
  Magic Bag (Su): A monaciello always carries its pouch with it. This pouch contains
    an extradimensional space and operates like a bag of holding (type I). If this
    pouch is separated from the monaciello, all of its former contents are lost, and
    it becomes a normal bag that contains a number of coins equal to double the treasure
    value of a creature of the gremlin's CR. A monaciello that loses its pouch must
    create a new one, a process that takes 1d4 days. Until the new pouch is finished,
    it remains a non-magical bag, only becoming a fully functional extradimensional
    space once completed.
  Stymie Channeling (Su): A monaciello gremlin is surrounded by an aura of blasphemy.
    Any creatures channeling energy within 20 feet of a monaciello must succeed at
    a DC 12 Will save or be unable to channel for that round. The use is not lost,
    but the action is wasted.
desc_long: |-
  Most often found in urban environments, this gremlin lives among humanity, taunting religious and scholarly organizations with its pranks. Monaciello gremlins are most commonly found in monasteries and cathedrals where they wriggle their way up from the sewers and catacombs to play tricks on the devout.

  These tricksters pull blankets off sleeping clergy members, harass servants, spoil food, and hide valuables from their owners. Enamored with gold, they often overinf late the value of things with illusions, and even throw handfuls of gold coins (or illusions of gold coins if they are feeling especially stingy) to distract creatures on their trail. They pull these coins from their ever-present magical bags, confident they can always pilfer more.

  A monaciello stands 2-1/2 feet tall and weighs approximately 20 pounds.

---

# Gremlin, Monaciello
Dressed in red robes like those of a _[[classes/Monk|monk]]_, this little monster displays a sharp-toothed smile and flips a gold coin in its hand.
**Source** Bestiary 4 pg. 144
**XP** 400
CE Small fey
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +6
**Aura** stymie _[[items/Armor Magic Abilities/Channeling|channeling]]_ (20 ft.; DC 12)

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+2 Dex, +1 size)
**hp** 14 (2d6+7)
**Fort** +2, **Ref** +5, **Will** +4; +4 vs. divine magic
**DR** 5/cold iron; **SR** 12

##### Offense
**Speed** 30 ft.
**Melee** bite +4 (1d4–2), _[[items/Weapon/Dagger|dagger]]_ +4 (1d3–2/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
At will—_[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Putrefy Food and Drink|putrefy food and drink]]_ (DC 11), _[[spells/Ghost Sound|ghost sound]]_ (DC 12), _[[spells/Silent Image|silent image]]_ (DC 12)
1/day—_[[spells/Glitterdust|glitterdust]]_

##### Statistics
**Str** 6, **Dex** 15, **Con** 14, **Int** 11, **Wis** 12, **Cha** 13
**Base Atk** +1; **CMB** –2; **CMD** 10
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +6, Disable Device +8, Escape Artist +7, Perception +6, Sense Motive +6, Stealth +18 (+14 when moving); **Racial Modifiers** +4 Disable Device, +4 Stealth (+0 when moving)
**Languages** Aklo
**SQ** _[[universal monster rules/Compression|compression]]_, magic bag

##### Ecology

**Environment** any urban
**Organization** solitary, pair, congregation (3–12), or infestation (13–20 plus 1–3 sorcerers of 1st–3rd level, 1 _[[classes/Rogue|rogue]]_ leader of 2nd–4th level, 2–14 trained dire rats, 2–5 trained venomous snakes, and 1–3 rat swarms)
**Treasure** double (always gold coins)

### Special Abilities

**Magic Bag (Su)** A monaciello always carries its pouch with it. This pouch contains an extradimensional space and operates like a bag of holding (type I). If this pouch is separated from the monaciello, all of its former contents are lost, and it becomes a normal bag that contains a number of coins equal to double the treasure value of a creature of the gremlin’s CR. A monaciello that loses its pouch must create a new one, a process that takes 1d4 days. Until the new pouch is finished, it remains a non-magical bag, only becoming a fully functional extradimensional space once completed.
**Stymie _Channeling_ (Su)** A monaciello gremlin is surrounded by an aura of _[[spells/Blasphemy|blasphemy]]_. Any creatures _channeling_ energy within 20 feet of a monaciello must succeed at a DC 12 Will save or be unable to channel for that round. The use is not lost, but the action is wasted.

##### Description

Most often found in urban environments, this gremlin lives among humanity, taunting religious and scholarly organizations with its pranks. Monaciello gremlins are most commonly found in monasteries and cathedrals where they wriggle their way up from the sewers and catacombs to play tricks on the devout.

These tricksters _[[universal monster rules/Pull|pull]]_ blankets off sleeping clergy members, harass servants, spoil food, and hide valuables from their owners. Enamored with gold, they often overinf late the value of things with illusions, and even throw handfuls of gold coins (or illusions of gold coins if they are feeling especially stingy) to distract creatures on their trail. They _pull_ these coins from their ever-present magical bags, confident they can always pilfer more.

A monaciello stands 2-1/2 feet tall and weighs approximately 20 pounds.