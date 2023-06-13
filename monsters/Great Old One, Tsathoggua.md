---
cssclass: [monsters]
title1: Great Old One, Tsathoggua
desc_short: Neither quite humanoid nor quite toad, this lumbering monstrosity maintains
  a malevolent expression on its batlike face.
title2: Tsathoggua
CR: 29
sources:
- name: 'Pathfinder #111: Dreams of the Yellow King'
  page: 84
  link: http://paizo.com/products/btpy9pmo?Pathfinder-Adventure-Path-111-Dreams-of-the-Yellow-King
XP: 6553600
alignment: CE
size: Large
type: aberration
subtypes:
- chaotic
- evil
- Great Old One
initiative:
  bonus: 21
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 38
  duration: 10 rounds
AC:
  AC: 47
  touch: 30
  flat_footed: 36
  components:
    dex: 11
    insight: 10
    natural: 17
    size: -1
HP:
  HP: 742
  long: 33d8+594
  fast_healing: 25
saves:
  fort: 29
  ref: 24
  will: 29
defensive_abilities:
- freedom of movement
- immortality
- insanity (DC 38)
DR:
- amount: 15
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- acid
- aging
- cold
- death effects
- disease
- energy drain
- mind-affecting effects
- paralysis
- petrification
resistances:
  electricity: 30
  sonic: 30
SR: 40
speeds:
  base: 50
  other_semicolon: air walk
attacks:
  melee:
  - - text: bite +42 (8d10+28/18-20/×3 plus feed)
      entries:
      - - damage: 8d10+28
          crit_range: 18-20
          crit_multiplier: 3
        - effect: feed
      attack: bite
      bonus:
      - 42
    - text: 2 claws +42 (5d6+28/18-20/×3 plus grab)
      entries:
      - - damage: 5d6+28
          crit_range: 18-20
          crit_multiplier: 3
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 42
  special:
  - constrict (4d6+25)
  - consume spellcaster
  - create spawn
  - feed
  - mythic power (10/day, surge +1d12)
  - outcast's dreams
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 29
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 27
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
    DC: 30
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 27
  - superscripts:
    - APG
    name: hungry pit
    source: default
    freq: 3/day
    DC: 27
  - name: power word stun
    source: default
    freq: 3/day
  - name: maze
    source: default
    freq: 1/day
  - name: weird
    source: default
    freq: 1/day
    DC: 31
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 29
    concentration: 41
spells:
  entries:
  - name: imprisonment
    source: '?'
    level: 9
    DC: 31
  - name: time stop
    source: '?'
    level: 9
  - name: polymorph any object
    source: '?'
    level: 8
    DC: 30
  - name: prismatic wall
    source: '?'
    level: 8
    DC: 30
  - name: greater teleport
    source: '?'
    level: 7
  - name: word of chaos
    source: '?'
    level: 7
    DC: 29
  - name: heal
    source: '?'
    level: 6
  - name: word of recall
    source: '?'
    level: 6
  - name: dominate person
    source: '?'
    level: 5
    DC: 27
  - name: wall of force
    source: '?'
    level: 5
  - name: black tentacles
    source: '?'
    level: 4
  - name: greater magic fang
    source: '?'
    level: 4
  - name: displacement
    source: '?'
    level: 3
  - name: fly
    source: '?'
    level: 3
  - name: command undead
    source: '?'
    level: 2
    DC: 24
  - name: invisibility
    source: '?'
    level: 2
  - name: mage armor
    source: '?'
    level: 1
  - name: reduce person
    source: '?'
    level: 1
    DC: 23
  - name: arcane mark
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
    DC: 22
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 29
    concentration: 41
    slots:
      9: 7
      8: 8
      7: 8
      6: 8
      5: 8
      4: 9
      3: 9
      2: 9
      1: 9
      0: at-will
ability_scores:
  STR: 48
  DEX: 33
  CON: 46
  INT: 31
  WIS: 32
  CHA: 35
BAB: 24
CMB: 44
CMB_other: +48 sunder
CMD: 75
CMD_other: 77 vs. sunder
feats:
- name: Arcane Strike
- name: Blinding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Empower Spell
- name: Eschew Materials
- name: Greater Sunder
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Sunder
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell
- name: Quicken Spell-Like Ability (feeblemind)
- name: Vital Strike
skills:
  Bluff: 45
  Fly: 45
  Intimidate: 48
  Knowledge (arcana): 46
  Knowledge (dungeoneering): 43
  Knowledge (geography): 43
  Knowledge (history): 43
  Knowledge (nature): 43
  Knowledge (religion): 43
  Perception: 47
  Sense Motive: 44
  Spellcraft: 46
  Stealth: 43
  Use Magic Device: 45
languages:
- Aklo
- telepathy 300 ft.
- tongues
special_qualities:
- adaptive spellcasting
- item creation
- powerful blows
ecology:
  environment: any (Darklands)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Adaptive Spellcasting (Su): Tsathoggua has mastered all forms of magic, be they
    arcane, divine, or psychic. He casts spells spontaneously, as per a sorcerer,
    but he can cast spells from any spell list. He can know up to two spells per spell
    level from 1st to 9th at any one time (and up to six 0-level spells at any one
    time), taken from any spell list. When he uses his consume spellcaster ability,
    he can swap out up to two spells currently known for any two spells known (and
    currently prepared in the case of prepared spellcasters) by his consumed victim.
    The only spells Tsathoggua can never know are those with the good or lawful descriptors.
    The spells listed above are those he favors, but GMs are free to alter that list
    as they wish for encounters with Tsathoggua.
  Consume Spellcaster (Su): When Tsathoggua kills a spellcaster while using his feed
    ability, the spellcaster's body shrivels into what appears to be a long-dead mummified
    corpse. Tsathoggua can learn any two spells known by the spellcaster (see adaptive
    spellcasting above) when he kills a spellcaster in this way, and he regains a
    number of hit points equal to the total number of spell levels still uncast by
    the consumed victim.
  Create Spawn (Su): Once every hour as a standard action, Tsathoggua can emit 1d4
    formless spawn from his body. These newly created formless spawn have free will
    and are fully grown, but they follow Tsathoggua's commands for 1d4 days after
    creation. Tsathoggua sometimes gifts newly created spawn to visitors he favors.
    Sometimes he just eats them. Those spawn that escape servitude or digestion slither
    off into the world on their own.
  Feed (Su): Whenever Tsathoggua deals bite damage to a creature, he drinks away vital
    essence, sanity, and bodily fluids alike. This causes 1d4 points of ability drain
    to all six ability scores. A successful DC 44 Fortitude saving throw reduces the
    1d4 points of ability drain to only one ability score, chosen by Tsathoggua. The
    save DC is Constitution-based.
  Great Old One Traits: Rules for Tsathoggua's Great Old One traits such as immortality,
    insanity, his mythic abilities, otherworldly insight, and unspeakable presence
    can be found on page 306 of Pathfinder RPG Bestiary 4.
  Immortality (Su): If Tsathoggua is slain, his body tears open and creates a burst
    of vile ooze that deals 20d8 points of acid damage to all creatures within a 60-foot
    spread. A total of 2d6 formless spawn immediately form in random spots throughout
    this area of effect, while the remainder of the gore seeps into the ground, reforming
    into Tsathoggua in a deep cavern on another world after 1d100 months have passed.
    All portals in Tsathoggua's domain that connect to the world on which he was slain
    deactivate and must be manually repaired by the Great Old One, a process that
    can take years or even decades but does not bar his return to that world via other
    means.
  Item Creation (Su): Tsathoggua is treated as having all item creation feats for
    the purposes of crafting magic items.
  Outcast's Dreams (Su): Tsathoggua can affect any creature with outcast's dreams
    that has succumbed to the Great Old One's unspeakable presence or that has ever
    offered him prayer or physically touched an altar dedicated to him within the
    walls of a still-standing temple of Tsathoggua. When Tsathoggua uses nightmare
    on such a target, the victim must also succeed at a DC 38 Will saving throw or
    feel cast out of society and spurned by friends and loved ones. The victim cannot
    benefit from the aid another action or provide aid to others, it must always attempt
    saving throws against beneficial spell effects if saving throws are allowed, and
    it takes a -4 penalty on all attack rolls, saving throws, and skill checks when
    any other creature of its type is within 30 feet of it. This is a mindaffecting
    effect. The save DC is Charisma-based.
  Powerful Blows (Ex): Tsathoggua's bite and claw attacks always apply 1-1/2 times
    his Strength modifier to damage.
  Unspeakable Presence (Su): Failing a DC 38 Will saving throw against Tsathoggua's
    unspeakable presence causes the victim to perceive Tsathoggua as its only ally;
    it treats all other creatures as enemies and does what it can to defend Tsathoggua
    and obey the Great Old One's commands, as if under the effects of dominate monster.
    This effect persists for as long as the victim remains within 300 feet of Tsathoggua.
    This is a mind-affecting effect. The save DC is Charisma-based.
desc_long: |-
  Known variously to his worshipers as the Father of Night, Saint Toad, the Sleeper in the Deep, and other appellations, Tsathoggua is among the more enigmatic of the Great Old Ones. Not only does he often interact with mortal life, but he has at times done so in a friendly or even charitable manner. Yet these moods are mercurial, and the Great Old One tires of company and attempts to eat those he had been aiding only a moment before. Those who worship him generally do not display this level of magnanimity; they are typically fanatic and violent in their methods of preserving the secrets of their sect.

  Tsathoggua appears as a bloated toadlike creature, covered with fur and wearing a strange, sleepy expression on his bat-like face.

---

# Great Old One, Tsathoggua
Neither quite humanoid nor quite toad, this lumbering monstrosity maintains a _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ expression on its batlike face.
**Source** Pathfinder #111: Dreams of the Yellow _[[npcs/King|King]]_ pg. 84
**XP** 6,553,600
CE Large aberration (chaotic, evil, Great Old One)
**Init** +21; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +47
**Aura** unspeakable presence (300 ft., DC 38, 10 rounds)

##### Defense

**AC** 47, touch 30, _[[conditions/Flat-Footed|flat-footed]]_ 36 (+11 Dex, +10 insight, +17 natural, –1 size)
**hp** 742 (33d8+594); _[[universal monster rules/Fast Healing|fast healing]]_ 25
**Fort** +29, **Ref** +24, **Will** +29
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 38); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, acid, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification; **Resist** electricity 30, sonic 30; **SR** 40

##### Offense
**Speed** 50 ft.; _[[spells/Air Walk|air walk]]_
**Melee** bite +42 (8d10+28/18–20/×3 plus feed), 2 claws +42 (5d6+28/18–20/×3 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (4d6+25), consume spellcaster, create spawn, feed, mythic power (10/day, surge +1d12), outcast’s dreams
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +41)
Constant—_air walk_, _freedom of movement_, _[[spells/Tongues|tongues]]_, _true seeing_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _insanity_ (DC 29), _[[spells/Nightmare|nightmare]]_ (DC 27), _[[spells/Sending|sending]]_
3/day—_[[spells/Demand|demand]]_ (DC 30), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 27), _[[spells/Hungry Pit|hungry pit]]_ (DC 27), _[[spells/Power Word Stun|power word stun]]_
1/day—_[[spells/Maze|maze]]_, _[[spells/Weird|weird]]_ (DC 31), _[[spells/Wish|wish]]_
**Spells Known **(CL 29th; concentration +41)
9th (7/day)—_[[spells/Imprisonment|imprisonment]]_ (DC 31), _[[spells/Time Stop|time stop]]_
8th (8/day)—_[[spells/Polymorph Any Object|polymorph any object]]_ (DC 30), _[[spells/Prismatic Wall|prismatic wall]]_ (DC 30)
7th (8/day)—greater teleport, _[[spells/Word Of Chaos|word of chaos]]_ (DC 29)
6th (8/day)—_[[spells/Heal|heal]]_, _[[spells/Word of Recall|word of recall]]_
5th (8/day)—_[[spells/Dominate Person|dominate person]]_ (DC 27), _[[spells/Wall Of Force|wall of force]]_
4th (9/day)—_[[spells/Black Tentacles|black tentacles]]_, greater _[[spells/Magic Fang|magic fang]]_
3rd (9/day)—_[[spells/Displacement|displacement]]_, fly
2nd (9/day)—_[[spells/Command Undead|command undead]]_ (DC 24), _[[spells/Invisibility|invisibility]]_
1st (9/day)—_[[spells/Mage Armor|mage armor]]_, _[[spells/Reduce Person|reduce person]]_ (DC 23)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 22), _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 48, **Dex** 33, **Con** 46, **Int** 31, **Wis** 32, **Cha** 35
**Base Atk** +24; **CMB** +44 (+48 sunder); **CMD** 75 (77 vs. sunder)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +45, Fly +45, Intimidate +48, Knowledge (arcana) +46, Knowledge (dungeoneering, geography, history, nature, religion) +43, Perception +47, Sense Motive +44, Spellcraft +46, Stealth +43, Use Magic Device +45
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.; _tongues_
**SQ** adaptive spellcasting, item creation, powerful blows

##### Ecology

**Environment** any (Darklands)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Adaptive Spellcasting (Su)** Tsathoggua has mastered all forms of magic, be they arcane, divine, or _[[classes/Psychic|psychic]]_. He casts spells spontaneously, as per a _[[classes/Sorcerer|sorcerer]]_, but he can cast spells from any spell list. He can know up to two spells per spell level from 1st to 9th at any one time (and up to six 0-level spells at any one time), taken from any spell list. When he uses his consume spellcaster ability, he can swap out up to two spells currently known for any two spells known (and currently prepared in the case of prepared spellcasters) by his consumed victim. The only spells Tsathoggua can never know are those with the good or lawful descriptors. The spells listed above are those he favors, but GMs are free to alter that list as they _wish_ for encounters with Tsathoggua.

**Consume Spellcaster (Su)** When Tsathoggua kills a spellcaster while using his feed ability, the spellcaster’s body shrivels into what appears to be a long-dead mummified corpse. Tsathoggua can learn any two spells known by the spellcaster (see adaptive spellcasting above) when he kills a spellcaster in this way, and he regains a number of hit points equal to the total number of spell levels still uncast by the consumed victim.

**Create Spawn (Su)** Once every hour as a standard action, Tsathoggua can emit 1d4 _[[monsters/Formless Spawn|formless spawn]]_ from his body. These newly created _formless spawn_ have free will and are fully grown, but they follow Tsathoggua’s commands for 1d4 days after creation. Tsathoggua sometimes gifts newly created spawn to visitors he favors. Sometimes he just eats them. Those spawn that escape servitude or digestion slither off into the world on their own.

**Feed (Su)** Whenever Tsathoggua deals bite damage to a creature, he drinks away vital essence, sanity, and bodily fluids alike. This causes 1d4 points of ability drain to all six ability scores. A successful DC 44 Fortitude saving throw reduces the 1d4 points of ability drain to only one ability score, chosen by Tsathoggua. The save DC is Constitution-based.

**Great Old One Traits** Rules for Tsathoggua’s Great Old One traits such as immortality, _insanity_, his mythic abilities, otherworldly insight, and unspeakable presence can be found on page 306 of Pathfinder RPG Bestiary 4.

**Immortality (Su)** If Tsathoggua is slain, his body tears open and creates a burst of vile ooze that deals 20d8 points of acid damage to all creatures within a 60-foot spread. A total of 2d6 _formless spawn_ immediately form in random spots throughout this area of effect, while the remainder of the gore seeps into the ground, reforming into Tsathoggua in a deep cavern on another world after 1d100 months have passed. All portals in Tsathoggua’s domain that connect to the world on which he was slain deactivate and must be manually repaired by the Great Old One, a process that can take years or even decades but does not bar his return to that world via other means.

**Item Creation (Su)** Tsathoggua is treated as having all item creation feats for the purposes of crafting magic items.

**Outcast’s Dreams (Su)** Tsathoggua can affect any creature with outcast’s dreams that has succumbed to the Great Old One’s unspeakable presence or that has ever offered him _[[spells/Prayer|prayer]]_ or physically touched an altar dedicated to him within the walls of a still-standing temple of Tsathoggua. When Tsathoggua uses _nightmare_ on such a target, the victim must also succeed at a DC 38 Will saving throw or feel _[[spells/Cast Out|cast out]]_ of society and spurned by friends and loved ones. The victim cannot benefit from the aid another action or provide aid to others, it must always attempt saving throws against beneficial spell effects if saving throws are allowed, and it takes a –4 penalty on all attack rolls, saving throws, and skill checks when any other creature of its type is within 30 feet of it. This is a mindaffecting effect. The save DC is Charisma-based.

**Powerful Blows (Ex)** Tsathoggua’s bite and claw attacks always apply 1-1/2 times his Strength modifier to damage.

**Unspeakable Presence (Su)** Failing a DC 38 Will saving throw against Tsathoggua’s unspeakable presence causes the victim to perceive Tsathoggua as its only ally; it treats all other creatures as enemies and does what it can to defend Tsathoggua and obey the Great Old One’s commands, as if under the effects of _[[spells/Dominate Monster|dominate monster]]_. This effect persists for as long as the victim remains within 300 feet of Tsathoggua. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

Known variously to his worshipers as the Father of Night, Saint Toad, the _[[feats/Sleeper|Sleeper]]_ in the Deep, and other appellations, Tsathoggua is among the more enigmatic of the Great Old Ones. Not only does he often interact with mortal life, but he has at times done so in a friendly or even charitable manner. Yet these moods are mercurial, and the Great Old One tires of company and attempts to eat those he had been aiding only a moment before. Those who worship him generally do not display this level of magnanimity; they are typically fanatic and violent in their methods of preserving the secrets of their sect.

Tsathoggua appears as a bloated toadlike creature, covered with fur and wearing a strange, sleepy expression on his bat-like face.