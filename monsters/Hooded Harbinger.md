---
cssclass: [monsters]
title1: Hooded Harbinger
desc_short: This creature resembles a mummified humanoid swathed in filthy, sallow
  rags. Its stooped posture and ragged coverings make its height hard to judge. Its
  arms appear abnormally long, or perhaps dislocated and hanging freely. A hood of
  the same jaundiced fabric obscures its face.
title2: Hooded Harbinger
CR: 12
sources:
- name: 'Pathfinder #112: The Whisper Out of Time'
  page: 88
  link: http://paizo.com/products/btpy9q9o?Pathfinder-Adventure-Path-112-The-Whisper-Out-of-Time
XP: 19200
alignment: CE
size: Medium
type: aberration
initiative:
  bonus: 8
senses:
  darkvision: 60
  see invisibility: true
auras:
- name: profane reek
  DC: 21
- name: unnatural aura
  radius: 30
AC:
  AC: 27
  touch: 17
  flat_footed: 23
  components:
    dex: 4
    natural: 10
    profane: 3
HP:
  HP: 161
  long: 17d8+85
saves:
  fort: 12
  ref: 11
  will: 13
DR:
- amount: 10
  weakness: lawful and slashing
immunities:
- death effects
- mind-affecting effects
- poison
resistances:
  cold: 10
SR: 23
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 slams +20 (2d6+8/19-20 plus trip)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
        - effect: trip
      count: 2
      attack: slams
      bonus:
      - 20
  - - text: melee touch +20 (bloodless touch)
      entries:
      - - effect: bloodless touch
      attack: melee touch
      bonus:
      - 20
  special:
  - channel negative energy 3/day (DC 21, command undead only)
  - manifest Yellow Sign
  - prophetic utterance
space: 5
reach: 10
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: At will
  - name: detect law
    source: default
    freq: At will
  - name: confusion
    source: default
    freq: 3/day
    DC: 17
  - name: mass hold person
    source: default
    freq: 3/day
    DC: 20
  - name: plane shift
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 15
  - name: teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: freedom of movement
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 15
    concentration: 18
ability_scores:
  STR: 26
  DEX: 18
  CON: 21
  INT: 16
  WIS: 13
  CHA: 17
BAB: 12
CMB: 20
CMD: 34
feats:
- name: Bleeding Critical
- name: Combat Casting
- name: Combat Reflexes
- is_bonus: true
  name: Command Undead
- name: Critical Focus
- name: Great Fortitude
- name: Improved Critical (slam)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
skills:
  Acrobatics: 24
  Climb: 28
  Escape Artist: 24
  Intimidate: 31
  Knowledge (religion): 27
  Perception: 21
  Stealth: 24
  _racial_mods:
    Knowledge (religion):
      _: 4
    Intimidate:
      _: 8
languages:
- Aklo
- Common
- telepathy 100 ft.
- tongues
special_qualities:
- terrible visage
ecology:
  environment: any
  organization: solitary
  treasure_type: none
special_abilities:
  Bloodless Touch (Ex): When a hooded harbinger makes a melee touch attack, its target
    must attempt a DC 23 Fortitude save. If the save is successful, the victim takes
    2d6+8 points of damage and is wracked by pain for 1 round, gaining the staggered
    condition. It is thereafter immune to that hooded harbinger's bloodless touch
    for 1 day. On a failed save, the portion of the victim's body that is touched
    begins to swell and turn purplishblack as the blood flow to it is restricted.
    This effect deals 4d6+12 points of damage per round and the victim gains the staggered
    and sickened conditions from the intense pain. After 1d4 rounds, the victim can
    attempt a new saving throw each round to try and end the effect. The effect can
    be ended sooner by a heal spell or a successful DC 23 Heal check. The Heal check
    requires a precise incision to the affected flesh, and consequently deals 2d6
    points of bleed damage to the victim as the pressure of the entrapped blood flow
    is released. Once a victim has been affected by a bloodless touch, it can't be
    affected by another until the effects of the first one have ended. If the effects
    are ended by a successful save, then that individual is immune to further bloodless
    touch attacks by that hooded harbinger for 1 day. The bloodless touch attack of
    a hooded harbinger affects only living creatures with recognizable physiology
    and a blood supply. Undead, oozes, most constructs, and creatures that are not
    subject to precision damage are immune to bloodless touch. The save DC is Constitution-based.
  Manifest Yellow Sign (Sp): Once per day, a hooded harbinger can trace a mystical
    pattern in the air, causing a glowing, immaterial image of the Yellow Sign to
    appear before it. This image remains in place for 1d4 minutes. Any creatures within
    100 feet who is able to see the sign (it glows as per light) must succeed at a
    DC 23 Will save or be confused for as long as the sign persists. The sign can
    be erased with dispel chaos, dispel evil, dispel magic, or erase with a successful
    DC 26 caster level check. Anyone under the effects of the Yellow Sign will not
    act against the hooded harbinger in any way, though that does not mean that they
    will follow its commands. The save DC is Charisma-based and includes a +2 racial
    bonus. This is a mind-affecting compulsion effect.
  Profane Reek (Su): The musty, carrion stench wafting from the foul folds of a hooded
    harbinger's rags extends in a 5-foot radius, creating an aura of obscene influence
    around the creature. This terrible smell gives a hooded harbinger a profane bonus
    to its AC equal to its Charisma modifier. In addition, any breathing creature
    that enters this cloud must succeed at a DC 21 Fortitude save or be affected as
    though under the mental effects of a mind fog spell for as long as it remains
    within the profane reek's area of effect and for 2d4 rounds after it leaves. A
    creature that succeeds at its save is immune to the mind fog effect of that hooded
    harbinger's profane reek for 1 day. The save DC is Charisma-based.
  Prophetic Utterance (Su): Three times per day as an immediate action, a hooded harbinger
    can mutter a prophetic utterance against any single creature within 100 feet that
    has just dealt damage to it. This mutter is unintelligible to anyone but the target,
    which hears the utterance as a telepathic message pronouncing its doom. The target
    is immediately affected by a doom spell (no save) for the next hour or until the
    utterance is successfully dispelled (requiring a successful DC 26 caster level
    check).
  Terrible Visage (Su): A hooded harbinger never reveals its face. Only if slain or
    rendered helpless can anyone attempt to remove the hood and reveal the harbinger's
    true visage. However, as layers of the stinking, rotten wrappings around its face
    are peeled back or cut away, new layers are found beneath. These many filth-crusted
    layers can be removed only with 1d4+2 rounds of effort. If they are successfully
    removed, only those adjacent to the creature can see the revealed countenance
    and anyone able to do so must succeed at a DC 21 Will save or be affected by an
    insanity spell. Those who succeed at their saves are unaffected, as their minds
    mercifully erase the image from their memories. Those cured of the insanity receive
    the same relief. Immediately after the hooded harbinger's face is revealed, its
    body explodes in a massive flash of light and concussive force that completely
    obliterates all evidence of it. Anyone within 10 feet of the corpse when it explodes
    takes 6d10 points of force damage (Reflex DC 23 half) and must attempt two DC
    23 Fortitude saves, one against blindness and one against deafness (both as per
    blindness/deafness). The save DC to resist the insanity effect is Charisma-based,
    and the save DCs to resist the explosion's effects are Constitution-based.
desc_long: |-
  It is said that the Crawling Chaos is the messenger of the Great Old Ones, but whether this is by their command or his own whim is debatable. Regardless of why, the Great Old One known as Hastur sometimes instead relies on his hooded harbingers to relay messages to his far-flung cults and even to the High Priest Not To Be Described of mystery-shrouded Leng. These dread figures swathed in filthy yellow rags bear the whispered tidings of their Unnamed Lord. There are those who even speculate that the veiled priest of Leng is actually the greatest of the hooded harbingers, who gained some measure of autonomy-but the truth of this remains unknown. Thought to have originated in distant Carcosa by unthinkable means, hooded harbingers are exceedingly rare, and seldom is more than one encountered at a time.

  Though tasked with the menial role of messengers, hooded harbingers take their charge very seriously. Infused with the hateful potency of their master, they are able to call upon many terrible powers in defense of their duties. When forced into combat, they prefer to trip opponents with the trailing ends of their ragged arm coverings and administer their bloodless touch to as many victims as possible. They always attempt to use plane shift to flee if in danger of imminent defeat.

  Serving as messengers for Hastur, hooded harbingers receive the communications they deliver directly from the Great Old One via mental transmission. Upon receiving the message, the hooded harbinger twitches and shakes as if it were having a seizure. During this time they are particularly dangerous, because if they are attacked or distracted in any way, they fly into a furious rage and the offender risks attracting the attention of the King in Yellow.

  No one has seen a hooded harbinger's face and lived to describe it. If its hood is pulled back, the creature's head is seen to be completely swathed in the same filthy rags that cover its body. If it is helpless, the rags can be unraveled, but each layer only gives way to dozens of layers of the tattered yellow cloth. Eventually, a face is revealed, but it appears to be the face of the unraveler. If she is lucky, her memories are immediately wiped clean. If she is less fortunate or less able to forget, she is driven insane.

---

# Hooded Harbinger
This creature resembles a mummified humanoid swathed in filthy, sallow rags. Its stooped posture and ragged coverings make its height hard to judge. Its arms appear abnormally long, or perhaps dislocated and hanging freely. A hood of the same jaundiced fabric obscures its face.
**Source** Pathfinder #112: The Whisper Out of Time pg. 88
**XP** 19,200
CE Medium aberration
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +21
**Aura** profane reek (DC 21), _[[universal monster rules/Unnatural Aura|unnatural aura]]_ (30 ft.)

##### Defense

**AC** 27, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+4 Dex, +10 natural, +3 profane)
**hp** 161 (17d8+85)
**Fort** +12, **Ref** +11, **Will** +13
**DR** 10/lawful and slashing; **Immune** death effects, mind-affecting effects, poison; **Resist** cold 10; **SR** 23

##### Offense
**Speed** 30 ft.
**Melee** 2 slams +20 (2d6+8/19–20 plus _[[universal monster rules/Trip|trip]]_) or melee touch +20 (bloodless touch)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 3/day (DC 21, _[[spells/Command Undead|command undead]]_ only), manifest _[[spells/Yellow Sign|Yellow Sign]]_, prophetic utterance
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th, concentration +18)
Constant—_see invisibility_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_
3/day—_[[spells/Confusion|confusion]]_ (DC 17), mass _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Plane Shift|plane shift]]_, _[[spells/Silence|silence]]_ (DC 15), teleport (self plus 50 lbs. of objects only)
1/day—_[[spells/Freedom of Movement|freedom of movement]]_

##### Statistics
**Str** 26, **Dex** 18, **Con** 21, **Int** 16, **Wis** 13, **Cha** 17
**Base Atk** +12; **CMB** +20; **CMD** 34
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Command Undead_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +24, _[[universal monster rules/Climb|Climb]]_ +28, Escape Artist +24, Intimidate +31, Knowledge (religion) +27, Perception +21, Stealth +24; **Racial Modifiers** +4 Knowledge (religion), +8 Intimidate
**Languages** Aklo, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., _tongues_
**SQ** terrible visage

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

### Special Abilities

**Bloodless Touch (Ex)** When a _[[monsters/Hooded Harbinger|hooded harbinger]]_ makes a melee touch attack, its target must attempt a DC 23 Fortitude save. If the save is successful, the victim takes 2d6+8 points of damage and is wracked by pain for 1 round, gaining the _[[conditions/Staggered|staggered]]_ condition. It is thereafter immune to that _hooded harbinger_’s bloodless touch for 1 day. On a failed save, the portion of the victim’s body that is touched begins to swell and turn purplishblack as the blood flow to it is restricted. This effect deals 4d6+12 points of damage per round and the victim gains the _staggered_ and _[[conditions/Sickened|sickened]]_ conditions from the _[[feats/Intense Pain|intense pain]]_. After 1d4 rounds, the victim can attempt a new saving throw each round to try and end the effect. The effect can be ended sooner by a _[[spells/Heal|heal]]_ spell or a successful DC 23 _Heal_ check. The _Heal_ check requires a precise incision to the affected flesh, and consequently deals 2d6 points of _[[universal monster rules/Bleed|bleed]]_ damage to the victim as the pressure of the entrapped blood flow is released. Once a victim has been affected by a bloodless touch, it can’t be affected by another until the effects of the first one have ended. If the effects are ended by a successful save, then that individual is immune to further bloodless touch attacks by that _hooded harbinger_ for 1 day. The bloodless touch attack of a _hooded harbinger_ affects only living creatures with recognizable physiology and a blood supply. Undead, oozes, most constructs, and creatures that are not subject to precision damage are immune to bloodless touch. The save DC is Constitution-based.

**Manifest _Yellow Sign_ (Sp)** Once per day, a _hooded harbinger_ can trace a mystical pattern in the air, causing a glowing, immaterial image of the _Yellow Sign_ to appear before it. This image remains in place for 1d4 minutes. Any creatures within 100 feet who is able to see the sign (it glows as per light) must succeed at a DC 23 Will save or be _[[conditions/Confused|confused]]_ for as long as the sign persists. The sign can be erased with _[[spells/Dispel Chaos|dispel chaos]]_, _[[spells/Dispel Evil|dispel evil]]_, _[[spells/Dispel Magic|dispel magic]]_, or _[[spells/Erase|erase]]_ with a successful DC 26 caster level check. Anyone under the effects of the _Yellow Sign_ will not act against the _hooded harbinger_ in any way, though that does not mean that they will follow its commands. The save DC is Charisma-based and includes a +2 racial bonus. This is a mind-affecting compulsion effect.

**Profane Reek (Su)** The musty, carrion _[[universal monster rules/Stench|stench]]_ wafting from the foul folds of a _hooded harbinger_’s rags extends in a 5-foot radius, creating an aura of obscene influence around the creature. This terrible smell gives a _hooded harbinger_ a profane bonus to its AC equal to its Charisma modifier. In addition, any breathing creature that enters this cloud must succeed at a DC 21 Fortitude save or be affected as though under the mental effects of a _[[spells/Mind Fog|mind fog]]_ spell for as long as it remains within the profane reek’s area of effect and for 2d4 rounds after it leaves. A creature that succeeds at its save is immune to the _mind fog_ effect of that _hooded harbinger_’s profane reek for 1 day. The save DC is Charisma-based.

**Prophetic Utterance (Su)** Three times per day as an immediate action, a _hooded harbinger_ can mutter a prophetic utterance against any single creature within 100 feet that has just dealt damage to it. This mutter is unintelligible to anyone but the target, which hears the utterance as a telepathic _[[spells/Message|message]]_ pronouncing its _[[spells/Doom|doom]]_. The target is immediately affected by a _doom_ spell (no save) for the next hour or until the utterance is successfully dispelled (requiring a successful DC 26 caster level check).

**Terrible Visage (Su)** A _hooded harbinger_ never reveals its face. Only if slain or rendered _[[conditions/Helpless|helpless]]_ can anyone attempt to remove the hood and reveal the harbinger’s true visage. However, as layers of the stinking, rotten wrappings around its face are peeled back or cut away, new layers are found beneath. These many filth-crusted layers can be removed only with 1d4+2 rounds of effort. If they are successfully removed, only those adjacent to the creature can see the revealed countenance and anyone able to do so must succeed at a DC 21 Will save or be affected by an _[[spells/Insanity|insanity]]_ spell. Those who succeed at their saves are unaffected, as their minds mercifully _erase_ the image from their memories. Those cured of the _insanity_ receive the same relief. Immediately after the _hooded harbinger_’s face is revealed, its body explodes in a massive flash of light and concussive force that completely obliterates all evidence of it. Anyone within 10 feet of the corpse when it explodes takes 6d10 points of force damage (Reflex DC 23 half) and must attempt two DC 23 Fortitude saves, one against blindness and one against deafness (both as per blindness/deafness). The save DC to resist the _insanity_ effect is Charisma-based, and the save DCs to resist the explosion’s effects are Constitution-based.

##### Description

It is said that the Crawling Chaos is the messenger of the Great Old Ones, but whether this is by their _[[spells/Command|command]]_ or his own whim is debatable. Regardless of why, the Great Old One known as Hastur sometimes instead relies on his hooded harbingers to relay messages to his far-flung cults and even to the High Priest Not To Be Described of mystery-shrouded Leng. These dread figures swathed in filthy yellow rags bear the whispered tidings of their Unnamed Lord. There are those who even speculate that the veiled priest of Leng is actually the greatest of the hooded harbingers, who gained some measure of autonomy—but the truth of this remains _[[monsters/Unknown|unknown]]_. Thought to have originated in distant Carcosa by unthinkable means, hooded harbingers are exceedingly rare, and seldom is more than one encountered at a time.

Though tasked with the menial role of messengers, hooded harbingers take their charge very seriously. Infused with the hateful potency of their master, they are able to call upon many terrible powers in defense of their duties. When forced into combat, they prefer to _trip_ opponents with the trailing ends of their ragged arm coverings and administer their bloodless touch to as many victims as possible. They always attempt to use _plane shift_ to flee if in danger of imminent defeat.

Serving as messengers for Hastur, hooded harbingers receive the communications they deliver directly from the Great Old One via mental transmission. Upon receiving the _message_, the _hooded harbinger_ twitches and _[[diseases/Shakes|shakes]]_ as if it were having a seizure. During this time they are particularly dangerous, because if they are attacked or distracted in any way, they fly into a _[[items/Weapon Magic Abilities/Furious|furious]]_ _[[spells/Rage|rage]]_ and the offender risks attracting the attention of the _[[npcs/King|King]]_ in Yellow.

No one has seen a _hooded harbinger_’s face and lived to describe it. If its hood is pulled back, the creature’s head is seen to be completely swathed in the same filthy rags that cover its body. If it is _helpless_, the rags can be unraveled, but each layer only gives way to dozens of layers of the tattered yellow cloth. Eventually, a face is revealed, but it appears to be the face of the unraveler. If she is _[[feats/Lucky|lucky]]_, her memories are immediately wiped clean. If she is less fortunate or less able to forget, she is driven insane.