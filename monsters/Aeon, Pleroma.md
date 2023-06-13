---
cssclass: [monsters]
title1: Aeon, Pleroma
desc_short: 'Within the shadows of this vaguely humanoid figure stir swirling colors
  and spheres, as if it encompassed all the night sky. '
title2: Pleroma
CR: 20
sources:
- name: Bestiary 2
  page: 12
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: N
size: Large
type: outsider
subtypes:
- aeon
- extraplanar
initiative:
  bonus: 12
senses:
  blindsight: 120
  darkvision: 120
  true seeing: true
AC:
  AC: 36
  touch: 24
  flat_footed: 27
  components:
    deflection: 6
    dex: 8
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 324
  long: 24d10+192
  fast_healing: 10
saves:
  fort: 24
  ref: 18
  will: 26
immunities:
- cold
- critical hits
- poison
resistances:
  electricity: 10
  fire: 10
SR: 31
speeds:
  base: 0
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: touch +30 (20d8 energy)
      entries:
      - - damage: 20d8
          type: energy
      attack: touch
      bonus:
      - 30
  special:
  - sphere of creation
  - sphere of oblivion
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: create food and water
    source: default
    freq: At will
  - name: mending
    source: default
    freq: At will
  - name: rusting grasp
    source: default
    freq: At will
    DC: 21
  - name: stone shape
    source: default
    freq: At will
  - name: wood shape
    source: default
    freq: At will
    DC: 19
  - name: fabricate
    source: default
    freq: 7/day
  - name: plant growth
    source: default
    freq: 7/day
  - name: sculpt sound
    source: default
    freq: 7/day
  - name: shout
    source: default
    freq: 7/day
    DC: 21
  - name: break enchantment
    source: default
    freq: 5/day
  - name: daylight
    source: default
    freq: 5/day
  - name: deeper darkness
    source: default
    freq: 5/day
  - name: freedom of movement
    source: default
    freq: 5/day
  - name: major creation
    source: default
    freq: 5/day
  - name: disintegrate
    source: default
    freq: 3/day
    DC: 23
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 25
  - name: mage's disjunction
    source: default
    freq: 1/day
    DC: 26
  - name: wish
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - name: astral projection
    source: Cleric
    level: 9
  - name: gate
    source: Cleric
    level: 9
  - name: implosion
    source: Cleric
    level: 9
    count: 3
    DC: 29
  - name: cloak of chaos
    source: Cleric
    level: 8
    DC: 28
  - name: holy aura
    source: Cleric
    level: 8
    DC: 28
  - name: shield of law
    source: Cleric
    level: 8
    DC: 28
  - name: summon monster VIII
    source: Cleric
    level: 8
  - name: unholy aura
    source: Cleric
    level: 8
    DC: 28
  - name: blasphemy
    source: Cleric
    level: 7
    DC: 27
  - name: destruction
    source: Cleric
    level: 7
    DC: 27
  - name: dictum
    source: Cleric
    level: 7
    DC: 27
  - name: holy word
    source: Cleric
    level: 7
    DC: 27
  - name: word of chaos
    source: Cleric
    level: 7
    DC: 27
  - name: banishment
    source: Cleric
    level: 6
    DC: 26
  - name: forbiddance
    source: Cleric
    level: 6
    DC: 26
  - name: geas
    source: Cleric
    level: 6
  - name: legend lore
    source: Cleric
    level: 6
  - name: repulsion
    source: Cleric
    level: 6
    DC: 26
  - name: veil
    source: Cleric
    level: 6
    DC: 26
  - name: contact other plane
    source: Cleric
    level: 5
  - name: dispel chaos
    source: Cleric
    level: 5
    DC: 25
  - name: dispel evil
    source: Cleric
    level: 5
    DC: 25
  - name: dispel good
    source: Cleric
    level: 5
    DC: 25
  - name: dispel law
    source: Cleric
    level: 5
    DC: 25
  - name: teleport
    source: Cleric
    level: 5
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 24
  - name: holy smite
    source: Cleric
    level: 4
    DC: 24
  - name: order's wraith
    source: Cleric
    level: 4
    DC: 21
  - name: restoration
    source: Cleric
    level: 4
  - name: scrying
    source: Cleric
    level: 4
    DC: 24
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 24
  - name: clairaudience/clairvoyance
    source: Cleric
    level: 3
  - name: magic circle against chaos
    source: Cleric
    level: 3
  - name: magic circle against evil
    source: Cleric
    level: 3
  - name: magic circle against good
    source: Cleric
    level: 3
  - name: magic circle against law
    source: Cleric
    level: 3
  - name: suggestion
    source: Cleric
    level: 3
    DC: 23
  - name: align weapon
    source: Cleric
    level: 2
  - name: detect thoughts
    source: Cleric
    level: 2
    DC: 22
  - name: enthrall
    source: Cleric
    level: 2
    DC: 22
  - name: make whole
    source: Cleric
    level: 2
  - name: see invisibility
    source: Cleric
    level: 2
  - name: undetectable alignment
    source: Cleric
    level: 2
  - name: zone of truth
    source: Cleric
    level: 2
    DC: 22
  - name: detect chaos
    source: Cleric
    level: 1
  - name: detect evil
    source: Cleric
    level: 1
  - name: detect good
    source: Cleric
    level: 1
  - name: detect law
    source: Cleric
    level: 1
  - name: identify
    source: Cleric
    level: 1
  - name: magic aura
    source: Cleric
    level: 1
  - name: true strike
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 20
    concentration: 27
ability_scores:
  STR: 24
  DEX: 27
  CON: 26
  INT: 26
  WIS: 31
  CHA: 25
BAB: 24
CMB: 32
CMD: 57
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Lightning Stance
- name: Mobility
- name: Wind Stance
skills:
  Appraise: 30
  Bluff: 32
  Fly: 16
  Heal: 30
  Intimidate: 27
  Knowledge (arcana): 47
  Knowledge (dungeoneering): 44
  Knowledge (engineering): 44
  Knowledge (nature): 47
  Knowledge (planes): 47
  Knowledge (religion): 47
  Perception: 41
  Sense Motive: 39
  Spellcraft: 30
  Stealth: 27
  Use Magic Device: 27
languages:
- envisaging
special_qualities:
- extension of all
- void form
ecology:
  environment: any (Outer Planes)
  organization: solitary or tribunal (1 pleroma, 3 akhanas, and 2-5 theletos)
  treasure_type: none
special_abilities:
  Energy Touch (Su): A pleroma's touch deals 20d8 points of damage from positive or
    negative energy, depending upon which type of energy would harm the creature touched.
    A pleroma's touch never heals damage.
  Spells: A pleroma casts spells as a 20th-level cleric, but does not have access
    to domains. A pleroma can cast certain sorcerer/wizard spells as divine spells.
  Sphere of Creation (Su): Three times per day, the pleroma can manifest a 2-foot-diameter
    sphere of white energy that hovers above its left hand. By concentrating, the
    pleroma can control this sphere, causing it to fly slowly at a speed of 10 feet
    per round. The sphere can travel in any direction, but must remain within 300
    feet of the pleroma or it immediately dissipates. Wherever the sphere travels,
    it leaves behind a 5-foot-wide path of new matter, creating either new terrain
    (such as swamp, tundra, desert, or forest) or a 10-foot-square wall composed of
    a single natural substance (such as clay, wood, or stone). Any existing matter,
    either living or nonliving that comes in contact with the sphere must make a DC
    30 Fortitude save or be absorbed and incorporated into the new substance (only
    freedom, miracle, or wish can rescue creatures so trapped). Creatures that save
    are pushed to the nearest unoccupied location adjacent to the newly created substance.
    The sphere is highly unstable and only lasts 1d4 minutes before exploding with
    a blinding flash. All creatures within 30 feet of the flash must make a DC 30
    Fortitude save or be permanently blinded. The save DCs are Constitution-based.
  Sphere of Oblivion (Su): Three times per day, the pleroma can manifest a 2-foot-diameter
    sphere of complete and utter darkness that hovers above its right hand. The sphere
    is an empty void similar to a sphere of annihilation. Any matter (living or nonliving)
    that touches the sphere must succeed on a DC 30 Fortitude save or be sucked into
    the sphere and destroyed. Larger objects (such as ships or buildings) are destroyed
    at a rate of one 10-foot cube per round of contact with the sphere. By concentrating,
    the pleroma can control this sphere, causing it to fly slowly at a speed of 10
    feet per round. The sphere can travel in any direction, but must remain within
    300 feet of the pleroma or it immediately dissipates. The sphere is highly unstable
    and only lasts 1d4 minutes before harmlessly imploding upon itself. Alternatively,
    the pleroma may hurl the sphere as a ranged touch attack (with a 10-foot range
    increment) against a single creature. When thrown in this manner, the sphere implodes
    immediately after the attack is resolved. The save DCs are Constitution-based.
desc_long: |-
  The pleroma is the most powerful of all the aeons. As a manifestation of the opposing acts of creation and destruction, a pleroma exists in a state of flux, its very form shifting between creation and oblivion within the ebon folds of its vaporous cloak. One who gazes upon a pleroma could spend days studying the continual changes of its form, which most resemble the shifting of celestial bodies within the universe sped up to a pace at which the swirling of galaxies and the tumble of planets form a strange dance. 

  Pleromas view the concepts of creation and oblivion not so much as separate processes, but rather as two parts of a cyclical passage that everything in existence must explore. Pleromas guide this progression, ensuring everything remains balanced, such that whatever is created can be destroyed, and that nothing becomes so static that these two processes slow to a halt. For everything that attains a state of semi-permanence, there must be many more things that do not, or rather that cannot ever be reformed into a state of permanence. While pleromas believe in eternity, they understand that eternity is cyclical and infinity is something that repeats itself. Therefore, eternity and infinity are states that can be changed, or altered, if only slightly. Pleromas maintain such changes are necessary to keep the cosmos from becoming static and unbalanced, a state they refer to as apocalypse, or the end of everything. 

  Of all the aeons, pleromas possess the strongest connection to the entity or concept they refer to as Monad. All aeons believe themselves to be extensions of this entity, and while they act freely and independently of the entity, they always act within the constricts of its will or needs. This behavior is not so much a state of servitude as a symbiosis in which the actions of the pleromas are universally beneficial to both themselves and the entity they are part of. Pleromas describe Monad as the sentience of the multiverse, from which all things are created through the recycling of everything that ever existed. 

  Pleromas typically travel alone. Their arrival in a region almost always heralds some sort of dramatic change. They pay little mind to the wants and needs of other creatures, and remain entirely focused upon their primary task. They avoid conflicts of ethics, wars, and similar pursuits, save when manipulating such events would help to restore the balance between creation and oblivion. Should any be so foolish as to attempt to interfere with or sway their work, pleromas immediately retaliate by bringing all of their significant powers and devastating abilities to bear until the intervention is destroyed.

---

# Aeon, Pleroma
Within the shadows of this vaguely humanoid figure stir swirling colors and spheres, as if it encompassed all the night sky.

**Source** Bestiary 2 pg. 12
**XP** 307,200

N Large outsider (aeon, extraplanar)
**Init** +12; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/True Seeing|true seeing]]_; Perception +41

##### Defense

**AC** 36, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+6 deflection, +8 Dex, +1 _[[feats/Dodge|dodge]]_, +12 natural, –1 size)
**hp** 324 (24d10+192); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +24, **Ref** +18, **Will** +26
**Immune** cold, critical hits, poison; **Resist** electricity 10, fire 10; **SR** 31

##### Offense
**Speed** 0 ft., fly 60 ft. (perfect)
**Melee** touch +30 (20d8 energy)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** sphere of creation, sphere of _[[monsters/Oblivion|oblivion]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
At will—_[[spells/Create Food and Water|create food and water]]_, _[[spells/Mending|mending]]_, _[[spells/Rusting Grasp|rusting grasp]]_ (DC 21), _[[spells/Stone Shape|stone shape]]_, _[[spells/Wood Shape|wood shape]]_ (DC 19)
7/day—_[[spells/Fabricate|fabricate]]_, _[[spells/Plant Growth|plant growth]]_, _[[spells/Sculpt Sound|sculpt sound]]_, _[[spells/Shout|shout]]_ (DC 21)
5/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Daylight|daylight]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Major Creation|major creation]]_
3/day—_[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 25)
1/day—mage’s disjunction (DC 26), _[[spells/Wish|wish]]_ (DC 26)
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 20th; concentration +27)
9th—_[[spells/Astral Projection|astral projection]]_, _[[spells/Gate|gate]]_, _[[spells/Implosion|implosion]]_ (3, DC 29)
8th—_[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 28), _[[spells/Holy Aura|holy aura]]_ (DC 28), _[[spells/Shield of Law|shield of law]]_ (DC 28), _[[spells/Summon Monster VIII|summon monster VIII]]_, _[[spells/Unholy Aura|unholy aura]]_ (DC 28)
7th—_[[spells/Blasphemy|blasphemy]]_ (DC 27), _[[spells/Destruction|destruction]]_ (DC 27), _[[spells/Dictum|dictum]]_ (DC 27), _[[spells/Holy Word|holy word]]_ (DC 27), _[[spells/Word Of Chaos|word of chaos]]_ (DC 27)
6th—_[[spells/Banishment|banishment]]_ (DC 26), _[[spells/Forbiddance|forbiddance]]_ (DC 26), geas, _[[spells/Legend Lore|legend lore]]_, _[[spells/Repulsion|repulsion]]_ (DC 26), _[[spells/Veil|veil]]_ (DC 26)
5th—_[[spells/Contact Other Plane|contact other plane]]_, _[[spells/Dispel Chaos|dispel chaos]]_ (DC 25), _[[spells/Dispel Evil|dispel evil]]_ (DC 25), _[[spells/Dispel Good|dispel good]]_ (DC 25), _[[spells/Dispel Law|dispel law]]_ (DC 25), teleport
4th—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 24), _[[spells/Holy Smite|holy smite]]_ (DC 24), order’s _[[monsters/Wraith|wraith]]_ (DC 21), _[[spells/Restoration|restoration]]_, _[[spells/Scrying|scrying]]_ (DC 24), _[[spells/Unholy Blight|unholy blight]]_ (DC 24)
3rd—clairaudience/clairvoyance, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Magic Circle against Law|magic circle against law]]_, _[[spells/Suggestion|suggestion]]_ (DC 23)
2nd—_[[spells/Align Weapon|align weapon]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 22), _[[spells/Enthrall|enthrall]]_ (DC 22), _[[spells/Make Whole|make whole]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Undetectable Alignment|undetectable alignment]]_, _[[spells/Zone of Truth|zone of truth]]_ (DC 22)
1st—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/Identify|identify]]_, _[[spells/Magic Aura|magic aura]]_, _[[spells/True Strike|true strike]]_
0—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 24, **Dex** 27, **Con** 26, **Int** 26, **Wis** 31, **Cha** 25
**Base Atk** +24; **CMB** +32; **CMD** 57 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Appraise +30, Bluff +32, Fly +16, _[[spells/Heal|Heal]]_ +30, Intimidate +27, Knowledge (arcana) +47, Knowledge (dungeoneering) +44, Knowledge (engineering) +44, Knowledge (nature) +47, Knowledge (planes) +47, Knowledge (religion) +47, Perception +41, Sense Motive +39, Spellcraft +30, Stealth +27, Use Magic Device +27
**Languages** envisaging
**SQ** extension of all, void form

##### Ecology

**Environment** any (Outer Planes)
**Organization** solitary or tribunal (1 pleroma, 3 akhanas, and 2–5 theletos)
**Treasure** none

### Special Abilities

**Energy Touch (Su)** A pleroma’s touch deals 20d8 points of damage from positive or negative energy, depending upon which type of energy would _[[spells/Harm|harm]]_ the creature touched. A pleroma’s touch never heals damage.
**Spells **A pleroma casts spells as a 20th-level _cleric_, but does not have access to domains. A pleroma can cast certain sorcerer/wizard spells as divine spells.
**Sphere of Creation (Su)** Three times per day, the pleroma can manifest a 2-foot-diameter sphere of white energy that hovers above its left hand. By concentrating, the pleroma can control this sphere, causing it to fly slowly at a speed of 10 feet per round. The sphere can travel in any direction, but must remain within 300 feet of the pleroma or it immediately dissipates. Wherever the sphere travels, it leaves behind a 5-foot-wide path of new matter, creating either new terrain (such as swamp, tundra, desert, or forest) or a 10-foot-square wall composed of a single natural substance (such as _[[items/Mundane/Clay|clay]]_, wood, or stone). Any existing matter, either living or nonliving that comes in contact with the sphere must make a DC 30 Fortitude save or be absorbed and incorporated into the new substance (only _[[spells/Freedom|freedom]]_, _[[spells/Miracle|miracle]]_, or _wish_ can rescue creatures so trapped). Creatures that save are pushed to the nearest unoccupied location adjacent to the newly created substance. The sphere is highly unstable and only lasts 1d4 minutes before exploding with a _[[feats/Blinding Flash|blinding flash]]_. All creatures within 30 feet of the flash must make a DC 30 Fortitude save or be permanently _[[conditions/Blinded|blinded]]_. The save DCs are Constitution-based.
**Sphere of _Oblivion_ (Su)** Three times per day, the pleroma can manifest a 2-foot-diameter sphere of complete and utter _[[spells/Darkness|darkness]]_ that hovers above its right hand. The sphere is an empty void similar to a _[[items/Wondrous Item/Sphere of Annihilation|sphere of annihilation]]_. Any matter (living or nonliving) that touches the sphere must succeed on a DC 30 Fortitude save or be sucked into the sphere and destroyed. Larger objects (such as ships or buildings) are destroyed at a rate of one 10-foot cube per round of contact with the sphere. By concentrating, the pleroma can control this sphere, causing it to fly slowly at a speed of 10 feet per round. The sphere can travel in any direction, but must remain within 300 feet of the pleroma or it immediately dissipates. The sphere is highly unstable and only lasts 1d4 minutes before harmlessly imploding upon itself. Alternatively, the pleroma may hurl the sphere as a ranged touch attack (with a 10-foot range increment) against a single creature. When thrown in this manner, the sphere implodes immediately after the attack is resolved. The save DCs are Constitution-based.

##### Description

The pleroma is the most powerful of all the aeons. As a manifestation of the opposing acts of creation and _destruction_, a pleroma exists in a state of flux, its very form shifting between creation and _oblivion_ within the ebon folds of its vaporous cloak. One who gazes upon a pleroma could spend days studying the continual changes of its form, which most resemble the shifting of celestial bodies within the universe sped up to a pace at which the swirling of galaxies and the tumble of planets form a strange dance.

Pleromas view the concepts of creation and _oblivion_ not so much as separate processes, but rather as two parts of a cyclical passage that everything in existence must explore. Pleromas guide this progression, ensuring everything remains _[[items/Armor Magic Abilities/Balanced|balanced]]_, such that whatever is created can be destroyed, and that nothing becomes so static that these two processes _[[spells/Slow|slow]]_ to a halt. For everything that attains a state of semi-permanence, there must be many more things that do not, or rather that cannot ever be reformed into a state of permanence. While pleromas believe in eternity, they understand that eternity is cyclical and infinity is something that repeats itself. Therefore, eternity and infinity are states that can be changed, or altered, if only slightly. Pleromas maintain such changes are necessary to keep the cosmos from becoming static and unbalanced, a state they refer to as apocalypse, or the end of everything.

Of all the aeons, pleromas possess the strongest connection to the entity or concept they refer to as Monad. All aeons believe themselves to be extensions of this entity, and while they act freely and independently of the entity, they always act within the constricts of its will or needs. This behavior is not so much a state of servitude as a symbiosis in which the actions of the pleromas are universally beneficial to both themselves and the entity they are part of. Pleromas describe Monad as the sentience of the multiverse, from which all things are created through the recycling of everything that ever existed.

Pleromas typically travel alone. Their arrival in a region almost always heralds some sort of dramatic change. They pay little mind to the wants and needs of other creatures, and remain entirely focused upon their primary task. They avoid conflicts of ethics, wars, and similar pursuits, save when manipulating such events would help to restore the balance between creation and _oblivion_. Should any be so foolish as to attempt to interfere with or sway their work, pleromas immediately retaliate by bringing all of their significant powers and devastating abilities to bear until the intervention is destroyed.