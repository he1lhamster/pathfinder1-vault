---
cssclass: [monsters]
title1: Vilderavn
desc_short: This knight wears armor patterned like raven feathers with a helmetshaped
  like a raven's head and gauntlets fit for oversized talons.
title2: Vilderavn
CR: 16
sources:
- name: Bestiary 5
  page: 268
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 76800
alignment: NE
size: Medium
type: fey
subtypes:
- shapechanger
initiative:
  bonus: 11
senses:
  deathwatch: true
  low-light vision: true
  see in darkness: true
  true seeing: true
auras:
- name: frightful presence
  radius: 30
  DC: 26
- name: shatter loyalties
AC:
  AC: 34
  touch: 24
  flat_footed: 26
  components:
    dex: 7
    dodge: 2
    insight,+10 natural: 5
HP:
  HP: 253
  long: 22d6+176
saves:
  fort: 17
  ref: 21
  will: 18
defensive_abilities:
- fate warden
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- curses
- death effects
- energy drain
- fear
SR: 27
speeds:
  base: 60
  fly: 110
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +23 (1d6+11 plus 1d6 bleed)
      entries:
      - - damage: 1d6+11
        - damage: 1d6
          type: bleed
      count: 2
      attack: claws
      bonus:
      - 23
    - text: bite +23(1d8+11/15-20 plus 1d6 bleed) or+5 cruel keen falchion +29/+29/+24/+19
        (2d4+21/15-20 plus1d6 bleed)
      entries:
      - - damage: 2d4+21
          type: plus1d6 bleed
          crit_range: 15-20
      attack: bite +23(1d8+11/15-20 plus 1d6 bleed) or+5 cruel keen falchion
      bonus:
      - 29
      - 29
      - 24
      - 19
  special:
  - bleed (1d6)
  - bloodbird
  - raven hexes (agony,cackle, charm, dire prophecy, disguise, evil eye,misfortune,
    retribution, speak in dreams)
  - soul eater
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: haste
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 20
  - name: crushing despair
    source: default
    freq: At will
    DC: 19
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: dispel magic
    source: default
    freq: At will
  - name: fear
    source: default
    freq: At will
    DC: 20
  - name: scrying
    source: default
    freq: At will
    DC: 20
  - name: suggestion
    source: default
    freq: At will
    DC: 19
  - name: circle of death
    source: default
    freq: 1/day
    DC: 22
  - name: ethereal jaunt
    source: default
    freq: 1/day
  - name: geas/quest
    source: default
    freq: 1/day
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 22
  - name: modify memory
    source: default
    freq: 1/day
    DC: 20
  - name: limited wish
    source: default
    freq: 1/month
    other: to non-fey only
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 32
  DEX: 25
  CON: 26
  INT: 19
  WIS: 20
  CHA: 23
BAB: 11
CMB: 22
CMD: 46
feats:
- name: Critical Focus
- name: Dodge
- name: Flyby Attack
- name: Great Fortitude
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lunge
- name: Mobility
- name: Power Attack
- name: Weapon Focus (falchion)
- name: Wind Stance
skills:
  Acrobatics: 31
  Bluff: 30
  Diplomacy: 21
  Disguise: 30
  Fly: 20
  Intimidate: 27
  Knowledge (history): 20
  Knowledge (nobility): 20
  Knowledge (local): 15
  Perception: 29
  Profession (soldier): 15
  Sense Motive: 25
  Stealth: 25
  Use Magic Device: 20
languages:
- Aklo
- Common
- Infernal
- Sylvan
- tongues
special_qualities:
- change shape (Small or Medium humanoid, peryton, wolf,or dire wolf, alter self or
  beast shape III)
- raven knight
ecology:
  environment: any
  organization: solitary, pair, or unkindness (3-5)
  treasure_type: standard
special_abilities:
  Bloodbird (Su): Bleed damage dealt by a vilderavn's naturaland manufactured weapons
    stacks with itself and othersources of bleed damage. In addition, the bleeding
    it causesis difficult to stanch-a successful DC 26 Heal check or aDC 26 caster
    level check (if using a magical healing effect) isrequired to stop the bleed damage.
    This is a curse effect.The DC is Charisma-based.
  Fate Warden (Su): A vilderavn gains an insight bonus to its ACequal to its Wisdom
    bonus, and as an immediate action itcan add its Wisdom bonus as an insight bonus
    on a savingthrow or opposed skill check.
  Raven Hexes (Sp, Su): A vilderavn can use the hexes listed inits special attacks
    entry as an 18th-level witch. The save DC to resist avilderavn's hex is 25, and
    is Charisma-based. A vilderavnalso uses its Charisma modifier, instead of its
    Intelligencemodifier, to determine the other variables of its hexes.
  Raven Knight (Sp): When a vilderavn assumes humanoid formwith its change shape ability,
    it loses its natural armor bonusbut becomes fully garbed in black +5 full plate
    that is almostpart of its body. This armor has no movement speed penalty,maximum
    Dexterity bonus, or armor check penalty. (For atypical vilderavn, this changes
    its AC to 38 and its flat-footedAC to 30.) Also as part of the transformation,
    it gains a +5cruel keen falchion formed from its vicious talons. Theseitems are
    part of the vilderavn's being and disappear whenit is slain. A vilderavn in humanoid
    form is considered tobe proficient in all types of armor, shields (except towershields),
    and martial weapons.
  Shatter Loyalties (Su): A vilderavn's frightful presencecreates disloyalty, doubt,
    and dissension in addition tofear. Creatures that fail their saves are no longer
    treatedas allies to other creatures and can't provide flanking, useor benefit
    from teamwork feats or aid another actions, orallow other creatures to move through
    their space. Anyspell or effect that requires a willing target fails if used onan
    affected creature, and even harmless effects requirean attack roll (if applicable)
    and require affected creaturesto attempt a saving throw to resist their effects
    (if a saveis allowed). Creatures that are immune to fear can still beaffected
    by the shatter loyalties component of a vilderavn'sfrightful presence; they ignore
    the shaken condition butare otherwise affected as described above. This is a mind-affectingeffect,
    and the save DC is Charisma-based.
  Soul Eater (Ex): A vilderavn's bite attack threatens a critical hiton an 18-20.
    If a vilderavn kills a humanoid foe with a criticalhit from its bite attack (including
    a coup de grace), it cantear out the victim's heart and consume its soul. Creaturesthat
    witness this savagery are frightened for 1d4 rounds, orshaken for 1 round if they
    succeed at a DC 27 Will save. Also,the vilderavn gains the benefits of death knell,
    and the slaincreature is affected as per rest eternal (caster level 18th).While
    the target remains dead, the vilderavn gains accessto that creature's memories
    and can use its change shapeability to assume a perfect likeness of the slain
    creature,gaining a +10 bonus on Bluff and Disguise checks made toimpersonate it.
    The vilderavn can store any number of souls.Slaying the vilderavn ends all its
    ongoing rest eternaleffects. The save DC is Charisma-based.
desc_long: |-
  A vilderavn is a malicious shapechanging spirit whosetypical form is that of an oversized raven with a wingspanof 6 to 8 feet that stands 2 to 3 feet tall. Vilderavnssometimes roam in the shape of wolves or dire wolves,and are known to appear as monstrous raven-wolf hybridsakin to black-feathered perytons. They can also walk inhumanoid guise when they wish, often assassinatingvictims of rank and assuming their victims' places.They have an unusual affection for their swords, oftengranting them threatening names.

  Vilderavns are drawn to war and suffering, oftenhaunting battlefields-especially during protractedsieges. They are particularly drawn toward rulers andcommanders, and might insinuate themselves into theconfidence of leaders with their clever tongues and deftrumor-mongering. They are deceivers and heralds ofwoe, seeking to lure the rulers of mortal kingdoms intojealous feuds and fruitless wars with one another. To dothis, they often cultivate reputations as master duelists,brilliant mercenary leaders, or unjustly banishednobility from distant lands. Regardless of their guises,vilderavns' advice usually seems wise and perceptive,steeped in an expansive knowledge of history,political rivalries, and cultural clashes, alongwith insights into the ways of war. Yet whiletheir counsel might lead to early victories,their ultimate purpose is to bring doom to allsides. At the height of the battle, when victory seemsnigh, a vilderavn often instigates a wave of betrayal,crippling erstwhile allies and bringing devastation.Only when a ruler's kingdom or a commander'sarmy lies in ruins does a vilderavn administer thecoup de grace.

  It is said that the first vilderavns were created bya vicious fey lord as a check and counter to thehubris of mortal rulers, especially those whoput their trust in armies and steel to drive backthe wild lands. The boasting and braggadocioof those mortals who believed they hadachieved mastery over the followers of the oldways offended the fey lord, who sent vilderavnsto infiltrate their ranks. The vilderavns watchedfrom the shadows and learned the ways of mortals,the better to use their own weapons and strategiesagainst them. In torment and blood, they peeledaway the secrets of mortals, laying the last truths of theirhearts bare before bestowing the gift of death on them. Evenin death, however, a vilderavn's victims languish, stretchedacross the threshold of the afterlife yet tethered to the feyspirit's merciless heart. Their minds are open books for thisfey to unravel and use in cruel and hurtful ways.

  Vilderavns sometimes amuse themselves by offeringfalse oracular advice or tempting bargains to mortals,promising power in exchange for the blood of innocents.A vilderavn typically claims to be cursed into its animalform, insisting that only innocent blood will release it.If its mark is foolish enough to accept its bargain, thevilderavn often returns wearing the innocent's fleshto torment its supposed ally and drive her to insanity. Avilderavn might even offer an irony-laced limited wish tosweeten its bargains and truly test a mortal's resolve.

---

# Vilderavn
This _[[npcs/Knight|knight]]_ wears armor patterned like raven feathers with a helmet

shaped like a raven’s head and gauntlets fit for oversized talons.
**Source** Bestiary 5 pg. 268
**XP** 76,800

NE Medium fey (shapechanger)
**Init** +11; **Senses** _[[spells/Deathwatch|deathwatch]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_,

_[[spells/True Seeing|true seeing]]_; Perception +29
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 26), _[[spells/Shatter|shatter]]_ loyalties

##### Defense

**AC** 34, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+7 Dex, +2 _[[feats/Dodge|dodge]]_, +5 insight,

+10 natural)
**hp** 253 (22d6+176)
**Fort** +17, **Ref** +21, **Will** +18
**Defensive Abilities** fate warden; **DR** 15/cold iron and good; **Immune** curses, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_; **SR** 27

##### Offense
**Speed** 60 ft., fly 110 ft. (average)
**Melee** 2 claws +23 (1d6+11 plus 1d6 _[[universal monster rules/Bleed|bleed]]_), bite +23

(1d8+11/15–20 plus 1d6 _bleed_) or

+5 _[[items/Weapon Magic Abilities/Cruel|cruel]]_ _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[items/Weapon/Falchion|falchion]]_ +29/+29/+24/+19 (2d4+21/15–20 plus

1d6 _bleed_)
**Special Attacks** _bleed_ (1d6), bloodbird, raven hexes (agony,

cackle, charm, dire prophecy, disguise, evil eye,

misfortune, _[[spells/Retribution|retribution]]_, speak in dreams), _[[monsters/Soul Eater|soul eater]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_deathwatch_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Haste|haste]]_, _[[spells/Tongues|tongues]]_, _true seeing_

At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Crushing Despair|crushing despair]]_ (DC 19), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _fear_ (DC 20), _[[spells/Scrying|scrying]]_ (DC 20), _[[spells/Suggestion|suggestion]]_ (DC 19)

1/day—_[[spells/Circle Of Death|circle of death]]_ (DC 22), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, geas/quest, mass _suggestion_ (DC 22), _[[spells/Modify Memory|modify memory]]_ (DC 20)

1/month—_[[spells/Limited Wish|limited wish]]_ (to non-fey only)

##### Statistics
**Str** 32, **Dex** 25, **Con** 26, **Int** 19, **Wis** 20, **Cha** 23
**Base Atk** +11; **CMB** +22; **CMD** 46
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_), _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +31, Bluff +30, Diplomacy +21, Disguise +30,

Fly +20, Intimidate +27, Knowledge (history, nobility) +20,

Knowledge (local) +15, Perception +29, Profession (soldier) +15,

Sense Motive +25, Stealth +25, Use Magic Device +20
**Languages** Aklo, Common, Infernal, Sylvan; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or _Medium_ humanoid, _[[monsters/Peryton|peryton]]_, _[[monsters/Wolf|wolf]]_,

or dire _wolf_, _[[spells/Alter Self|alter self]]_ or _[[spells/Beast Shape III|beast shape III]]_), raven _knight_

##### Ecology

**Environment** any
**Organization** solitary, pair, or unkindness (3–5)
**Treasure** standard

### Special Abilities

**Bloodbird (Su)** _Bleed_ damage dealt by a _[[monsters/Vilderavn|vilderavn]]_’s natural

and manufactured weapons stacks with itself and other

sources of _bleed_ damage. In addition, the bleeding it causes

is difficult to stanch—a successful DC 26 _[[spells/Heal|Heal]]_ check or a

DC 26 caster level check (if using a magical healing effect) is

required to stop the _bleed_ damage. This is a curse effect.

The DC is Charisma-based.

**Fate Warden (Su)** A _vilderavn_ gains an insight bonus to its AC

equal to its Wisdom bonus, and as an immediate action it

can add its Wisdom bonus as an insight bonus on a saving

throw or opposed skill check.

**Raven Hexes (Sp, Su)** A _vilderavn_ can use the hexes listed in

its special attacks entry as an 18th-level _[[classes/Witch|witch]]_. The save DC to resist a

_vilderavn_’s hex is 25, and is Charisma-based. A _vilderavn_

also uses its Charisma modifier, instead of its Intelligence

modifier, to determine the other variables of its hexes.

**Raven _Knight_ (Sp)** When a _vilderavn_ assumes humanoid form

with its _change shape_ ability, it loses its natural armor bonus

but becomes fully garbed in black +5 _[[items/Armor/Full plate|full plate]]_ that is almost

part of its body. This armor has no movement speed penalty,

maximum Dexterity bonus, or armor check penalty. (For a

typical _vilderavn_, this changes its AC to 38 and its _flat-footed_

AC to 30.) Also as part of the _[[spells/Transformation|transformation]]_, it gains a +5

_cruel_ _keen_ _falchion_ formed from its _[[items/Weapon Magic Abilities/Vicious|vicious]]_ talons. These

items are part of the _vilderavn_’s being and disappear when

it is slain. A _vilderavn_ in humanoid form is considered to

be proficient in all types of armor, shields (except tower

shields), and martial weapons.
**_Shatter_ Loyalties (Su)** A _vilderavn_’s _frightful presence_

creates disloyalty, doubt, and dissension in addition to

_fear_. Creatures that fail their saves are no longer treated

as allies to other creatures and can’t provide flanking, use

or benefit from teamwork feats or aid another actions, or

allow other creatures to move through their space. Any

spell or effect that requires a willing target fails if used on

an affected creature, and even harmless effects require

an attack roll (if applicable) and require affected creatures

to attempt a saving throw to resist their effects (if a save

is allowed). Creatures that are immune to _fear_ can still be

affected by the _shatter_ loyalties component of a _vilderavn_’s

_frightful presence_; they ignore the _[[conditions/Shaken|shaken]]_ condition but

are otherwise affected as described above. This is a mind-affecting

effect, and the save DC is Charisma-based.
**_Soul Eater_ (Ex)** A _vilderavn_’s bite attack threatens a critical hit

on an 18–20. If a _vilderavn_ kills a humanoid foe with a critical

hit from its bite attack (including a coup de _[[spells/Grace|grace]]_), it can

tear out the victim’s heart and consume its soul. Creatures

that _[[spells/Witness|witness]]_ this savagery are _[[conditions/Frightened|frightened]]_ for 1d4 rounds, or

_shaken_ for 1 round if they succeed at a DC 27 Will save. Also,

the _vilderavn_ gains the benefits of _[[spells/Death Knell|death knell]]_, and the slain

creature is affected as per _[[spells/Rest Eternal|rest eternal]]_ (caster level 18th).

While the target remains dead, the _vilderavn_ gains access

to that creature’s memories and can use its _change shape_

ability to assume a perfect likeness of the slain creature,

gaining a +10 bonus on Bluff and Disguise checks made to

impersonate it. The _vilderavn_ can store any number of souls.

Slaying the _vilderavn_ ends all its ongoing _rest eternal_

effects. The save DC is Charisma-based.

##### Description

A _vilderavn_ is a malicious shapechanging spirit whose

typical form is that of an oversized raven with a wingspan

of 6 to 8 feet that stands 2 to 3 feet tall. Vilderavns

sometimes roam in the shape of wolves or dire wolves,

and are known to appear as monstrous raven-wolf hybrids

akin to black-feathered perytons. They can also walk in

humanoid guise when they _[[spells/Wish|wish]]_, often assassinating

victims of rank and assuming their victims’ places.

They have an unusual affection for their swords, often

granting them threatening names.

Vilderavns are drawn to war and suffering, often

haunting battlefields—especially during protracted

sieges. They are particularly drawn toward rulers and

commanders, and might insinuate themselves into the

confidence of leaders with their clever _tongues_ and deft

rumor-mongering. They are deceivers and heralds of

woe, seeking to lure the rulers of mortal kingdoms into

jealous feuds and fruitless wars with one another. To do

this, they often cultivate reputations as master duelists,

brilliant mercenary leaders, or unjustly banished

nobility from distant lands. Regardless of their guises,

vilderavns’ advice usually seems wise and perceptive,

steeped in an expansive knowledge of history,

political rivalries, and cultural clashes, along

with insights into the ways of war. Yet while

their counsel might lead to early victories,

their ultimate purpose is to bring _[[spells/Doom|doom]]_ to all

sides. At the height of the battle, when victory seems

nigh, a _vilderavn_ often instigates a wave of betrayal,

crippling erstwhile allies and bringing devastation.

Only when a ruler’s kingdom or a commander’s

army lies in ruins does a _vilderavn_ administer the

coup de _grace_.

It is said that the first vilderavns were created by

a _vicious_ fey lord as a check and counter to the

hubris of mortal rulers, especially those who

put their trust in armies and steel to drive back

the wild lands. The boasting and braggadocio

of those mortals who believed they had

achieved mastery over the followers of the old

ways offended the fey lord, who sent vilderavns

to infiltrate their ranks. The vilderavns watched

from the shadows and learned the ways of mortals,

the better to use their own weapons and strategies

against them. In torment and blood, they peeled

away the secrets of mortals, laying the last truths of their

hearts bare before bestowing the gift of death on them. Even

in death, however, a _vilderavn_’s victims languish, stretched

across the threshold of the afterlife yet tethered to the fey

spirit’s merciless heart. Their minds are open books for this

fey to unravel and use in _cruel_ and _[[feats/Hurtful|hurtful]]_ ways.

Vilderavns sometimes amuse themselves by offering

false oracular advice or tempting bargains to mortals,

promising power in exchange for the blood of innocents.

A _vilderavn_ typically claims to be cursed into its animal

form, insisting that only _[[feats/Innocent Blood|innocent blood]]_ will release it.

If its mark is foolish enough to accept its bargain, the

_vilderavn_ often returns wearing the innocent’s flesh

to torment its supposed ally and drive her to _[[spells/Insanity|insanity]]_. A

_vilderavn_ might even offer an irony-laced _limited wish_ to

sweeten its bargains and truly test a mortal’s resolve.