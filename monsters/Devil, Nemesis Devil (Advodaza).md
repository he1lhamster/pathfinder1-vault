---
cssclass: [monsters]
title1: Devil, Nemesis Devil (Advodaza)
desc_short: This ancient monstrosity has the torso of a massively muscled giant,
title2: Nemesis Devil (Advodaza)
CR: 18
sources:
- name: Bestiary 4
  page: 54
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 153600
alignment: LE
size: Huge
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 11
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 36
  touch: 15
  flat_footed: 29
  components:
    armor: 7
    dex: 7
    natural: 14
    size: -2
HP:
  HP: 297
  long: 18d10+198
saves:
  fort: 21
  ref: 18
  will: 13
defensive_abilities:
- idol armor
DR:
- amount: 10
  weakness: good and silver
immunities:
- cold
- dismissal
- electricity
- fire
- poison
- sonic
resistances:
  acid: 10
SR: 29
speeds:
  base: 40
  fly: 80
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +28 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: bite
      bonus:
      - 28
    - text: 2 claws +28 (1d8+12 plus infernal wound)
      entries:
      - - damage: 1d8+12
        - effect: infernal wound
      count: 2
      attack: claws
      bonus:
      - 28
    - text: 2 slams +26 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: slams
      bonus:
      - 26
    - text: tail slap +26 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: tail slap
      bonus:
      - 26
  special:
  - infernal wound
space: 15
reach: 15
reach_other: 20 ft. with tail
spell_like_abilities:
  entries:
  - name: gaseous form
    source: default
    freq: At will
  - name: greater invisibility
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: scorching ray
    source: default
    freq: At will
  - name: whispering wind
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: 3/day
    DC: 24
  - name: dispel magic
    source: default
    freq: 3/day
  - name: ethereal jaunt
    source: default
    freq: 3/day
  - name: harm
    source: default
    freq: 3/day
    DC: 23
  - name: heal
    source: default
    freq: 3/day
    DC: 23
  - name: hold monster
    source: default
    freq: 3/day
    DC: 22
  - name: wall of stone
    source: default
    freq: 3/day
  - name: greater scrying
    source: default
    freq: 1/day
    DC: 21
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: horned devil
      chance: 60%
  - name: unhallow
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 23
ability_scores:
  STR: 34
  DEX: 25
  CON: 30
  INT: 23
  WIS: 25
  CHA: 24
BAB: 18
CMB: 32
CMB_other: +36 bull rush
CMD: 49
CMD_other: 51 vs. bull rush, 53 vs. trip
feats:
- name: Awesome Blow
- name: Flyby Attack
- name: Greater Bull Rush
- name: Hover
- name: Improved Bull Rush
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Toughness
skills:
  Acrobatics: 25
    when jumping: 29
  Bluff: 28
  Diplomacy: 28
  Fly: 24
  Intimidate: 28
  Knowledge (arcana): 27
  Knowledge (planes): 27
  Knowledge (religion): 27
  Perception: 28
  Sense Motive: 28
  Spellcraft: 24
  Stealth: 20
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
- telepathy 100 ft.
special_qualities:
- devil mark
- false divinity (Trickery)
ecology:
  environment: any (Hell)
  organization: solitary or pantheon (2-5)
  treasure_type: double
special_abilities:
  Devil Mark (Su): An advodaza can grant worthy servants a measure of its power. As
    a full-round action, an advodaza can touch a willing creature, marking it with
    a unique symbol. For as long as the creature is marked, it gains a spell-like
    ability it can use once per day. This spell-like ability comes from the advodaza's
    chosen domain (see false divinity, below). The target can also telepathically
    communicate with the advodaza over any distance while on the same plane. An advodaza
    can dismiss its mark as a standard action, no matter where the bearer is. It can
    also, as a standard action, cause pain to a mark bearer that deals 6d6 points
    of damage with no saving throw. An advodaza can mark multiple creatures, up to
    a number equal to its Hit Dice (typically 18).
  False Divinity (Su): |-
    Each advodaza chooses one cleric domain and gains the domain spells (5th level and lower) of that domain as spell-like abilities. Each of these abilities can be used 3 times per day. The advodaza does not gain any of the domain's granted powers. Most advodazas possess powers from the Evil, Fire, Law, Trickery, War, or Weather domains, though any domains except Good or Chaos are possible. These spell-like abilities are not included in the stat block above.

    Evil Domain: align weapon (evil only), dispel good, magic circle against good, protection from good, unholy blight
     Fire Domain: burning hands, fire shield, fireball, produce flame, wall of fire
     Law Domain: align weapon (law only), dispel chaos, magic circle against chaos, order's wrath, protection from chaos
     Trickery Domain: confusion, disguise self, false vision, invisibility, nondetection
     War Domain: divine power, flame strike, magic vestment, magic weapon, spiritual weapon
     Weather Domain: call lightning, fog cloud, ice storm, obscuring mist, sleet storm
  Idol Armor (Su): Advodazas armor themselves in fallen idols and ornaments of devotion.
    This armor grants an advodaza a +7 armor bonus to AC and immunity to cold, electricity,
    and sonic damage, as well as immunity to the spell dismissal. The spells chaos
    hammer, holy smite, holy word, and word of chaos destroy this armor, removing
    the devil's armor bonus to AC and its immunities (its cold immunity is replaced
    with the devil's normal cold resistance of 10). The armor is automatically destroyed
    if the advodaza is slain. If uninterrupted for 1 hour, an advodaza can summon
    new armor to replace its destroyed protection.
  Infernal Wound (Su): An advodaza's assaults leave vicious marks that do not easily
    heal. The damage an advodaza inflicts with its claws leaves persistent wounds
    that deal 2d6 points of bleed damage. Bleeding caused in this way is difficult
    to stanch-a successful DC 29 Heal check is required to stop the bleeding, and
    anyone attempting to magically heal a creature suffering from an infernal wound
    must succeed at a DC 29 caster level check or the spell does not function. Success
    indicates the healing works normally and stops all bleed effects. The Heal check
    DC and caster level DC are Constitution-based.
desc_long: |-
  False gods, fallen demagogues, nemesis devils-all are names for the fiends known collectively as advodazas. They survive from dark ages past, when mortals offered worship to base things and unwholesome spirits that masqueraded as baleful gods. Although time and faith have turned against these beings, the most tenacious of their kind have refused to fade into oblivion, and to these obstinate corruptors and one-time deities the gates of Hell swing wide and welcoming. These lords of cults and masters of forgotten mysteries find renewed vigor in the depths of the Pit, and those seeking to restore their power and lordship over mortalkind undergo terrible indoctrinations and binding rites that transform them over the ages into true devils. What emerge are shades of half-remembered demigods, fallen princes seeking to claim their subjects anew, and fiends of blasphemy: the idol-clad advodazas.

  Fantastically ancient beings, advodazas rose from spirits worshiped by mortals in distant ages, typically as part of primitive and deranged cults. While humanoids still huddled in crude shelters, begging any power that would listen to protect them from storms, beasts, enemies, hunger, and countless other fears, the spirits of the land, sky, and animals were the first to give heed. Not deities, but elusive inf luences, these forces heard the early prayers and worked what appeared to be miracles in return for sacrifices and adoration. Slowly, these formless vestiges took shape as idols, fetishes, palladia, and all manner of cult images. Yet as knowledge of true deities and the powers they offered worshipers spread, the old spirits were either forgotten or demonized and rooted out.

  All advodazas desire to eventually return to the Material Plane, where they might tempt new followers to serve, sacrifice, and raise idols to their names. Though merciless, advodazas appeal to many mortals because of the directness of their interaction and their willingness to grant power or to violently smite enemies for a seemingly paltry price. In death, however, advodazas' servants find no divine realm, nor do they sit beside some grand deity. When they die, there is only Hell.

  No two advodazas look exactly alike. Each one embodies the powers and spheres of influence for which it was worshiped in ages past and subsequently anthropomorphized as a monstrous being. Typically, this results in quadrupedal and half-bestial shapes that bristle with terrible wings, hooves, claws, and fangs. Universally, though, they bear the broken remnants of their fallen faith-in the form of cracked idols worn like armor, profane talismans crafted into jewelry, or fearful totems wielded like massive weapons-and bristle with archaic power and unquenchable arrogance. Despite this wide range of appearances, all advodazas possess the same core abilities, though some particularly ancient or powerful fiends possess augmented or even unique abilities.

  Most advodazas stand about 18 feet tall and weigh approximately 9 tons.

---

# Devil, Nemesis Devil (Advodaza)
This ancient monstrosity has the torso of a massively muscled giant,
**Source** Bestiary 4 pg. 54
**XP** 153,600

LE Huge outsider (devil, evil, extraplanar, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +28

##### Defense

**AC** 36, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+7 armor, +7 Dex, +14 natural, –2 size)
**hp** 297 (18d10+198)
**Fort** +21, **Ref** +18, **Will** +13
**Defensive Abilities** idol armor; **DR** 10/good and silver; **Immune** cold, _[[spells/Dismissal|dismissal]]_, electricity, fire, poison, sonic; **Resist** acid 10; **SR** 29

##### Offense
**Speed** 40 ft., fly 80 ft. (average)
**Melee** bite +28 (2d6+12), 2 claws +28 (1d8+12 plus infernal wound), 2 slams +26 (1d8+6), tail slap +26 (2d6+6)
**Space** 15 ft., **Reach** 15 ft. (20 ft. with tail)
**Special Attacks** infernal wound
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
At will—_[[spells/Gaseous Form|gaseous form]]_, greater _[[spells/Invisibility, Greater|invisibility, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Harm|harm]]_ (DC 23), _[[spells/Heal|heal]]_ (DC 23), _[[spells/Hold Monster|hold monster]]_ (DC 22), _[[spells/Wall Of Stone|wall of stone]]_
1/day—greater _[[spells/Scrying|scrying]]_ (DC 21), _[[universal monster rules/Summon|summon]]_ (level 7, horned devil 60%), _[[spells/Unhallow|unhallow]]_

##### Statistics
**Str** 34, **Dex** 25, **Con** 30, **Int** 23, **Wis** 25, **Cha** 24
**Base Atk** +18; **CMB** +32 (+36 bull rush); **CMD** 49 (51 vs. bull rush, 53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +25 (+29 when jumping), Bluff +28, Diplomacy +28, Fly +24, Intimidate +28, Knowledge (arcana, planes, religion) +27, Perception +28, Sense Motive +28, Spellcraft +24, Stealth +20; **Racial Modifier** +4 Acrobatics when jumping
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** devil mark, false divinity (Trickery)

##### Ecology

**Environment** any (Hell)
**Organization** solitary or pantheon (2–5)
**Treasure** double

### Special Abilities

**Devil Mark (Su)** An advodaza can grant worthy servants a measure of its power. As a full-round action, an advodaza can touch a willing creature, marking it with a unique symbol. For as long as the creature is marked, it gains a spell-like ability it can use once per day. This spell-like ability comes from the advodaza’s chosen domain (see false divinity, below). The target can also telepathically communicate with the advodaza over any distance while on the same plane. An advodaza can dismiss its mark as a standard action, no matter where the bearer is. It can also, as a standard action, cause pain to a mark bearer that deals 6d6 points of damage with no saving throw. An advodaza can mark multiple creatures, up to a number equal to its Hit Dice (typically 18).

**False Divinity (Su)** Each advodaza chooses one _[[classes/Cleric|cleric]]_ domain and gains the domain spells (5th level and lower) of that domain as _spell-like abilities_. Each of these abilities can be used 3 times per day. The advodaza does not gain any of the domain’s granted powers. Most advodazas possess powers from the Evil, Fire, Law, Trickery, War, or Weather domains, though any domains except Good or Chaos are possible. These _spell-like abilities_ are not included in the stat block above.

Evil Domain: _[[spells/Align Weapon|align weapon]]_ (evil only), _[[spells/Dispel Good|dispel good]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Unholy Blight|unholy blight]]_
 Fire Domain: _[[spells/Burning Hands|burning hands]]_, _[[spells/Fire Shield|fire shield]]_, _[[spells/Fireball|fireball]]_, _[[spells/Produce Flame|produce flame]]_, _[[spells/Wall Of Fire|wall of fire]]_
 Law Domain: _align weapon_ (law only), _[[spells/Dispel Chaos|dispel chaos]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, order’s wrath, _[[spells/Protection From Chaos|protection from chaos]]_
 Trickery Domain: _[[spells/Confusion|confusion]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/False Vision|false vision]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Nondetection|nondetection]]_
 War Domain: _[[spells/Divine Power|divine power]]_, _[[spells/Flame Strike|flame strike]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
 Weather Domain: _[[spells/Call Lightning|call lightning]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sleet Storm|sleet storm]]_

**Idol Armor (Su)** Advodazas armor themselves in _[[monsters/Fallen|fallen]]_ idols and ornaments of devotion. This armor grants an advodaza a +7 armor bonus to AC and _[[universal monster rules/Immunity|immunity]]_ to cold, electricity, and sonic damage, as well as _immunity_ to the spell _dismissal_. The spells _[[spells/Chaos Hammer|chaos hammer]]_, _[[spells/Holy Smite|holy smite]]_, _[[spells/Holy Word|holy word]]_, and _[[spells/Word Of Chaos|word of chaos]]_ destroy this armor, removing the devil’s armor bonus to AC and its immunities (its cold _immunity_ is replaced with the devil’s normal cold _[[universal monster rules/Resistance|resistance]]_ of 10). The armor is automatically destroyed if the advodaza is slain. If uninterrupted for 1 hour, an advodaza can _summon_ new armor to replace its destroyed protection.

**Infernal Wound (Su)** An advodaza’s assaults leave _[[items/Weapon Magic Abilities/Vicious|vicious]]_ marks that do not easily _heal_. The damage an advodaza inflicts with its claws leaves persistent wounds that deal 2d6 points of _[[universal monster rules/Bleed|bleed]]_ damage. Bleeding caused in this way is difficult to stanch—a successful DC 29 _Heal_ check is required to stop the bleeding, and anyone attempting to magically _heal_ a creature suffering from an infernal wound must succeed at a DC 29 caster level check or the spell does not function. Success indicates the healing works normally and stops all _bleed_ effects. The _Heal_ check DC and caster level DC are Constitution-based.

##### Description

False gods, _fallen_ demagogues, _[[feats/Nemesis|nemesis]]_ devils—all are names for the fiends known collectively as advodazas. They survive from dark ages past, when mortals offered worship to base things and unwholesome spirits that masqueraded as baleful gods. Although time and faith have turned against these beings, the most tenacious of their kind have refused to fade into _[[monsters/Oblivion|oblivion]]_, and to these obstinate corruptors and one-time deities the gates of Hell swing wide and welcoming. These lords of cults and masters of forgotten mysteries find renewed _[[spells/Vigor|vigor]]_ in the depths of the Pit, and those seeking to restore their power and lordship over mortalkind undergo terrible indoctrinations and _[[spells/Binding|binding]]_ rites that transform them over the ages into true devils. What emerge are _[[spells/Shades|shades]]_ of half-remembered demigods, _fallen_ princes seeking to claim their subjects anew, and fiends of _blasphemy_: the idol-clad advodazas.

Fantastically ancient beings, advodazas rose from spirits worshiped by mortals in distant ages, typically as part of primitive and deranged cults. While humanoids still huddled in crude shelters, begging any power that would listen to protect them from storms, beasts, enemies, hunger, and countless other fears, the spirits of the land, sky, and animals were the first to give heed. Not deities, but elusive inf luences, these forces heard the early prayers and worked what appeared to be miracles in return for sacrifices and _[[spells/Adoration|adoration]]_. Slowly, these formless vestiges took shape as idols, fetishes, palladia, and all manner of cult images. Yet as knowledge of true deities and the powers they offered worshipers spread, the old spirits were either forgotten or demonized and rooted out.

All advodazas desire to eventually return to the Material Plane, where they might tempt new followers to serve, _[[spells/Sacrifice|sacrifice]]_, and raise idols to their names. Though merciless, advodazas appeal to many mortals because of the directness of their interaction and their willingness to grant power or to violently smite enemies for a seemingly paltry price. In death, however, advodazas’ servants find no divine realm, nor do they sit beside some grand deity. When they die, there is only Hell.

No two advodazas look exactly alike. Each one embodies the powers and spheres of influence for which it was worshiped in ages past and subsequently anthropomorphized as a monstrous being. Typically, this results in quadrupedal and half-bestial shapes that _[[spells/Bristle|bristle]]_ with terrible wings, hooves, claws, and fangs. Universally, though, they bear the _[[conditions/Broken|broken]]_ remnants of their _fallen_ faith—in the form of cracked idols worn like armor, profane talismans crafted into _[[items/Mundane/Jewelry|jewelry]]_, or fearful totems wielded like massive weapons—and _bristle_ with archaic power and unquenchable arrogance. Despite this wide range of appearances, all advodazas possess the same core abilities, though some particularly ancient or powerful fiends possess augmented or even unique abilities.

Most advodazas stand about 18 feet tall and weigh approximately 9 tons.