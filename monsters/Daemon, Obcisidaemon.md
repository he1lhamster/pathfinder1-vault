---
cssclass: [monsters]
title1: Daemon, Obcisidaemon
desc_short: This massive fiend has eagle wings, a tusked canine face, anda muscular
  frame. It wields an immense, cruel-looking halberd.
title2: Obcisidaemon
CR: 19
sources:
- name: Bestiary 6
  page: 72
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 3: Horsemen of the Apocalypse'
  page: 50
  link: http://paizo.com/products/btpy8odg?Pathfinder-Campaign-Setting-Book-of-the-Damned-Volume-3-Horsemen-of-the-Apocalypse
XP: 204800
alignment: NE
size: Gargantuan
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 60
  deathwatch: true
  true seeing: true
auras:
- name: scorched earth
  radius: 60
  DC: 28
- name: unholy aura
  DC: 25
AC:
  AC: 34
  touch: 14
  flat_footed: 30
  components:
    deflection: 4
    dex: 4
    natural,-4 size: 20
HP:
  HP: 319
  long: 22d10+198
saves:
  fort: 26
  ref: 15
  will: 22
DR:
- amount: 15
  weakness: good and silver
immunities:
- acid
- death effects
- disease,poison
resistances:
  cold: 30
  electricity: 30
  fire: 30
SR: 30
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 unholy halberd +28/+23/+18/+13 (4d8+13/19-20/×3plus inherit soul)
      entries:
      - - damage: 4d8+13
          type: /19-20/×3plus inherit soul
      attack: +1 unholy halberd
      bonus:
      - 28
      - 23
      - 18
      - 13
    - text: bite +21 (2d8+4)
      entries:
      - - damage: 2d8+4
      attack: bite
      bonus:
      - 21
  special:
  - cloak of souls
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 25
  - name: cloudkill
    source: default
    freq: At will
    DC: 22
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: quickened cloudkill
    source: default
    freq: 3/day
    DC: 22
  - name: destruction
    source: default
    freq: 3/day
    DC: 24
  - name: fire storm
    source: default
    freq: 3/day
    DC: 25
  - name: incendiary cloud
    source: default
    freq: 3/day
    DC: 25
  - name: spell turning
    source: default
    freq: 3/day
  - name: mass hold person
    source: default
    freq: 1/day
    DC: 24
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 26
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: purrodaemon
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 26
  DEX: 19
  CON: 28
  INT: 13
  WIS: 21
  CHA: 24
BAB: 22
CMB: 34
CMB_other: +38 sunder
CMD: 52
CMD_other: 54 vs. sunder
feats:
- name: Bleeding Critical
- name: Critical Focus
- name: Greater Sunder
- name: GreaterVital Strike
- name: Improved Critical (halberd)
- name: Improved Sunder
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability(cloudkill)
- name: Vital Strike
- name: Weapon Focus (halberd)
skills:
  Bluff: 32
  Fly: 23
  Intimidate: 32
  Knowledge (history,planes): 15
  Perception: 30
  Sense Motive: 30
  Spellcraft: 26
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- warfare mastery
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or holocaust (3-6)
  treasure_type: standard
  treasure:
  - +1 unholy halberd
  - other treasure
special_abilities:
  Cloak of Souls (Su): 'An obcisidaemon is attended by the souls it has captured-a
    mass often resembling a tattered, ethereal cloak or a roiling cloud of dust at
    its feet. When an obcisidaemon successfully captures a soul with its inherit soul
    ability, the soul becomes a part of its cloak of souls, taking up one soul slot.
    An obcisidaemon has a number of soul slots equal to its Charisma modifier (7 for
    the typical obcisidaemon). Destroying the daemon frees any souls in its cloak,
    though this does not return the deceased creatures to life. Any attempt to resurrect
    a creature whose soul is trapped in a cloak of souls requires a DC 28 caster level
    check. Failure results in the spell having no effect, while success tears the
    victim's soul free from the cloak and returns the creature to life as normal.
    If the daemon is in an unholy location, such as that created by an unhallow spell
    or on Abaddon, the DC of this caster level check increases by 2. Once a soul is
    consumed, only miracle or wish can restore the creature to life. As a swift action,
    an obcisidaemon can consume a soul from its cloak to achieve one of the following
    effects. • Increase the save DC of the next spell-like ability the obcisidaemon
    uses that round by 2. • Gain the benefit of a heal spell. • Grant a single weapon
    wielded by the obcisidaemon one of the following weapon abilities for 1 round:
    flaming burst, icy burst, shocking burst, or wounding.'
  Inherit Soul (Su): Whenever an obcisidaemon kills a creature with a weapon it wields,
    that creature must immediately succeed at a DC 30 Fortitude save or be consumed
    by the daemon's cloak of souls. This is a death effect. If the cloak cannot consume
    this soul without exceeding its number of soul slots, the daemon can release a
    soul as a free action in order to make room for the new soul; otherwise, the killed
    creature automatically succeeds at its save and its soul is not absorbed. The
    save DC is Constitution-based.
  Scorched Earth (Su): A creature that dies within 60 feet of an obcisidaemon and
    is not drawn into the daemon's cloak of souls via its inherit soul ability must
    immediately succeed at a DC 28 Fortitude save or its body is utterly consumed
    in unholy fire equivalent to the effect of a destruction spell. The save DC is
    Charisma-based.
  Warfare Mastery (Ex): Although the typical obcisidaemon fights with a halberd, these
    daemons are proficient with all weapons. An obcisidaemon will sometimes eschew
    the typical +1 unholy halberd its kind favors for the favored weapon of the specific
    Horseman it serves.
desc_long: |-
  The towering and devastating obcisidaemon personifies the darkest elements of war. Obcisidaemons strip away the veneer of honor and battlefield glory and the complexity of wartime tactics, leaving behind only the brutal and violent truth of conflict at its core, and then divest it of any humanity to reveal naught but scorched earth and genocide. Reflecting the disgraceful values of ethnic cleansing, depopulation, and all other forms of the clinical, systematic obliteration of civilian populations, obcisidaemons are among the most powerful members of daemonkind. These paragons of inhumanity arrive in the heart of great cities and leave wastelands of rubble and ashes in their wakes. Where an obcisidaemon walks, not even the ghosts of the dead remain to lament the destruction, for the daemon wipes out not only innocent individuals, but also their entire histories and bloodlines, ensuring that no future exists for its victims in any sense of the word. 

  When a mortal commits an act of genocide in life and goes to Abaddon in death, it has a chance of forming into an obcisidaemon if it survives long enough as a member of the hunted. Such individuals rarely have trouble managing the unforgiving wastes, as they have already proven willing to destroy any and all possible allies in order to ensure their own survival, making betrayal an impossibility and solitude an inevitability. A vicious soul that eventually develops into an obcisidaemon becomes a lone, wandering mass of slaughter that acts as a harbinger of undiscriminating and unforgiving death to all who dare stand in its path. In life, the soul perhaps desired to kill only a particular chosen population; as an obcisidaemon, however, the being seeks the obliteration of all mortals. 

  Peculiar to an obcisidaemon is the cloak of souls that seems to seep from its enormous body, a symbol of its destructive abilities providing onlookers a hint of the sheer scope of its murderous capabilities. When an obcisidaemon lays slaughter to entire populations, it does not feast on all of the souls at once, but captures victims for later use. When the fiend needs to unleash a particularly potent rampage upon a resistant population, it consumes these reserved souls in order to strengthen its powers and ensure its success in total annihilation. Some obcisidaemons have developed eldritch methods to craft and shape these soul fragments, and use them to drape themselves in the material. 

  Devoted to the wanton, systematic slaughter of all mortal life, most obcisidaemons serve Szuriel, the Horseman of War, who shares similar ideals. In her service, obcisidaemons act as high-ranking officers at the head of armies of purrodaemons, to take advantage of their skill at the pragmatic art of organized massacres. Occasionally, an obcisidaemon instead serves Apollyon, occupying a similar role at the head of a titanic flight of leukodaemons sowing clouds of poison across miles of terrain in its passing. Sometimes, an amassed group of obcisidaemons might trail behind an invading daemonic army, guaranteeing that no trace of the butchered mortals remains among the ashes and salted earth. These obcisidaemons not only ensure that all life perishes, but that the land is thereafter uninhabitable by any living creatures. 

  Some obcisidaemons serve no particular member of the Four Horsemen, instead choosing to function as independent agents of genocide and endless eons of wartime slaughter. These nomadic, self-serving beings wander from plane to plane, laying waste to one civilization after another. Some obcisidaemons intentionally spread their true names to the Material Plane, hoping for a foolish evil summoner to call upon them, knowing that no mere mortal could control their awesome power. Such summoners often end up among the first souls to be devoured and woven into the cloud of tormented spirits that cloaks the rampaging obcisidaemon. 

  Obcisidaemons stand 25 feet tall, have wingspans of 30 feet, and weigh over 15,000 pounds, but rumors whisper of specimens that are nearly three times this size.

---

# Daemon, Obcisidaemon
This massive fiend has _[[monsters/Eagle|eagle]]_ wings, a tusked canine face, and

a muscular frame. It wields an immense, cruel-looking _[[items/Weapon/Halberd|halberd]]_.
**Source** Bestiary 6 pg. 72, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 3: Horsemen of the Apocalypse pg. 50
**XP** 204,800

NE Gargantuan outsider (daemon, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/True Seeing|true seeing]]_;

Perception +30
**Aura** scorched earth (60 ft., DC 28), _[[spells/Unholy Aura|unholy aura]]_ (DC 25)

##### Defense

**AC** 34, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+4 deflection, +4 Dex, +20 natural,

–4 size)
**hp** 319 (22d10+198)
**Fort** +26, **Ref** +15, **Will** +22
**DR** 15/good and silver; **Immune** acid, death effects, disease,

poison; **Resist** cold 30, electricity 30, fire 30; **SR** 30

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** +1 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _halberd_ +28/+23/+18/+13 (4d8+13/19–20/×3

plus inherit soul), bite +21 (2d8+4)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** cloak of souls
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_deathwatch_, _true seeing_, _unholy aura_ (DC 25) 
At will—_[[spells/Cloudkill|cloudkill]]_ (DC 22), greater teleport (self plus 50 lbs. of objects only) 
3/day—quickened _cloudkill_ (DC 22), _[[spells/Destruction|destruction]]_ (DC 24), _[[spells/Fire Storm|fire storm]]_ (DC 25), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 25), _[[spells/Spell Turning|spell turning]]_ 
1/day—mass _[[spells/Hold Person|hold person]]_ (DC 24), _[[spells/Meteor Swarm|meteor swarm]]_ (DC 26), _[[universal monster rules/Summon|summon]]_ (level 9, 1 purrodaemon 50%)

##### Statistics
**Str** 26, **Dex** 19, **Con** 28, **Int** 13, **Wis** 21, **Cha** 24
**Base Atk** +22; **CMB** +34 (+38 sunder); **CMD** 52 (54 vs. sunder)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Sunder|Greater Sunder]]_, Greater

_[[feats/Vital Strike|Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (_halberd_), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_

(_cloudkill_), _Vital Strike_, _[[feats/Weapon Focus|Weapon Focus]]_ (_halberd_)
**Skills** Bluff +32, Fly +23, Intimidate +32, Knowledge (history,

planes) +15, Perception +30, Sense Motive +30, Spellcraft +26
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** warfare mastery

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or holocaust (3–6)
**Treasure** standard (+1 _unholy_ _halberd_, other treasure)

### Special Abilities

**Cloak of Souls (Su)** An obcisidaemon is attended by the souls it has captured—a mass often resembling a tattered, ethereal cloak or a roiling cloud of dust at its feet. When an obcisidaemon successfully captures a soul with its inherit soul ability, the soul becomes a part of its cloak of souls, taking up one soul slot. An obcisidaemon has a number of soul slots equal to its Charisma modifier (7 for the typical obcisidaemon). Destroying the daemon frees any souls in its cloak, though this does not return the deceased creatures to life. Any attempt to resurrect a creature whose soul is trapped in a cloak of souls requires a DC 28 caster level check. Failure results in the spell having no effect, while success tears the victim’s soul free from the cloak and returns the creature to life as normal. If the daemon is in an _unholy_ location, such as that created by an _[[spells/Unhallow|unhallow]]_ spell or on Abaddon, the DC of this caster level check increases by 2. Once a soul is consumed, only _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ can restore the creature to life. As a swift action, an obcisidaemon can consume a soul from its cloak to achieve one of the following effects.

* • Increase the save DC of the next spell-like ability the obcisidaemon uses that round by 2. 
* • Gain the benefit of a _[[spells/Heal|heal]]_ spell. 
* • Grant a single weapon wielded by the obcisidaemon one of the following weapon abilities for 1 round: _[[items/Weapon Magic Abilities/Flaming Burst|flaming burst]]_, _[[items/Weapon Magic Abilities/Icy Burst|icy burst]]_, _[[items/Weapon Magic Abilities/Shocking Burst|shocking burst]]_, or _[[items/Weapon Magic Abilities/Wounding|wounding]]_.

**Inherit Soul (Su)** Whenever an obcisidaemon kills a creature with a weapon it wields, that creature must immediately succeed at a DC 30 Fortitude save or be consumed by the daemon’s cloak of souls. This is a death effect. If the cloak cannot consume this soul without exceeding its number of soul slots, the daemon can release a soul as a free action in order to make room for the new soul; otherwise, the killed creature automatically succeeds at its save and its soul is not absorbed. The save DC is Constitution-based.
**Scorched Earth (Su)** A creature that dies within 60 feet of an obcisidaemon and is not drawn into the daemon’s cloak of souls via its inherit soul ability must immediately succeed at a DC 28 Fortitude save or its body is utterly consumed in _unholy_ fire equivalent to the effect of a _destruction_ spell. The save DC is Charisma-based.

**Warfare Mastery (Ex)** Although the typical obcisidaemon fights with a _halberd_, these daemons are proficient with all weapons. An obcisidaemon will sometimes eschew the typical +1 _unholy_ _halberd_ its kind favors for the favored weapon of the specific Horseman it serves.

##### Description

The towering and devastating obcisidaemon personifies the darkest elements of war. Obcisidaemons strip away the veneer of honor and battlefield glory and the complexity of wartime tactics, leaving behind only the brutal and violent truth of conflict at its core, and then divest it of any humanity to reveal naught but scorched earth and genocide. _[[items/Armor Magic Abilities/Reflecting|Reflecting]]_ the disgraceful values of ethnic cleansing, depopulation, and all other forms of the clinical, systematic obliteration of civilian populations, obcisidaemons are among the most powerful members of daemonkind. These paragons of inhumanity arrive in the heart of great cities and leave wastelands of rubble and ashes in their wakes. Where an obcisidaemon walks, not even the ghosts of the dead remain to lament the _destruction_, for the daemon wipes out not only innocent individuals, but also their entire histories and bloodlines, ensuring that no future exists for its victims in any sense of the word.

When a mortal commits an act of genocide in life and goes to Abaddon in death, it has a chance of forming into an obcisidaemon if it survives long enough as a member of the hunted. Such individuals rarely have trouble managing the unforgiving wastes, as they have already proven willing to destroy any and all possible allies in order to ensure their own survival, making betrayal an impossibility and solitude an inevitability. A _[[items/Weapon Magic Abilities/Vicious|vicious]]_ soul that eventually develops into an obcisidaemon becomes a lone, wandering mass of slaughter that acts as a harbinger of undiscriminating and unforgiving death to all who dare stand in its path. In life, the soul perhaps desired to kill only a particular chosen population; as an obcisidaemon, however, the being seeks the obliteration of all mortals.

Peculiar to an obcisidaemon is the cloak of souls that seems to seep from its enormous body, a symbol of its destructive abilities providing onlookers a hint of the sheer scope of its murderous capabilities. When an obcisidaemon lays slaughter to entire populations, it does not feast on all of the souls at once, but captures victims for later use. When the fiend needs to unleash a particularly _[[items/Weapon Magic Abilities/Potent|potent]]_ rampage upon a resistant population, it consumes these reserved souls in order to strengthen its powers and ensure its success in total annihilation. Some obcisidaemons have developed eldritch methods to craft and shape these soul fragments, and use them to drape themselves in the material.

Devoted to the wanton, systematic slaughter of all mortal life, most obcisidaemons serve Szuriel, the Horseman of War, who shares similar ideals. In her service, obcisidaemons act as high-ranking officers at the head of armies of purrodaemons, to take advantage of their skill at the pragmatic art of organized massacres. Occasionally, an obcisidaemon instead serves Apollyon, occupying a similar role at the head of a _[[items/Armor Magic Abilities/Titanic|titanic]]_ _[[universal monster rules/Flight|flight]]_ of leukodaemons sowing clouds of poison across miles of terrain in its passing. Sometimes, an amassed group of obcisidaemons might trail behind an invading daemonic army, guaranteeing that no trace of the butchered mortals remains among the ashes and salted earth. These obcisidaemons not only ensure that all life perishes, but that the land is thereafter uninhabitable by any living creatures.

Some obcisidaemons serve no particular member of the Four Horsemen, instead choosing to function as independent agents of genocide and endless eons of wartime slaughter. These nomadic, self-serving beings wander from plane to plane, laying waste to one civilization after another. Some obcisidaemons intentionally spread their true names to the Material Plane, hoping for a foolish evil _[[classes/Summoner|summoner]]_ to call upon them, knowing that no mere mortal could control their awesome power. Such summoners often end up among the first souls to be devoured and woven into the cloud of tormented spirits that cloaks the _[[items/Armor Magic Abilities/Rampaging|rampaging]]_ obcisidaemon.

Obcisidaemons stand 25 feet tall, have wingspans of 30 feet, and weigh over 15,000 pounds, but rumors whisper of specimens that are nearly three times this size.