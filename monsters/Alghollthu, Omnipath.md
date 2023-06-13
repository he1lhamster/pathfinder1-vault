---
cssclass: [monsters]
title1: Alghollthu, Omnipath
desc_short: This monstrous eel-like creature has jaws within jaws, each bearing transparent,
  glasslike teeth.
title2: Omnipath
CR: 18
sources:
- name: Occult Bestiary
  page: 38
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
- name: Bestiary 6
  page: 204
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 153600
alignment: LE
size: Gargantuan
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 13
senses:
  darkvision: 60
AC:
  AC: 33
  touch: 15
  flat_footed: 24
  components:
    armor: 4
    dex: 9
    natural: 14
    size: -4
HP:
  HP: 300
  long: 24d8+192
  fast_healing: 10
saves:
  fort: 18
  ref: 19
  will: 19
immunities:
- electricity
- mind-affecting effects
resistances:
  cold: 20
SR: 29
speeds:
  base: 15
  swim: 100
attacks:
  melee:
  - - text: triple-jawed bite +26 (3d6+11 plus slime/19-20)
      entries:
      - - damage: 3d6+11
          crit_range: 19-20
        - effect: slime
      attack: triple-jawed bite
      bonus:
      - 26
    - text: tail slap +23 (3d6+5 plus slime)
      entries:
      - - damage: 3d6+5
        - effect: slime
      attack: tail slap
      bonus:
      - 23
  special:
  - mucus cloud
  - slime
  - thought barrage
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: dominate person
    source: default
    freq: At will
    DC: 22
  - name: arcane eye
    source: default
    freq: 3/day
  - name: dominate monster
    source: default
    freq: 3/day
    DC: 26
  - name: geas/quest
    source: default
    freq: 3/day
    DC: 23
  - name: mind fog
    source: default
    freq: 3/day
    DC: 22
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 22
  - name: astral projection
    source: default
    freq: 1/day
  - name: veil
    source: default
    freq: 1/day
    DC: 23
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - superscripts:
    - OA
    name: ectoplasmic eruption
    source: Psychic
    level: 7
    DC: 24
  - superscripts:
    - OA
    name: psychic crush III
    source: Psychic
    level: 7
    DC: 24
  - superscripts:
    - OA
    name: incorporeal chains
    source: Psychic
    level: 6
  - superscripts:
    - OA
    name: mind thrust VI
    source: Psychic
    level: 6
    DC: 23
  - superscripts:
    - OA
    name: primal regression
    source: Psychic
    level: 6
    DC: 23
  - superscripts:
    - OA
    name: etheric shards
    source: Psychic
    level: 5
    DC: 22
  - superscripts:
    - OA
    name: explode head
    source: Psychic
    level: 5
    DC: 22
  - superscripts:
    - OA
    name: mind swap
    source: Psychic
    level: 5
    DC: 22
  - superscripts:
    - OA
    name: possession
    source: Psychic
    level: 5
    DC: 22
  - superscripts:
    - OA
    name: condensed ether
    source: Psychic
    level: 4
  - superscripts:
    - OA
    name: mindwipe
    source: Psychic
    level: 4
    DC: 21
  - superscripts:
    - OA
    name: riding possession
    source: Psychic
    level: 4
    DC: 21
  - name: stoneskin
    source: Psychic
    level: 4
  - superscripts:
    - OA
    name: babble
    source: Psychic
    level: 3
    DC: 20
  - superscripts:
    - OA
    name: catatonia
    source: Psychic
    level: 3
  - name: displacement
    source: Psychic
    level: 3
  - superscripts:
    - OA
    name: synesthesia
    source: Psychic
    level: 3
    DC: 20
  - superscripts:
    - OA
    name: aversion
    source: Psychic
    level: 2
    DC: 19
  - name: invisibility
    source: Psychic
    level: 2
  - superscripts:
    - OA
    name: paranoia
    source: Psychic
    level: 2
    DC: 19
  - name: resist energy
    source: Psychic
    level: 2
  - name: touch of idiocy
    source: Psychic
    level: 2
  - superscripts:
    - OA
    name: deja vu
    source: Psychic
    level: 1
  - superscripts:
    - OA
    name: psychic reading
    source: Psychic
    level: 1
  - name: shield
    source: Psychic
    level: 1
  - superscripts:
    - OA
    name: thought echo
    source: Psychic
    level: 1
  - name: true strike
    source: Psychic
    level: 1
  - name: arcane mark
    source: Psychic
    level: 0
  - name: bleed
    source: Psychic
    level: 0
    DC: 17
  - name: detect magic
    source: Psychic
    level: 0
  - superscripts:
    - OA
    name: grave words
    source: Psychic
    level: 0
  - name: mage hand
    source: Psychic
    level: 0
  - name: open/close
    source: Psychic
    level: 0
  - name: prestidigitation
    source: Psychic
    level: 0
  - name: read magic
    source: Psychic
    level: 0
  - superscripts:
    - OA
    name: telekinetic projectile
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 32
  DEX: 28
  CON: 27
  INT: 25
  WIS: 21
  CHA: 24
BAB: 18
CMB: 33
CMD: 52
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Great Fortitude
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (bite)
- superscripts:
  - OA
  name: Hidden Presence
- superscripts:
  - OA
  name: Intrusive Presence
- superscripts:
  - OA
  name: Manipulative Presence
skills:
  Bluff: 25
  Diplomacy: 23
  Disguise: 25
  Intimidate: 25
  Knowledge (arcana): 25
  Knowledge (dungeoneering): 25
  Knowledge (engineering): 25
  Knowledge (geography): 25
  Knowledge (history): 25
  Knowledge (local): 25
  Knowledge (nature): 25
  Knowledge (nobility): 25
  Knowledge (planes): 25
  Knowledge (religion): 25
  Perception: 30
  Sense Motive: 24
  Spellcraft: 35
  Stealth: 24
  Swim: 28
  Use Magic Device: 30
languages:
- Aboleth
- Aklo
- Aquan
- Azlanti
- Common
- Undercommon
- telepathy 300 ft.
- tongues
special_qualities:
- servant of the mesh
- telepathic mesh
- vast knowledge
ecology:
  environment: any water
  organization: solitary or mesh (1 plus 2-48 aboleths, veiled masters, and other
    dominated creatures)
  treasure_type: double
special_abilities:
  Mucus Cloud (Ex): While underwater, an omnipath exudes a cloud of transparent slime
    20 feet from itself in all directions. All creatures in this area must succeed
    at a DC 30 Fortitude saving throw each round or lose their ability to breathe
    air (but gain the ability to breathe water) for 24 hours. Renewed contact with
    the mucus cloud and failing another saving throw extends the effect for another
    24 hours. An omnipath can suppress or reactivate this ability as a swift action.
    The save DC is Constitution-based.
  Servant of the Mesh (Su): Any creature subjected to both an omnipath's mucus cloud
    and slime attacks that fails its saving throws against both attacks begins to
    transform into a creature better suited to serving as part of the omnipath's telepathic
    mesh. The creature takes a -6 penalty on Will saving throws to resist domination
    by the omnipath and on saving throws to resist becoming part of the telepathic
    mesh.
  Slime (Ex): A creature hit by any of an omnipath's natural attacks must succeed
    at a DC 30 Fortitude saving throw or have its skin and flesh transform into a
    clear, slimy membrane over the course of 1d4 rounds. The creature's new flesh
    is soft and tender, reducing its Constitution score by 4 as long as the condition
    persists. If the creature's flesh isn't kept moist, it dries quickly and the victim
    takes 1d12 points of damage every 10 minutes. Remove disease and similar effects
    can restore an afflicted creature to normal, but immunity to disease offers no
    protection from this attack. The save DC is Constitution-based.
  Spells: An omnipath can cast spells as a 15th-level psychic (Pathfinder RPG Occult
    Adventures 60).
  Telepathic Mesh (Su): |-
    An omnipath can form telepathic connections between a select group of creatures. This ability functions only for creatures that are on the same plane as the omnipath. Only aboleths, veiled masters, and creatures dominated by an aboleth or a veiled master can be added to the telepathic mesh. As a standard action, an omnipath can add a number of creatures equal to twice its Hit Dice to its telepathic mesh. Creatures added to the telepathic mesh can attempt a DC 29 Will save; a successful save negates this effect. Aboleths and veiled masters must be within 30 feet of an omnipath to initially be included within the telepathic mesh, but targets dominated by those creatures later can be added to the telepathic mesh no matter the distance, so long as all parties are on the same plane. A creature that leaves the same plane as the omnipath is no longer considered to be part of the telepathic mesh and can attempt a new DC 29 Will saving throw upon returning to remain free from the telepathic mesh. As an immediate action, an omnipath can remove any creature from the telepathic mesh.

     An omnipath can communicate telepathically with all individual creatures in the telepathic mesh simultaneously. All creatures within the mesh are considered valid targets for all forms of possession employed by the omnipath. As long as at least two creatures in the telepathic mesh are within 12 miles of each other, if one creature in the mesh is aware of a particular danger, all of the other creatures in the mesh are as well. No creature in the group is considered flanked or flat-footed unless all of them are.

     An omnipath can share the senses of up to six of the creatures in the telepathic mesh. It can stop sharing the senses of one target and switch to another's senses as a standard action. The save DC is Intelligence-based.
  Thought Barrage (Su): As a standard action, an omnipath can fire three rays of shimmering
    blue-white energy from the glowing balls of light on its tail as a ranged touch
    attack with a range of 300 feet (no range increment). Any creature struck must
    succeed at a DC 29 Will saving throw or be stunned for 1 round. The save DC is
    Charisma-based.
  Triple-Jawed Bite (Ex): An omnipath has three jaws nestled within one another. An
    omnipath can make a bite attack as a standard action. If that attack hits, the
    omnipath can make a second bite attack as a free action. If the second bite attack
    hits, the target must succeed at a DC 30 Will saving throw or be shaken for 1d4
    rounds, and the omnipath can make a third bite attack as a free action. If the
    third bite attack is successful, the target must succeed at a DC 30 Fortitude
    saving throw or be staggered for 1d4 rounds. The save DCs are Constitution-based.
  Vast Knowledge (Ex): Gleaning countless pieces of information from a vast network
    of active minds it can access at any time, an omnipath treats all Knowledge skills
    as class skills. In addition, it gains a +4 racial bonus on Intelligence-, Wisdom-,
    and Charisma-based checks when using skills in which it has ranks.
desc_long: |-
  Hidden away in secret lairs, omnipaths serve as information hubs between othagu (aboleths, veiled masters, and other such creatures). Using their special ability to establish a network of minds throughout the Darklands and Golarion's oceans, omnipaths allow veiled masters and aboleths-as well as those they mentally control-to orchestrate their nefarious plans. Omnipaths possess a keen intellect and recall everything they (and those within the mesh) experience, leading to a wealth of varied information that is shared between omnipaths as a sort of experience library. Omnipaths also serve as an alarm system for the veiled masters they serve, for each omnipath can communicate with all creatures in its telepathic mesh simultaneously. An omnipath can use the senses of all creatures within its mesh, and any creature that would harm one of the creatures in the mesh immediately becomes known to all other beings the omnipath is mentally linked to.

  Very few surface dwellers have ever encountered an omnipath, but through the use of their possession abilities, many omnipaths have walked in the light of the surface world, riding within their victims. The omnipaths' library of experiences provides them insight into the cultures and practices of the surface, allowing them to feign the expected responses on behalf of their dominated victims. In some cases, friends and family of a victim have failed to recognize that something was amiss with a victim's behavior for years, and sometimes the deception is never uncovered, giving the omnipaths-and those they serve-spies within the surface world that serve until their deaths.

  Omnipaths possess a strange mindset, inscrutable to sane minds, though they are an orderly and meticulous race. While aboleths and veiled masters are skilled spellcasters with powerful illusion and enchantment spell-like abilities, omnipaths' primary powers are in their minds, and they pursue psychic magic. Omnipaths have a strange obsession with eyes and consider them a delicacy.

  An omnipath is 25 feet long and weighs 2 tons.

---

# Alghollthu, Omnipath
This monstrous eel-like creature has jaws within jaws, each bearing transparent, glasslike teeth.
**Source** Occult Bestiary pg. 38, Bestiary 6 pg. 204
**XP** 153,600

LE Gargantuan aberration (aquatic)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +30

##### Defense

**AC** 33, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +9 Dex, +14 natural, –4 size)
**hp** 300 (24d8+192); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +18, **Ref** +19, **Will** +19
**Immune** electricity, mind-affecting effects; **Resist** cold 20; **SR** 29

##### Offense
**Speed** 15 ft., swim 100 ft.
**Melee** triple-jawed bite +26 (3d6+11 plus slime/19–20), tail slap +23 (3d6+5 plus slime)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** mucus cloud, slime, thought barrage
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Mage Armor|mage armor]]_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Dominate Person|dominate person]]_ (DC 22)
3/day—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Dominate Monster|dominate monster]]_ (DC 26), geas/quest (DC 23), _[[spells/Mind Fog|mind fog]]_ (DC 22), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 22)
1/day—_[[spells/Astral Projection|astral projection]]_, _[[spells/Veil|veil]]_ (DC 23)
**_[[classes/Psychic|Psychic]]_ Spells Known **(CL 15th; concentration +22)
7th (5/day)—_[[spells/Ectoplasmic Eruption|ectoplasmic eruption]]_ (DC 24), _[[spells/Psychic Crush III|psychic crush III]]_ (DC 24)
6th (7/day)—_[[spells/Incorporeal Chains|incorporeal chains]]_, _[[spells/Mind Thrust VI|mind thrust VI]]_ (DC 23), _[[spells/Primal Regression|primal regression]]_ (DC 23)
5th (7/day)—_[[spells/Etheric Shards|etheric shards]]_ (DC 22), _[[spells/Explode Head|explode head]]_ (DC 22), _[[spells/Mind Swap|mind swap]]_ (DC 22), _[[spells/Possession|possession]]_ (DC 22)
4th (7/day)—_[[spells/Condensed Ether|condensed ether]]_, _[[spells/Mindwipe|mindwipe]]_ (DC 21), _[[spells/Riding Possession|riding possession]]_ (DC 21), _[[spells/Stoneskin|stoneskin]]_
3rd (8/day)—_[[spells/Babble|babble]]_ (DC 20), _[[spells/Catatonia|catatonia]]_, _[[spells/Displacement|displacement]]_, _[[spells/Synesthesia|synesthesia]]_ (DC 20)
2nd (8/day)—_[[spells/Aversion|aversion]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Paranoia|paranoia]]_ (DC 19), _[[spells/Resist Energy|resist energy]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (8)—_[[spells/Deja Vu|deja vu]]_, _[[spells/Psychic Reading|psychic reading]]_, _[[spells/Shield|shield]]_, _[[spells/Thought Echo|thought echo]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 17), _detect magic_, _[[spells/Grave Words|grave words]]_, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Telekinetic Projectile|telekinetic projectile]]_

##### Statistics
**Str** 32, **Dex** 28, **Con** 27, **Int** 25, **Wis** 21, **Cha** 24
**Base Atk** +18; **CMB** +33; **CMD** 52
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _[[spells/Hidden Presence|Hidden Presence]]_, _[[feats/Intrusive Presence|Intrusive Presence]]_, _[[feats/Manipulative Presence|Manipulative Presence]]_
**Skills** Bluff +25, Diplomacy +23, Disguise +25, Intimidate +25, Knowledge (arcana, dungeoneering, engineering, geography, history, local, nature, nobility, planes, religion) +25, Perception +30, Sense Motive +24, Spellcraft +35, Stealth +24, Swim +28, Use Magic Device +30
**Languages** Aboleth, Aklo, Aquan, Azlanti, Common, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.; _tongues_
**SQ** servant of the mesh, telepathic mesh, vast knowledge

##### Ecology

**Environment** any water
**Organization** solitary or mesh (1 plus 2–48 aboleths, veiled masters, and other dominated creatures)
**Treasure** double

### Special Abilities

**Mucus Cloud (Ex)** While _[[items/Weapon Magic Abilities/Underwater|underwater]]_, an omnipath exudes a cloud of transparent slime 20 feet from itself in all directions. All creatures in this area must succeed at a DC 30 Fortitude saving throw each round or lose their ability to breathe air (but gain the ability to breathe water) for 24 hours. Renewed contact with the mucus cloud and failing another saving throw extends the effect for another 24 hours. An omnipath can suppress or reactivate this ability as a swift action. The save DC is Constitution-based.
**Servant of the Mesh (Su)** Any creature subjected to both an omnipath’s mucus cloud and slime attacks that fails its saving throws against both attacks begins to transform into a creature better suited to serving as part of the omnipath’s telepathic mesh. The creature takes a –6 penalty on Will saving throws to resist domination by the omnipath and on saving throws to resist becoming part of the telepathic mesh.
**Slime (Ex)** A creature hit by any of an omnipath’s _[[universal monster rules/Natural Attacks|natural attacks]]_ must succeed at a DC 30 Fortitude saving throw or have its skin and flesh transform into a clear, slimy membrane over the course of 1d4 rounds. The creature’s new flesh is soft and tender, reducing its Constitution score by 4 as long as the condition persists. If the creature’s flesh isn’t kept moist, it dries quickly and the victim takes 1d12 points of damage every 10 minutes. _[[spells/Remove Disease|Remove disease]]_ and similar effects can restore an afflicted creature to normal, but _[[universal monster rules/Immunity|immunity]]_ to disease offers no protection from this attack. The save DC is Constitution-based.
**Spells** An omnipath can cast spells as a 15th-level _psychic_ (Pathfinder RPG Occult Adventures 60).

**Telepathic Mesh (Su)** An omnipath can form telepathic connections between a select group of creatures. This ability functions only for creatures that are on the same plane as the omnipath. Only aboleths, veiled masters, and creatures dominated by an aboleth or a veiled master can be added to the telepathic mesh. As a standard action, an omnipath can add a number of creatures equal to twice its Hit Dice to its telepathic mesh. Creatures added to the telepathic mesh can attempt a DC 29 Will save; a successful save negates this effect. Aboleths and veiled masters must be within 30 feet of an omnipath to initially be included within the telepathic mesh, but targets dominated by those creatures later can be added to the telepathic mesh no matter the distance, so long as all parties are on the same plane. A creature that leaves the same plane as the omnipath is no longer considered to be part of the telepathic mesh and can attempt a new DC 29 Will saving throw upon returning to remain free from the telepathic mesh. As an immediate action, an omnipath can remove any creature from the telepathic mesh.

An omnipath can communicate telepathically with all individual creatures in the telepathic mesh simultaneously. All creatures within the mesh are considered valid targets for all forms of _possession_ employed by the omnipath. As long as at least two creatures in the telepathic mesh are within 12 miles of each other, if one creature in the mesh is aware of a particular danger, all of the other creatures in the mesh are as well. No creature in the group is considered flanked or _flat-footed_ unless all of them are.

An omnipath can share the senses of up to six of the creatures in the telepathic mesh. It can stop sharing the senses of one target and switch to another’s senses as a standard action. The save DC is Intelligence-based.

**Thought Barrage (Su)** As a standard action, an omnipath can fire three rays of shimmering blue-white energy from the glowing balls of light on its tail as a ranged touch attack with a range of 300 feet (no range increment). Any creature struck must succeed at a DC 29 Will saving throw or be _[[conditions/Stunned|stunned]]_ for 1 round. The save DC is Charisma-based.

**Triple-Jawed Bite (Ex)** An omnipath has three jaws nestled within one another. An omnipath can make a bite attack as a standard action. If that attack hits, the omnipath can make a second bite attack as a free action. If the second bite attack hits, the target must succeed at a DC 30 Will saving throw or be _[[conditions/Shaken|shaken]]_ for 1d4 rounds, and the omnipath can make a third bite attack as a free action. If the third bite attack is successful, the target must succeed at a DC 30 Fortitude saving throw or be _[[conditions/Staggered|staggered]]_ for 1d4 rounds. The save DCs are Constitution-based.

**Vast Knowledge (Ex)** Gleaning countless pieces of information from a vast network of active minds it can access at any time, an omnipath treats all Knowledge skills as class skills. In addition, it gains a +4 racial bonus on Intelligence-, Wisdom-, and Charisma-based checks when using skills in which it has ranks.

##### Description

Hidden away in secret lairs, omnipaths serve as information hubs between othagu (aboleths, veiled masters, and other such creatures). Using their special ability to establish a network of minds throughout the Darklands and Golarion’s oceans, omnipaths allow veiled masters and aboleths—as well as those they mentally control—to orchestrate their nefarious plans. Omnipaths possess a _[[items/Weapon Magic Abilities/Keen|keen]]_ intellect and recall everything they (and those within the mesh) experience, leading to a wealth of varied information that is shared between omnipaths as a sort of experience library. Omnipaths also serve as an _[[spells/Alarm|alarm]]_ system for the veiled masters they serve, for each omnipath can communicate with all creatures in its telepathic mesh simultaneously. An omnipath can use the senses of all creatures within its mesh, and any creature that would _[[spells/Harm|harm]]_ one of the creatures in the mesh immediately becomes known to all other beings the omnipath is mentally linked to.

Very few surface dwellers have ever encountered an omnipath, but through the use of their _possession_ abilities, many omnipaths have walked in the light of the surface world, riding within their victims. The omnipaths’ library of experiences provides them insight into the cultures and practices of the surface, allowing them to feign the expected responses on behalf of their dominated victims. In some cases, friends and family of a victim have failed to recognize that something was amiss with a victim’s behavior for years, and sometimes the deception is never uncovered, giving the omnipaths—and those they serve—spies within the surface world that serve until their deaths.

Omnipaths possess a strange mindset, inscrutable to sane minds, though they are an orderly and meticulous race. While aboleths and veiled masters are skilled spellcasters with powerful illusion and enchantment _spell-like abilities_, omnipaths’ primary powers are in their minds, and they pursue _[[universal monster rules/Psychic Magic|psychic magic]]_. Omnipaths have a strange obsession with eyes and consider them a delicacy.

An omnipath is 25 feet long and weighs 2 tons.