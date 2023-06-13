---
cssclass: [monsters]
title1: Warped One
desc_short: 'This insane, twisted, humanoid-shaped tangle of limbs and gnashing teeth
  thrashes and howls, all too eager to wreak havoc. '
title2: Warped One
CR: 8
sources:
- name: The Worldwound
  page: 62
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 4800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
auras:
- name: warp field
  radius: 30
AC:
  AC: 21
  touch: 14
  flat_footed: 17
  components:
    dex: 4
    natural: 7
HP:
  HP: 105
  long: 10d10+50
saves:
  fort: 12
  ref: 9
  will: 9
defensive_abilities:
- amorphous
- insane
immunities:
- mind-affecting effects
- petrification
- polymorph effects
resistances:
  electricity: 10
SR: 19
speeds:
  base: 30
attacks:
  melee:
  - - text: 4 claws +16 (1d4+6/19-20)
      entries:
      - - damage: 1d4+6
          crit_range: 19-20
      count: 4
      attack: claws
      bonus:
      - 16
  special:
  - fleshwarping
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: unstable summoning
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 8
    concentration: 10
ability_scores:
  STR: 22
  DEX: 19
  CON: 20
  INT: 12
  WIS: 5
  CHA: 15
BAB: 10
CMB: 16
CMD: 30
CMD_other: 34 vs. trip
feats:
- name: Combat Reflexes
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Skill Focus (Stealth)
skills:
  Acrobatics: 17
  Climb: 19
  Knowledge (planes): 14
  Perception: 10
  Stealth: 23
  Swim: 19
  Use Magic Device: 15
languages:
- Abyssal
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or mob (3-14)
  treasure_type: standard
special_abilities:
  Fleshwarping (Su): |-
    A warped one's body constantly shifts and changes as raw Abyssal energies course through it, reshaping and rebuilding it in minor but hideous ways. Once a warped one enters combat, these growing energies begin to alter its statistics in small ways. At the start of a warped one's turn, roll on the following table to see what additional effect its fleshwarping has on it for that round-all of the following mutations have a duration of 1 round unless otherwise noted. 

     d8Result 1Infusion of Chaos: The warped one's body ripples and shifts rapidly as it grows and absorbs fingers, tendrils, sightless eyes, toothless mouths, tumors, and other mostly useless organs out of its body. The warped one gains DR 10/lawful. 2Enhanced Musculature: The warped one grows much more muscular. It gains a +2 enhancement bonus on melee attack rolls, melee weapon damage, CMB checks, Strength-based checks, and to its CMD. 3Lean and Swift: The warped one grows lean and agile, with longer legs and additional joints in its limbs. It gains a +2 dodge bonus to its AC, a +2 enhancement bonus on Reflex saves, and its speed increases by 10 feet. 4Prismatic Scales: Multicolored scales grow from the warped one's flesh. It gains resistance to acid 10, cold 10, and fire 10. 5Razor-Sharp Talons: The warped one's claws grow additional, sharper talons. Its claw attacks gain bleed 1d6. 6Multiple Eyes: The warped one grows additional eyes and other sensory organs. It gains a +8 bonus on Perception checks and gains all-around vision. 7Accelerated Metabolism: The warped one sheds its claws and teeth and immediately grows new ones, its wounds heal, and its colors grow brighter. It gains a +2 enhancement bonus on Fortitude saves and immediately heals 3d8+10 points of damage (if it's currently unwounded, it gains these hit points as temporary hit points that last for 1 hour or until depleted). 8Armor Plating: The warped one grows a thick hide and dark scaly plates granting it DR 5/, and its natural armor bonus increases by +4.
  Insanity (Ex): A warped one's mind is completely unhinged, a raw chaos of madness.
    It uses its Charisma modifier on Will saves instead of its Wisdom modifier, and
    it is immune to mind-affecting effects. Any attempt to contact a warped one telepathically
    (including using spells like detect thoughts) produces a backlash effect, dealing
    1d4 points of Charisma damage to the one attempting the contact. A DC 17 Will
    save negates this effect. The save DC is Charisma-based.
  Unstable Summoning (Sp): |-
    A warped one can rend the boundaries between worlds to summon creatures to aid it in combat, but it has little control over what sorts of monsters or demons respond to its summonings. When a warped one uses its unstable summoning, there's a 50% chance that a creature (or a group of creatures) arrives to aid the warped one. Creatures summoned in this way are immune to that particular warped one's warp field. To determine the nature of the summoned aid, roll on the table below. This is a 5th-level spell effect. 

    d8Result 11d4+1 mephits (determine type randomly) 21d4+1 Medium elementals (determine type randomly) 31d3 salamanders 41d3 Large elementals (determine type randomly) 51d3 babaus 61 shadow demon 71 succubus 81 warped one
  Warp Field (Su): |-
    A warped one exudes a field of mental and physical entropic energy to a radius of 30 feet that twists and warps the minds and bodies of all other living creatures. Creatures who begin their turn inside of a warp field must succeed at a DC 17 Will save. Failure indicates that the creature is confused for 1 round and suffers one mutation from the table below. These mutations emerge swiftly and painfully, causing the victim to become sickened for 1 round and to gain one random mutation from the following table for 1 round. Once a creature succeeds at its saving throw against a warp field, it is immune to further effects from that specific warped one's warp field for 24 hours. This is a polymorph effect. The save DCs are Charisma-based. 

    d8Result 1Club Foot: One of your feet becomes badly deformed. Reduce your speed by 10 feet. 2Cataracts: Your eyes film over with cataracts. You are blinded. 3Demonic Horns: You grow several bony horns from your skull. You must succeed at a DC 17 Reflex save or any headband or hat you wear becomes broken. 4Boneless Mass: You fall prone and your movement rate is reduced to 0 feet. You must succeed at a DC 17 Fortitude save to avoid being stunned for 1 round. 5Twisted Hands: Your hands twist and deform. You drop all held objects and worn rings and cannot use your hands to make attacks or cast spells for 1 round. 6Twisted Visage: Your face deforms into a hideous mockery. You cannot speak or cast spells with verbal components. 7Malnourished: You become skeletally thin. All worn items (save boots, head, and headband items) drop from your body, and you must succeed at a DC 17 Fortitude save to avoid being entangled in your gear. When you return to your normal shape 1 round later, dropped items remain on the ground in your square. 8Obesity: You become monstrously obese. Your land speed is reduced to 5 feet. In addition, if you fail a DC 17 Reflex save, any items you have equipped in the armor, belt, body, chest, neck, shoulders, or wrist slots become broken.
desc_long: |-
  Demons form from the interaction of sinful human souls upon the fecundity of the Abyss itself, but this is not the only way the demonic plane creates life. In certain parts of this blasphemous realm, non-sinful souls or even living humanoids can be overwhelmed and transformed into demon-like creatures. So powerful are the energies corrupting and warping these humanoids that chaotic force continues to leak from their creations and continuously affect the creatures' flesh-forever twisting and mutating them in endless agony. These poor victims have been transformed into warped ones. 

  No two warped ones look exactly alike, although they all share certain common features. They always appear as two to four demonic humanoids awkwardly fused together into a single human-sized monstrosity. While they can have several limbs, they always have four that sport particularly sharp talons. Once a warped one enters combat, the excitement of imminent bloodshed (both that of its victims and of itself ) causes the entropic energies within it to change and mutate. A fight against a warped one is a harrowing experience, for not only do the warped one's physical traits change continuously, these mutations affect and cripple those nearby in devastating ways. 

  As using a warped one in combat adds lots of additional dice rolls to encounters, you may want to “synchronize” their fleshwarping and warp-field abilities when using multiple warped ones in battles, so each round they all exhibit the same trait and their warp fields all have the same effect. A warped one is 7 feet tall and weighs 350 pounds.

---

# Warped One
This insane, twisted, humanoid-shaped tangle of limbs and
gnashing teeth thrashes and howls, all too eager to wreak havoc.

**Source** The Worldwound pg. 62
**XP** 4,800
CE Medium outsider (chaotic, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10
**Aura** warp field (30 ft.)

##### Defense

**AC** 21, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 Dex, +7 natural)
**hp** 105 (10d10+50)
**Fort** +12, **Ref** +9, **Will** +9
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_, insane; **Immune** mind-affecting
effects, petrification, _[[spells/Polymorph|polymorph]]_ effects; **Resist** electricity 10; **SR** 19

##### Offense
**Speed** 30 ft.
**Melee** 4 claws +16 (1d4+6/19–20)
**Special Attacks** fleshwarping
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +10)
Constant—_[[spells/Blur|blur]]_
At will—_[[spells/Dimension Door|dimension door]]_ (self plus 50 lbs. of objects only)
1/day—unstable summoning

##### Statistics
**Str** 22, **Dex** 19, **Con** 20, **Int** 12, **Wis** 5, **Cha** 15
**Base Atk** +10; **CMB** +16; **CMD** 30 (34 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), Improved
Initiative, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Acrobatics +17, _[[universal monster rules/Climb|Climb]]_ +19, Knowledge (planes) +14,
Perception +10, Stealth +23, Swim +19, Use Magic Device +15
**Languages** Abyssal

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or mob (3–14)
**Treasure** standard

### Special Abilities

**Fleshwarping (Su)** A _[[monsters/Warped One|warped one]]_’s body constantly shifts
and changes as raw Abyssal energies course through it,
reshaping and rebuilding it in minor but hideous ways. Once
a _warped one_ enters combat, these _[[items/Weapon Magic Abilities/Growing|growing]]_ energies begin
to alter its statistics in small ways. At the start of a warped
one’s turn, roll on the following table to see what additional
effect its fleshwarping has on it for that round—all of the
following mutations have a duration of 1 round unless
otherwise noted.

**d8****Result**
1Infusion of Chaos: The _warped one_’s body ripples
and shifts rapidly as it grows and absorbs fingers,
tendrils, sightless eyes, toothless mouths, tumors,
and other mostly useless organs out of its body. The
_warped one_ gains DR 10/lawful.
2Enhanced Musculature: The _warped one_ grows much
more muscular. It gains a +2 enhancement bonus
on melee attack rolls, melee weapon damage, CMB
checks, Strength-based checks, and to its CMD.
3Lean and Swift: The _warped one_ grows lean and
_[[items/Weapon Magic Abilities/Agile|agile]]_, with longer legs and additional joints in its
limbs. It gains a +2 _[[feats/Dodge|dodge]]_ bonus to its AC, a +2
enhancement bonus on Reflex saves, and its speed
increases by 10 feet.
4Prismatic Scales: Multicolored scales grow from the
_warped one_’s flesh. It gains _[[universal monster rules/Resistance|resistance]]_ to acid 10, cold
 10, and fire 10.
5Razor-Sharp Talons: The _warped one_’s claws grow
additional, sharper talons. Its claw attacks gain _[[universal monster rules/Bleed|bleed]]_
 1d6.
6Multiple Eyes: The _warped one_ grows additional eyes
and other sensory organs. It gains a +8 bonus on
Perception checks and gains _[[universal monster rules/All-Around Vision|all-around vision]]_.
7Accelerated Metabolism: The _warped one_ sheds its
claws and teeth and immediately grows new ones, its
wounds _[[spells/Heal|heal]]_, and its colors grow brighter. It gains a +2
enhancement bonus on Fortitude saves and immediately
heals 3d8+10 points of damage (if it’s currently
unwounded, it gains these hit points as temporary hit
points that last for 1 hour or until depleted).
8Armor Plating: The _warped one_ grows a thick hide
and dark scaly plates granting it DR 5/, and its natural
armor bonus increases by +4.

**_[[spells/Insanity|Insanity]]_ (Ex)** A _warped one_’s mind is completely unhinged, a
raw chaos of madness. It uses its Charisma modifier on Will
saves instead of its Wisdom modifier, and it is immune to
mind-affecting effects. Any attempt to contact a _warped one_
telepathically (including using spells like _[[spells/Detect Thoughts|detect thoughts]]_)
produces a backlash effect, dealing 1d4 points of Charisma
damage to the one attempting the contact. A DC 17 Will save
negates this effect. The save DC is Charisma-based.

**Unstable Summoning (Sp)** A _warped one_ can _[[universal monster rules/Rend|rend]]_ the
boundaries between worlds to _[[universal monster rules/Summon|summon]]_ creatures to aid it in
combat, but it has little control over what sorts of monsters
or demons respond to its summonings. When a _warped one_
uses its unstable summoning, there’s a 50% chance that a
creature (or a group of creatures) arrives to aid the warped
one. Creatures summoned in this way are immune to that
particular _warped one_’s warp field. To determine the nature
of the summoned aid, roll on the table below. This is a 5th-level
spell effect.

**d8****Result**
11d4+1 mephits (determine type randomly)
21d4+1 _Medium_ elementals (determine type randomly)
31d3 salamanders
41d3 Large elementals (determine type randomly)
51d3 babaus
61 _[[items/Armor Magic Abilities/Shadow|shadow]]_ demon
71 succubus
81 _warped one_

**Warp Field (Su)** A _warped one_ exudes a field of mental and
physical entropic energy to a radius of 30 feet that twists
and warps the minds and bodies of all other living creatures.
Creatures who begin their turn inside of a warp field must
succeed at a DC 17 Will save. Failure indicates that the
creature is _[[conditions/Confused|confused]]_ for 1 round and suffers one mutation
from the table below. These mutations emerge swiftly and
painfully, causing the victim to become _[[conditions/Sickened|sickened]]_ for 1 round
and to gain one random mutation from the following table
for 1 round. Once a creature succeeds at its saving throw
against a warp field, it is immune to further effects from
that specific _warped one_’s warp field for 24 hours. This is a
_polymorph_ effect. The save DCs are Charisma-based.

**d8****Result**
1Club Foot: One of your feet becomes badly deformed.
Reduce your speed by 10 feet.
2Cataracts: Your eyes film over with cataracts. You
are _[[conditions/Blinded|blinded]]_.
3Demonic Horns: You grow several bony horns from
your skull. You must succeed at a DC 17 Reflex save or
any headband or _[[items/Mundane/Hat|hat]]_ you wear becomes _[[conditions/Broken|broken]]_.
4Boneless Mass: You fall _[[conditions/Prone|prone]]_ and your movement
rate is reduced to 0 feet. You must succeed at a DC 17
Fortitude save to avoid being _[[conditions/Stunned|stunned]]_ for 1 round.
5Twisted Hands: Your hands twist and deform. You
drop all held objects and worn rings and cannot use
your hands to make attacks or cast spells for 1 round.
6Twisted Visage: Your face deforms into a hideous
mockery. You cannot speak or cast spells with
verbal components.
7Malnourished: You become skeletally thin. All worn
items (save boots, head, and headband items) drop
from your body, and you must succeed at a DC 17
Fortitude save to avoid being _[[conditions/Entangled|entangled]]_ in your gear.
When you return to your normal shape 1 round later,
dropped items remain on the ground in your square.
8Obesity: You become monstrously obese. Your land
speed is reduced to 5 feet. In addition, if you fail a
DC 17 Reflex save, any items you have equipped in
the armor, belt, body, chest, neck, shoulders, or wrist
slots become _broken_.

##### Description

Demons form from the interaction of sinful human souls
upon the fecundity of the Abyss itself, but this is not the
only way the demonic plane creates life. In certain parts
of this blasphemous realm, non-sinful souls or even
living humanoids can be overwhelmed and transformed
into demon-like creatures. So powerful are the energies
corrupting and warping these humanoids that chaotic
force continues to leak from their creations and
continuously affect the creatures’ flesh—forever twisting
and mutating them in endless agony. These poor victims
have been transformed into warped ones.

No two warped ones look exactly alike, although they
all share certain common features. They always appear
as two to four demonic humanoids awkwardly fused
together into a single human-sized monstrosity. While
they can have several limbs, they always have four that sport
particularly sharp talons. Once a _warped one_ enters combat,
the excitement of imminent bloodshed (both that of its
victims and of itself ) causes the entropic energies within
it to change and mutate. A fight against a _warped one_ is
a _[[spells/Harrowing|harrowing]]_ experience, for not only do the _warped one_’s
physical traits change continuously, these mutations affect
and cripple those nearby in devastating ways.

As using a _warped one_ in combat adds lots of additional
dice rolls to encounters, you may want to “synchronize” their
fleshwarping and warp-field abilities when using multiple
warped ones in battles, so each round they all exhibit the
same trait and their warp fields all have the same effect.
A _warped one_ is 7 feet tall and weighs 350 pounds.