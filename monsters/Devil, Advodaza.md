---
cssclass: [monsters]
title1: Devil, Advodaza
desc_short: The rending, thunderous clangor of rushing claws heralds the charge of
  this fire-eyed ruin, a terror of flame-seared hide and saber-like spines shaped
  in a monstrously muscled centauric form. The true terrible ferocity of the thing
  lies hidden, restrained beneath armor and wings of crumbling stone carved with icons
  as ancient as they are undeniable and profane.
title2: Advodaza
CR: 18
sources:
- name: 'Pathfinder #30: The Twice-Damned Prince'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8d54
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
  AC: 35
  touch: 15
  flat_footed: 28
  components:
    armor: 6
    dex: 7
    natural: 14
    size: -2
HP:
  HP: 297
  long: 18d10+198
saves:
  fort: 21
  ref: 18
  will: 15
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
    - text: 2 claws +28 (1d8+12 plus infernal wounds)
      entries:
      - - damage: 1d8+12
        - effect: infernal wounds
      count: 2
      attack: claws
      bonus:
      - 28
    - text: 2 hooves +26 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: hooves
      bonus:
      - 26
    - text: tail +26 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: tail
      bonus:
      - 26
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
    DC: 21
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
  - name: scrying
    source: default
    freq: 1/day
    DC: 22
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
CMD: 49
CMD_other: 53 vs. trip
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
  Bluff: 28
  Diplomacy: 28
  Escape Artist: 25
  Fly: 24
  Intimidate: 28
  Knowledge (arcana): 27
  Knowledge (planes): 27
  Knowledge (religion): 27
  Perception: 28
  Sense Motive: 28
  Spellcraft: 24
  Stealth: 20
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
- false divinity
ecology:
  environment: any (Hell)
  organization: solitary or pantheon (2-5)
  treasure_type: double
special_abilities:
  Devil Mark (Su): An advodaza can grant worthy servants a measure of its power. As
    a full-round action, an advodaza can touch a willing adjacent creature, marking
    it with a unique symbol similar to an arcane mark. This symbol can be either visible
    or invisible, as the devil chooses. For as long as the target possesses the mark,
    it gains a spell-like ability it can use once per day. This spell-like ability
    comes from the advodaza's chosen domain (see the false divinity ability). The
    target also gains the ability to telepathically communicate with the advodaza
    over any distance as long as the two creatures are on the same plane. An advodaza
    can mark multiple creatures, up to an amount equaling its Hit Dice (typically
    18). An advodaza can dispel its mark as a standard action, no matter where the
    bearer is. It can also, as a standard action, deal pain to a mark bearer that
    causes 6d6 points of damage with no saving throw. An advodaza's mark cannot be
    removed physically, but a dispel magic or erase spell that succeeds on a dispel
    check or caster level check of DC 30 removes the effect.
  False Divinity (Su): |-
    Advodazas possess areas of concern as deities do, but on a far smaller scale. Each advodaza chooses one cleric domain and gains the domain spells (up to 5th level) of that domain as spell-like abilities, each of which it can use 3 times per day. The advodaza does not gain any of the domain's granted powers. Most advodazas possess powers from the Evil, Fire, Law, War, or Weather domains, though any domain is possible.

    Evil Domain: align weapon (evil only), dispel good, magic circle against good, protection from good, unholy blight

    Fire Domain: burning hands, fire shield, fireball, produce flame, wall of fire

    Law Domain: align weapon (law only), dispel chaos, magic circle against chaos, order's wrath, protection from chaos

    War Domain: divine power, flame strike, magic vestment, magic weapon, spiritual weapon

    Weather Domain: call lightning, fog cloud, ice storm, obscuring mist, sleet storm
  Idol Armor (Su): Advodazas armor themselves in their fallen idols and ornaments
    of devotion. This armor grants an advodaza a +6 armor bonus to AC and immunity
    to cold, electricity, and sonic damage, as well as immunity to the spell dismissal.
    The spells chaos hammer, holy smite, holy word, and word of chaos destroy this
    armor, removing the devil's armor bonus to AC and immunities (its cold immunity
    decreases to its normal resistance 10). If uninterrupted for 1 hour, an advodaza
    can summon new armor to replace its destroyed protection.
  Infernal Wound (Su): The damage an advodaza deals with its claws causes persistent
    wounds that deal 2d6 points of bleed damage. Bleeding caused in this way is difficult
    to stanch-a DC 30 Heal check stops the damage, and any attempt to heal a creature
    suffering from an infernal wound must succeed on a DC 30 caster level check or
    the spell does not function. Success indicates the healing works normally and
    stops all bleed effects. The Heal check and caster level DC are Constitution-based.
desc_long: |-
  False gods, fallen demagogues, nemesis devils-the fiends known collectively as advodazas survive from dark ages past, when mortals offered worship to base things and unwholesome spirits masqueraded as baleful gods. Although time and faith have turned against these beings, the most tenacious of their kind have refused to fade into oblivion, and to these obstinate corruptors and one-time deities the gates of Hell swing wide and welcoming. These lords of cults and masters of forgotten mysteries find renewed vigor in the depths of the Pit, and those seeking to renew their power and lordship over mortalkind undergo terrible indoctrinations and binding rites that transform them over the ages into true devils. What emerge are eidolons of half-remembered demigods, fallen princes seeking to claim their subjects anew, devils of faith, and fiends of blasphemy- the idol-clad advodazas.

  No two advodazas look exactly alike, each embodying the powers and concerns that saw it worshiped in ages past and subsequently anthropomorphized as a monstrous being. Typically, this results in quadrupedal, half-bestial shapes bristling with terrible wings, hooves, claws, and fangs. Universally, though, they bear the broken remnants of their fallen faith, usually in the form of cracked idols worn like armor, profane talismans crafted into jewelry, or fearful totems wielded like massive weapons. Despite their range of appearances, all advodazas possess the same core abilities, though some particularly ancient or powerful fiends possess unique abilities. Most advodazas stand 18 feet tall and weigh nearly 9 tons.

---

# Devil, Advodaza
The rending, thunderous clangor of rushing claws heralds the charge of this fire-eyed ruin, a terror of flame-seared hide and saber-like spines shaped in a monstrously muscled centauric form. The true terrible _[[universal monster rules/Ferocity|ferocity]]_ of the thing lies hidden, restrained beneath armor and wings of crumbling stone carved with icons as ancient as they are undeniable and profane.
**Source** Pathfinder #30: The Twice-Damned Prince pg. 80
**XP** 153,600

LE Huge outsider (devil, evil, extraplanar, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +28

##### Defense

**AC** 35, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+6 armor, +7 Dex, +14 natural, -2 size)
**hp** 297 (18d10+198)
**Fort** +21, **Ref** +18, **Will** +15
**Defensive Abilities** idol armor; **DR** 10/good and silver; **Immune** cold, _[[spells/Dismissal|dismissal]]_, electricity, fire, poison, sonic; **Resist** acid 10; **SR** 29

##### Offense
**Speed** 40 ft., fly 80 ft. (average)
**Melee** bite +28 (2d6+12), 2 claws +28 (1d8+12 plus infernal wounds), 2 hooves +26 (1d8+6), tail +26 (2d6+6)
**Space** 15 ft., **Reach** 15 ft. (20 ft. with tail)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
At will — _[[spells/Gaseous Form|gaseous form]]_, greater _[[spells/Invisibility|invisibility]]_ (DC 21), greater teleport (self plus 50 lbs. of objects only), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Whispering Wind|whispering wind]]_
3/day — _[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Harm|harm]]_ (DC 23), _[[spells/Heal|heal]]_ (DC 23), _[[spells/Hold Monster|hold monster]]_ (DC 22), _[[spells/Wall Of Stone|wall of stone]]_
1/day — _[[spells/Scrying|scrying]]_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 7, horned devil, 60%), _[[spells/Unhallow|unhallow]]_

##### Statistics
**Str** 34, **Dex** 25, **Con** 30, **Int** 23, **Wis** 25, **Cha** 24
**Base Atk** +18; **CMB** +32; **CMD** 49 (53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +28, Diplomacy +28, Escape Artist +25, Fly +24, Intimidate +28, Knowledge (arcana) +27, Knowledge (planes) +27, Knowledge (religion) +27, Perception +28, Sense Motive +28, Spellcraft +24, Stealth +20
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** devil mark, false divinity

##### Ecology

**Environment** any (Hell)
**Organization** solitary or pantheon (2-5)
**Treasure** double

### Special Abilities

**Devil Mark (Su)** An advodaza can grant worthy servants a measure of its power. As a full-round action, an advodaza can touch a willing adjacent creature, marking it with a unique symbol similar to an _[[spells/Arcane Mark|arcane mark]]_. This symbol can be either visible or _[[conditions/Invisible|invisible]]_, as the devil chooses. For as long as the target possesses the mark, it gains a spell-like ability it can use once per day. This spell-like ability comes from the advodaza’s chosen domain (see the false divinity ability). The target also gains the ability to telepathically communicate with the advodaza over any distance as long as the two creatures are on the same plane. An advodaza can mark multiple creatures, up to an amount equaling its Hit Dice (typically 18). An advodaza can dispel its mark as a standard action, no matter where the bearer is. It can also, as a standard action, deal pain to a mark bearer that causes 6d6 points of damage with no saving throw. An advodaza’s mark cannot be removed physically, but a _dispel magic_ or _[[spells/Erase|erase]]_ spell that succeeds on a dispel check or caster level check of DC 30 removes the effect.

**False Divinity (Su)** Advodazas possess areas of concern as deities do, but on a far smaller scale. Each advodaza chooses one _[[classes/Cleric|cleric]]_ domain and gains the domain spells (up to 5th level) of that domain as _spell-like abilities_, each of which it can use 3 times per day. The advodaza does not gain any of the domain’s granted powers. Most advodazas possess powers from the Evil, Fire, Law, War, or Weather domains, though any domain is possible.

Evil Domain: _[[spells/Align Weapon|align weapon]]_ (evil only), _[[spells/Dispel Good|dispel good]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Unholy Blight|unholy blight]]_

Fire Domain: _[[spells/Burning Hands|burning hands]]_, _[[spells/Fire Shield|fire shield]]_, _[[spells/Fireball|fireball]]_, _[[spells/Produce Flame|produce flame]]_, _[[spells/Wall Of Fire|wall of fire]]_

Law Domain: _align weapon_ (law only), _[[spells/Dispel Chaos|dispel chaos]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, order’s wrath, _[[spells/Protection From Chaos|protection from chaos]]_

War Domain: _[[spells/Divine Power|divine power]]_, _[[spells/Flame Strike|flame strike]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_

Weather Domain: _[[spells/Call Lightning|call lightning]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sleet Storm|sleet storm]]_

**Idol Armor (Su)** Advodazas armor themselves in their _[[monsters/Fallen|fallen]]_ idols and ornaments of devotion. This armor grants an advodaza a +6 armor bonus to AC and _[[universal monster rules/Immunity|immunity]]_ to cold, electricity, and sonic damage, as well as _immunity_ to the spell _dismissal_. The spells _[[spells/Chaos Hammer|chaos hammer]]_, _[[spells/Holy Smite|holy smite]]_, _[[spells/Holy Word|holy word]]_, and _[[spells/Word Of Chaos|word of chaos]]_ destroy this armor, removing the devil’s armor bonus to AC and immunities (its cold _immunity_ decreases to its normal _[[universal monster rules/Resistance|resistance]]_ 10). If uninterrupted for 1 hour, an advodaza can _summon_ new armor to replace its destroyed protection.

**Infernal Wound (Su)** The damage an advodaza deals with its claws causes persistent wounds that deal 2d6 points of _[[universal monster rules/Bleed|bleed]]_ damage. Bleeding caused in this way is difficult to stanch—a DC 30 _Heal_ check stops the damage, and any attempt to _heal_ a creature suffering from an infernal wound must succeed on a DC 30 caster level check or the spell does not function. Success indicates the healing works normally and stops all _bleed_ effects. The _Heal_ check and caster level DC are Constitution-based.

##### Description

False gods, _fallen_ demagogues, _[[feats/Nemesis|nemesis]]_ devils—the fiends known collectively as advodazas survive from dark ages past, when mortals offered worship to base things and unwholesome spirits masqueraded as baleful gods. Although time and faith have turned against these beings, the most tenacious of their kind have refused to fade into _[[monsters/Oblivion|oblivion]]_, and to these obstinate corruptors and one-time deities the gates of Hell swing wide and welcoming. These lords of cults and masters of forgotten mysteries find renewed _[[spells/Vigor|vigor]]_ in the depths of the Pit, and those seeking to renew their power and lordship over mortalkind undergo terrible indoctrinations and _[[spells/Binding|binding]]_ rites that transform them over the ages into true devils. What emerge are eidolons of half-remembered demigods, _fallen_ princes seeking to claim their subjects anew, devils of faith, and fiends of _blasphemy_— the idol-clad advodazas.

No two advodazas look exactly alike, each embodying the powers and concerns that _[[items/Mundane/Saw|saw]]_ it worshiped in ages past and subsequently anthropomorphized as a monstrous being. Typically, this results in quadrupedal, half-bestial shapes bristling with terrible wings, hooves, claws, and fangs. Universally, though, they bear the _[[conditions/Broken|broken]]_ remnants of their _fallen_ faith, usually in the form of cracked idols worn like armor, profane talismans crafted into _[[items/Mundane/Jewelry|jewelry]]_, or fearful totems wielded like massive weapons. Despite their range of appearances, all advodazas possess the same core abilities, though some particularly ancient or powerful fiends possess unique abilities. Most advodazas stand 18 feet tall and weigh nearly 9 tons.