---
cssclass: [monsters]
title1: Charnel God
desc_short: This porphyry statue depicts a three-headed goddess with draconicwings,
  a long tail, and a deadly looking longbow in her hands.
title2: Charnel God
CR: 23
sources:
- name: Bestiary 6
  page: 54
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 819200
alignment: CE
size: Large
type: construct
initiative:
  bonus: 11
senses:
  darkvision: 60
  divine sense: true
  low-light vision: true
  true seeing: true
auras:
- name: divine antithesis
  radius: 60
  DC: 35
AC:
  AC: 42
  touch: 32
  flat_footed: 31
  components:
    dex: 11
    natural,+12 profane: 10
    size: -1
HP:
  HP: 485
  long: 26d10+342
  fast_healing: 10
saves:
  fort: 20
  ref: 19
  will: 20
defensive_abilities:
- divine antithesis
DR:
- amount: 15
  weakness: '-'
immunities:
- constructtraits
resistances:
  acid: 30
  cold: 30
  electricity: 30
  fire: 30
SR: 34
speeds:
  base: 60
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 bites +37 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: bites
      bonus:
      - 37
    - text: gore +37 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: gore
      bonus:
      - 37
    - text: 2 slams +37(1d6+12)
      entries:
      - - damage: 1d6+12
      count: 2
      attack: slams
      bonus:
      - 37
  ranged:
  - - text: +5 unholy composite longbow +42/+37/+32/+27(2d6+17/19-20/×3)
      entries:
      - - damage: 2d6+17
          crit_range: 19-20
          crit_multiplier: 3
      attack: +5 unholy composite longbow
      bonus:
      - 42
      - 37
      - 32
      - 27
  special:
  - severance
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: align weapon
    source: default
    freq: At will
    other: chaos only
  - name: animate dead
    source: default
    freq: At will
  - name: cause fear
    source: default
    freq: At will
    DC: 23
  - name: chaos hammer
    source: default
    freq: At will
    DC: 26
  - name: death knell
    source: default
    freq: At will
  - name: death ward
    source: default
    freq: At will
  - name: dispel law
    source: default
    freq: At will
  - name: magic circle against law
    source: default
    freq: At will
  - name: protection from law
    source: default
    freq: At will
  - name: slay living
    source: default
    freq: At will
    DC: 27
  - name: animate objects
    source: default
    freq: 3/day
  - name: cloak of chaos
    source: default
    freq: 3/day
    DC: 30
  - name: create greater undead
    source: default
    freq: 3/day
  - name: create undead
    source: default
    freq: 3/day
  - name: destruction
    source: default
    freq: 3/day
    DC: 29
  - name: word of chaos
    source: default
    freq: 3/day
    DC: 29
  - name: summon monster
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 23
    concentration: 35
ability_scores:
  STR: 34
  DEX: 33
  CON:
  INT: 27
  WIS: 30
  CHA: 35
BAB: 26
CMB: 39
CMD: 72
feats:
- name: Clustered Shots
- name: Combat Reflexes
- name: Deadly Aim
- name: Far Shot
- name: Improved Critical (composite longbow)
- name: Improved Precise Shot
- name: Improved Snap Shot
- name: Iron Will
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Snap Shot
- name: Weapon Focus (composite longbow)
skills:
  Fly: 42
  Intimidate: 38
  Knowledge (arcana): 34
  Knowledge (planes,religion): 34
  Perception: 36
  Sleight of Hand: 37
  Spellcraft: 34
  Stealth: 33
  Survival: 36
languages:
- Abyssal
- Common
- telepathy 300 ft.
special_qualities:
- divinity lost
- favored weapon
- hideous will
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
special_abilities:
  Divine Antithesis (Ex): A charnel god is immune to any divine spell that allows
    spell resistance. Additionally, creatures within 60 feet of a charnel god gain
    spell resistance against divine spells equal to 11 + the charnel god's CR (34
    for most charnel gods). Creatures cannot voluntarily lower this spell resistance.
  Divine Sense (Su): A charnel god can identify servants of the gods on sight, can
    immediately determine whether a creature it sees is capable of casting divine
    spells, and knows the highest level of spell that creature is capable of casting.
    It gains a +8 insight bonus on all Perception and Sense Motive checks attempted
    against such targets.
  Divinity Lost (Su): A charnel god gains, as spell-like abilities, the domain spells
    of two domains granted by the deity from which it formed. It can use domain spells
    of 5th level or lower as at-will spell-like abilities, spells of 6th to 8th level
    three times per day as spell-like abilities, and 9th level spells once per day
    as spell-like abilities. The caster level for these abilities equals the charnel
    god's CR (23 for most charnel gods), and the save DCs are Charisma-based. The
    charnel god does not gain any of these domains' granted powers. The charnel god
    presented above has the Death and Chaos domains, and these spell-like abilities
    are included in its stat block.
  Favored Weapon (Su): As a free action, a charnel god can conjure a weapon from the
    fragments of its former divine power. This weapon is always a +5 unholy weapon
    of the type favored by the deceased deity. The weapon functions only for the charnel
    god and vanishes if it leaves the charnel god's possession. Melee weapons created
    in this way are treated as if they were made of adamantine for the purposes of
    determining their resistance to damage and their ability to bypass hardness. Ranged
    weapons created in this way do not provoke attacks of opportunity when the charnel
    god uses them.
  Hideous Will (Ex): A charnel god is suffused with profane divine energy. It gains
    a profane bonus to its AC and Fortitude saving throws equal to its Charisma modifier.
    Additionally, it uses its Charisma modifier in place of its Constitution modifier
    when calculating its hit points.
  Severance (Su): As a swift action that doesn't provoke attacks of opportunity, a
    charnel god can attempt to sever the connection between a creature and its divine
    patron. The target must be within 60 feet of the charnel god, and it must attempt
    a DC 35 Will save to avoid being cut off from the divine. If successful, the target
    cannot be targeted by this ability again for 24 hours. If the target fails, it
    becomes stunned for 1 round and then permanently staggered thereafter. This ability
    has no effect on characters who don't have levels in any class that grants divine
    spellcasting, but it does affect characters who have minimal divine spellcasting
    abilities, such as paladins or rangers. This is a curse effect. Atonement can
    remove this effect, but only if the caster succeeds at a DC 35 caster level check.
    The save DC is Charisma-based.
desc_long: |-
  The gods are no less strange and terrifying in death than in life. Though the death of any god is staggeringly rare, some do meet violent ends, often at the hands of other deities. When this happens, the deity's death casts fragments of the god's power out among the planes. These fragments are sometimes drawn to places where the god was worshiped in its life, where they can produce miraculous effects, such as striking the god's devout followers deaf or blind, or granting visions of the god's demise. Sometimes these shards of power go unnoticed and boil away into nothing over time. But sometimes, something far more terrible occurs-such fragments can find a new home within a graven image of the former deity, forming a new creature: a charnel god. 

  Regardless of the deceased god's alignment or nature, all charnel gods are beings of sublime wickedness fueled by bitter anger. The memory of being killed and cast into the void leaves charnel gods utterly and cruelly insane. Further, they feel the pain of being incomplete, of being only a small portion of what they once were, and this torments them. Charnel gods have some memories of their time as gods, but any recollections are fragmented and muddled. A charnel god might be able to share a hidden secret it knew in its former life, but it could just as easily confuse the details or call forth a false memory, making it an unreliable source of wisdom. Charnel gods resent such questions anyway, as remembering their former lives only reminds them of their pitiful current state. 

  Those who believe encountering a charnel god will be a chance to reconnect with a deceased divine patron are in for a rude awakening. Without exception, charnel gods detest any who once worshiped them. Unable to come to terms with the fact that they were defeated, they blame the incompetence or faithlessness of their former worshipers for their deaths. Charnel gods also hate the servants of other deities, though with less fervor than they feel toward their own former followers. To a charnel god, all worshipers are false and deserve to be punished for their lack of loyalty and devotion. 

  At the same time, charnel gods long for mortals' worship. Truly, that is a charnel god's greatest wish-to once again be venerated, offered sacrifices, and loved and feared above all else in the world. Charnel gods cannot grant spells like a true deity, and so must rely on their own terrible powers and fearsome demeanor to cow and bully others into worshiping them. Their cults rarely last long, for the charnel god is an easily angered and fickle deity. 

  The example charnel god presented here was once a demon lord of the hunt who was slain by a vengeful goddess. When creating a charnel god of a different deity, GMs should replace some or all of the charnel god's feats and skills to better support that deity's favored weapon and fighting style. Likewise, the charnel god's melee attacks should be altered as needed, but the end result should approximate the average damage a CR 23 creature might deal in a round. Note that charnel gods like the one detailed above can attack with their natural attacks as secondary attacks when attacking with ranged weapons. 

  A charnel god stands 15 feet tall and weighs 12 tons.

---

# Charnel God
This porphyry _[[spells/Statue|statue]]_ depicts a three-headed goddess with draconic

wings, a long tail, and a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ looking _[[items/Weapon/Longbow|longbow]]_ in her hands.
**Source** Bestiary 6 pg. 54
**XP** 819,200
CE Large construct
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., divine sense, _[[universal monster rules/Low-Light Vision|low-light vision]]_,

_[[spells/True Seeing|true seeing]]_; Perception +36
**Aura** divine antithesis (60 ft., DC 35)

##### Defense

**AC** 42, touch 32, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+11 Dex, +10 natural,

+12 profane, –1 size)
**hp** 485 (26d10+342); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +20, **Ref** +19, **Will** +20
**Defensive Abilities** divine antithesis; **DR** 15/—; **Immune** construct

traits; **Resist** acid 30, cold 30, electricity 30, fire 30; **SR** 34

##### Offense
**Speed** 60 ft., fly 60 ft. (good)
**Melee** 2 bites +37 (2d6+12), gore +37 (1d8+6), 2 slams +37

(1d6+12)
**Ranged** +5 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Composite longbow|composite longbow]]_ +42/+37/+32/+27

(2d6+17/19–20/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** severance
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +35)
Constant—_true seeing_ 
At will—_[[spells/Align Weapon|align weapon]]_ (chaos only), _[[spells/Animate Dead|animate dead]]_, _[[spells/Cause Fear|cause fear]]_ (DC 23), _[[spells/Chaos Hammer|chaos hammer]]_ (DC 26), _[[spells/Death Knell|death knell]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Dispel Law|dispel law]]_, _[[spells/Magic Circle against Law|magic circle against law]]_, _[[spells/Protection From Law|protection from law]]_, _[[spells/Slay Living|slay living]]_ (DC 27) 
3/day—_[[spells/Animate Objects|animate objects]]_, _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 30), _[[spells/Create Greater Undead|create greater undead]]_, _[[spells/Create Undead|create undead]]_, _[[spells/Destruction|destruction]]_ (DC 29), _[[spells/Word Of Chaos|word of chaos]]_ (DC 29) 
1/day—_[[universal monster rules/Summon|summon]]_ monster

##### Statistics
**Str** 34, **Dex** 33, **Con** —, **Int** 27, **Wis** 30, **Cha** 35
**Base Atk** +26; **CMB** +39; **CMD** 72
**Feats** _[[feats/Clustered Shots|Clustered Shots]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Far Shot|Far Shot]]_, _[[feats/Improved Critical|Improved Critical]]_ (_composite longbow_), _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Improved Snap Shot|Improved Snap Shot]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Snap Shot|Snap Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite longbow_)
**Skills** Fly +42, Intimidate +38, Knowledge (arcana, planes,

religion) +34, Perception +36, Sleight of Hand +37,

Spellcraft +34, Stealth +33, Survival +36
**Languages** Abyssal, Common; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** divinity lost, favored weapon, hideous will

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

### Special Abilities

**Divine Antithesis (Ex)** A _[[monsters/Charnel God|charnel god]]_ is immune to any divine spell that allows _[[universal monster rules/Spell Resistance|spell resistance]]_. Additionally, creatures within 60 feet of a _charnel god_ gain _spell resistance_ against divine spells equal to 11 + the _charnel god_’s CR (34 for most charnel gods). Creatures cannot voluntarily lower this _spell resistance_.

**Divine Sense (Su)** A _charnel god_ can _[[spells/Identify|identify]]_ servants of the gods on sight, can immediately determine whether a creature it sees is capable of casting divine spells, and knows the highest level of spell that creature is capable of casting. It gains a +8 insight bonus on all Perception and Sense Motive checks attempted against such targets.

**Divinity Lost (Su)** A _charnel god_ gains, as _spell-like abilities_, the domain spells of two domains granted by the deity from which it formed. It can use domain spells of 5th level or lower as at-will _spell-like abilities_, spells of 6th to 8th level three times per day as _spell-like abilities_, and 9th level spells once per day as _spell-like abilities_. The caster level for these abilities equals the _charnel god_’s CR (23 for most charnel gods), and the save DCs are Charisma-based. The _charnel god_ does not gain any of these domains’ granted powers. The _charnel god_ presented above has the Death and Chaos domains, and these _spell-like abilities_ are included in its stat block.

**Favored Weapon (Su)** As a free action, a _charnel god_ can conjure a weapon from the fragments of its former _[[spells/Divine Power|divine power]]_. This weapon is always a +5 _unholy_ weapon of the type favored by the deceased deity. The weapon functions only for the _charnel god_ and vanishes if it leaves the _charnel god_’s _[[spells/Possession|possession]]_. Melee weapons created in this way are treated as if they were made of adamantine for the purposes of determining their _[[universal monster rules/Resistance|resistance]]_ to damage and their ability to bypass hardness. Ranged weapons created in this way do not provoke attacks of opportunity when the _charnel god_ uses them.

**Hideous Will (Ex)** A _charnel god_ is suffused with profane divine energy. It gains a profane bonus to its AC and Fortitude saving throws equal to its Charisma modifier. Additionally, it uses its Charisma modifier in place of its Constitution modifier when calculating its hit points.
**Severance (Su)** As a swift action that doesn’t provoke attacks of opportunity, a _charnel god_ can attempt to sever the connection between a creature and its divine patron. The target must be within 60 feet of the _charnel god_, and it must attempt a DC 35 Will save to avoid being cut off from the divine. If successful, the target cannot be targeted by this ability again for 24 hours. If the target fails, it becomes _[[conditions/Stunned|stunned]]_ for 1 round and then permanently _[[conditions/Staggered|staggered]]_ thereafter. This ability has no effect on characters who don’t have levels in any class that grants divine spellcasting, but it does affect characters who have minimal divine spellcasting abilities, such as paladins or rangers. This is a curse effect. _[[spells/Atonement|Atonement]]_ can remove this effect, but only if the caster succeeds at a DC 35 caster level check. The save DC is Charisma-based.

##### Description

The gods are no less strange and terrifying in death than in life. Though the death of any god is staggeringly rare, some do meet violent ends, often at the hands of other deities. When this happens, the deity’s death casts fragments of the god’s power out among the planes. These fragments are sometimes drawn to places where the god was worshiped in its life, where they can produce miraculous effects, such as striking the god’s devout followers deaf or blind, or granting visions of the god’s demise. Sometimes these shards of power _[[feats/Go Unnoticed|go unnoticed]]_ and boil away into nothing over time. But sometimes, something far more terrible occurs—such fragments can find a new home within a graven image of the former deity, forming a new creature: a _charnel god_.

Regardless of the deceased god’s alignment or nature, all charnel gods are beings of sublime wickedness fueled by _[[items/Armor Magic Abilities/Bitter|bitter]]_ anger. The memory of being killed and cast into the void leaves charnel gods utterly and cruelly insane. Further, they feel the pain of being incomplete, of being only a small portion of what they once were, and this torments them. Charnel gods have some memories of their time as gods, but any recollections are fragmented and muddled. A _charnel god_ might be able to share a hidden secret it knew in its former life, but it could just as easily confuse the details or call forth a false memory, making it an unreliable source of wisdom. Charnel gods resent such questions anyway, as remembering their former lives only reminds them of their pitiful current state.

Those who believe encountering a _charnel god_ will be a chance to reconnect with a deceased divine patron are in for a rude awakening. Without exception, charnel gods detest any who once worshiped them. Unable to come to terms with the fact that they were defeated, they blame the incompetence or faithlessness of their former worshipers for their deaths. Charnel gods also hate the servants of other deities, though with less fervor than they feel toward their own former followers. To a _charnel god_, all worshipers are false and deserve to be punished for their lack of loyalty and devotion.

At the same time, charnel gods long for mortals’ worship. Truly, that is a _charnel god_’s greatest _[[spells/Wish|wish]]_—to once again be venerated, offered sacrifices, and loved and feared above all else in the world. Charnel gods cannot grant spells like a true deity, and so must rely on their own terrible powers and fearsome demeanor to cow and bully others into worshiping them. Their cults rarely last long, for the _charnel god_ is an easily angered and fickle deity.

The example _charnel god_ presented here was once a demon lord of the hunt who was slain by a vengeful goddess. When creating a _charnel god_ of a different deity, GMs should replace some or all of the _charnel god_’s feats and skills to better support that deity’s favored weapon and fighting style. Likewise, the _charnel god_’s melee attacks should be altered as needed, but the end result should approximate the average damage a CR 23 creature might deal in a round. Note that charnel gods like the one detailed above can attack with their _[[universal monster rules/Natural Attacks|natural attacks]]_ as secondary attacks when attacking with ranged weapons.

A _charnel god_ stands 15 feet tall and weighs 12 tons.