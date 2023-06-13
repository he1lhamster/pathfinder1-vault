---
cssclass: [monsters]
title1: Blood Queen
desc_short: This hideous monstrosity looks like an enormous curled maggot, varicolored
  like deeply bruised flesh. Three flailing tentacles adorn each side of the thing's
  huge, pulsating mouth, and five more arch from its hindquarters.
title2: Blood Queen
CR: 23
sources:
- name: Isles of the Shackles
  page: 44
  link: http://paizo.com/products/btpy8qzx?Pathfinder-Campaign-Setting-Isles-of-the-Shackles
XP: 819200
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- native
initiative:
  bonus: 4
senses:
  blindsight: 120
  surrogate senses: true
AC:
  AC: 38
  touch: 6
  flat_footed: 38
  components:
    natural: 32
    size: -4
HP:
  HP: 471
  long: 23d10+345
  regeneration: 10
  regeneration_weakness: good
saves:
  fort: 28
  ref: 9
  will: 24
DR:
- amount: 15
  weakness: epic and lawful
immunities:
- disease
- electricity
- mindaffecting effects
- poison
- sonic
SR: 34
speeds:
  base: 10
attacks:
  melee:
  - - text: bite +29 (2d6+10)
      entries:
      - - damage: 2d6+10
      attack: bite
      bonus:
      - 29
    - text: 5 stings +29 (2d6+10/19-20 plus 2d6 electricity)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
        - damage: 2d6
          type: electricity
      count: 5
      attack: stings
      bonus:
      - 29
    - text: 6 tentacles +24 (2d8+5/19-20 plus grab)
      entries:
      - - damage: 2d8+5
          crit_range: 19-20
        - effect: grab
      count: 6
      attack: tentacles
      bonus:
      - 24
  special:
  - horrifying bellow
  - swallow whole (15d6 acid damage, AC 26, 47 hp)
  - unholy gestation
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: cacophonous call
    source: default
    freq: 5/day
    DC: 25
  - name: deeper darkness
    source: default
    freq: 5/day
  - name: dispel good
    source: default
    freq: 5/day
    DC: 28
  - name: inflict critical wounds
    source: default
    freq: 5/day
    DC: 27
  - name: greater command
    source: default
    freq: 3/day
    DC: 28
  - name: mass suffocation
    source: default
    freq: 1/day
    DC: 32
  sources:
  - name: default
    CL: 23
    concentration: 36
ability_scores:
  STR: 30
  DEX: 11
  CON: 40
  INT: 20
  WIS: 29
  CHA: 37
BAB: 23
CMB: 37
CMB_other: +41 grapple
CMD: 47
feats:
- name: Alertness
- name: Awesome Blow
- name: Bleeding Critical
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (sting)
- name: Improved Critical (tentacles)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 39
  Diplomacy: 39
  Heal: 32
  Intimidate: 39
  Knowledge (arcana): 28
  Knowledge (history): 28
  Knowledge (planes): 31
  Knowledge (religion): 31
  Perception: 39
  Sense Motive: 39
  Spellcraft: 31
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Kuru
- Undercommon
- telepathy 100 ft.
special_qualities:
- blood link
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
special_abilities:
  Blood Link (Su): Three times per day as a standard action, the Blood Queen may psychically
    link to up to 23 Hit Dice of kuru within 100 feet of either itself or one of its
    kuru surrogates; it may choose which specific kuru it would like to affect with
    this ability, but HD that are not sufficient to affect a creature are wasted.
    Any kuru linked to in this way must succeed at a DC 28 Will save or be forced
    to carry out the Blood Queen's telepathic commands to the best of its ability.
    In addition, a linked kuru gains a +4 morale bonus to Strength and Constitution
    and is immune to mind-affecting effects. The blood link lasts for 1 minute or
    until the Blood Queen ends the effect (a free action). When the blood link is
    broken, the affected kuru takes 1 point of Intelligence damage and cannot be linked
    to again for 24 hours. The save DC is Charisma-based.
  Horrifying Bellow (Su): Three times per day as a standard action, the Blood Queen
    can release a terrifying bellow that affects a 30-foot-radius spread. Any creature
    within the affected area must succeed at a DC 34 Will save or be paralyzed for
    1d4 rounds. The save DC is Charisma-based.
  Surrogate Senses (Su): In addition to its blindsight, the Blood Queen can constantly
    see and hear through its unholy kuru surrogates as though with a permanent clairaudience/clairvoyance
    spell. If at any time one of the Blood Queen's surrogates is killed, it is dazed
    for 1 round.
  Unholy Gestation (Ex): |-
    Whenever the Blood Queen swallows an unconscious humanoid or renders a humanoid unconscious with its swallow whole ability, it moves the victim through its digestive track, where the victim no longer takes damage, but rather begins to gestate within the Blood Queen's transformative stomach for 1d4 rounds. After the creature has finished gestating, it is regurgitated from the hindquarters of the Blood Queen, encased in an opaque mucous pod. Any attempt to remove a gestated humanoid from its pod causes massive system shock, and the humanoid takes 6d6 points of damage unless it succeeds at a DC 25 Fortitude save or those releasing it succeed at a DC 25 Heal check. As a swift action, the Blood Queen can send strong telepathic emanations to any pod within 100 feet, causing it to violently explode. The resulting spray of bilious ooze deals 6d6 points of acid damage to the creature encased in the pod and to any creatures in a 15-foot-radius burst.

    Alternatively, the Blood Queen may allow an encased humanoid to continue to gestate for at least 24 hours, and after that duration may release the fully metamorphosed creature from its pod at any point. When released, the victim completes its transformation into a kuru surrogate (see the Kuru Surrogate section below). The Blood Queen may create any number of pods, but can only possess up to six kuru surrogates at any one time (if the Blood Queen releases a seventh kuru surrogate from its mucus pod, the oldest surrogate immediately dies no matter where it is and the Blood Queen is dazed for 1 round). The save DCs are Constitution-based.
desc_long: |-
  Millennia ago, when the repugnant cyclops empire of Ghol-Gan populated the Shackles, its foul and alien gods sent powerful servants from beyond to act as their intermediaries, guiding and corrupting the empire until its ignominious collapse, at which point the gods and their minions fled Golarion altogether. However, one of these vile servants remained even after Ghol-Gan's collapse, a wretched horror known as the Blood Queen. It has dwelt for centuries in its foul subterranean chamber in a ruined Ghol-Gan temple called Ganagsau in the Cannibal Isles, and it was this blasphemous being who transformed the kuru into the degenerate race they are today, convincing them that it is a living goddess worthy of their veneration. The Blood Queen has a kuru high priest who goes by the name Bukrugsor, and this devoted thrall sees to it that his dark patron is brought regular sacrificial victims and offerings of blood.

  The Blood Queen has no eyes, per se-rather, what look like angry pustules all over its bloated body act as sensory organs. In addition, it is able to see and hear the world through the various kuru surrogates its followers have interspersed throughout the Cannibal Isles. Its grotesque mouth is capable of articulating a number of languages, though if it deigns to speak with a creature it usually does so via its telepathy. While the Blood Queen uses the short tentacles that extend from its mouth to devour prey and sacrificial offerings, the tentacles that emanate from its hindquarters are long, muscular, and tipped with bonelike stingers that allow it to manipulate objects and electrify victims.

  The Blood Queen is nearly immobile, being a massive, swollen beast that sits in the middle of a huge underground temple chamber in its ruined cathedral. While it may slowly undulate its bulk in one direction or another, in the years since its appearance on Golarion, the Blood Queen has grown far too large to fit through any of the limestone chamber's exits. Only the Blood Queen's high priest, those destined to become surrogate kuru, or sacrifices to the behemoth monster are allowed within this foul throne room. Sometimes unwilling sacrifices are dropped into the chamber from a hole in the ceiling and the exits are sealed so that the Blood Queen may toy with its food before it feeds. A being of monumental evil, the Blood Queen expresses its rage at its divine abandonment by spreading as much pain and havoc as it can. Whether it ever escapes its ancient, self-made prison remains to be seen, though all right-thinking creatures that know of its existence shudder at the prospect.

---

# Blood Queen
This hideous monstrosity looks like an enormous curled maggot, varicolored like deeply bruised flesh. Three flailing tentacles adorn each side of the thing’s huge, pulsating mouth, and five more arch from its hindquarters.
**Source** Isles of the Shackles pg. 44
**XP** 819,200
CE Gargantuan outsider (native)
**Init** +4; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., surrogate senses; Perception +39

##### Defense

**AC** 38, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+32 natural, –4 size)
**hp** 471 (23d10+345); _[[universal monster rules/Regeneration|regeneration]]_ 10 (good)
**Fort** +28, **Ref** +9, **Will** +24
**DR** 15/epic and lawful; **Immune** disease, electricity, mindaffecting effects, poison, sonic; **SR** 34

##### Offense
**Speed** 10 ft.
**Melee** bite +29 (2d6+10), 5 stings +29 (2d6+10/19–20 plus 2d6 electricity), 6 tentacles +24 (2d8+5/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** horrifying bellow, _[[universal monster rules/Swallow Whole|swallow whole]]_ (15d6 acid damage, AC 26, 47 hp), _[[items/Weapon Magic Abilities/Unholy|unholy]]_ gestation
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +36)
5/day—_[[spells/Cacophonous Call|cacophonous call]]_ (DC 25), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Good|dispel good]]_ (DC 28), _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 27)
3/day—greater _[[spells/Command|command]]_ (DC 28)
1/day—mass _[[spells/Suffocation|suffocation]]_ (DC 32)

##### Statistics
**Str** 30, **Dex** 11, **Con** 40, **Int** 20, **Wis** 29, **Cha** 37
**Base Atk** +23; **CMB** +37 (+41 grapple); **CMD** 47
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (sting), _Improved Critical_ (tentacles), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +39, Diplomacy +39, _[[spells/Heal|Heal]]_ +32, Intimidate +39, Knowledge (arcana) +28, Knowledge (history) +28, Knowledge (planes) +31, Knowledge (religion) +31, Perception +39, Sense Motive +39, Spellcraft +31
**Languages** Abyssal, Aklo, Common, Draconic, _[[monsters/Kuru|Kuru]]_, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** blood link

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

### Special Abilities

**Blood Link (Su)** Three times per day as a standard action, the _[[monsters/Blood Queen|Blood Queen]]_ may psychically link to up to 23 Hit Dice of _kuru_ within 100 feet of either itself or one of its _kuru_ surrogates; it may choose which specific _kuru_ it would like to affect with this ability, but HD that are not sufficient to affect a creature are wasted. Any _kuru_ linked to in this way must succeed at a DC 28 Will save or be forced to carry out the _Blood Queen_’s telepathic commands to the best of its ability. In addition, a linked _kuru_ gains a +4 morale bonus to Strength and Constitution and is immune to mind-affecting effects. The blood link lasts for 1 minute or until the _Blood Queen_ ends the effect (a free action). When the blood link is _[[conditions/Broken|broken]]_, the affected _kuru_ takes 1 point of Intelligence damage and cannot be linked to again for 24 hours. The save DC is Charisma-based.

**Horrifying Bellow (Su) **Three times per day as a standard action, the _Blood Queen_ can release a terrifying bellow that affects a 30-foot-radius spread. Any creature within the affected area must succeed at a DC 34 Will save or be _[[conditions/Paralyzed|paralyzed]]_ for 1d4 rounds. The save DC is Charisma-based.
**Surrogate Senses (Su)** In addition to its _blindsight_, the _Blood Queen_ can constantly see and hear through its _unholy_ _kuru_ surrogates as though with a permanent clairaudience/clairvoyance spell. If at any time one of the _Blood Queen_’s surrogates is killed, it is _[[conditions/Dazed|dazed]]_ for 1 round.

**_Unholy_ Gestation (Ex)** Whenever the _Blood Queen_ swallows an _[[conditions/Unconscious|unconscious]]_ humanoid or renders a humanoid _unconscious_ with its _swallow whole_ ability, it moves the victim through its digestive track, where the victim no longer takes damage, but rather begins to gestate within the _Blood Queen_’s _[[items/Weapon Magic Abilities/Transformative|transformative]]_ stomach for 1d4 rounds. After the creature has finished gestating, it is regurgitated from the hindquarters of the _Blood Queen_, encased in an opaque mucous pod. Any attempt to remove a gestated humanoid from its pod causes massive system _[[items/Weapon Magic Abilities/Shock|shock]]_, and the humanoid takes 6d6 points of damage unless it succeeds at a DC 25 Fortitude save or those releasing it succeed at a DC 25 _Heal_ check. As a swift action, the _Blood Queen_ can send strong telepathic emanations to any pod within 100 feet, causing it to violently explode. The resulting spray of bilious ooze deals 6d6 points of acid damage to the creature encased in the pod and to any creatures in a 15-foot-radius burst.

Alternatively, the _Blood Queen_ may allow an encased humanoid to continue to gestate for at least 24 hours, and after that duration may release the fully metamorphosed creature from its pod at any point. When released, the victim completes its _[[spells/Transformation|transformation]]_ into a _kuru_ surrogate (see the _Kuru_ Surrogate section below). The _Blood Queen_ may create any number of pods, but can only possess up to six _kuru_ surrogates at any one time (if the _Blood Queen_ releases a seventh _kuru_ surrogate from its mucus pod, the oldest surrogate immediately dies no matter where it is and the _Blood Queen_ is _dazed_ for 1 round). The save DCs are Constitution-based.

##### Description

Millennia ago, when the repugnant _[[monsters/Cyclops|cyclops]]_ empire of Ghol-Gan populated the Shackles, its foul and alien gods sent powerful servants from beyond to act as their intermediaries, guiding and corrupting the empire until its ignominious collapse, at which point the gods and their minions fled Golarion altogether. However, one of these vile servants remained even after Ghol-Gan’s collapse, a wretched horror known as the _Blood Queen_. It has dwelt for centuries in its foul subterranean chamber in a ruined Ghol-Gan temple _[[items/Weapon Magic Abilities/Called|called]]_ Ganagsau in the Cannibal Isles, and it was this blasphemous being who transformed the _kuru_ into the degenerate race they are today, convincing them that it is a living goddess worthy of their veneration. The _Blood Queen_ has a _kuru_ high priest who goes by the name Bukrugsor, and this devoted thrall sees to it that his dark patron is brought regular sacrificial victims and offerings of blood.

The _Blood Queen_ has no eyes, per se—rather, what look like angry pustules all over its bloated body act as sensory organs. In addition, it is able to see and hear the world through the various _kuru_ surrogates its followers have interspersed throughout the Cannibal Isles. Its grotesque mouth is capable of articulating a number of languages, though if it deigns to speak with a creature it usually does so via its _telepathy_. While the _Blood Queen_ uses the short tentacles that extend from its mouth to devour prey and sacrificial offerings, the tentacles that emanate from its hindquarters are long, muscular, and tipped with bonelike stingers that allow it to manipulate objects and electrify victims.

The _Blood Queen_ is nearly immobile, being a massive, swollen beast that sits in the middle of a huge underground temple chamber in its ruined cathedral. While it may slowly undulate its bulk in one direction or another, in the years since its appearance on Golarion, the _Blood Queen_ has grown far too large to fit through any of the limestone chamber’s exits. Only the _Blood Queen_’s high priest, those destined to become surrogate _kuru_, or sacrifices to the behemoth monster are allowed within this foul throne room. Sometimes unwilling sacrifices are dropped into the chamber from a hole in the ceiling and the exits are sealed so that the _Blood Queen_ may toy with its food before it feeds. A being of monumental evil, the _Blood Queen_ expresses its _[[spells/Rage|rage]]_ at its divine abandonment by spreading as much pain and havoc as it can. Whether it ever escapes its ancient, self-made prison remains to be seen, though all right-thinking creatures that know of its existence shudder at the prospect.