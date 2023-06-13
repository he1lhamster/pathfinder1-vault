---
cssclass: [monsters]
title1: Archdevil, Baalzebul
desc_short: This swarm of droning black f lies teems in the semblance of awinged angel
  with glowing red eyes.
title2: Baalzebul
CR: 30
sources:
- name: Bestiary 6
  page: 16
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9830400
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 14
senses:
  blindsight: 120
  darkvision: 60
  detect chaos: true
  detect good: true
  see in darkness: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 39
- name: shield of law
  DC: 30
AC:
  AC: 48
  touch: 40
  flat_footed: 37
  components:
    deflection: 4
    dex: 10
    dodge,+8 natural: 1
    profane: 16
    size: -1
HP:
  HP: 717
  long: 35d10+525
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 30
  ref: 30
  will: 36
  other: +8 vs. mind-affecting effects
defensive_abilities:
- infernal resurrection
- mind blank
- swarmbody
- usurpation
DR:
- amount: 20
  weakness: epic, good, and silver
immunities:
- ability damage
- ability drain
- charm
- cold
- compulsion
- deatheffects
- disease
- energy drain
- fire
- petrification
- poison
resistances:
  acid: 30
SR: 41
speeds:
  fly: 120
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +5 adamantine good-outsider-bane icy burst unholylongsword +53/+48/+43/+38
        (2d6+24/17-20 plus 1d6 cold) or2 slams +47 (8d6+13)
      entries:
      - - damage: 8d6+13
      attack: +5 adamantine good-outsider-bane icy burst unholylongsword +53/+48/+43/+38
        (2d6+24/17-20 plus 1d6 cold) or2 slams
      bonus:
      - 47
  special:
  - biting blackflies
  - hellfrost
  - suffocating swarm
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: shield of law
    source: default
    freq: Constant
    DC: 30
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - name: curse of disgust
    source: default
    freq: At will
    DC: 27
  - is_mythic_spell: true
    name: desecrate
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dictum
    source: default
    freq: At will
    DC: 29
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater invisibility
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: icy prison
    source: default
    freq: At will
    DC: 27
  - name: insect plague
    source: default
    freq: At will
  - is_mythic_spell: true
    name: order's wrath
    source: default
    freq: At will
    DC: 26
  - name: unhallow
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
    DC: 30
  - is_mythic_spell: true
    name: finger of death
    source: default
    freq: 3/day
    DC: 29
  - name: quickened freezing sphere
    source: default
    freq: 3/day
  - is_mythic_spell: true
    name: empowered cone of cold
    source: default
    freq: 3/day
  - name: summon devils
    source: default
    freq: 3/day
  - name: mass suffocation
    source: default
    freq: 1/day
    DC: 31
  - is_mythic_spell: true
    name: time stop
    source: default
    freq: 1/day
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 42
    mythic_restriction: Baalzebul can use this ability's mythic version in his infernal
      realm.
ability_scores:
  STR: 36
  DEX: 30
  CON: 41
  INT: 35
  WIS: 32
  CHA: 35
BAB: 35
CMB: 49
CMD: 90
CMD_other: can't be tripped
feats:
- name: Critical Focus
- name: Dazzling Display
- name: Dodge
- name: Empower Spell-Like Ability (cone of cold)
- name: Flyby Attack
- name: Improved Critical(longsword)
- name: Improved Initiative
- name: Improved Iron Will
- name: IronWill
- name: Lightning Stance
- name: Mobility
- name: Power Attack
- name: QuickenSpell-Like Ability (freezing sphere)
- name: Shatter Defenses
- name: Sickening Critical
- name: Skill Focus (Bluff)
- name: Weapon Focus(longsword)
- name: Wind Stance
skills:
  Acrobatics: 48
  Bluff: 56
  Diplomacy: 50
  Disguise: 50
  Fly: 54
  Intimidate: 50
  Knowledge (arcana): 47
  Knowledge (history,local): 47
  Knowledge (nobility): 47
  Knowledge (religion): 47
  Knowledge (planes): 50
  Linguistics: 50
  Perception: 49
  Sense Motive: 49
  Spellcraft: 47
  Stealth: 44
  Use Magic Device: 47
languages:
- all (language mastery)
- telepathy 300 ft.
special_qualities:
- lord of the flies
- swarm master
ecology:
  environment: any (Hell)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - +5 adamantine good-outsider-bane icy burstunholy longsword
  - other treasure
special_abilities:
  Biting Blackflies (Ex): Baalzebul's body consists of innumerable flies. The first
    time in a round a creature strikes him with a melee touch attack, natural attack,
    or unarmed strike, the creature is subjected to these flies' savage stings and
    bites. The creature takes 7d6 points of damage and must succeed at a DC 42 Fortitude
    save or become nauseated with pain for 1 round. These biting flies cling tenaciously
    to the attacker for 1 round, dealing 7d6 points of damage on the attacker's next
    turn (but not threatening nausea). Any damage from an area effect destroys clinging
    flies, though they share Baalzebul's resistances and immunities, including spell
    resistance. If Baalzebul does not move more than 5 feet in a round, any creature
    that approaches or begins its turn within 10 feet of him is affected in the same
    way. Any number of targets can be affected in a round by the biting blackflies,
    but no more than once per round per target. The save DC is Constitution-based.
  Hellfrost (Su): Half of any cold damage dealt by Baalzebul is unholy damage that
    is not reduced by cold resistance or cold immunity. Devils are immune to this
    unholy damage, but it is doubled against creatures with the good subtype.
  Lord of the Flies (Su): Any creature flying under its own power (not by means of
    a magic item, spell, or spell-like ability) that tries to attack Baalzebul in
    melee must succeed at a DC 39 Will save or the attack fails and is wasted. In
    addition, if it fails the save, the attacker is so awed by Baalzebul's majesty
    that it cannot look at him directly for 1d4 rounds. Creatures that succeed at
    the save are immune to this effect for 24 hours. This is a mind-affecting effect.
    The save DC is Charisma-based.
  Suffocating Swarm (Su): Baalzebul can collapse into a swarm of flies or reform his
    body as a free action; when he is discorporated, his sword becomes part of the
    swarm and his Strength score becomes 1. Baalzebul functions as a true swarm of
    Fine creatures when discorporated, filling four squares as he chooses, and has
    a swarm attack that deals 7d6+26 points of damage. Any creature that fails at
    a DC 42 Fortitude save against his distraction attack is nauseated and begins
    suffocating, as a suffocation spell (CL 30th). If killed by this suffocation,
    the creature arises 1 minute later infested by a hellwasp swarm (a successful
    DC 42 Fortitude save immediately before death negates). The save DCs are Constitution-based.
  Swarm Body (Ex): Baalzebul's body is composed of millions of tiny flies. He can
    pass without difficulty through narrow holes, openings, and cracks as if in gaseous
    form. He has no discernible anatomy and is not subject to critical hits or flanking,
    and he takes only half damage from attacks dealing bludgeoning, piercing, or slashing
    damage. If reduced below 0 hit points, he discorporates into a suffocating swarm
    (as above) and is staggered, but does not fall unconscious. Baalzebul is immune
    to any physical spell or effect that targets a specific number of creatures (including
    single target spells and rays) unless he chooses to target himself with such effects,
    though he is still subject to mind-affecting effects. He takes half again as much
    damage (+50%) from area effects, including splash weapons. Baalzebul is treated
    as a single Large creature for the purpose of wind effects.
  Swarm Master (Su): Baalzebul is immune to swarm damage and swarm effects (such as
    distraction). As a swift action, he can direct the movement of any unintelligent
    swarm within 30 feet.
  Usurpation (Su): When a creature within 30 feet targets itself with a spell or effect,
    as an immediate action Baalzebul can gain the same effects as the caster (including
    interacting normally with a caster using time stop). Baalzebul can have only one
    usurped spell effect at a time; copying a new effect causes him to forfeit any
    previously copied effect.
desc_long: |-
  Baalzebul was once the chief lieutenant of the Prince of Darkness. The glorious Hell's Angel sought to rule at Asmodeus's side, but he was greatly vexed at being relegated to stand alongside other archdevils. When he demanded a higher station, claiming he should rule over multitudes, the Lord of Hell annihilated his magnificent angelic form, replacing it with swarms of insects so he might rule over them in their millions as Lord of the Flies. Chastened, Baalzebul has brooded on vengeance ever since, harboring an insatiable urge to prove himself greatest among Hell's lords. His knowledge and power are vast, but so are his caprice, ego, love of flattery, and tendency to lash out at any perceived slight. 

  Baalzebul resembles a 15-foot-tall armored angel and has a body composed of flies.

---

# Archdevil, Baalzebul
This swarm of droning black f lies teems in the semblance of a

winged angel with glowing red eyes.
**Source** Bestiary 6 pg. 16
**XP** 9,830,400

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +14; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_,

_[[spells/Detect Good|detect good]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +49
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 39), _[[spells/Shield of Law|shield of law]]_ (DC 30)

##### Defense

**AC** 48, touch 40, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+4 deflection, +10 Dex, +1 _[[feats/Dodge|dodge]]_,

+8 natural, +16 profane, –1 size)
**hp** 717 (35d10+525); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +30, **Ref** +30, **Will** +36; +8 vs. mind-affecting effects
**Defensive Abilities** infernal _[[spells/Resurrection|resurrection]]_, _[[spells/Mind Blank|mind blank]]_, swarm

body, usurpation; **DR** 20/epic, good, and silver; **Immune** ability damage, ability drain, charm, cold, compulsion, death

effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, fire, petrification, poison; **Resist** acid 30; **SR** 41

##### Offense
**Speed** fly 120 ft. (perfect)
**Melee** +5 adamantine good-outsider-bane _[[items/Weapon Magic Abilities/Icy Burst|icy burst]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_

_[[items/Weapon/Longsword|longsword]]_ +53/+48/+43/+38 (2d6+24/17–20 plus 1d6 cold) or

2 slams +47 (8d6+13)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** biting blackflies, hellfrost, suffocating swarm
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +42)
Constant—_detect chaos_, _detect good_, _mind blank_, _shield of law_ (DC 30), _true seeing_ 
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Curse Of Disgust|curse of disgust]]_ (DC 27), _[[spells/Desecrate|desecrate]]_, _[[spells/Dictum|dictum]]_ (DC 29), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Invisibility, Greater|invisibility, greater]]_ teleport, _[[spells/Icy Prison|icy prison]]_ (DC 27), _[[spells/Insect Plague|insect plague]]_, order’s wrath (DC 26), _[[spells/Unhallow|unhallow]]_ 
3/day—_[[spells/Demand|demand]]_ (DC 30), _[[spells/Finger Of Death|finger of death]]_ (DC 29), quickened _[[spells/Freezing Sphere|freezing sphere]]_, empowered _[[spells/Cone of Cold|cone of cold]]_, _[[universal monster rules/Summon|summon]]_ devils 
1/day—mass _[[spells/Suffocation|suffocation]]_ (DC 31), _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_ 
 Baalzebul can use this ability’s mythic version in his infernal realm.

##### Statistics
**Str** 36, **Dex** 30, **Con** 41, **Int** 35, **Wis** 32, **Cha** 35
**Base Atk** +35; **CMB** +49; **CMD** 90 (can’t be tripped)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _Dodge_, Empower Spell-

Like Ability (_cone of cold_), _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_

(_longsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, Iron

Will, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, Quicken

Spell-Like Ability (_freezing sphere_), _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Skill Focus|Skill Focus]]_ (Bluff), _[[feats/Weapon Focus|Weapon Focus]]_

(_longsword_), _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +48, Bluff +56, Diplomacy +50, Disguise +50,

Fly +54, Intimidate +50, Knowledge (arcana, history,

local, nobility, religion) +47, Knowledge (planes) +50,

Linguistics +50, Perception +49, Sense Motive +49,

Spellcraft +47, Stealth +44, Use Magic Device +47
**Languages** all (language mastery); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** lord of the flies, swarm master

##### Ecology

**Environment** any (Hell)
**Organization** solitary (unique)
**Treasure** triple (+5 adamantine good-outsider-bane _icy burst_

_unholy_ _longsword_, other treasure)

### Special Abilities

**Biting Blackflies (Ex)** Baalzebul’s body consists of innumerable flies. The first time in a round a creature strikes him with a melee touch attack, natural attack, or unarmed strike, the creature is subjected to these flies’ savage stings and bites. The creature takes 7d6 points of damage and must succeed at a DC 42 Fortitude save or become _[[conditions/Nauseated|nauseated]]_ with pain for 1 round. These biting flies cling tenaciously to the attacker for 1 round, dealing 7d6 points of damage on the attacker’s next turn (but not threatening nausea). Any damage from an area effect destroys clinging flies, though they share Baalzebul’s resistances and immunities, including _[[universal monster rules/Spell Resistance|spell resistance]]_. If Baalzebul does not move more than 5 feet in a round, any creature that approaches or begins its turn within 10 feet of him is affected in the same way. Any number of targets can be affected in a round by the biting blackflies, but no more than once per round per target. The save DC is Constitution-based.

**Hellfrost (Su)** Half of any cold damage dealt by Baalzebul is _unholy_ damage that is not reduced by cold _[[universal monster rules/Resistance|resistance]]_ or cold _[[universal monster rules/Immunity|immunity]]_. Devils are immune to this _unholy_ damage, but it is doubled against creatures with the good subtype.

**Lord of the Flies (Su)** Any creature flying under its own power (not by means of a magic item, spell, or spell-like ability) that tries to attack Baalzebul in melee must succeed at a DC 39 Will save or the attack fails and is wasted. In addition, if it fails the save, the attacker is so awed by Baalzebul’s majesty that it cannot look at him directly for 1d4 rounds. Creatures that succeed at the save are immune to this effect for 24 hours. This is a mind-affecting effect. The save DC is Charisma-based.
**Suffocating Swarm (Su)** Baalzebul can collapse into a swarm of flies or reform his body as a free action; when he is discorporated, his sword becomes part of the swarm and his Strength score becomes 1. Baalzebul functions as a true swarm of Fine creatures when discorporated, filling four squares as he chooses, and has a swarm attack that deals 7d6+26 points of damage. Any creature that fails at a DC 42 Fortitude save against his _[[universal monster rules/Distraction|distraction]]_ attack is _nauseated_ and begins suffocating, as a _suffocation_ spell (CL 30th). If killed by this _suffocation_, the creature arises 1 minute later infested by a _[[monsters/Hellwasp Swarm|hellwasp swarm]]_ (a successful DC 42 Fortitude save immediately before death negates). The save DCs are Constitution-based.
**Swarm Body (Ex)** Baalzebul’s body is composed of millions of tiny flies. He can pass without difficulty through narrow holes, openings, and cracks as if in _[[spells/Gaseous Form|gaseous form]]_. He has no discernible anatomy and is not subject to critical hits or flanking, and he takes only half damage from attacks dealing bludgeoning, piercing, or slashing damage. If reduced below 0 hit points, he discorporates into a suffocating swarm (as above) and is _[[conditions/Staggered|staggered]]_, but does not fall _[[conditions/Unconscious|unconscious]]_. Baalzebul is immune to any physical spell or effect that targets a specific number of creatures (including single target spells and rays) unless he chooses to target himself with such effects, though he is still subject to mind-affecting effects. He takes half again as much damage (+50%) from area effects, including splash weapons. Baalzebul is treated as a single Large creature for the purpose of wind effects.
**Swarm Master (Su)** Baalzebul is immune to swarm damage and swarm effects (such as _distraction_). As a swift action, he can direct the movement of any unintelligent swarm within 30 feet.

**Usurpation (Su)** When a creature within 30 feet targets itself with a spell or effect, as an immediate action Baalzebul can gain the same effects as the caster (including interacting normally with a caster using _time stop_). Baalzebul can have only one usurped spell effect at a time; copying a new effect causes him to forfeit any previously copied effect.

##### Description

Baalzebul was once the chief lieutenant of the Prince of _[[spells/Darkness|Darkness]]_. The _[[items/Weapon Magic Abilities/Glorious|glorious]]_ Hell’s Angel sought to rule at Asmodeus’s side, but he was greatly vexed at being relegated to stand alongside other archdevils. When he demanded a higher station, claiming he should rule over multitudes, the Lord of Hell annihilated his magnificent angelic form, replacing it with swarms of insects so he might rule over them in their millions as Lord of the Flies. Chastened, Baalzebul has brooded on _[[feats/Vengeance|vengeance]]_ ever since, harboring an insatiable urge to prove himself greatest among Hell’s lords. His knowledge and power are vast, but so are his caprice, ego, love of flattery, and tendency to lash out at any perceived slight.

Baalzebul resembles a 15-foot-tall armored angel and has a body composed of flies.