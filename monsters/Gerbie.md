---
cssclass: [monsters]
title1: Gerbie
desc_short: This half-mouse, half-lizard creature has large eyes and stands on its
  hind legs, radiating an air of goodwill.
title2: Gerbie
CR: 4
sources:
- name: The First World, Realm of the Fey
  page: 62
  link: http://paizo.com/products/btpy9op9?Pathfinder-Campaign-Setting-The-First-World-Realm-of-the-Fey
XP: 1200
alignment: CG
size: Small
type: fey
initiative:
  bonus: 3
senses:
  low-light vision: true
auras:
- name: friendship
  radius: 60
  DC: 18
AC:
  AC: 17
  touch: 15
  flat_footed: 13
  components:
    dex: 3
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 38
  long: 7d6+14
saves:
  fort: 3
  ref: 8
  will: 8
DR:
- amount: 10
  weakness: cold iron
SR: 15
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +7 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: bite
      bonus:
      - 7
  - - text: touch +8 (forget)
      entries:
      - - effect: forget
      attack: touch
      bonus:
      - 8
  special:
  - forget
  - mental cacophony
spell_like_abilities:
  entries:
  - name: calm animals
    source: default
    freq: At will
    DC: 16
  - name: calm emotions
    source: default
    freq: At will
    DC: 17
  - name: charm monster
    source: default
    freq: At will
    DC: 18
  - name: tongues
    source: default
    freq: At will
    DC: 17
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 17
  sources:
  - name: default
    CL: 7
    concentration: 12
ability_scores:
  STR: 6
  DEX: 16
  CON: 13
  INT: 11
  WIS: 16
  CHA: 21
BAB: 3
CMB: 0
CMD: 14
feats:
- name: Dodge
- name: Toughness
- name: Weapon Finesse
- name: Weapon Focus (touch)
skills:
  Acrobatics: 12
  Diplomacy: 19
  Handle Animal: 12
  Heal: 10
  Perception: 13
  Perform (comedy): 9
  Ride: 10
  _racial_mods:
    Diplomacy:
      _: 4
languages:
- First Speech
- truespeech
special_qualities:
- charmer
ecology:
  environment: any (First World)
  organization: solitary, pair, or party (3-6)
  treasure_type: standard
special_abilities:
  Aura of Friendship (Sp): Any creature within 60 feet of a gerbie must succeed at
    a DC 18 Will saving throw or have its attitude adjusted to friendly toward both
    the gerbie and any other creatures currently within the aura's area of effect,
    as per charm monster. This positive attitude toward other targets of the ability
    lasts for 1 day after leaving the gerbie's aura. A creature that leaves and reenters
    a gerbie's aura can attempt another saving throw. A creature that successfully
    saves against this ability is immune to that gerbie's aura for 24 hours. Being
    attacked by another creature within the aura (including the gerbie) immediately
    ends the forced friendliness toward that creature and prompts a new save against
    the aura, with the standard +5 bonus for being threatened while charmed. The save
    DC is Charisma-based.
  Charmer (Su): A creature targeted by the gerbie's charm monster spell-like ability
    does not receive the +5 bonus to its saving throw if being attacked by the gerbie
    or its allies. This does not apply to the aura of friendship ability.
  Forget (Su): A gerbie that makes a successful touch attack on a creature can cause
    it to forget something, as if it had failed its saving throw against modify memory,
    save that the effect is immediate and the gerbie does not need to spend time visualizing
    the modification.
  Mental Cacophony (Su): As a standard action, a gerbie can force any creature within
    100 feet to attempt a DC 18 Will saving throw or be sickened for 1d10 rounds as
    its mind is overloaded by the surface thoughts of trees, bugs, and any other living
    things around it. The affected character cannot process or interpret this information,
    though certain thoughts may stand out at the GM's discretion. The save DC is Charisma-based.
desc_long: |-
  Gerbies are the fey of interspecies empathy and communication, devoted to fostering harmony and friendship. They abhor violence, and attempt to prevent it by granting adversaries the ability to talk to and understand each other. When that doesn't work, gerbies see nothing wrong with direct magical intervention, either forcing the foes into friendship or causing creatures to forget whatever painful memories made them want to fight in the first place.

   While the adorable gerbies can make excellent friends and companions- helping further diplomacy, translate documents, and throw parties-gerbies often see it as their duty to “protect and correct” soldiers, rampaging monsters, and others whose professions involve violence, which can lead to no end of hassle for adventurers looking to slay their way to glory. In such situations, the best answer is usually to humor the gerbie until it falls asleep or gets distracted, then slip out of its friendship aura and flee quickly. While gerbie settlements tend to be idyllic places, full of laughter and huts built from hollowed-out mushrooms, many gerbies feel called to wander the world teaching other creatures the value of friendship. Though they understand that some creatures need to eat meat to live, gerbies themselves are zealous advocates of vegetarianism.

   A typical gerbie is 3 feet tall and weighs 20 pounds.

---

# Gerbie
This half-mouse, half-lizard creature has large eyes and stands on its hind legs, radiating an air of goodwill.
**Source** The First World, Realm of the Fey pg. 62
**XP** 1,200

CG Small fey
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13
**Aura** friendship (60 ft., DC 18)

##### Defense

**AC** 17, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +1 dodge, +2 natural, +1 size)
**hp** 38 (7d6+14)
**Fort** +3, **Ref** +8, **Will** +8
**DR** 10/cold iron; **SR** 15

##### Offense
**Speed** 30 ft.
**Melee** bite +7 (1d4-2) or
touch +8 (forget)
**Special Attacks** forget, mental cacophony
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
At will—_[[spells/Calm Animals|calm animals]]_ (DC 16), _[[spells/Calm Emotions|calm emotions]]_ (DC 17), _[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Tongues|tongues]]_ (DC 17)
 3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17)

##### Statistics
**Str** 6, **Dex** 16, **Con** 13, **Int** 11, **Wis** 16, **Cha** 21
**Base Atk** +3; **CMB** +0; **CMD** 14
**Feats** _Dodge_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (touch)
**Skills** Acrobatics +12, Diplomacy +19, Handle Animal +12, _[[spells/Heal|Heal]]_ +10, Perception +13, Perform (comedy) +9, Ride +10; **Racial Modifiers** +4 Diplomacy
**Languages** First Speech; truespeech
**SQ** charmer

##### Ecology

**Environment** any (First World)
**Organization** solitary, pair, or party (3-6)
**Treasure** standard

### Special Abilities

**Aura of Friendship (Sp)** Any creature within 60 feet of a _[[monsters/Gerbie|gerbie]]_ must succeed at a DC 18 Will saving throw or have its attitude adjusted to friendly toward both the _gerbie_ and any other creatures currently within the aura’s area of effect, as per _charm monster_. This positive attitude toward other targets of the ability lasts for 1 day after leaving the _gerbie_’s aura. A creature that leaves and reenters a _gerbie_’s aura can attempt another saving throw. A creature that successfully saves against this ability is immune to that _gerbie_’s aura for 24 hours. Being attacked by another creature within the aura (including the _gerbie_) immediately ends the forced friendliness toward that creature and prompts a new save against the aura, with the standard +5 bonus for being threatened while charmed. The save DC is Charisma-based.

**Charmer (Su)** A creature targeted by the _gerbie_’s _charm monster_ spell-like ability does not receive the +5 bonus to its saving throw if being attacked by the _gerbie_ or its allies. This does not apply to the aura of friendship ability.

**Forget (Su)** A _gerbie_ that makes a successful touch attack on a creature can cause it to forget something, as if it had failed its saving throw against _[[spells/Modify Memory|modify memory]]_, save that the effect is immediate and the _gerbie_ does not need to spend time visualizing the modification.

**Mental Cacophony (Su)** As a standard action, a _gerbie_ can force any creature within 100 feet to attempt a DC 18 Will saving throw or be _[[conditions/Sickened|sickened]]_ for 1d10 rounds as its mind is overloaded by the surface thoughts of trees, bugs, and any other living things around it. The affected character cannot process or interpret this information, though certain thoughts may stand out at the GM’s discretion. The save DC is Charisma-based.

##### Description

Gerbies are the fey of interspecies _[[feats/Empathy|empathy]]_ and communication, devoted to fostering harmony and friendship. They abhor violence, and attempt to prevent it by granting adversaries the ability to talk to and understand each other. When that doesn’t work, gerbies see nothing wrong with direct magical intervention, either forcing the foes into friendship or causing creatures to forget whatever painful memories made them want to fight in the first place.

While the adorable gerbies can make excellent friends and companions— helping further diplomacy, translate documents, and throw parties—gerbies often see it as their duty to “protect and correct” soldiers, _[[items/Armor Magic Abilities/Rampaging|rampaging]]_ monsters, and others whose professions involve violence, which can lead to no end of hassle for adventurers looking to slay their way to glory. In such situations, the best answer is usually to humor the _gerbie_ until it falls asleep or gets distracted, then slip out of its friendship aura and flee quickly. While _gerbie_ settlements tend to be idyllic places, full of laughter and huts built from hollowed-out mushrooms, many gerbies feel _[[items/Weapon Magic Abilities/Called|called]]_ to wander the world teaching other creatures the value of friendship. Though they understand that some creatures need to eat meat to live, gerbies themselves are zealous advocates of vegetarianism.

A typical _gerbie_ is 3 feet tall and weighs 20 pounds.