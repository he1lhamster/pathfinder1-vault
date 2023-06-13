---
cssclass: [monsters]
title1: Demon Lord, Pazuzu
desc_short: Held aloft by four great feathered wings, this hawk-faced fiend has a
  scorpion's tail and carries a black metal scepter.
title2: Pazuzu
CR: 30
sources:
- name: Bestiary 4
  page: 50
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 9830400
alignment: CE
size: Large
type: outsider
subtypes:
- air
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 13
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: frightful presence
  radius: 180
  DC: 40
  duration: 10 rounds
- name: locusts
  radius: 10
  other:
  - distraction
  DC: 43
- name: unholy aura
  DC: 31
AC:
  AC: 48
  touch: 38
  flat_footed: 39
  components:
    deflection: 4
    dex: 9
    natural: 10
    profane: 16
    size: -1
HP:
  HP: 752
  long: 35d10+560
  other: regeneration (deific or mythic)
saves:
  fort: 31
  ref: 32
  will: 35
defensive_abilities:
- Abyssal resurrection
- avian mastery
- freedom of movement
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage
- ability drain
- charm effects
- compulsion effects
- cold
- death effects
- electricity
- energy drain
- petrification
- poison
resistances:
  acid: 30
  cold: 30
  fire: 30
SR: 41
speeds:
  base: 60
  fly: 150
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +5 anarchic keen unholy longsword +54/+49/+44/+39 (2d6+20/17-20)
      entries:
      - - damage: 2d6+20
          crit_range: 17-20
      attack: +5 anarchic keen unholy longsword
      bonus:
      - 54
      - 49
      - 44
      - 39
    - text: bite +49 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: bite
      bonus:
      - 49
    - text: claw +49 (1d6+15)
      entries:
      - - damage: 1d6+15
      attack: claw
      bonus:
      - 49
    - text: sting +49 (2d8+15 plus poison)
      entries:
      - - damage: 2d8+15
        - effect: poison
      attack: sting
      bonus:
      - 49
    - text: 2 talons +49 (1d6+15)
      entries:
      - - damage: 1d6+15
      count: 2
      attack: talons
      bonus:
      - 49
  special:
  - hear name
  - poison
  - possession
  - profane
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
    other: winged animals only
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 31
  - name: astral projection
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: At will
    DC: 30
  - name: control winds
    source: default
    freq: At will
  - name: desecrate
    source: default
    freq: At will
  - name: dominate person
    source: default
    freq: At will
    DC: 28
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: shapechange
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 28
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 27
  - name: quickened dominate person
    source: default
    freq: 3/day
    DC: 28
  - name: summon demons
    source: default
    freq: 3/day
  - name: symbol of persuasion
    source: default
    freq: 3/day
    DC: 29
  - name: sympathy
    source: default
    freq: 3/day
    DC: 31
  - name: whirlwind
    source: default
    freq: 3/day
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 32
  - name: time stop
    source: default
    freq: 1/day
  - name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 43
ability_scores:
  STR: 40
  DEX: 28
  CON: 42
  INT: 33
  WIS: 34
  CHA: 36
BAB: 35
CMB: 51
CMB_other: +55 sunder
CMD: 92
CMD_other: 94 vs. sunder
feats:
- name: Bleeding Critical
- name: Combat Expertise
- name: Combat Reflexes
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Rod
- name: Craft Wondrous Item
- name: Critical Focus
- name: Flyby Attack
- name: Greater Sunder
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Sunder
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (dominate person)
- name: Vital Strike
skills:
  Acrobatics: 47
    when jumping: 59
  Bluff: 51
  Diplomacy: 51
  Fly: 53
  Intimidate: 48
  Knowledge (arcana): 49
  Knowledge (local): 46
  Knowledge (nature): 46
  Knowledge (nobility): 46
  Knowledge (planes): 49
  Knowledge (religion): 46
  Perception: 58
  Sense Motive: 50
  Spellcraft: 49
  Stealth: 43
  Survival: 47
  Use Magic Device: 48
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Auran
- Celestial
- Common
- Draconic
- telepathy 300 ft.
special_qualities:
- demon lord traits
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - Scepter of Shibaxet
  - other treasure
special_abilities:
  Aura of Locusts (Su): Pazuzu exhales clouds of locusts. In any round in which he
    does not move more than 5 feet, he is surrounded by a 10-foot-radius spread of
    these creatures. Any creature that enters this area must succeed at a DC 43 Fortitude
    save or be nauseated for 1 round. The save DC is Constitution-based.
  Avian Mastery (Su): Any creature flying under its own power (flight from a source
    other than a spell, spell-like ability, or magic item) that attempts to attack
    Pazuzu with a melee attack must attempt a DC 40 Will save. If it fails, the creature
    can't follow through with the attack, that part of its action is lost, and it
    can't directly attack Pazuzu for 1d4 rounds. Once a creature succeeds at this
    save, it is immune to this ability for 24 hours. The save DC is Charisma-based.
  Hear Name (Su): Pazuzu hears his name whenever it is spoken, regardless of distance-this
    ability functions even across planar boundaries. If a creature speaks Pazuzu's
    name aloud three times in the same breath, Pazuzu automatically knows that creature's
    precise location and name. If Pazuzu is on the same plane as someone who speaks
    his name three times in a single breath, he can immediately attempt to possess
    that creature.
  Poison (Ex): Sting-injury; save Fort DC 43; frequency 1/round for 6 rounds; effect
    1d6 Wisdom drain and nauseated; cure 3 consecutive saves.
  Possession (Su): Once per day as a swift action, Pazuzu can attempt to possess a
    single living creature within 1 mile, provided he knows the target's name. The
    target can resist this possession attempt by succeeding at a DC 43 Will save.
    A lawful creature gains a +10 bonus on this saving throw, and a good creature
    gains a +20 bonus on the saving throw (these bonuses stack). If the creature successfully
    saves, it is immune to possession attempts by Pazuzu for the rest of its life.
    If the saving throw fails, Pazuzu can control the possessed creature from afar.
    While possessing a creature, Pazuzu automatically knows every thought that creature
    has. By concentrating, he can sense the creature's surroundings using that creature's
    senses. As a swift action, he can cause the creature to perform any ability it
    can perform on its own. Pazuzu can use any of his spell-like abilities through
    a possessed target, with the effects resolving as if the possessed creature had
    created the effect. Possession is permanent, but Pazuzu can only possess one creature
    at a time. When Pazuzu isn't actively controlling the target, it can take its
    own actions. Dispel chaos or dispel evil ends this possession effect as if it
    were an enchantment spell, but unless the caster of the spell succeeds at a DC
    30 caster level check, as a swift action Pazuzu can attempt to possess the caster
    as he is driven out of the target. A creature possessed by Pazuzu is immune to
    protection from evil, magic circle against evil, and any similar effects. The
    save DC is Charisma-based.
  Profane Wishcraft (Su): A creature that accepts a wish from Pazuzu immediately becomes
    chaotic evil unless it succeeds at a DC 43 Will save. A creature that becomes
    chaotic evil in this way gains the benefits of a good hope spell for 1 week, followed
    by the effects of crushing despair for 1d6 months (CL 30th). The save DC is Charisma-based.
  Swarm Master (Su): Pazuzu is immune to swarm damage and other swarm effects (such
    as distraction). As a swift action, he can direct the movement of any swarm within
    30 feet.
desc_long: Pazuzu is among the oldest and most powerful of all demon lords. His Abyssal
  realm is located in one of that plane's greatest rifts. This vertical realm includes
  an immense city, at the heart of which can be found Shibaxet, Pazuzu's personal
  rookery and palace. Pazuzu appears as a four-winged, 15-foot-tall fiend. He takes
  great delight in corrupting mortals, particularly those of a pure heart and soul,
  offering them any one wish in return for nothing but their innocence.

---

# Demon Lord, Pazuzu
Held aloft by four great feathered wings, this hawk-faced fiend has a scorpion’s tail and carries a black metal scepter.
**Source** Bestiary 4 pg. 50
**XP** 9,830,400
CE Large outsider (air, chaotic, demon, evil, extraplanar)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +58
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 40, 10 rounds), locusts (10 ft., _[[universal monster rules/Distraction|distraction]]_, DC 43), _[[spells/Unholy Aura|unholy aura]]_ (DC 31)

##### Defense

**AC** 48, touch 38, _[[conditions/Flat-Footed|flat-footed]]_ 39 (+4 deflection, +9 Dex, +10 natural, +16 profane, –1 size)
**hp** 752 (35d10+560); _[[universal monster rules/Regeneration|regeneration]]_ (deific or mythic)
**Fort** +31, **Ref** +32, **Will** +35
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, avian mastery, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron, epic, and good; **Immune** ability damage, ability drain, charm effects, compulsion effects, cold, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification, and poison; **Resist** acid 30, cold 30, fire 30; **SR** 41

##### Offense
**Speed** 60 ft., fly 150 ft. (perfect)
**Melee** +5 _[[items/Weapon Magic Abilities/Anarchic|anarchic]]_ _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Longsword|longsword]]_ +54/+49/+44/+39 (2d6+20/17–20), bite +49 (2d6+15), claw +49 (1d6+15), sting +49 (2d8+15 plus poison), 2 talons +49 (1d6+15)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** hear name, poison, _[[spells/Possession|possession]]_, profane
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +43)
Constant—_detect good_, _detect law_, _freedom of movement_, _[[spells/Speak with Animals|speak with animals]]_ (winged animals only), _true seeing_, _unholy aura_ (DC 31)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_* (DC 30), _[[spells/Control Winds|control winds]]_, _[[spells/Desecrate|desecrate]]_*, _[[spells/Dominate Person|dominate person]]_* (DC 28), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Shapechange|shapechange]]_, _[[spells/Telekinesis|telekinesis]]_* (DC 28), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_* (DC 27)
3/day—quickened _dominate person_* (DC 28), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 29), _[[spells/Sympathy|sympathy]]_ (DC 31), _[[universal monster rules/Whirlwind|whirlwind]]_*
1/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 32), _[[spells/Time Stop|time stop]]_*, _[[spells/Wish|wish]]_*
* Pazuzu can use the mythic version of this ability in his realm.

##### Statistics
**Str** 40, **Dex** 28, **Con** 42, **Int** 33, **Wis** 34, **Cha** 36
**Base Atk** +35; **CMB** +51 (+55 sunder); **CMD** 92 (94 vs. sunder)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Rod|Craft Rod]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +47 (+59 when jumping), Bluff +51, Diplomacy +51, Fly +53, Intimidate +48, Knowledge (arcana) +49, Knowledge (local) +46, Knowledge (nature) +46, Knowledge (nobility) +46, Knowledge (planes) +49, Knowledge (religion) +46, Perception +58, Sense Motive +50, Spellcraft +49, Stealth +43, Survival +47, Use Magic Device +48; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Auran, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** demon lord traits

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple (_[[items/Wondrous Item/Scepter of Shibaxet|Scepter of Shibaxet]]_, other treasure)

### Special Abilities

**Aura of Locusts (Su)** Pazuzu exhales clouds of locusts. In any round in which he does not move more than 5 feet, he is surrounded by a 10-foot-radius spread of these creatures. Any creature that enters this area must succeed at a DC 43 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Constitution-based.

**Avian Mastery (Su)** Any creature flying under its own power (_[[universal monster rules/Flight|flight]]_ from a source other than a spell, spell-like ability, or magic item) that attempts to attack Pazuzu with a melee attack must attempt a DC 40 Will save. If it fails, the creature can’t follow through with the attack, that part of its action is lost, and it can’t directly attack Pazuzu for 1d4 rounds. Once a creature succeeds at this save, it is immune to this ability for 24 hours. The save DC is Charisma-based.

**Hear Name (Su)** Pazuzu hears his name whenever it is spoken, regardless of distance—this ability functions even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries. If a creature speaks Pazuzu’s name aloud three times in the same breath, Pazuzu automatically knows that creature’s precise location and name. If Pazuzu is on the same plane as someone who speaks his name three times in a single breath, he can immediately attempt to possess that creature.

**Poison (Ex)** Sting—injury; save Fort DC 43; frequency 1/round for 6 rounds; effect 1d6 Wisdom drain and _nauseated_; cure 3 consecutive saves.

**_Possession_ (Su)** Once per day as a swift action, Pazuzu can attempt to possess a single living creature within 1 mile, provided he knows the target’s name. The target can resist this _possession_ attempt by succeeding at a DC 43 Will save. A lawful creature gains a +10 bonus on this saving throw, and a good creature gains a +20 bonus on the saving throw (these bonuses stack). If the creature successfully saves, it is immune to _possession_ attempts by Pazuzu for the rest of its life. If the saving throw fails, Pazuzu can control the possessed creature from afar. While possessing a creature, Pazuzu automatically knows every thought that creature has. By concentrating, he can sense the creature’s surroundings using that creature’s senses. As a swift action, he can cause the creature to perform any ability it can perform on its own. Pazuzu can use any of his _spell-like abilities_ through a possessed target, with the effects resolving as if the possessed creature had created the effect. _Possession_ is permanent, but Pazuzu can only possess one creature at a time. When Pazuzu isn’t actively controlling the target, it can take its own actions. _[[spells/Dispel Chaos|Dispel chaos]]_ or _[[spells/Dispel Evil|dispel evil]]_ ends this _possession_ effect as if it were an enchantment spell, but unless the caster of the spell succeeds at a DC 30 caster level check, as a swift action Pazuzu can attempt to possess the caster as he is driven out of the target. A creature possessed by Pazuzu is immune to _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, and any similar effects. The save DC is Charisma-based.

**Profane Wishcraft (Su)** A creature that accepts a _wish_ from Pazuzu immediately becomes chaotic evil unless it succeeds at a DC 43 Will save. A creature that becomes chaotic evil in this way gains the benefits of a _[[spells/Good Hope|good hope]]_ spell for 1 week, followed by the effects of _[[spells/Crushing Despair|crushing despair]]_ for 1d6 months (CL 30th). The save DC is Charisma-based.
**Swarm Master (Su)** Pazuzu is immune to swarm damage and other swarm effects (such as _distraction_). As a swift action, he can direct the movement of any swarm within 30 feet.

##### Description

Pazuzu is among the oldest and most powerful of all demon lords. His Abyssal realm is located in one of that plane’s greatest rifts. This vertical realm includes an immense city, at the heart of which can be found Shibaxet, Pazuzu’s personal rookery and palace. Pazuzu appears as a four-winged, 15-foot-tall fiend. He takes great delight in corrupting mortals, particularly those of a pure heart and soul, offering them any one _wish_ in return for nothing but their _[[spells/Innocence|innocence]]_.