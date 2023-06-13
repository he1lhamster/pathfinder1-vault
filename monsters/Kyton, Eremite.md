---
cssclass: [monsters]
title1: Kyton, Eremite
desc_short: This blood-soaked humanoid is festooned with razored shards of metal.
  Skeletal wings protrude from its bleeding shoulders.
title2: Eremite
CR: 20
sources:
- name: Bestiary 3
  page: 172
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 307200
alignment: LE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 12
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 38
  touch: 19
  flat_footed: 29
  components:
    dex: 8
    dodge: 1
    natural: 19
HP:
  HP: 310
  long: 20d10+200
  regeneration: 15
  regeneration_weakness: good weapons and spells, silver weapons
saves:
  fort: 22
  ref: 16
  will: 19
DR:
- amount: 15
  weakness: good and silver
immunities:
- cold
- fear effects
- nonlethal damage
- pain
SR: 31
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +30 (2d6+10 plus pain)
      entries:
      - - damage: 2d6+10
        - effect: pain
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d6+10/19-20 plus grab and pain)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
        - effect: grab
        - effect: pain
      count: 2
      attack: claws
      bonus:
      - 30
    - text: 2 wings +25 (1d8+5 plus pain)
      entries:
      - - damage: 1d8+5
        - effect: pain
      count: 2
      attack: wings
      bonus:
      - 25
  special:
  - evisceration
  - unnerving gaze (30 ft., DC 31)
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: inflict critical wounds
    source: default
    freq: At will
    DC: 25
  - name: shadow walk
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 26
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 27
  - name: dimensional lock
    source: default
    freq: 3/day
  - name: forcecage
    source: default
    freq: 3/day
    DC: 28
  - name: greater shadow evocation
    source: default
    freq: 3/day
    DC: 29
  - name: heal
    source: default
    freq: 3/day
    other: self only
  - name: insanity
    source: default
    freq: 3/day
    DC: 28
  - name: mass inflict critical wounds
    source: default
    freq: 3/day
    DC: 29
  - name: plane shift
    source: default
    freq: 3/day
    DC: 28
  - name: shades
    source: default
    freq: 3/day
    DC: 30
  - name: symbol of pain
    source: default
    freq: 3/day
    DC: 26
  - name: wall of force
    source: default
    freq: 3/day
  - name: binding
    source: default
    freq: 1/day
    DC: 29
  - name: trap the soul
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 20
    concentration: 31
ability_scores:
  STR: 30
  DEX: 27
  CON: 30
  INT: 22
  WIS: 21
  CHA: 33
BAB: 20
CMB: 30
CMB_other: +34 grapple
CMD: 49
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Skill Focus (Perception)
- name: Spell Penetration
skills:
  Bluff: 34
  Diplomacy: 34
  Fly: 12
  Heal: 28
  Intimidate: 34
  Knowledge (arcana): 16
  Knowledge (dungeoneering): 16
  Knowledge (nature): 16
  Knowledge (planes): 29
  Knowledge (religion): 16
  Perception: 34
  Sense Motive: 28
  Spellcraft: 29
  Stealth: 31
  Use Magic Device: 31
languages:
- Common
- Infernal
- telepathy 100 ft.
special_qualities:
- graft flesh
- shadow traveler
ecology:
  environment: any (Plane of Shadow)
  organization: solitary, pair, or cell (3-5)
  treasure_type: double
special_abilities:
  Immune to Pain (Su): An eremite is immune to nonlethal damage, as well as to all
    magical effects associated with extreme pain, such as a symbol of pain, another
    eremite's pain attack, or similar effects at the GM's discretion.
  Evisceration (Ex): When an eremite grapples a foe, it can quickly eviscerate or
    otherwise surgically alter its victim by excising a bit of flesh or a part of
    an internal organ as a swift action, causing the victim to take 1d8 points of
    ability drain-the exact ability score drained is chosen by the eremite. The victim
    can resist this effect with a DC 28 Fortitude save. The save DC is Dexterity-based.
  Graft Flesh (Su): Once per day, an eremite may graft any bit of flesh or bone harvested
    via its evisceration ability within the previous hour to its own body as a full-round
    action that provokes an attack of opportunity. Doing so grants the eremite the
    effects of a heal and a greater restoration spell (caster level 20th).
  Pain (Su): Any creature struck by an eremite's natural attacks must make a DC 30
    Fortitude save or become staggered for 1 round from the pain. As long as a creature
    is staggered by this effect, it takes a -4 penalty on all saving throws made to
    resist the eremite's spell-like and extraordinary abilities. The save DC is Constitution-based.
  Shadow Traveler (Ex): When an eremite uses plane shift to travel to the Plane of
    Shadow, it arrives at its intended destination with complete accuracy. When an
    eremite uses shadow walk, it moves at a rate of 100 miles per hour.
  Unnerving Gaze (Ex): A creature that succumbs to an eremite's unnerving gaze becomes
    paralyzed with fear for 1d4 rounds as it finds itself almost longing to submit
    its flesh to the kyton. At the end of any round it remains paralyzed in this way,
    the victim must make a DC 31 Will save or take 1d4 points of Wisdom drain from
    encroaching madness. This is a mind-affecting fear effect.
desc_long: |-
  Eremites are among the eldest and most mutilated of kytons, having inflicted such massive damage to themselves that they feel little pain and no fear. The typical eremite is completely covered in blood-caked bandages, tattered cords of black leather, and thousands of jagged shards of razor-sharp metal. These fragments are all that holds the creature's mutilated flesh together, yet they do so with a strength far greater than that granted by mortal flesh and bone.

  Rather than concentrating solely on physical or even spiritual alterations, eremites seek to blur the very lines around being, physicality, and individuality. They desire only the most powerful beings to augment themselves with, traveling across vast swaths of the Material Plane in search of the most promising additions to their bodily collection and harvesting only the finest parts-the ripest spleen, the most alluring veins, the most succulent eyes. When an eremite encounters a creature that possess a so-called “perfect part,” the powerful kyton seeks to capture that creature alive so that it can study how that perfect part functions as part of the creature's physiology before it finally decides to surgically remove it and attach it to its own body-often in a way not quite in keeping with the part's original use. A gifted bard's tongue might, for example, be nailed to a kyton's palm or sewn into its heart, while the eyes of a beautiful queen might be stitched into the kyton's torso. To the eremite, these hideous changes and choices somehow enhance the perfection of the harvested part, while to others they merely enhance the horror that the creature represents.

  While eremites do hold an appreciation for inspection of their targets as well as introspection regarding their own powers and identity, their primary occupation is the understanding of pain and suffering, which they pursue by inflicting the most heinous cruelties upon their victims. An eremite seeks to deliver as much agony as possible to its victims after capturing them, allowing them to undergo extreme amounts of trauma before letting them perish. An eremite often rends its own flesh in the same manner as it does its victim's, so as to experience the pain alongside it.

  While pursuing a chosen victim, an eremite utilizes its supernatural abilities to distract and distress a given target before it captures and drags it back to the Plane of Shadow via plane shift. Bargaining with an eremite is not usually an option, though if a particularly powerful victim can offer an eremite advice or aid, or otherwise assist in harvesting an even more interesting catch, an eremite can sometimes be convinced to let the helpful victim escape. It's worth remembering, though, that kytons as a whole have little patience for the petty pursuits of honor and pride, seeing such feelings as traits that ultimately spell the end for baser creatures. The only thing that matters to an eremite is the testing of its boundaries as well as the boundaries of existence itself. Just because an eremite might be convinced to let someone go in trade for an opportunity for a greater catch doesn't mean that once that other target is secured the eremite will cease its attempts to capture and harvest its original target. One who manages to distract and subsequently escape an eremite is well-advised to spend the rest of his life on the run.

  A typical eremite stands approximately 7 feet tall and weighs about 200 pounds. While their general form is something of a humanoid shape, exact appearances can vary wildly between eremites as they harvest and graft particularly unusual pieces of flesh to their bodies from increasingly exotic victims.

---

# Kyton, Eremite
This blood-soaked humanoid is festooned with razored shards of metal. Skeletal wings protrude from its bleeding shoulders.
**Source** Bestiary 3 pg. 172
**XP** 307,200

LE Medium outsider (evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +34

##### Defense

**AC** 38, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+8 Dex, +1 _[[feats/Dodge|dodge]]_, +19 natural)
**hp** 310 (20d10+200); _[[universal monster rules/Regeneration|regeneration]]_ 15 (good weapons and spells, silver weapons)
**Fort** +22, **Ref** +16, **Will** +19
**DR** 15/good and silver; **Immune** cold, _[[universal monster rules/Fear|fear]]_ effects, nonlethal damage, pain; **SR** 31

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** bite +30 (2d6+10 plus pain), 2 claws +30 (2d6+10/19–20 plus _[[universal monster rules/Grab|grab]]_ and pain), 2 wings +25 (1d8+5 plus pain)
**Special Attacks** evisceration, unnerving _[[universal monster rules/Gaze|gaze]]_ (30 ft., DC 31)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +31)
Constant—_true seeing_
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 25), _[[spells/Shadow Walk|shadow walk]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 26)
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 27), _[[spells/Dimensional Lock|dimensional lock]]_, _[[spells/Forcecage|forcecage]]_ (DC 28), greater _[[spells/Shadow Evocation|shadow evocation]]_ (DC 29), _[[spells/Heal|heal]]_ (self only), _[[spells/Insanity|insanity]]_ (DC 28), mass _inflict critical wounds_ (DC 29), _[[spells/Plane Shift|plane shift]]_  (DC 28), _[[spells/Shades|shades]]_ (DC 30), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 26), _[[spells/Wall Of Force|wall of force]]_
1/day—_[[spells/Binding|binding]]_ (DC 29), _[[spells/Trap the Soul|trap the soul]]_ (DC 29)

##### Statistics
**Str** 30, **Dex** 27, **Con** 30, **Int** 22, **Wis** 21, **Cha** 33
**Base Atk** +20; **CMB** +30 (+34 grapple); **CMD** 49
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Bluff +34, Diplomacy +34, Fly +12, _Heal_ +28, Intimidate +34, Knowledge (arcana) +16, Knowledge (dungeoneering) +16, Knowledge (nature) +16, Knowledge (planes) +29, Knowledge (religion) +16, Perception +34, Sense Motive +28, Spellcraft +29, Stealth +31, Use Magic Device +31
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** graft flesh, _[[items/Armor Magic Abilities/Shadow|shadow]]_ traveler

##### Ecology

**Environment** any (Plane of _Shadow_)
**Organization** solitary, pair, or cell (3–5)
**Treasure** double

### Special Abilities

**Immune to Pain (Su)** An eremite is immune to nonlethal damage, as well as to all magical effects associated with extreme pain, such as a _symbol of pain_, another eremite’s pain attack, or similar effects at the GM’s discretion.

**Evisceration (Ex)** When an eremite grapples a foe, it can quickly eviscerate or otherwise surgically alter its victim by excising a bit of flesh or a part of an internal organ as a swift action, causing the victim to take 1d8 points of ability drain—the exact ability score drained is chosen by the eremite. The victim can resist this effect with a DC 28 Fortitude save. The save DC is Dexterity-based.

**Graft Flesh (Su)** Once per day, an eremite may graft any bit of flesh or bone harvested via its evisceration ability within the previous hour to its own body as a full-round action that provokes an attack of opportunity. Doing so grants the eremite the effects of a _heal_ and a greater _[[spells/Restoration|restoration]]_ spell (caster level 20th).

**Pain (Su)** Any creature struck by an eremite’s _[[universal monster rules/Natural Attacks|natural attacks]]_ must make a DC 30 Fortitude save or become _[[conditions/Staggered|staggered]]_ for 1 round from the pain. As long as a creature is _staggered_ by this effect, it takes a –4 penalty on all saving throws made to resist the eremite’s spell-like and extraordinary abilities. The save DC is Constitution-based.
**_Shadow_ Traveler (Ex)** When an eremite uses _plane shift_ to travel to the Plane of _Shadow_, it arrives at its intended destination with complete accuracy. When an eremite uses _shadow walk_, it moves at a rate of 100 miles per hour.

**Unnerving _Gaze_ (Ex)** A creature that succumbs to an eremite’s unnerving _gaze_ becomes _[[conditions/Paralyzed|paralyzed]]_ with _fear_ for 1d4 rounds as it finds itself almost longing to submit its flesh to the _kyton_. At the end of any round it remains _paralyzed_ in this way, the victim must make a DC 31 Will save or take 1d4 points of Wisdom drain from encroaching madness. This is a mind-affecting _fear_ effect.

##### Description

Eremites are among the eldest and most mutilated of kytons, having inflicted such massive damage to themselves that they feel little pain and no _fear_. The typical eremite is completely covered in blood-caked bandages, tattered cords of black leather, and thousands of jagged shards of razor-sharp metal. These fragments are all that holds the creature’s mutilated flesh together, yet they do so with a strength far greater than that granted by mortal flesh and bone.

Rather than concentrating solely on physical or even spiritual alterations, eremites seek to _[[spells/Blur|blur]]_ the very lines around being, physicality, and individuality. They desire only the most powerful beings to augment themselves with, traveling across vast swaths of the Material Plane in search of the most promising additions to their bodily collection and _[[items/Weapon Magic Abilities/Harvesting|harvesting]]_ only the finest parts—the ripest spleen, the most alluring veins, the most succulent eyes. When an eremite encounters a creature that possess a so-called “perfect part,” the powerful _kyton_ seeks to capture that creature alive so that it can study how that perfect part functions as part of the creature’s physiology before it finally decides to surgically remove it and _[[universal monster rules/Attach|attach]]_ it to its own body—often in a way not quite in keeping with the part’s original use. A gifted _[[classes/Bard|bard]]_’s tongue might, for example, be nailed to a _kyton_’s palm or sewn into its heart, while the eyes of a beautiful queen might be stitched into the _kyton_’s torso. To the eremite, these hideous changes and choices somehow enhance the perfection of the harvested part, while to others they merely enhance the horror that the creature represents.

While eremites do hold an appreciation for inspection of their targets as well as introspection regarding their own powers and identity, their primary occupation is the understanding of pain and suffering, which they pursue by inflicting the most heinous cruelties upon their victims. An eremite seeks to deliver as much agony as possible to its victims after capturing them, allowing them to undergo extreme amounts of trauma before letting them perish. An eremite often rends its own flesh in the same manner as it does its victim’s, so as to experience the pain alongside it.

While pursuing a chosen victim, an eremite utilizes its supernatural abilities to distract and distress a given target before it captures and drags it back to the Plane of _Shadow_ via _plane shift_. Bargaining with an eremite is not usually an option, though if a particularly powerful victim can offer an eremite advice or aid, or otherwise assist in _harvesting_ an even more interesting catch, an eremite can sometimes be convinced to let the helpful victim escape. It’s worth remembering, though, that kytons as a whole have little patience for the petty pursuits of honor and pride, seeing such feelings as traits that ultimately spell the end for baser creatures. The only thing that matters to an eremite is the testing of its boundaries as well as the boundaries of existence itself. Just because an eremite might be convinced to let someone go in trade for an opportunity for a greater catch doesn’t mean that once that other target is secured the eremite will cease its attempts to capture and harvest its original target. One who manages to distract and subsequently escape an eremite is well-advised to spend the rest of his life on the run.

A typical eremite stands approximately 7 feet tall and weighs about 200 pounds. While their general form is something of a humanoid shape, exact appearances can vary wildly between eremites as they harvest and graft particularly unusual pieces of flesh to their bodies from increasingly exotic victims.