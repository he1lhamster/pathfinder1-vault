---
cssclass: [monsters]
title1: Euryale
desc_short: This creature has the upper body of a woman, the lower body of asnake,
  and a mass of undulating cobras for hair.
title2: Euryale
CR: 20
sources:
- name: Bestiary 6
  page: 120
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 307200
alignment: CE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 15
senses:
  blindsight: 60
  darkvision: 120
  true seeing: true
AC:
  AC: 37
  touch: 32
  flat_footed: 25
  components:
    dex: 11
    dodge: 1
    natural,+10 profane: 5
HP:
  HP: 367
  long: 21d10+252
saves:
  fort: 19
  ref: 23
  will: 20
  other: +4 vs. death effects, +8 vs. mindaffectingeffects
defensive_abilities:
- absorb essence
- all-around vision,death ward
- mind blank
- profane visions
DR:
- amount: 15
  weakness: goodand slashing
immunities:
- blindness
- daze
- petrification,poison
- sonic
speeds:
  base: 60
  other_semicolon: earth glide
  burrow: 30
attacks:
  melee:
  - - text: viper rod +35/+30/+25/+20 (1d8+14 plus poison)
      entries:
      - - damage: 1d8+14
        - effect: poison
      attack: viper rod
      bonus:
      - 35
      - 30
      - 25
      - 20
    - text: 6 snake bites +28 (1d6+4 plus poison)
      entries:
      - - damage: 1d6+4
        - effect: poison
      count: 6
      attack: snake bites
      bonus:
      - 28
  ranged:
  - - text: viper fangs +37/+32/+27/+22 (1d8+5/×3 plus poison)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
        - effect: poison
      attack: viper fangs
      bonus:
      - 37
      - 32
      - 27
      - 22
  special:
  - gaze
  - irresistible poison
  - poison
  - shatteringshriek
  - snake independence
  - statue control
  - viper rod
space: 5
reach: 5
reach_other: 10 ft. with snake bites
spell_like_abilities:
  entries:
  - name: death ward
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: true seeing At will-divination
    source: default
    freq: Constant
  - name: flesh to stone
    source: default
    freq: Constant
    DC: 26
  - name: greater shout
    source: default
    freq: Constant
    DC: 28
  - name: stone shape
    source: default
    freq: Constant
  - name: delayed blast fireball
    source: default
    freq: 3/day
    other: sonic damage
    DC: 27
  - name: quickened flesh to stone
    source: default
    freq: 3/day
    DC: 26
  - name: sonic thrust
    source: default
    freq: 3/day
    DC: 25
  - name: commune
    source: default
    freq: 1/day
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 20
    concentration: 30
spells:
  entries:
  - name: clashing rocks
    source: Oracle
    level: 9
    DC: 29
  - name: greater spell immunity
    source: Oracle
    level: 8
  - name: unholy aura
    source: Oracle
    level: 8
    DC: 28
  - name: ethereal jaunt
    source: Oracle
    level: 7
  - name: greater scrying
    source: Oracle
    level: 7
    DC: 27
  - name: statue
    source: Oracle
    level: 7
  - name: greater dispel magic
    source: Oracle
    level: 6
  - name: heal
    source: Oracle
    level: 6
  - name: stone tell
    source: Oracle
    level: 6
  - name: life bubble
    source: Oracle
    level: 5
  - name: plane shift
    source: Oracle
    level: 5
    DC: 25
  - name: righteous might
    source: Oracle
    level: 5
  - name: slay living
    source: Oracle
    level: 5
    DC: 25
  - name: air walk
    source: Oracle
    level: 4
  - name: cure serious wounds
    source: Oracle
    level: 4
  - name: divine power
    source: Oracle
    level: 4
  - name: freedom of movement
    source: Oracle
    level: 4
  - name: dispel magic
    source: Oracle
    level: 3
  - name: invisibility purge
    source: Oracle
    level: 3
  - name: magic vestment
    source: Oracle
    level: 3
  - name: meld into stone
    source: Oracle
    level: 3
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: eagle's splendor
    source: Oracle
    level: 2
  - name: resist energy
    source: Oracle
    level: 2
  - name: sound burst
    source: Oracle
    level: 2
    DC: 22
  - name: stone call
    source: Oracle
    level: 2
  - name: command
    source: Oracle
    level: 1
    DC: 21
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: endure elements
    source: Oracle
    level: 1
  - name: sanctuary
    source: Oracle
    level: 1
    DC: 21
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 20
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: purify food and drink
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  - name: virtue
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 18
    concentration: 28
    slots:
      9: 4
      8: 6
      7: 7
      6: 8
      5: 8
      4: 8
      3: 8
      2: 9
      1: 9
      0: at-will
ability_scores:
  STR: 28
  DEX: 32
  CON: 35
  INT: 29
  WIS: 26
  CHA: 31
BAB: 21
CMB: 30
CMD: 62
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Extend Spell
- name: Improved Initiative
- name: Multiattack
- name: PowerAttack
- name: Quicken Spell
- name: Quicken Spell-Like Ability (flesh tostone)
- name: Skill Focus (Perception)
skills:
  Bluff: 31
  Diplomacy: 31
  Disguise: 31
  Intimidate: 34
  Knowledge (arcana): 30
  Knowledge (history): 30
  Knowledge (religion): 30
  Perception: 38
  Perform (sing): 31
  Sense Motive: 29
  Spellcraft: 30
  Stealth: 35
  Use Magic Device: 31
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal,Terran
- Undercommon
special_qualities:
- change shape (Medium humanoid; alter self)
ecology:
  environment: any
  organization: solitary, pair, triumvirate (3), or cult (1 plus4-17 medusas)
  treasure_type: standard
special_abilities:
  Absorb Essence (Ex): Whenever a creature that has been petrified is destroyed within
    60 feet of a euryale, the euryale gains the effects of a cure serious wounds spell
    and a restoration spell (both at CL 20th).
  Gaze (Su): The euryale's gaze attack has a range of 30 feet and turns the target
    to stone permanently (Fortitude DC 32 negates). The save DC is Constitution-based.
  Irresistible Poison (Ex): A creature must roll twice and take the lower result on
    all saving throws against a euryale's poison effects. If the creature would normally
    be immune to poison, the immunity doesn't apply, but it only needs to roll its
    save once. Delay poison doesn't delay her poison effects; they still occur immediately.
    A euryale gains a +4 bonus on saving throws against neutralize poison cast against
    her to negate her venomous attacks.
  Poison (Ex): Snake bite, viper fangs, or viper rod-injury; save Fort DC 32; frequency
    1/round for 6 rounds; effect 1d4 Dex damage, 1d4 Con damage, and vulnerable to
    sonic for 1 minute; cure 3 consecutive saves. The save DC is Constitution-based.
  Profane Visions (Ex): A euryale's prophetic visions allow her to avoid misfortune.
    She gains a profane bonus to Armor Class equal to her Charisma bonus, and whenever
    she would be forced to reroll a d20 or to roll a d20 twice and take the lower
    result, she takes the higher result of the two rolls instead.
  Shattering Shriek (Su): Whenever a euryale uses one of her sonic spell-like abilities,
    any sonic damage dealt by the spell increases by 1 point per die. In addition,
    sonic damage from her spell-like abilities bypasses the hardness of a petrified
    creature, and the damage is not halved when applied to petrified creatures. (A
    typical Medium petrified creature has 30 hit points.) A petrified creature that
    is destroyed by the effects of a euryale's shattering shriek explodes into a 20-foot
    burst of jagged stone shards, dealing 4d6 points of slashing damage to any creatures
    in that area (Reflex DC 30 half); this explosion heals the euryale as detailed
    in absorb essence above. The save DC is Charisma-based.
  Snake Independence (Ex): A euryale's snakes are independently intelligent and can
    attack even when she doesn't. No matter what action the euryale takes, she can
    still always make all six snake bite attacks on her turn. Even when she doesn't
    attack with any other weapons that round, her snake bites always count as secondary
    attacks.
  Spells: A euryale casts spells as an 18th-level oracle.
  Statue Control (Su): A euryale can control the statues of any creatures she petrifies
    via her spells or special abilities as long as they remain within 120 feet of
    her. Petrified creatures are treated as animated stone objects (Pathfinder RPG
    Bestiary 14). While the typical Medium animated object is almost insignificant
    in a CR 20 encounter, the euryale often commands these statues to move so as to
    provide her cover or to place them in areas where she can shatter them to deal
    the most damage to foes (see the shattering shriek ability on page 120). The euryale's
    control over these statues is a purely mental act that takes no action. A euryale
    can control a number of statues at once equal to her Charisma modifier (10 for
    the typical euryale).
  Viper Rod (Su): Any blunt weapon or object a euryale holds becomes a rod of the
    viper with a +5 enhancement bonus that uses her poison instead of its usual poison.
    She can flick the snake head of her viper rod to fire poisoned fangs as a ranged
    attack. Treat these attacks as if she fired arrows from a +5 longbow; fangs launched
    in this manner deliver her poison
desc_long: |-
  Euryales are powerful medusa matriarchs and among the most favored agents of Lamashtu, the Mother of Monsters. Long ago, Lamashtu tricked these medusa forebears with a gift that tainted and empowered them into becoming beings of madness and evil, twisting them into forms even more monstrous than their medusa sisters. Euryales delight in destroying their foes in ways they find particularly cruel, such as transforming one of a pair of lovers into a statue and then commanding the statue to destroy the still-living lover. Because of the oracular powers of these creatures, there are tales of desperate folk who seek out euryales for answers, but these tales invariably end poorly-those few petitioners who receive the answers they seek find they would have been better off never knowing. In most cases, an encounter with a euryale is destined for disaster. However, they are endlessly fascinated by poisons, so a creature that can satisfy a euryale's curiosity by teaching it new poison lore (a daunting task in its own right) can likely avoid destruction in a chance meeting. Euryales find themselves distant from medusa society, unless they hold together a cult of fawning medusas by force. While they occasionally form triumvirates among themselves, they are more likely to find companionship among like-minded zealots of other races, particularly lamia matriarchs (Pathfinder RPG Bestiary 2 175) or mariliths. 

  Most euryales willingly embrace the taint of madness and lovingly serve the Mother of Monsters, but there are some who seek to eschew it, whether simply to be free of Lamashtu's influence and live an evil life more like that of a normal medusa, or to follow a path of redemption. These rare heretical euryales have alignments other than chaotic evil as well as additional powers gained through their struggle to control their own destinies. Typically they advance by Hit Dice, although it's also fairly common for them to take up to 2 oracle levels to improve their oracle spellcasting and to represent the curse the Mother of Monsters inflicted upon them for daring to cross her. 

  A euryale is 7 feet tall and weighs 460 pounds.

---

# Euryale
This creature has the upper body of a woman, the lower body of a

snake, and a mass of undulating cobras for hair.
**Source** Bestiary 6 pg. 120
**XP** 307,200
CE Medium monstrous humanoid
**Init** +15; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/True Seeing|true seeing]]_;

Perception +38

##### Defense

**AC** 37, touch 32, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+11 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural,

+10 profane)
**hp** 367 (21d10+252)
**Fort** +19, **Ref** +23, **Will** +20; +4 vs. death effects, +8 vs. mindaffecting

effects
**Defensive Abilities** absorb essence, _[[universal monster rules/All-Around Vision|all-around vision]]_,

_[[spells/Death Ward|death ward]]_, _[[spells/Mind Blank|mind blank]]_, profane visions; **DR** 15/good

and slashing; **Immune** blindness, _[[spells/Daze|daze]]_, petrification,

poison, sonic

##### Offense
**Speed** 60 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft.; _[[universal monster rules/Earth Glide|earth glide]]_
**Melee** viper rod +35/+30/+25/+20 (1d8+14 plus poison),

6 snake bites +28 (1d6+4 plus poison)
**Ranged** viper fangs +37/+32/+27/+22 (1d8+5/×3 plus poison)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with snake bites)
**Special Attacks** _[[universal monster rules/Gaze|gaze]]_, irresistible poison, poison, _[[items/Weapon Magic Abilities/Shattering|shattering]]_

shriek, snake independence, _[[spells/Statue|statue]]_ control, viper rod
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +30)
Constant—_death ward_, _mind blank_, _true seeing_ At will—_[[spells/Divination|divination]]_, _[[spells/Flesh to Stone|flesh to stone]]_ (DC 26), greater _[[spells/Shout|shout]]_ (DC 28), _[[spells/Stone Shape|stone shape]]_ 
3/day—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (sonic damage) (DC 27), quickened _flesh to stone_ (DC 26), _[[spells/Sonic Thrust|sonic thrust]]_ (DC 25) 
1/day—_[[spells/Commune|commune]]_, _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 29)
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 18th; concentration +28)
9th (4)—_[[spells/Clashing Rocks|clashing rocks]]_ (DC 29) 
8th (6)—greater _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Unholy Aura|unholy aura]]_ (DC 28) 
7th (7)—_[[spells/Ethereal Jaunt|ethereal jaunt]]_, greater _[[spells/Scrying|scrying]]_ (DC 27), _statue_ 
6th (8)—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heal|heal]]_, _[[spells/Stone Tell|stone tell]]_ 
5th (8)—_[[spells/Life Bubble|life bubble]]_, _[[spells/Plane Shift|plane shift]]_ (DC 25), _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 25) 
4th (8)—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_ 
3rd (8)—_dispel magic_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Meld into Stone|meld into stone]]_ 
2nd (9)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Resist Energy|resist energy]]_, _[[spells/Sound Burst|sound burst]]_ (DC 22), _[[spells/Stone Call|stone call]]_ 
1st (9)—_[[spells/Command|command]]_ (DC 21), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 21), _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 20), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 28, **Dex** 32, **Con** 35, **Int** 29, **Wis** 26, **Cha** 31
**Base Atk** +21; **CMB** +30; **CMD** 62 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, Power

Attack, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (flesh to

stone), _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +31, Diplomacy +31, Disguise +31, Intimidate +34,

Knowledge (arcana, history, religion) +30, Perception +38,

Perform (sing) +31, Sense Motive +29, Spellcraft +30,

Stealth +35, Use Magic Device +31
**Languages** Abyssal, Celestial, Common, Draconic, Infernal,

Terran, Undercommon
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_Medium_ humanoid; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any
**Organization** solitary, pair, triumvirate (3), or cult (1 plus

4–17 medusas)
**Treasure** standard

### Special Abilities

**Absorb Essence (Ex)** Whenever a creature that has been _[[conditions/Petrified|petrified]]_ is destroyed within 60 feet of a _[[monsters/Euryale|euryale]]_, the _euryale_ gains the effects of a _cure serious wounds_ spell and a _[[spells/Restoration|restoration]]_ spell (both at CL 20th).

**_Gaze_ (Su)** The _euryale_’s _gaze_ attack has a range of 30 feet and turns the target to stone permanently (Fortitude DC 32 negates). The save DC is Constitution-based.

**Irresistible Poison (Ex)** A creature must roll twice and take the lower result on all saving throws against a _euryale_’s poison effects. If the creature would normally be immune to poison, the _[[universal monster rules/Immunity|immunity]]_ doesn’t apply, but it only needs to roll its save once. _[[spells/Delay Poison|Delay poison]]_ doesn’t delay her poison effects; they still occur immediately. A _euryale_ gains a +4 bonus on saving throws against _[[spells/Neutralize Poison|neutralize poison]]_ cast against her to negate her venomous attacks.

**Poison (Ex)** Snake bite, viper fangs, or viper rod—injury; save Fort DC 32; frequency 1/round for 6 rounds; effect 1d4 Dex damage, 1d4 Con damage, and vulnerable to sonic for 1 minute; cure 3 consecutive saves. The save DC is Constitution-based.

**Profane Visions (Ex)** A _euryale_’s prophetic visions allow her to avoid misfortune. She gains a profane bonus to Armor Class equal to her Charisma bonus, and whenever she would be forced to reroll a d20 or to roll a d20 twice and take the lower result, she takes the higher result of the two rolls instead.
**_Shattering_ Shriek (Su)** Whenever a _euryale_ uses one of her sonic _spell-like abilities_, any sonic damage dealt by the spell increases by 1 point per die. In addition, sonic damage from her _spell-like abilities_ bypasses the hardness of a _petrified_ creature, and the damage is not halved when applied to _petrified_ creatures. (A typical _Medium_ _petrified_ creature has 30 hit points.) A _petrified_ creature that is destroyed by the effects of a _euryale_’s _shattering_ shriek explodes into a 20-foot burst of jagged stone shards, dealing 4d6 points of slashing damage to any creatures in that area (Reflex DC 30 half); this explosion heals the _euryale_ as detailed in absorb essence above. The save DC is Charisma-based.
**Snake Independence (Ex)** A _euryale_’s snakes are independently intelligent and can attack even when she doesn’t. No matter what action the _euryale_ takes, she can still always make all six snake bite attacks on her turn. Even when she doesn’t attack with any other weapons that round, her snake bites always count as secondary attacks.
**Spells** A _euryale_ casts spells as an 18th-level _oracle_.
**_Statue_ Control (Su)** A _euryale_ can control the statues of any creatures she petrifies via her spells or special abilities as long as they remain within 120 feet of her. _Petrified_ creatures are treated as _[[items/Armor Magic Abilities/Animated|animated]]_ stone objects (Pathfinder RPG Bestiary 14). While the typical _Medium_ _[[monsters/Animated Object|animated object]]_ is almost insignificant in a CR 20 encounter, the _euryale_ often commands these statues to move so as to provide her cover or to place them in areas where she can _[[spells/Shatter|shatter]]_ them to deal the most damage to foes (see the _shattering_ shriek ability on page 120). The _euryale_’s control over these statues is a purely mental act that takes no action. A _euryale_ can control a number of statues at once equal to her Charisma modifier (10 for the typical _euryale_).

**Viper Rod (Su)** Any blunt weapon or object a _euryale_ holds becomes a _[[items/Rod/Rod of the Viper|rod of the viper]]_ with a +5 enhancement bonus that uses her poison instead of its usual poison. She can flick the snake head of her viper rod to fire poisoned fangs as a ranged attack. Treat these attacks as if she fired arrows from a +5 _[[items/Weapon/Longbow|longbow]]_; fangs launched in this manner deliver her poison

##### Description

Euryales are powerful _[[monsters/Medusa|medusa]]_ matriarchs and among the most favored agents of Lamashtu, the Mother of Monsters. Long ago, Lamashtu tricked these _medusa_ forebears with a gift that tainted and empowered them into becoming beings of madness and evil, twisting them into forms even more monstrous than their _medusa_ sisters. Euryales delight in destroying their foes in ways they find particularly _[[items/Weapon Magic Abilities/Cruel|cruel]]_, such as transforming one of a pair of lovers into a _statue_ and then commanding the _statue_ to destroy the still-living lover. Because of the oracular powers of these creatures, there are tales of desperate folk who seek out euryales for answers, but these tales invariably end poorly—those few petitioners who receive the answers they seek find they would have been better off never knowing. In most cases, an encounter with a _euryale_ is destined for disaster. However, they are endlessly _[[conditions/Fascinated|fascinated]]_ by poisons, so a creature that can satisfy a _euryale_’s curiosity by teaching it new poison lore (a daunting task in its own right) can likely avoid _[[spells/Destruction|destruction]]_ in a chance meeting. Euryales find themselves distant from _medusa_ society, unless they hold together a cult of fawning medusas by force. While they occasionally form triumvirates among themselves, they are more likely to find companionship among like-minded zealots of other races, particularly _[[monsters/Lamia|lamia]]_ matriarchs (Pathfinder RPG Bestiary 2 175) or mariliths.

Most euryales willingly embrace the taint of madness and lovingly serve the Mother of Monsters, but there are some who seek to eschew it, whether simply to be free of Lamashtu’s influence and live an evil life more like that of a normal _medusa_, or to follow a path of _[[feats/Redemption|redemption]]_. These rare _[[items/Weapon Magic Abilities/Heretical|heretical]]_ euryales have alignments other than chaotic evil as well as additional powers gained through their struggle to control their own destinies. Typically they advance by Hit Dice, although it’s also fairly common for them to take up to 2 _oracle_ levels to improve their _oracle_ spellcasting and to represent the curse the Mother of Monsters inflicted upon them for daring to cross her.

A _euryale_ is 7 feet tall and weighs 460 pounds.