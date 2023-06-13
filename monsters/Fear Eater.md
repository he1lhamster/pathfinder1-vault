---
cssclass: [monsters]
title1: Fear Eater
desc_short: A distressingly humanoid face and stubby arms grow from this maggotlike
  creature's body.
title2: Fear Eater
CR: 5
sources:
- name: Occult Bestiary
  page: 27
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 1600
alignment: NE
size: Medium
type: fey
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 18
  touch: 16
  flat_footed: 12
  components:
    dex: 6
    natural: 2
HP:
  HP: 52
  long: 8d6+24
saves:
  fort: 5
  ref: 12
  will: 7
DR:
- amount: 5
  weakness: cold iron
immunities:
- disease
- fear
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: 2 claws +10 (1d6+2 plus anxiety spores)
      entries:
      - - damage: 1d6+2
        - effect: anxiety spores
      count: 2
      attack: claws
      bonus:
      - 10
  special:
  - anxiety spores
  - dread burst
  - fungal snare
spell_like_abilities:
  entries:
  - name: cause fear
    source: default
    freq: At will
    DC: 13
  - name: dancing lights
    source: default
    freq: At will
  - name: faerie fire
    source: default
    freq: 3/day
  - superscripts:
    - OA
    name: paranoia
    source: default
    freq: 3/day
    DC: 14
  - name: fear
    source: default
    freq: 1/day
  - name: feather fall
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 5
    concentration: 7
ability_scores:
  STR: 14
  DEX: 22
  CON: 17
  INT: 11
  WIS: 12
  CHA: 15
BAB: 4
CMB: 6
CMD: 22
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Power Attack
- name: Weapon Finesse
skills:
  Acrobatics: 17
  Climb: 21
  Intimidate: 10
  Perception: 12
  Sense Motive: 12
  Stealth: 17
  _racial_mods:
    Climb:
      _: 8
languages:
- Aklo
- Undercommon
ecology:
  environment: any underground
  organization: solitary, pair, or band (3-6)
  treasure_type: standard
special_abilities:
  Anxiety Spores (Ex): |-
    Any creature struck by the fear eater's claws must succeed at a DC 17 Fortitude saving throw or be infected with anxiety spores, which cause nervousness and muscle tremors.

    Anxiety Spores: Disease-injury; save Fort DC 17; onset 1 round; frequency 1/minute; effect cumulative -1 penalty on saving throws against emotion-manipulating effects (maximum -5); cure 2 consecutive saves
  Dread Burst (Su): As a standard action, a fear eater can cause mushrooms to erupt
    from any creature within 30 feet already infected with its anxiety spores. The
    targeted creature takes 1d6 points of Charisma damage (Fortitude DC 17 negates)
    as the growing spores siphon away her emotions. If the affected creature is currently
    shaken, frightened, or panicked, any creature within 10 feet gains the same condition
    for 1d4 rounds (Will DC 17 negates). This is a mind-affecting fear effect. The
    save DCs are Charisma-based.
  Fungal Snare (Ex): Once every 1d4 rounds, a fear eater can spew a fungal mass up
    to 30 feet, which explodes and coats all creatures within a 10-foot-radius burst
    with sticky filaments. Creatures other than fear eaters are entangled (Reflex
    DC 17 negates). An entangled creature can attempt to break free with a successful
    DC 14 Strength or Escape Artist check as a move action. The save DC is Charisma-based.
desc_long: |-
  These malicious fey prowl the darkest corners of the world, inspiring terror to fertilize the curious fungal fruits that sustain them. Fear eaters tend vast gardens of luminescent mushrooms that grow upon the bound, cringing bodies of their captives. The mushrooms drain emotions from the creatures fertilizing them, and their spores cause spikes of fear in their hosts, which spur the mushrooms to grow even larger. Many such gardens can be found in the stalactite-city known as the Court of Ether, for its dark fey inhabitants crave the piquant misery contained in the mushrooms and consider them a delicacy to be used in only the most bizarre culinary delights. Despite their role in production of these despair-laced luxuries, fear eaters are welcome only on the margins of most fey societies, and most fey rulers prefer to purchase their specialities through intermediaries rather than be seen associating with fear eaters directly.

  Fear eaters are interested only in breeding the perfect mushrooms, and can be dangerous opponents when hunting new fertilizer or protecting their crops. The average fear eater is 8 feet long and weighs 400 pounds.

---

# Fear Eater
A distressingly humanoid face and stubby arms grow from this maggotlike creature’s body.
**Source** Occult Bestiary pg. 27
**XP** 1,600

NE Medium fey
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 18, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+6 Dex, +2 natural)
**hp** 52 (8d6+24)
**Fort** +5, **Ref** +12, **Will** +7
**DR** 5/cold iron; **Immune** disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 claws +10 (1d6+2 plus anxiety spores)
**Special Attacks** anxiety spores, dread burst, fungal _[[spells/Snare|snare]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th, concentration +7)
At will—_[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Dancing Lights|dancing lights]]_
3/day—_[[spells/Faerie Fire|faerie fire]]_, _[[spells/Paranoia|paranoia]]_ (DC 14)
1/day—_fear_, _[[spells/Feather Fall|feather fall]]_

##### Statistics
**Str** 14, **Dex** 22, **Con** 17, **Int** 11, **Wis** 12, **Cha** 15
**Base Atk** +4; **CMB** +6; **CMD** 22 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +17, _Climb_ +21, Intimidate +10, Perception +12, Sense Motive +12, Stealth +17; **Racial Modifiers** +8 _Climb_
**Languages** Aklo, Undercommon

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or band (3–6)
**Treasure** standard

### Special Abilities

**Anxiety Spores (Ex)** Any creature struck by the _[[feats/Fear Eater|fear eater]]_’s claws must succeed at a DC 17 Fortitude saving throw or be infected with anxiety spores, which cause nervousness and muscle tremors.

Anxiety Spores: Disease—injury; save Fort DC 17; onset 1 round; frequency 1/minute; effect cumulative –1 penalty on saving throws against emotion-manipulating effects (maximum –5); cure 2 consecutive saves

**Dread Burst (Su)** As a standard action, a _fear eater_ can cause mushrooms to erupt from any creature within 30 feet already infected with its anxiety spores. The targeted creature takes 1d6 points of Charisma damage (Fortitude DC 17 negates) as the _[[items/Weapon Magic Abilities/Growing|growing]]_ spores siphon away her emotions. If the affected creature is currently _[[conditions/Shaken|shaken]]_, _[[conditions/Frightened|frightened]]_, or _[[conditions/Panicked|panicked]]_, any creature within 10 feet gains the same condition for 1d4 rounds (Will DC 17 negates). This is a mind-affecting _fear_ effect. The save DCs are Charisma-based.

**Fungal _Snare_ (Ex)** Once every 1d4 rounds, a _fear eater_ can spew a fungal mass up to 30 feet, which explodes and coats all creatures within a 10-foot-radius burst with _[[items/Weapon Magic Abilities/Sticky|sticky]]_ filaments. Creatures other than _fear_ eaters are _[[conditions/Entangled|entangled]]_ (Reflex DC 17 negates). An _entangled_ creature can attempt to break free with a successful DC 14 Strength or Escape Artist check as a move action. The save DC is Charisma-based.

##### Description

These malicious fey prowl the darkest corners of the world, inspiring terror to fertilize the curious fungal fruits that sustain them. _Fear_ eaters tend vast gardens of luminescent mushrooms that grow upon the bound, cringing bodies of their captives. The mushrooms drain emotions from the creatures fertilizing them, and their spores cause spikes of _fear_ in their hosts, which spur the mushrooms to grow even larger. Many such gardens can be found in the stalactite-city known as the Court of Ether, for its dark fey inhabitants crave the piquant misery contained in the mushrooms and consider them a delicacy to be used in only the most bizarre culinary delights. Despite their role in production of these despair-laced luxuries, _fear_ eaters are welcome only on the margins of most fey societies, and most fey rulers prefer to purchase their specialities through intermediaries rather than be seen associating with _fear_ eaters directly.

_Fear_ eaters are interested only in breeding the perfect mushrooms, and can be dangerous opponents when hunting new fertilizer or protecting their crops. The average _fear eater_ is 8 feet long and weighs 400 pounds.