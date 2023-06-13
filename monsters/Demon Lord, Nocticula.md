---
cssclass: [monsters]
title1: Demon Lord, Nocticula
desc_short: This frighteningly majestic creature spreads wide her runeadorned wings.
  Molten iron weeps from her hooves, and her three tails are studded with barbs.
title2: Nocticula
CR: 30
sources:
- name: 'Pathfinder #76: The Midnight Isles'
  page: 86
  link: http://paizo.com/products/btpy92lf?Pathfinder-Adventure-Path-76-The-Midnight-Isles
XP: 9830400
alignment: CE
size: Medium
type: outsider
subtypes:
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
  see in darkness: true
  true seeing: true
auras:
- name: seductive presence
  radius: 180
  DC: 43
- name: unholy aura
  DC: 33
AC:
  AC: 48
  touch: 41
  flat_footed: 35
  components:
    deflection: 4
    dex: 13
    natural: 7
    profane: 14
HP:
  HP: 774
  long: 36d10+576
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 32
  ref: 37
  will: 35
defensive_abilities:
- Abyssal resurrection
- freedom of movement
DR:
- amount: 20
  weakness: cold iron, epic, and lawful
immunities:
- ability damage and drain
- charm and compulsion effects
- death effects
- electricity
- energy drain
- fire
- petrification
- poison
resistances:
  acid: 30
  cold: 30
SR: 41
speeds:
  base: 60
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +48 (1d8+12 plus 1d4 Cha drain)
      entries:
      - - damage: 1d8+12
        - damage: 1d4
          type: Cha drain
      count: 2
      attack: claws
      bonus:
      - 48
    - text: 3 stings +48 (2d6+12/19-20 plus poison)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
        - effect: poison
      count: 3
      attack: stings
      bonus:
      - 48
    - text: 2 hooves +43 (1d4+6 plus 1d6 fire and burn)
      entries:
      - - damage: 1d4+6
        - damage: 1d6
          type: fire
        - effect: burn
      count: 2
      attack: hooves
      bonus:
      - 43
    - text: 2 wings +43 (1d4+6)
      entries:
      - - damage: 1d4+6
      count: 2
      attack: wings
      bonus:
      - 43
  ranged:
  - - text: Shadowkiss +54/+49/+44/+39 (1d4+20/17-20 plus poison)
      entries:
      - - damage: 1d4+20
          crit_range: 17-20
        - effect: poison
      attack: Shadowkiss
      bonus:
      - 54
      - 49
      - 44
      - 39
  special:
  - burn (3d6 fire, DC 44)
  - cruel shot
  - domination
  - energy drain
  - poison
  - profane ascension
  - sneak attack +4d6
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
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 33
  - name: astral projection
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: At will
    DC: 32
  - name: chaos hammer
    source: default
    freq: At will
    DC: 29
  - name: deeper darkness
    source: default
    freq: At will
  - name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: power word blind
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 30
  - name: shapechange
    source: default
    freq: At will
  - name: unhallow
    source: default
    freq: At will
  - name: finger of death
    source: default
    freq: 3/day
    DC: 32
  - name: quickened mass suggestion
    source: default
    freq: 3/day
    DC: 31
  - name: summon demons
    source: default
    freq: 3/day
  - name: symbol of death
    source: default
    freq: 3/day
    DC: 33
  - name: soul bind
    source: default
    freq: 1/day
    DC: 34
  - name: time stop
    source: default
    freq: 1/day
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 34
  sources:
  - name: default
    CL: 30
ability_scores:
  STR: 34
  DEX: 36
  CON: 42
  INT: 35
  WIS: 32
  CHA: 40
BAB: 36
CMB: 48
CMD: 89
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Deadly Aim
- name: Flyby Attack
- name: Greater Feint
- name: Improved Critical (hand crossbow)
- name: Improved Critical (sting)
- name: Improved Feint
- name: Point-Blank Shot
- name: Precise Shot
- name: Quicken Spell-Like Ability (mass suggestion)
- name: Rapid Reload (hand crossbow)
- name: Rapid Shot
- name: Staggering Critical
skills:
  Acrobatics: 52
  Bluff: 62
  Diplomacy: 54
  Disguise: 51
  Fly: 56
  Intimidate: 51
  Knowledge (arcana): 48
  Knowledge (local): 48
  Knowledge (nobility): 48
  Knowledge (planes): 51
  Knowledge (religion): 51
  Perception: 58
  Perform (dance): 51
  Sense Motive: 50
  Sleight of Hand: 49
  Spellcraft: 48
  Stealth: 52
  Use Magic Device: 54
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Undercommon
- telepathy 300 ft.
- tongues
special_qualities:
- change shape (any humanoid; alter self)
- swift transformation
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - Shadowkiss
  - 100,000 gp in various jewelry
  - other treasure
special_abilities:
  Cruel Shot (Ex): Nocticula is adept at making ranged attacks to strike cruel shots
    that deal significant and humiliating damage. She adds her Charisma bonus to all
    damage dealt by ranged weapons.
  Domination (Su): As a standard action, Nocticula can crush a foe's will. The target
    must be visible to Nocticula and within 120 feet. It must succeed at a DC 43 Will
    save or fall instantly under Nocticula's influence as dominate monster (CL 30th).
    If she uses domination against a humanoid creature, she may instead choose to
    use the ability as a swift action, and it functions as dominate person. As long
    as the target is under this effect, it gains a +4 profane bonus on all saving
    throws against targets other than Nocticula.
  Energy Drain (Su): Nocticula's energy drain functions identically to that of a succubus
    (Pathfinder RPG Bestiary 68), except that she drains 2 levels when she uses this
    ability against mythic creatures, or 1d6+4 levels against non-mythic creatures.
  Poison (Ex): Sting or hand crossbow-injury; save Fort DC 44; frequency 1/round for
    6 rounds; effect 1d4 Wisdom drain plus paralysis for 1 round. Anyone who fails
    two consecutive saves against this poison is permanently blinded. The save DC
    is Constitution-based.
  Profane Ascension (Su): As a swift action while in an act of passion with a willing
    mortal, Nocticula may grant a profane ascension. The target's name appears in
    glowing Abyssal runes on Nocticula's wings, and a crimson mark manifests somewhere
    on the target's body. The target immediately gains a +6 profane bonus to any one
    ability score of its choice, a +4 profane bonus to any other ability score of
    its choice, and the see in darkness ability. A single creature may have only one
    profane ascension in effect at any one time. As long as the effect persists, Nocticula
    can communicate telepathically with the target across any distance and may use
    any of her spell-like abilities through the target, manifesting them as if the
    target were using them. A profane ascension may be removed by a miracle or wish.
    Nocticula can remove it as a free action, dealing 4d6 points of Charisma drain
    and imparting 1d10+10 permanent negative levels to the victim.
  Seductive Presence (Su): Unlike most demon lords, Nocticula does not possess a frightful
    presence ability. Rather, she has a seductive presence that she can activate as
    a free action whenever she speaks or uses a spell-like ability. Anyone within
    180 feet who fails a DC 43 Fortitude save loses any immunity to mind-affecting
    effects, charm effects, and compulsion effects, and becomes fascinated by Nocticula
    for 5d4 rounds. A creature affected by a mind-affecting effect while within this
    aura remains affected even after leaving Nocticula's seductive presence. Creatures
    that succeed at this saving throw are immune to this ability for 24 hours. The
    save DC is Charisma-based.
  Shadowkiss: Nocticula's favored weapon is Shadowkiss, a +5 unholy hand crossbow
    that magically creates ammunition as it fires. Once a target is damaged by a bolt
    fired from Shadowkiss, the hand crossbow gains the bane weapon special ability
    against that target's creature type on all further attacks. Shadowkiss may only
    have one bane effect in place at one time. Bolts fired from Shadowkiss gain the
    ghost touch ability (an effect not normally available to ranged weapons).
  Swift Transformation (Ex): Nocticula can use her change shape ability as a free
    action.
desc_long: |-
  Nocticula is the demon lord of assassins, darkness, and lust, and rules the Abyssal realm of the Midnight Isles, a vast archipelago formed around the murdered remnants of dozens of demon lords and other powerful foes. Having been the first succubus and then having ascended to become a demigoddess, Nocticula now sets her eyes at a greater prize-full divinity. Lamashtu is the only demon lord who has accomplished this task so far, but Nocticula aims to be the second. What kind of deity she might become is anyone's guess-some believe that Nocticula is secretly seeking redemption from her demonic nature. Others say these rumors were seeded by Nocticula herself as a grand lie to distract her enemies from her true goal of becoming an assassin and seducer of gods.

  Nocticula is certainly mercurial in her personality and attitude. She may simply murder or enslave visitors to her realm, or she may welcome them with open arms-even those who one would think were her enemies. Only a fool accepts her invitation without suspicion, for what the queen of succubi wants may change dramatically from one moment to the next.

---

# Demon Lord, Nocticula
This frighteningly majestic creature spreads wide her runeadorned wings. Molten iron weeps from her hooves, and her three tails are studded with barbs.
**Source** Pathfinder #76: The Midnight Isles pg. 86
**XP** 9,830,400
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +58
**Aura** seductive presence (180 ft., DC 43), _[[spells/Unholy Aura|unholy aura]]_ (DC 33)

##### Defense

**AC** 48, touch 41, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+4 _[[spells/Deflection|deflection]]_, +13 Dex, +7 natural, +14 profane)
**hp** 774 (36d10+576); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +32, **Ref** +37, **Will** +35
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron, epic, and lawful; **Immune** _[[universal monster rules/Ability Damage and Drain|ability damage and drain]]_, charm and compulsion effects, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, fire, petrification, poison; **Resist** acid 30, cold 30; **SR** 41

##### Offense
**Speed** 60 ft., fly 90 ft. (good)
**Melee** 2 claws +48 (1d8+12 plus 1d4 Cha drain), 3 stings +48 (2d6+12/19–20 plus poison), 2 hooves +43 (1d4+6 plus 1d6 fire and _[[universal monster rules/Burn|burn]]_), 2 wings +43 (1d4+6)
**Ranged** Shadowkiss +54/+49/+44/+39 (1d4+20/17–20 plus poison)
**Special Attacks** _burn_ (3d6 fire, DC 44), _[[items/Weapon Magic Abilities/Cruel|cruel]]_ shot, domination, _energy drain_, poison, profane _[[spells/Ascension|ascension]]_, sneak attack +4d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th)
Constant—_detect good_, _detect law_, _freedom of movement_, _[[spells/Tongues|tongues]]_, _true seeing_, _unholy aura_ (DC 33)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_ (DC 32), _[[spells/Chaos Hammer|chaos hammer]]_ (DC 29), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 30), _[[spells/Shapechange|shapechange]]_, _[[spells/Unhallow|unhallow]]_
3/day—_[[spells/Finger Of Death|finger of death]]_ (DC 32), quickened mass _[[spells/Suggestion|suggestion]]_ (DC 31), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol of Death|symbol of death]]_ (DC 33)
1/day—_[[spells/Soul Bind|soul bind]]_ (DC 34), _[[spells/Time Stop|time stop]]_, _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 34)

##### Statistics
**Str** 34, **Dex** 36, **Con** 42, **Int** 35, **Wis** 32, **Cha** 40
**Base Atk** +36; **CMB** +48; **CMD** 89
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Feint|Greater Feint]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Hand crossbow|hand crossbow]]_), _Improved Critical_ (sting), _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (mass _suggestion_), _[[feats/Rapid Reload|Rapid Reload]]_ (_hand crossbow_), _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Acrobatics +52, Bluff +62, Diplomacy +54, Disguise +51, Fly +56, Intimidate +51, Knowledge (arcana, local, nobility) +48, Knowledge (planes, religion) +51, Perception +58, Perform (dance) +51, Sense Motive +50, Sleight of Hand +49, Spellcraft +48, Stealth +52, Use Magic Device +54; **Racial Modifiers** +8 Bluff, +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft., _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid; _[[spells/Alter Self|alter self]]_), swift _[[spells/Transformation|transformation]]_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple (Shadowkiss, 100,000 gp in various _[[items/Mundane/Jewelry|jewelry]]_, other treasure)

### Special Abilities

**_Cruel_ Shot (Ex)** Nocticula is adept at making ranged attacks to strike _cruel_ shots that deal significant and humiliating damage. She adds her Charisma bonus to all damage dealt by ranged weapons.

**Domination (Su)** As a standard action, Nocticula can crush a foe’s will. The target must be visible to Nocticula and within 120 feet. It must succeed at a DC 43 Will save or fall instantly under Nocticula’s influence as _[[spells/Dominate Monster|dominate monster]]_ (CL 30th). If she uses domination against a humanoid creature, she may instead choose to use the ability as a swift action, and it functions as _[[spells/Dominate Person|dominate person]]_. As long as the target is under this effect, it gains a +4 profane bonus on all saving throws against targets other than Nocticula.

**_Energy Drain_ (Su)** Nocticula’s _energy drain_ functions identically to that of a succubus (Pathfinder RPG Bestiary 68), except that she drains 2 levels when she uses this ability against mythic creatures, or 1d6+4 levels against non-mythic creatures.

**Poison (Ex)** Sting or _hand crossbow_—injury; save Fort DC 44; frequency 1/round for 6 rounds; effect 1d4 Wisdom drain plus _[[universal monster rules/Paralysis|paralysis]]_ for 1 round. Anyone who fails two consecutive saves against this poison is permanently _[[conditions/Blinded|blinded]]_. The save DC is Constitution-based.

**Profane _Ascension_ (Su)** As a swift action while in an act of passion with a willing mortal, Nocticula may grant a profane _ascension_. The target’s name appears in glowing Abyssal runes on Nocticula’s wings, and a crimson mark manifests somewhere on the target’s body. The target immediately gains a +6 profane bonus to any one ability score of its choice, a +4 profane bonus to any other ability score of its choice, and the _see in darkness_ ability. A single creature may have only one profane _ascension_ in effect at any one time. As long as the effect persists, Nocticula can communicate telepathically with the target across any distance and may use any of her _spell-like abilities_ through the target, manifesting them as if the target were using them. A profane _ascension_ may be removed by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_. Nocticula can remove it as a free action, dealing 4d6 points of Charisma drain and imparting 1d10+10 permanent negative levels to the victim.
**Seductive Presence (Su)** Unlike most demon lords, Nocticula does not possess a _[[universal monster rules/Frightful Presence|frightful presence]]_ ability. Rather, she has a seductive presence that she can activate as a free action whenever she speaks or uses a spell-like ability. Anyone within 180 feet who fails a DC 43 Fortitude save loses any _[[universal monster rules/Immunity|immunity]]_ to mind-affecting effects, charm effects, and compulsion effects, and becomes _[[conditions/Fascinated|fascinated]]_ by Nocticula for 5d4 rounds. A creature affected by a mind-affecting effect while within this aura remains affected even after leaving Nocticula’s seductive presence. Creatures that succeed at this saving throw are immune to this ability for 24 hours. The save DC is Charisma-based.
**Shadowkiss** Nocticula’s favored weapon is Shadowkiss, a +5 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _hand crossbow_ that magically creates ammunition as it fires. Once a target is damaged by a bolt fired from Shadowkiss, the _hand crossbow_ gains the _[[spells/Bane|bane]]_ weapon special ability against that target’s creature type on all further attacks. Shadowkiss may only have one _bane_ effect in place at one time. Bolts fired from Shadowkiss gain the _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ ability (an effect not normally available to ranged weapons).
**Swift _Transformation_ (Ex)** Nocticula can use her _change shape_ ability as a free action.

##### Description

Nocticula is the demon lord of assassins, _[[spells/Darkness|darkness]]_, and lust, and rules the Abyssal realm of the Midnight Isles, a vast archipelago formed around the murdered remnants of dozens of demon lords and other powerful foes. Having been the first succubus and then having ascended to become a demigoddess, Nocticula now sets her eyes at a greater prize—full divinity. Lamashtu is the only demon lord who has accomplished this task so far, but Nocticula aims to be the second. What kind of deity she might become is anyone’s guess—some believe that Nocticula is secretly seeking _[[feats/Redemption|redemption]]_ from her demonic nature. Others say these rumors were seeded by Nocticula herself as a grand lie to distract her enemies from her true goal of becoming an assassin and seducer of gods.

Nocticula is certainly mercurial in her personality and attitude. She may simply murder or enslave visitors to her realm, or she may welcome them with _[[spells/Open Arms|open arms]]_—even those who one would think were her enemies. Only a fool accepts her invitation without suspicion, for what the queen of succubi wants may change dramatically from one moment to the next.