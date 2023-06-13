---
cssclass: [monsters]
title1: Demon, Gallu
desc_short: 'This horned, winged, wolf-headed demon has bone-white flesh onto which
  have been riveted plates of spiky armor. '
title2: Gallu
CR: 19
sources:
- name: The Worldwound
  page: 44
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 204800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
  true seeing: true
auras:
- name: cloak of chaos
  radius: 20
  DC: 25
- name: havoc
  radius: 30
AC:
  AC: 34
  touch: 18
  flat_footed: 30
  components:
    armor: 8
    deflection: 4
    dex: 4
    natural: 8
HP:
  HP: 332
  long: 19d10+228
  fast_healing: 10
saves:
  fort: 27
  ref: 16
  will: 21
defensive_abilities:
- armor plating
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- bleed
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 30
speeds:
  base: 50
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 wounding falchion +31/+26/+21/+16 (2d4+17/15-20)
      entries:
      - - damage: 2d4+17
          crit_range: 15-20
      attack: +1 wounding falchion
      bonus:
      - 31
      - 26
      - 21
      - 16
    - text: bite +25 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 25
    - text: gore +25 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: gore
      bonus:
      - 25
  special:
  - rain of blood
  - wounding blood
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 25
  - name: true seeing
    source: default
    freq: Constant
  - name: confusion
    source: default
    freq: At will
    DC: 21
  - name: fear
    source: default
    freq: At will
    DC: 21
  - name: geas/quest
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 22
  - name: dimensional lock
    source: default
    freq: 3/day
  - name: quickened hold monster
    source: default
    freq: 3/day
    DC: 22
  - name: song of discord
    source: default
    freq: 3/day
    DC: 22
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 26
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: gallu
      amount: 1
      chance: 20%
    - name: marilith
      amount: 1
      chance: 35%
    - name: nalfeshnees
      amount: 1d4
      chance: 60%
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 25
  - name: word of chaos
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 19
    concentration: 26
ability_scores:
  STR: 33
  DEX: 18
  CON: 34
  INT: 18
  WIS: 23
  CHA: 25
BAB: 19
CMB: 30
CMB_other: +32 bull rush
CMD: 48
CMD_other: 50 vs. bull rush
feats:
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (falchion)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (hold monster)
- name: Staggering Critical
- name: Vital Strike
skills:
  Bluff: 29
  Disguise: 29
  Fly: 30
  Intimidate: 37
  Knowledge (engineering): 26
  Knowledge (history): 26
  Knowledge (planes): 26
  Perception: 36
  Ride: 26
  Sense Motive: 28
  _racial_mods:
    Intimidate:
      _: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- change shape (alter self, Small or Medium humanoid)
ecology:
  environment: any (Abyss)
  organization: solitary or platoon (1 gallu, 1-3 mariliths, and 3-12 vrocks)
  treasure_type: standard
  treasure:
  - +1 falchion
  - other treasure
special_abilities:
  Armor Plating (Su): 'The armor plates covering much of a gallu's body grant it a
    +8 armor bonus. They also function as armor spikes during grapples, but cannot
    be used as offhand weapons. In addition, these armor plates can possess one additional
    armor special ability chosen from the following options: acid resistance 20, cold
    resistance 20, fire resistance 20, ghost touch, moderate fortification, or sonic
    resistance 20. A gallu demon can switch the active armor special quality once
    per hour as a swift action-as a general rule, the gallu demon keeps the armor
    plating set to moderate fortification. These armor plates do not encumber the
    gallu or impose armor check penalties, maximum Dex bonuses, or arcane spell failure
    chances. They cannot be removed, sundered, or destroyed while the gallu lives,
    and they rust away into nonmagical fragments of iron upon the gallu's death.'
  Aura of Havoc (Su): A gallu's presence wreaks havoc, infusing battlefields with
    elements of chaos and entropy that disrupt careful coordination and tactical plotting
    by manipulating fate and chance. This aura extends to a 30-foot radius around
    the gallu. The aid another action can never grant bonuses in this area, nor does
    flanking grant bonuses to hit in the affected area (although flanked foes remain
    susceptible to sneak attack damage). A creature summoned into this area by any
    creature other than a demon must succeed at a DC 26 Will save to avoid being confused
    for 1d4 rounds. Paladins and creatures with the lawful subtype must make a DC
    26 Will save each round they begin their turn in this aura to avoid being nauseated
    for 1 round. Demons ignore the effects of a gallu's aura of havoc. The save DCs
    are Charisma-based.
  Rain of Blood (Su): As a standard action once per minute, a gallu can command the
    wounds of all creatures within 30 feet to erupt into a gory deluge of blood; any
    wounded creature in the area of effect immediately takes 3d6 points of damage
    from the rain of blood and must succeed at a DC 31 Fortitude saving throw. Failure
    indicates that the damage becomes bleed damage and the affected creature becomes
    staggered from the pain as long as the bleed damage continues. Creatures that
    are immune to bleed damage are immune to this ability's effects. The save DCs
    are Constitution-based.
  Wounding Blood (Su): The spikes that hold a gallu's armor plates in place extend
    as far into the demon's body as they do outside of it, causing rivulets of blood
    to constantly run from the creature's flesh. This continual bleeding does not
    inconvenience or harm the gallu; instead, it grants the wounding special ability
    to all manufactured weapons wielded by the gallu. The dripping blood does not
    affect the gallu's natural attacks.
desc_long: |-
  On the endless battlefields of the Abyss, the demon lords' vast armies clash and tear at each other in horrific displays of warfare and bloodshed. These conflicts often arise from border disputes between demonic realms, or when one demon lord finds an excuse to attack another. But many of these immense wars have no good reason at all, for gallus eagerly foment war for war's sake; they are master engineers of martial strife. These hateful, destructive demons arise from the souls of warmongers and war profiteers-nefarious leaders, corrupt priests, or subversive merchants who used their power to perpetuate existing wars or even to trigger new ones, all for the express purpose of personal gain or sadistic pleasure. 

  Known to some as warmonger demons, the gallus are not as enormous as many of the other powerful demons; despite their near-human size, however, they are among the deadliest of demonkind. Standing 8 feet tall and weighing 450 pounds, these creatures have wolf like (but hairless) horned heads, batlike wings, and pale flesh. Their feet end in hooves, and their tails resemble those of lions. Gallus can assume humanoid shape as well, and typically do so when interacting with mortals, allowing them to more easily sow seeds of war among those they interact with. 

  These demons are relatively difficult to summon- gate spells can conjure them from the Abyss, but few other mortal spells can call them forth. As a result, most gallus encountered outside the Abyss have traveled there via portals or similar methods. Gallus are innately crafty creatures; when coming to a new world, they resist their natural urges to destroy in favor of infiltration. Extraordinarily patient, they can spend decades or more in disguise as they subtly build their inf luence and acquire positions of power; they then use those positions to incite government officials and other powerful individuals to wage war on their neighbors. Only when the hostilities have completely devastated their host, leaving it in smoking ruins, do gallus shed their human flesh and appear in their true form to gloat and torment the conflict's few survivors before moving on to seek fresh victims. 

  In the Worldwound, gallus serve an additional role as commanders in the numerous demonic armies. Many control multiple divisions, each led by a marilith general, and report in turn to one of the Worldwound's leaders, like Khorramzadeh, Areelu, or Aponavicius. But not all of the Worldwound's gallus command armies. Those who serve Baphomet primarily utilize their deceptive natures to infiltrate various Mendevian mercenary orders, Mammoth Lord barbarian tribes, settlements on the fringes of more civilized lands, and other factions arrayed against the Worldwound. From within those groups, they serve as advisors, urging those they've infiltrated into launching ill-timed or poorly planned attacks on their demonic foes. These gallus occasionally feed their humanoid “allies” legitimate intelligence about demonic fortifications or troop movements, knowing that a little truth can go a long way in encouraging mortals to act upon their more violent urges.

---

# Demon, Gallu
This horned, winged, wolf-headed demon has bone-white flesh
onto which have been riveted plates of spiky armor.

**Source** The Worldwound pg. 44
**XP** 204,800
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +36
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (20 ft., DC 25), havoc (30 ft.)

##### Defense

**AC** 34, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+8 armor, +4 _[[spells/Deflection|deflection]]_, +4 Dex,
+8 natural)
**hp** 332 (19d10+228); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +27, **Ref** +16, **Will** +21
**Defensive Abilities** armor plating; **DR** 15/cold iron and good; **Immune** _[[universal monster rules/Bleed|bleed]]_, electricity, poison; **Resist** acid 10, cold 10,
fire 10; **SR** 30

##### Offense
**Speed** 50 ft., fly 50 ft. (good)
**Melee** +1 _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _[[items/Weapon/Falchion|falchion]]_ +31/+26/+21/+16 (2d4+17/15–20),
bite +25 (1d8+5), gore +25 (1d6+5)
**Special Attacks** rain of blood, _wounding_ blood
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +26)
Constant—_cloak of chaos_ (DC 25), _true seeing_
At will—_[[spells/Confusion|confusion]]_ (DC 21), _[[universal monster rules/Fear|fear]]_ (DC 21), geas/quest,
greater teleport (self plus 50 lbs. of objects only),
_[[spells/Telekinesis|telekinesis]]_ (DC 22)
3/day—_[[spells/Dimensional Lock|dimensional lock]]_, quickened _[[spells/Hold Monster|hold monster]]_ (DC 22),
_[[spells/Song of Discord|song of discord]]_ (DC 22)
1/day—mass _hold monster_ (DC 26), _[[universal monster rules/Summon|summon]]_ (level 7,
 1 gallu 20%, 1 marilith 35%, or 1d4 nalfeshnees 60%),
_[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 25), _[[spells/Word Of Chaos|word of chaos]]_ (DC 24)

##### Statistics
**Str** 33, **Dex** 18, **Con** 34, **Int** 18, **Wis** 23, **Cha** 25
**Base Atk** +19; **CMB** +30 (+32 bull rush); **CMD** 48 (50 vs. bull rush)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_
(_falchion_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_
(_hold monster_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +29, Disguise +29, Fly +30, Intimidate +37,
Knowledge (engineering) +26, Knowledge (history) +26,
Knowledge (planes) +26, Perception +36, Ride +26, Sense
Motive +28; **Racial Modifiers** +8 Intimidate, +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Alter Self|alter self]]_, Small or _Medium_ humanoid)

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or platoon (1 gallu, 1–3 mariliths, and
 3–12 vrocks)
**Treasure** standard (+1 _falchion_, other treasure)

### Special Abilities

**Armor Plating (Su)** The armor plates covering much of a
gallu’s body grant it a +8 armor bonus. They also function
as armor spikes during grapples, but cannot be used as offhand
weapons. In addition, these armor plates can possess
one additional armor special ability chosen from the
following options: acid _[[universal monster rules/Resistance|resistance]]_ 20, cold _resistance_ 20,
fire _resistance_ 20, _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_, moderate _[[universal monster rules/Fortification|fortification]]_, or
sonic _resistance_ 20. A gallu demon can switch the active
armor special quality once per hour as a swift action—as
a general rule, the gallu demon keeps the armor plating
set to moderate _fortification_. These armor plates do not
encumber the gallu or impose armor check penalties,
maximum Dex bonuses, or arcane spell failure chances.
They cannot be removed, sundered, or destroyed while the
gallu lives, and they rust away into nonmagical fragments
of iron upon the gallu’s death.

**Aura of Havoc (Su)** A gallu’s presence wreaks havoc, infusing
battlefields with elements of chaos and entropy that disrupt
careful coordination and tactical plotting by manipulating
fate and chance. This aura extends to a 30-foot radius
around the gallu. The aid another action can never grant
bonuses in this area, nor does flanking grant bonuses to
hit in the affected area (although flanked foes remain
susceptible to sneak attack damage). A creature summoned
into this area by any creature other than a demon must
succeed at a DC 26 Will save to avoid being _[[conditions/Confused|confused]]_ for
 1d4 rounds. Paladins and creatures with the lawful subtype
must make a DC 26 Will save each round they begin their
turn in this aura to avoid being _[[conditions/Nauseated|nauseated]]_ for 1 round.
Demons ignore the effects of a gallu’s aura of havoc. The
save DCs are Charisma-based.

**Rain of Blood (Su)** As a standard action once per minute, a
gallu can _[[spells/Command|command]]_ the wounds of all creatures within 30
feet to erupt into a _[[items/Weapon Magic Abilities/Gory|gory]]_ deluge of blood; any wounded
creature in the area of effect immediately takes 3d6 points
of damage from the rain of blood and must succeed at a
DC 31 Fortitude saving throw. Failure indicates that the
damage becomes _bleed_ damage and the affected creature
becomes _[[conditions/Staggered|staggered]]_ from the pain as long as the _bleed_
damage continues. Creatures that are immune to _bleed_
damage are immune to this ability’s effects. The save DCs
are Constitution-based.

**_Wounding_ Blood (Su)** The spikes that hold a gallu’s armor
plates in place extend as far into the demon’s body as they
do outside of it, causing rivulets of blood to constantly
run from the creature’s flesh. This continual bleeding does
not inconvenience or _[[spells/Harm|harm]]_ the gallu; instead, it grants
the _wounding_ special ability to all manufactured weapons
wielded by the gallu. The dripping blood does not affect the
gallu’s _[[universal monster rules/Natural Attacks|natural attacks]]_.

##### Description

On the endless battlefields of the Abyss, the demon
lords’ vast armies clash and tear at each other in horrific
displays of warfare and bloodshed. These conflicts often
arise from border disputes between demonic realms, or
when one demon lord finds an excuse to attack another.
But many of these immense wars have no good reason
at all, for gallus eagerly foment war for war’s sake; they
are master engineers of martial strife. These hateful,
destructive demons arise from the souls of warmongers
and war profiteers—nefarious leaders, corrupt priests, or
subversive merchants who used their power to perpetuate
existing wars or even to trigger new ones, all for the
express purpose of personal gain or sadistic pleasure.

Known to some as _[[feats/Warmonger|warmonger]]_ demons, the gallus are
not as enormous as many of the other powerful demons;
despite their near-human size, however, they are among
the deadliest of demonkind. Standing 8 feet tall and
weighing 450 pounds, these creatures have _[[monsters/Wolf|wolf]]_ like (but
hairless) horned heads, batlike wings, and pale flesh.
Their feet end in hooves, and their tails resemble those
of lions. Gallus can assume humanoid shape as well, and
typically do so when interacting with mortals, allowing
them to more easily sow seeds of war among those they
interact with.

These demons are relatively difficult to _summon_—
_[[spells/Gate|gate]]_ spells can conjure them from the Abyss, but
few other mortal spells can call them forth. As
a result, most gallus encountered outside the
Abyss have traveled there via portals or similar
methods. Gallus are innately crafty creatures;
when coming to a new world, they resist
their natural urges to destroy in favor of
infiltration. Extraordinarily patient, they can
spend decades or more in disguise as they
subtly build their inf luence and acquire
positions of power; they then use those
positions to incite government officials
and other powerful individuals to wage
war on their neighbors. Only when the
hostilities have completely devastated
their host, leaving it in smoking ruins,
do gallus shed their human flesh and
appear in their _[[spells/True Form|true form]]_ to gloat and
torment the conflict’s few survivors
before moving on to seek fresh victims.

In the Worldwound, gallus serve an
additional role as commanders in the
numerous demonic armies. Many control
multiple divisions, each led by a marilith
general, and report in turn to one of the
Worldwound’s leaders, like Khorramzadeh,
Areelu, or Aponavicius. But not all of the
Worldwound’s gallus _command_ armies. Those
who serve Baphomet primarily utilize their _[[items/Weapon Magic Abilities/Deceptive|deceptive]]_
natures to infiltrate various Mendevian mercenary
orders, Mammoth Lord _[[classes/Barbarian|barbarian]]_ tribes, settlements on
the fringes of more civilized lands, and other factions
arrayed against the Worldwound. From within those
groups, they serve as advisors, urging those they’ve
infiltrated into launching ill-timed or poorly planned
attacks on their demonic foes. These gallus occasionally
feed their humanoid “allies” legitimate intelligence about
demonic fortifications or troop movements, knowing
that a little truth can go a long way in encouraging
mortals to act upon their more violent urges.