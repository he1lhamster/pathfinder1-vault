---
cssclass: [monsters]
title1: Psychopomp, Yamaraj
desc_short: The head of this winged, dragonlike beast is crowned with long spines.
  Sooty feathers cover its body.
title2: Yamaraj
CR: 20
sources:
- name: Bestiary 4
  page: 222
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #48: Shadows of Gallowspire'
  page: 86
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8mgb
XP: 307200
alignment: N
size: Huge
type: outsider
subtypes:
- extraplanar
- psychopomp
initiative:
  bonus: 16
senses:
  darkvision: 60
  detect thoughts: true
  low-light vision: true
  spiritsense: true
  true seeing: true
auras:
- name: fear
  radius: 30
  DC: 32
AC:
  AC: 40
  touch: 21
  flat_footed: 27
  components:
    armor: 4
    dex: 12
    dodge: 1
    natural: 15
    size: -2
HP:
  HP: 337
  long: 25d10+200
  fast_healing: 10
saves:
  fort: 22
  ref: 20
  will: 25
defensive_abilities:
- lightning drinker
DR:
- amount: 15
  weakness: adamantine
immunities:
- cold
- electricity
- death effects
- disease
- poison
SR: 31
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
  swim: 40
attacks:
  melee:
  - - text: bite +32 (2d6+9/19-20 plus grab and poison)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d6+9)
      entries:
      - - damage: 2d6+9
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +30 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: tail slap
      bonus:
      - 30
    - text: 2 wings +30 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 30
  special:
  - breath weapon (60-ft. cone, 20d6 cold, Reflex DC 30 half, usable every 1d4 rounds;
    or beetles)
  - poison
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 22
  - name: mage armor
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: reincarnate
    source: default
    freq: At will
  - superscripts:
    - APG
    name: rest eternal
    source: default
    freq: At will
  - name: scrying
    source: default
    freq: At will
  - superscripts:
    - APG
    name: share language
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 25
  - name: tongues
    source: default
    freq: At will
  - name: circle of death
    source: default
    freq: 3/day
    DC: 26
  - name: forcecage
    source: default
    freq: 3/day
    DC: 27
  - name: miracle
    source: default
    freq: 3/day
    DC: 29
    other: see final judgment
  - name: quickened lightning bolt
    source: default
    freq: 3/day
    DC: 23
  - name: undeath to death
    source: default
    freq: 3/day
    DC: 26
  - name: soul bind
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any one CR 19
    - name: lower psychopomp
      chance: 100%
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 20
    concentration: 30
ability_scores:
  STR: 28
  DEX: 35
  CON: 27
  INT: 24
  WIS: 28
  CHA: 31
BAB: 25
CMB: 36
CMB_other: +38 bull rush, +40 grapple
CMD: 59
CMD_other: 61 vs. bull rush, 63 vs. trip
feats:
- name: Combat Reflexes
- name: Dodge
- name: Hover
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (lightning bolt)
- name: Spell Penetration
- name: Wind Stance
skills:
  Acrobatics: 37
    when jumping: 41
  Bluff: 38
  Diplomacy: 35
  Fly: 40
  Intimidate: 35
  Knowledge (arcana): 32
  Knowledge (planes): 35
  Knowledge (religion): 32
  Perception: 37
  Sense Motive: 37
  Spellcraft: 32
  Stealth: 32
  Swim: 42
  _racial_mods:
    Acrobatics:
      when jumping: 4
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Infernal
special_qualities:
- final judgment
- spirit touch
ecology:
  environment: any (Purgatory)
  organization: solitary
  treasure_type: standard
special_abilities:
  Breath Weapon (Su): In addition to its cold breath weapon, a yamaraj can breath
    a 60-foot cone of beetles and other insectile scavengers. Creatures in the breath
    weapon's area take 16d6 points of slashing damage and are nauseated for 1d4 rounds
    (Reflex 30 halves damage and negates nausea). The scavengers persist as a swarm
    around the affected creature that is closest to the breath weapon's point of origin;
    this swarm has the same statistics as an army ant swarm, but its distraction DC
    is the same as the yamaraj's breath weapon DC. The save DC is Constitution-based.
  Final Judgment (Su): 'A yamaraj can only use its miracle spell-like ability to restore
    a slain outsider to life or to reproduce the following spell effects: banishment,
    dimensional anchor, greater restoration, plane shift, true resurrection.'
  Lightning Drinker (Su): A yamaraj absorbs electricity to strengthen itself. If struck
    by an electrical attack, it heals 1 hit point per 3 points of electricity damage
    the attack would otherwise deal. If the amount of healing would cause the yamaraj
    to exceed its full normal hit points, it gains any excess as temporary hit points
    (up to a maximum of 100), which last up to 1 hour.
  Poison (Ex): Bite-injury; save Fort DC 30; frequency 1/round for 6 rounds; effect
    1d4 Dex drain; cure 3 consecutive saves.
desc_long: |-
  Equal parts regal and horrifying to mortal sensibilities, yamarajes preside as judges of death and dispensers of ultimate justice. Superstitions of the living call them by many names-the final judges, the grave magistrates, the dragons who eat men's souls-but all agree that these nobles of death wither even the stoutest hearts. The grave magistrates glide with authority throughout Purgatory, commanding flocks of lesser psychopomps, tolerating the ministrations of devils and angels bickering for souls of note, and ordering the endless procession of petitioners. Many also serve as diplomats or military commanders to maintain Purgatory's neutrality, but any such role is secondary to maintaining the flow of souls and the balance of the multiverse. Though in theory each yamaraj answers to the gods of death, in practice each is unquestioned within its own courtroom.

  Yamarajes vaguely resemble black dragons, though they are easily distinguished once one realizes the gigantic creatures are cloaked in feathers rather than scales. Each yamaraj measures at least 30 feet in length and weighs 4 tons. Despite their massive size and largely sedentary duties, yamarajes show astounding grace when they move.

  Impossibly old, yamarajes are outsiders forged from lesser psychopomps or the souls of legendary mortals. As with other outsiders, they need not eat, drink, or sleep to survive, and the grave magistrates normally remain perched upon Purgatory's ruins for months at a time, overseeing the smooth organization of their realm. Hard work wears at their immortal drive, and like living lords, they eagerly indulge in exquisite banquets during their infrequent personal time. These bacchanals make for strange bedfellows among outsiders, as solars and pit fiends may hobnob alongside one another, vying for the attention of a yamaraj to help organize the release of judged souls and attempting to win future favors.

  When called into physical action, all yamarajes can breathe raw decay in the form of clouds of carrion-eating insects, and their venom saps the youth and vitality from living creatures.

  Yamarajes serve as lower judges and lords of Purgatory, directing the activities of other outsiders there, presiding over the dead, pre-sorting souls destined for ultimate judgment by the death gods, and seeing to the efficiency and safety of the plane's infinite inhabitants. As the highest order of psychopomps, they are simultaneously the most dedicated to their role as shepherds of the dead and the most prone to impressing their own opinions on their work in the form of overturning precedents, rambling speeches, and extensive opinions attached to rulings. Such flexibility is necessary when making immortal decisions based on the ever-changing actions of the living, but frustrates more absolute outsiders to no end.

  Unsurprisingly, yamarajes tend to vary greatly from one individual to the next. Most develop deep interests in various worldly subjects that determine the sorts of mortals they ultimately choose to watch over. A given yamaraj might go out of its way to seek out artisans, followers of specific deities, or thieves, depending on its studies or whatever has come to interest it during that eon. Yamarajes might seek to guard such pet souls, ensuring their safe travels through Purgatory, learning more from the souls as they journey together, and ultimately advocating that the death gods grant a more peaceful judgment. Others act in reverse, finding certain sorts of mortals truly disgusting, tormenting their souls through their procession to the goddess's throne, and even suggesting that the spirits should face particularly monstrous damnations. How a yamaraj reacts to an individual thus proves unpredictable, depending on its changeable tastes. Such idiosyncrasies vary between individual yamarajes, and might change over the course of centuries.

  Just as many yamarajes become fascinated with souls possessing specific experiences or from certain backgrounds, some of the psychopomps go out of their way to judge beings from specific worlds, collecting bits of information and insight with every creature that passes them by. Thus, some become experts on one or multiple worlds, having spent eternities ferreting out the histories and secrets of worlds from firsthand accounts over millennia of inquiries. Many yamarajes welcome the opportunity to share the details of their investigations, though they sometimes see inquiries into their worlds of expertise as opportunities to conscript new allies to aid the psychopomps' cause. Standing at the pinnacle of their race, yamarajes are well informed as to the challenges and goals of many subservient psychopomps, and might only negotiate with mortals who perform a service in aid of their underlings.

---

# Psychopomp, Yamaraj
The head of this winged, dragonlike beast is crowned with long spines. Sooty feathers cover its body.
**Source** Bestiary 4 pg. 222, Pathfinder #48: Shadows of Gallowspire pg. 86
**XP** 307,200

N Huge outsider (extraplanar, psychopomp)
**Init** +16; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Thoughts|detect thoughts]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, spiritsense, _[[spells/True Seeing|true seeing]]_; Perception +37
**Aura** _[[universal monster rules/Fear|fear]]_ (30 ft., DC 32)

##### Defense

**AC** 40, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+4 armor, +12 Dex, +1 dodge, +15 natural, –2 size)
**hp** 337 (25d10+200); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +22, **Ref** +20, **Will** +25
**Defensive Abilities** lightning drinker; **DR** 15/adamantine; **Immune** cold, electricity, death effects, disease, poison; **SR** 31

##### Offense
**Speed** 40 ft., fly 60 ft. (good), swim 40 ft.
**Melee** bite +32 (2d6+9/19–20 plus _[[universal monster rules/Grab|grab]]_ and poison), 2 claws +32 (2d6+9), tail slap +30 (2d6+4), 2 wings +30 (1d8+4)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d6 cold, Reflex DC 30 half, usable every 1d4 rounds; or beetles), poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +30)
Constant—_detect thoughts_ (DC 22), _[[spells/Mage Armor|mage armor]]_, _true seeing_
At will—greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Reincarnate|reincarnate]]_, _[[spells/Rest Eternal|rest eternal]]_, _[[spells/Scrying|scrying]]_, _[[spells/Share Language|share language]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 25), _[[spells/Tongues|tongues]]_
3/day—_[[spells/Circle Of Death|circle of death]]_ (DC 26), _[[spells/Forcecage|forcecage]]_ (DC 27), _[[spells/Miracle|miracle]]_ (DC 29) (see final judgment), quickened _[[spells/Lightning Bolt|lightning bolt]]_ (DC 23), _[[spells/Undeath to Death|undeath to death]]_ (DC 26)
1/day—_[[spells/Soul Bind|soul bind]]_, _[[universal monster rules/Summon|summon]]_ (level 9, any one CR 19 or lower psychopomp 100%), _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 29)

##### Statistics
**Str** 28, **Dex** 35, **Con** 27, **Int** 24, **Wis** 28, **Cha** 31
**Base Atk** +25; **CMB** +36 (+38 bull rush, +40 grapple); **CMD** 59 (61 vs. bull rush, 63 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_lightning bolt_), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +37 (+41 when jumping), Bluff +38, Diplomacy +35, Fly +40, Intimidate +35, Knowledge (arcana) +32, Knowledge (planes) +35, Knowledge (religion) +32, Perception +37, Sense Motive +37, Spellcraft +32, Stealth +32, Swim +42; **Racial Modifiers** +4 Acrobatics when jumping
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Infernal
**SQ** final judgment, spirit touch

##### Ecology

**Environment** any (Purgatory)
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Su)** In addition to its cold _breath weapon_, a yamaraj can breath a 60-foot cone of beetles and other insectile scavengers. Creatures in the _breath weapon_’s area take 16d6 points of slashing damage and are _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds (Reflex 30 halves damage and negates nausea). The scavengers persist as a swarm around the affected creature that is closest to the _breath weapon_’s point of origin; this swarm has the same statistics as an army ant swarm, but its _[[universal monster rules/Distraction|distraction]]_ DC is the same as the yamaraj’s _breath weapon_ DC. The save DC is Constitution-based.

**Final Judgment (Su)** A yamaraj can only use its _miracle_ spell-like ability to restore a slain outsider to life or to reproduce the following spell effects: _[[spells/Banishment|banishment]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, greater _[[spells/Restoration|restoration]]_, _[[spells/Plane Shift|plane shift]]_, _[[spells/True Resurrection|true resurrection]]_.

**Lightning Drinker (Su)** A yamaraj absorbs electricity to strengthen itself. If struck by an electrical attack, it heals 1 hit point per 3 points of electricity damage the attack would otherwise deal. If the amount of healing would cause the yamaraj to exceed its full normal hit points, it gains any excess as temporary hit points (up to a maximum of 100), which last up to 1 hour.

**Poison (Ex)** Bite—injury; save Fort DC 30; frequency 1/round for 6 rounds; effect 1d4 Dex drain; cure 3 consecutive saves.

##### Description

Equal parts regal and horrifying to mortal sensibilities, yamarajes preside as judges of death and dispensers of ultimate justice. Superstitions of the living call them by many names—the final judges, the grave magistrates, the dragons who eat men’s souls—but all agree that these nobles of death wither even the stoutest hearts. The grave magistrates _[[spells/Glide|glide]]_ with authority throughout Purgatory, commanding flocks of lesser psychopomps, tolerating the ministrations of devils and angels bickering for souls of note, and ordering the endless procession of petitioners. Many also serve as diplomats or military commanders to maintain Purgatory’s neutrality, but any such role is secondary to maintaining the flow of souls and the balance of the multiverse. Though in theory each yamaraj answers to the gods of death, in practice each is unquestioned within its own courtroom.

Yamarajes vaguely resemble black dragons, though they are easily distinguished once one realizes the gigantic creatures are cloaked in feathers rather than scales. Each yamaraj measures at least 30 feet in length and weighs 4 tons. Despite their massive size and largely sedentary duties, yamarajes show astounding _[[spells/Grace|grace]]_ when they move.

Impossibly old, yamarajes are outsiders forged from lesser psychopomps or the souls of legendary mortals. As with other outsiders, they need not eat, drink, or sleep to survive, and the grave magistrates normally remain perched upon Purgatory’s ruins for months at a time, overseeing the smooth organization of their realm. Hard work wears at their immortal drive, and like living lords, they eagerly indulge in exquisite banquets during their infrequent personal time. These bacchanals make for strange bedfellows among outsiders, as solars and pit fiends may hobnob alongside one another, vying for the attention of a yamaraj to help organize the release of judged souls and attempting to win future favors.

When _[[items/Weapon Magic Abilities/Called|called]]_ into physical action, all yamarajes can breathe raw decay in the form of clouds of carrion-eating insects, and their venom saps the youth and vitality from living creatures.

Yamarajes serve as lower judges and lords of Purgatory, directing the activities of other outsiders there, presiding over the dead, pre-sorting souls destined for ultimate judgment by the death gods, and seeing to the efficiency and safety of the plane’s infinite inhabitants. As the highest order of psychopomps, they are simultaneously the most dedicated to their role as shepherds of the dead and the most _[[conditions/Prone|prone]]_ to impressing their own opinions on their work in the form of overturning precedents, rambling speeches, and extensive opinions attached to rulings. Such flexibility is necessary when making immortal decisions based on the ever-changing actions of the living, but frustrates more absolute outsiders to no end.

Unsurprisingly, yamarajes tend to vary greatly from one individual to the next. Most develop deep interests in various worldly subjects that determine the sorts of mortals they ultimately choose to watch over. A given yamaraj might go out of its way to seek out artisans, followers of specific deities, or thieves, depending on its studies or whatever has come to interest it during that eon. Yamarajes might seek to _[[npcs/Guard|guard]]_ such pet souls, ensuring their safe travels through Purgatory, learning more from the souls as they journey together, and ultimately advocating that the death gods grant a more _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_ judgment. Others act in reverse, finding certain sorts of mortals truly disgusting, tormenting their souls through their procession to the goddess’s throne, and even suggesting that the spirits should face particularly monstrous damnations. How a yamaraj reacts to an individual thus proves unpredictable, depending on its changeable tastes. Such idiosyncrasies vary between individual yamarajes, and might change over the course of centuries.

Just as many yamarajes become _[[conditions/Fascinated|fascinated]]_ with souls possessing specific experiences or from certain backgrounds, some of the psychopomps go out of their way to judge beings from specific worlds, collecting bits of information and insight with every creature that passes them by. Thus, some become experts on one or multiple worlds, having spent eternities ferreting out the histories and secrets of worlds from firsthand accounts over millennia of inquiries. Many yamarajes welcome the opportunity to share the details of their investigations, though they sometimes see inquiries into their worlds of expertise as opportunities to conscript new allies to aid the psychopomps’ cause. Standing at the pinnacle of their race, yamarajes are well informed as to the challenges and goals of many subservient psychopomps, and might only negotiate with mortals who perform a service in aid of their underlings.