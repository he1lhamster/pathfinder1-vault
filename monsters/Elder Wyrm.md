---
cssclass: [monsters]
title1: Elder Wyrm
desc_short: This mighty, two-headed dragon has a six-legged serpentine body that ends
  in a writhing, whiplike tail.
title2: Elder Wyrm
CR: 24
sources:
- name: Bestiary 6
  page: 108
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 1228800
alignment: N
size: Colossal
type: dragon
initiative:
  bonus: 16
senses:
  darkvision: 300
  low-light vision: true
  scent: true
  true seeing: true
auras:
- name: frightful presence
  radius: 300
  DC: 33
AC:
  AC: 42
  touch: 14
  flat_footed: 30
  components:
    dex: 12
    natural: 28
    size: -8
HP:
  HP: 528
  long: 32d12+320
  fast_healing: 20
saves:
  fort: 28
  ref: 30
  will: 24
DR:
- amount: 20
  weakness: epic
immunities:
- acid
- charm
- curses
- electricity
- fear
- paralysis
- petrification
- sleep
resistances:
  cold: 30
  fire: 30
  sonic: 30
SR: 35
speeds:
  base: 50
  climb: 50
  fly: 250
  fly_maneuverability: poor
  swim: 50
attacks:
  melee:
  - - text: 2 bites +40 (4d8+16/19-20 plus myth-drinker)
      entries:
      - - damage: 4d8+16
          crit_range: 19-20
        - effect: myth-drinker
      count: 2
      attack: bites
      bonus:
      - 40
    - text: 2 claws +40 (2d8+16)
      entries:
      - - damage: 2d8+16
      count: 2
      attack: claws
      bonus:
      - 40
    - text: 2 tail slaps +35 (4d6+8/19-20)
      entries:
      - - damage: 4d6+8
          crit_range: 19-20
      count: 2
      attack: tail slaps
      bonus:
      - 35
  special:
  - breath weapon
  - godslayer
  - rend (2 bites, 4d8+16 plus myth-drinker)
  - swift tail
  - synchronized strike
  - tail snap
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: miracle
    source: default
    freq: 1/month
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - name: dominate monster
    source: Sorcerer
    level: 9
    DC: 26
  - name: foresight
    source: Sorcerer
    level: 9
  - name: time stop
    source: Sorcerer
    level: 9
  - name: greater prying eyes
    source: Sorcerer
    level: 8
  - name: maze
    source: Sorcerer
    level: 8
  - name: sunburst
    source: Sorcerer
    level: 8
    DC: 25
  - name: greater arcane sight
    source: Sorcerer
    level: 7
  - name: greater scrying
    source: Sorcerer
    level: 7
    DC: 24
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 23
  - name: mass suggestion
    source: Sorcerer
    level: 6
    DC: 23
  - name: shadow walk
    source: Sorcerer
    level: 6
    DC: 23
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 22
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 22
  - name: hold monster
    source: Sorcerer
    level: 5
    DC: 22
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: arcane eye
    source: Sorcerer
    level: 4
  - name: bestow curse
    source: Sorcerer
    level: 4
    DC: 21
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: stone shape
    source: Sorcerer
    level: 4
  - name: clairaudience/clairvoyance
    source: Sorcerer
    level: 3
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 20
  - name: blur
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 19
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: whispering wind
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: comprehend languages
    source: Sorcerer
    level: 1
  - name: expeditious retreat
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 17
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 17
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 20
    concentration: 27
    slots:
      9: 6
      8: 6
      7: 7
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 43
  DEX: 34
  CON: 30
  INT: 17
  WIS: 22
  CHA: 25
BAB: 32
CMB: 56
CMD: 78
CMD_other: 86 vs. trip
feats:
- name: Alertness
- name: Arcane Strike
- name: Combat Reflexes
- name: Empower Spell
- name: Flyby Attack
- name: Greater Spell Penetration
- name: Greater Vital Strike
- name: Hover
- name: Improved Critical (bite)
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lunge
- name: Power Attack
- name: Quicken Spell
- name: Vital Strike
skills:
  Acrobatics: 44
  Bluff: 42
  Climb: 24
  Diplomacy: 42
  Fly: 0
  Intimidate: 42
  Knowledge (arcana): 38
  Perception: 49
  Sense Motive: 45
  Spellcraft: 38
  Swim: 24
  Use Magic Device: 42
  _racial_mods:
    Perception:
      _: 4
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Infernal
- Undercommon
special_qualities:
- impossible coordination
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
special_abilities:
  Breath Weapon (Su): Each of an elder wyrm's heads can expel a breath weapon, each
    of which can be used once every 1d4 rounds. The first breath weapon is a 500-foot
    line of lighting that deals 20d10 points of electricity damage (Reflex DC 36 half).
    The second is a 250-foot cone of caustic gas that deals 20d10 points of acid damage
    (Fortitude DC 36 half). If an elder wyrm uses both breath weapons simultaneously-such
    as by readying an action with its impossible coordination ability-the electrical
    charge causes the gas to explode; rather than dealing acid or electricity damage,
    the explosion instead deals 40d10 points of fire damage to all creatures in a
    250-foot cone (Reflex DC 36 half) and causes damaged creatures to catch fire,
    taking 6d10 points of fire damage each round for 1d4 rounds, unless they succeed
    at a second DC 36 Reflex save. The save DCs are Constitution-based.
  Godslayer (Ex): An elder wyrm's natural attacks overcome damage reduction and regeneration
    as per epic and magic weapons. As a swift action, the elder wyrm can grant its
    natural weapons one alignment property and one material property for this purpose.
    These secondary properties last for 1 hour or until the elder wyrm uses this ability
    again to select new properties.
  Impossible Coordination (Ex): An elder wyrm can plan and execute a vast number of
    schemes in a short time. When an encounter starts, an elder wyrm rolls twice for
    initiative. Once per minute, it can act on both initiative counts and can use
    the delay or ready actions independently at each initiative. On other rounds,
    it uses the higher initiative count.
  Myth-Drinker (Su): An elder wyrm's bite and rend attacks deal an additional 2d6
    points of damage to creatures with mythic tiers or the mythic subtype. When an
    elder wyrm confirms a critical hit with its bite attack against such a target,
    the target loses 1d4 uses of mythic power. For each use of mythic power lost,
    the elder wyrm either regains 2d10 hit points or can attempt a saving throw against
    one ongoing effect; on a successful save, the effect ends immediately. At the
    GM's discretion, this ability could apply to mighty albeit non-mythic divine creations,
    such as behemoths, demodands, titans, and outsiders whose CR is 20 or higher;
    in this case the elder wyrm benefits as though the target had lost two uses of
    mythic power.
  Spells: An elder wyrm casts spells as per a 20th-level sorcerer.
  Swift Tail (Ex): An elder worm can strike twice in a round with its tail slap when
    it makes a full attack.
  Synchronized Strike (Ex): An elder wyrm's two heads work in perfect concert when
    making attacks, snaking apart to strike targets from opposite directions. Once
    per round, the elder wyrm can perform two bite attacks as an attack action, such
    as when performing a charge or making an attack or opportunity. When an elder
    wyrm uses both bite attacks against a creature that is at least one size category
    smaller than it is, the elder wyrm is treated as if both heads were flanking the
    target for the purposes of resolving the attacks.
  Tail Snap (Su): As a full-round action, an elder wyrm can make two tail slap attacks
    against a single creature it can reach. If one tail slap hits, the target must
    also succeed at a DC 36 Fortitude save or be stunned for 1 round. If both hit,
    the tail's impact causes a 10-foot-radius burst of concussive force centered on
    the target, dealing 10d10 points of sonic damage to all creatures in the area
    and stunning them for 1 round (Fortitude DC 36 negates the stunned effect). The
    elder wyrm is unharmed by this effect. The save DC is Constitution-based
desc_long: |-
  Over the eons, gods and would-be divinities have unleashed countless monstrosities on the multiverse in vain attempts to create worshipers or punish oath breakers, or just out of spite. Many such beasts outlive their usefulness and run amok, defying their creators' commands to stand down. 

  Elder wyrms were once divine avengers, granted life in order to seek and destroy rogue agents of the gods and other such abominations. After annihilating several condemned species, the dragons broke free from the gods' control. Despite this, elder wyrms have a flexible but insistent sense of justice instilled in them by their divine mandate, and acting as the judge, jury, and executioner of mighty foes scratches an existential itch. The few elder wyrms that live on a given planet spend much of their time dozing in secluded places, waking occasionally to hunt or seek out injustices to punish based on their individual interests and moods. This cycle of inactivity leaves most elder wyrms woefully ill-informed of current events, though once they have cause to pay attention, their keen intellects and powerful divinations allow them to gather and process several centuries of news in short order. 

  Because they wake so rarely, elder wyrms often become centerpieces of local legends and cautionary tales. Especially convincing or foolhardy heroes might even seek out an elder wyrm in order to direct its vengeful wrath against a specific target, though the wyrm is just as likely to determine that the heroes are more worthy of destruction than their targets. Having two heads does, after all, make elder wyrms better equipped to see both sides of an issue and render judgment. Each head can think independently and seamlessly share control of the body, allowing the dragon to perform dizzying acts of synchronicity. Often the two heads' personalities diverge, leading to good-natured bickering and debate between the two, much to the dread of anxious onlookers. 

  An elder wyrm is 100 feet long and weighs 25,000 pounds.

---

# Elder Wyrm
This mighty, two-headed dragon has a six-legged serpentine body that ends in a writhing, whiplike tail.
**Source** Bestiary 6 pg. 108
**XP** 1,228,800

N Colossal dragon
**Init** +16; **Senses** _[[spells/Darkvision|darkvision]]_ 300 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +49
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 33)

##### Defense

**AC** 42, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+12 Dex, +28 natural, –8 size)
**hp** 528 (32d12+320); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +28, **Ref** +30, **Will** +24
**DR** 20/epic; **Immune** acid, charm, curses, electricity, _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Paralysis|paralysis]]_, petrification, sleep; **Resist** cold 30, fire 30, sonic 30; **SR** 35

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft., fly 250 ft. (poor), swim 50 ft.
**Melee** 2 bites +40 (4d8+16/19–20 plus myth-drinker), 2 claws +40 (2d8+16), 2 tail slaps +35 (4d6+8/19–20)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, godslayer, _[[universal monster rules/Rend|rend]]_ (2 bites, 4d8+16 plus myth-drinker), swift tail, synchronized strike, tail snap
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_true seeing_ 
1/month—_[[spells/Miracle|miracle]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known** (CL 20th; concentration +27)
9th (6)—_[[spells/Dominate Monster|dominate monster]]_ (DC 26), _[[spells/Foresight|foresight]]_, _[[spells/Time Stop|time stop]]_ 
8th (6)—greater _[[spells/Prying Eyes|prying eyes]]_, _[[spells/Maze|maze]]_, _[[spells/Sunburst|sunburst]]_ (DC 25) 
7th (7)—greater _[[spells/Arcane Sight, Greater|arcane sight, greater]]_ _[[spells/Scrying|scrying]]_ (DC 24), greater teleport 
6th (7)—_[[spells/Disintegrate|disintegrate]]_ (DC 23), mass _[[spells/Suggestion|suggestion]]_ (DC 23), _[[spells/Shadow Walk|shadow walk]]_ (DC 23) 
5th (7)—_[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 22), _[[spells/Hold Monster|hold monster]]_ (DC 22), _[[spells/Wall Of Force|wall of force]]_ 
4th (7)—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Bestow Curse|bestow curse]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[spells/Stone Shape|stone shape]]_ 
3rd (8)—clairaudience/clairvoyance, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 20) 
2nd (8)—_[[spells/Blur|blur]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Whispering Wind|whispering wind]]_ 
1st (8)—_[[spells/Alarm|alarm]]_, _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Shield|shield]]_, _[[spells/Unseen Servant|unseen servant]]_ 
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 17), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 43, **Dex** 34, **Con** 30, **Int** 17, **Wis** 22, **Cha** 25
**Base Atk** +32; **CMB** +56; **CMD** 78 (86 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +44, Bluff +42, _Climb_ +24, Diplomacy +42, Fly +0, Intimidate +42, Knowledge (arcana) +38, Perception +49, Sense Motive +45, Spellcraft +38, Swim +24, Use Magic Device +42; **Racial Modifiers** +4 Perception
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Infernal, Undercommon
**SQ** impossible coordination

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Breath Weapon_ (Su)** Each of an _[[monsters/Elder Wyrm|elder wyrm]]_’s heads can expel a _breath weapon_, each of which can be used once every 1d4 rounds. The first _breath weapon_ is a 500-foot line of lighting that deals 20d10 points of electricity damage (Reflex DC 36 half). The second is a 250-foot cone of caustic gas that deals 20d10 points of acid damage (Fortitude DC 36 half). If an _elder wyrm_ uses both breath weapons simultaneously—such as by readying an action with its impossible coordination ability—the electrical charge causes the gas to explode; rather than dealing acid or electricity damage, the explosion instead deals 40d10 points of fire damage to all creatures in a 250-foot cone (Reflex DC 36 half) and causes damaged creatures to catch fire, taking 6d10 points of fire damage each round for 1d4 rounds, unless they succeed at a second DC 36 Reflex save. The save DCs are Constitution-based.

**Godslayer (Ex)** An _elder wyrm_’s _[[universal monster rules/Natural Attacks|natural attacks]]_ overcome _[[universal monster rules/Damage Reduction|damage reduction]]_ and _[[universal monster rules/Regeneration|regeneration]]_ as per epic and magic weapons. As a swift action, the _elder wyrm_ can grant its natural weapons one alignment property and one material property for this purpose. These secondary properties last for 1 hour or until the _elder wyrm_ uses this ability again to select new properties.

**Impossible Coordination (Ex)** An _elder wyrm_ can plan and execute a vast number of schemes in a short time. When an encounter starts, an _elder wyrm_ rolls twice for initiative. Once per minute, it can act on both initiative counts and can use the delay or ready actions independently at each initiative. On other rounds, it uses the higher initiative count.

**Myth-Drinker (Su)** An _elder wyrm_’s bite and _rend_ attacks deal an additional 2d6 points of damage to creatures with mythic tiers or the mythic subtype. When an _elder wyrm_ confirms a critical hit with its bite attack against such a target, the target loses 1d4 uses of mythic power. For each use of mythic power lost, the _elder wyrm_ either regains 2d10 hit points or can attempt a saving throw against one ongoing effect; on a successful save, the effect ends immediately. At the GM’s discretion, this ability could apply to mighty albeit non-mythic divine creations, such as behemoths, demodands, titans, and outsiders whose CR is 20 or higher; in this case the _elder wyrm_ benefits as though the target had lost two uses of mythic power.
**Spells** An _elder wyrm_ casts spells as per a 20th-level _sorcerer_.
**Swift Tail (Ex)** An elder worm can strike twice in a round with its tail slap when it makes a full attack.
**Synchronized Strike (Ex)** An _elder wyrm_’s two heads work in perfect concert when making attacks, snaking apart to strike targets from opposite directions. Once per round, the _elder wyrm_ can perform two bite attacks as an attack action, such as when performing a charge or making an attack or opportunity. When an _elder wyrm_ uses both bite attacks against a creature that is at least one size category smaller than it is, the _elder wyrm_ is treated as if both heads were flanking the target for the purposes of resolving the attacks.

**Tail Snap (Su)** As a full-round action, an _elder wyrm_ can make two tail slap attacks against a single creature it can reach. If one tail slap hits, the target must also succeed at a DC 36 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1 round. If both hit, the tail’s _[[items/Weapon Magic Abilities/Impact|impact]]_ causes a 10-foot-radius burst of concussive force centered on the target, dealing 10d10 points of sonic damage to all creatures in the area and stunning them for 1 round (Fortitude DC 36 negates the _stunned_ effect). The _elder wyrm_ is unharmed by this effect. The save DC is Constitution-based

##### Description

Over the eons, gods and would-be divinities have unleashed countless monstrosities on the multiverse in vain attempts to create worshipers or punish oath breakers, or just out of _[[spells/Spite|spite]]_. Many such beasts outlive their usefulness and run amok, defying their creators’ commands to stand down.

Elder wyrms were once divine avengers, granted life in order to seek and destroy _[[classes/Rogue|rogue]]_ agents of the gods and other such abominations. After annihilating several condemned species, the dragons broke free from the gods’ control. Despite this, elder wyrms have a flexible but insistent sense of justice instilled in them by their divine mandate, and acting as the judge, jury, and executioner of mighty foes scratches an existential itch. The few elder wyrms that live on a given planet spend much of their time dozing in secluded places, waking occasionally to hunt or seek out injustices to punish based on their individual interests and moods. This cycle of inactivity leaves most elder wyrms woefully ill-informed of current events, though once they have cause to pay attention, their _[[items/Weapon Magic Abilities/Keen|keen]]_ intellects and powerful divinations allow them to gather and process several centuries of news in short order.

Because they wake so rarely, elder wyrms often become centerpieces of local legends and cautionary tales. Especially convincing or foolhardy heroes might even seek out an _elder wyrm_ in order to direct its vengeful wrath against a specific target, though the wyrm is just as likely to determine that the heroes are more worthy of _[[spells/Destruction|destruction]]_ than their targets. Having two heads does, after all, make elder wyrms better equipped to see both sides of an issue and render judgment. Each head can think independently and seamlessly share control of the body, allowing the dragon to perform dizzying acts of synchronicity. Often the two heads’ personalities diverge, leading to good-natured bickering and debate between the two, much to the dread of anxious onlookers.

An _elder wyrm_ is 100 feet long and weighs 25,000 pounds.