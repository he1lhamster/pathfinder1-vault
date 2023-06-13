---
cssclass: [monsters]
title1: Anemos
desc_short: Strong winds whip around this majestic being, and lightning crackles from
  her eyes and flickers along her skin.
title2: Anemos
CR: 18
sources:
- name: Bestiary 5
  page: 20
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 153600
alignment: N
size: Medium
type: outsider
subtypes:
- air
- elemental
- extraplanar
initiative:
  bonus: 14
senses:
  blindsight: 120
  darkvision: 60
AC:
  AC: 34
  touch: 30
  flat_footed: 24
  components:
    deflection: 10
    dex: 10
    natural: 4
HP:
  HP: 341
  long: 22d10+220
  regeneration: 15
  regeneration_weakness: earth; see earthbane
saves:
  fort: 23
  ref: 23
  will: 17
defensive_abilities:
- windblessed
DR:
- amount: 15
  weakness: '-'
immunities:
- daze
- electricity
- elemental traits
resistances:
  cold: 30
  fire: 30
SR: 29
weaknesses:
- earthbane
speeds:
  base: 30
  fly: 480
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +5 shock thundering spear +31/+26/+21/+16 (1d8+11/19-20/×3 plus 1d6 electricity)
      entries:
      - - damage: 1d8+11
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: electricity
      attack: +5 shock thundering spear
      bonus:
      - 31
      - 26
      - 21
      - 16
  ranged:
  - - text: thunderstorm blast +32 (20d6+30/19-20 bludgeoning)
      entries:
      - - damage: 20d6+30
          type: bludgeoning
          crit_range: 19-20
      attack: thunderstorm blast
      bonus:
      - 32
  - - text: electric blast +32 touch (10d6+5/19-20 electricity)
      entries:
      - - damage: 10d6+5
          type: electricity
          crit_range: 19-20
      attack: electric blast
      bonus:
      - 32
      touch: true
  - - text: air blast +32 (10d6+20/19-20 half bludgeoning and half electricity)
      entries:
      - - damage: 10d6+20
          type: half bludgeoning and half electricity
          crit_range: 19-20
      attack: air blast
      bonus:
      - 32
  special:
  - aerokinesis
  - infusions (chain, cloud, cyclone, extreme range, gusting infusion, pushing infusion,
    thundering infusion)
  - manifest thunderbolt
  - wind orchestra
spell_like_abilities:
  entries:
  - name: fickle winds
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: control weather
    source: default
    freq: At will
  - name: control winds
    source: default
    freq: At will
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 29
  - name: summon monster IX
    source: default
    freq: 1/day
    other: 1d3 elder air elementals only
  sources:
  - name: default
    CL: 20
    concentration: 30
ability_scores:
  STR: 18
  DEX: 31
  CON: 30
  INT: 23
  WIS: 26
  CHA: 31
BAB: 22
CMB: 26
CMD: 57
feats:
- name: Combat Reflexes
- name: Deadly Aim
- name: Flyby Attack
- name: Improved Critical (kinetic blast)
- name: Improved Critical (spear)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Precise Shot
- name: Iron Will
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Acrobatics: 35
  Fly: 43
  Knowledge (geography): 31
  Knowledge (nature): 31
  Knowledge (planes): 31
  Perception: 33
  Perform (wind instruments): 37
  Sense Motive: 33
  Spellcraft: 28
  Stealth: 35
  Survival: 30
  Use Magic Device: 35
languages:
- Aquan
- Auran
- Common
- Ignan
- Sylvan
- Terran
special_qualities:
- manifest thunderbolt
- utility wild talents (air's reach, greater windsight, ride the blast, windsight)
- wind form
ecology:
  environment: any sky (Plane of Air or Material Plane)
  organization: solitary or council (4)
  treasure_type: triple
special_abilities:
  Aerokinesis (Sp, Su): An anemos has access to a variety of air wild talents as if
    it were a 20th-level kineticist. As a being of pure wind, it can perform the air
    and electric simple blasts and the thunderstorm composite blast at no burn cost.
    The anemos gains infusions and utility talents listed under its other special
    abilities, but doesn't gain any other abilities of a 20th-level kineticist.
  Earthbane: An anemos's windblessed ability and regeneration are suppressed whenever
    any part of the creature is submerged at least 1 inch into earth (including dirt,
    mud, or clay). While an anemos is airborne, only pure elemental earth attacks
    (like an earth simple blast or an earth elemental's slam attack) can suppress
    the anemos's regeneration.
  Infusions (Su): An anemos has access to the kineticist form and substance infusions
    listed in its Special Attacks entry, which it can apply to any of the blasts granted
    by its aerokinesis ability without needing to accept burn. This applies to only
    the base burn cost; an anemos can't accept additional burn to gain a greater effect
    with infusions such as pushing infusion.
  Manifest Thunderbolt (Su): An anemos's spear is an actual thunderbolt, which it
    can form at will as a free action.
  Utility Wild Talents (Sp, Su: ) An anemos gains access to the kineticist utility
    wild talents listed in its SQ entry.
  Wind Form (Ex): An anemos can cause its body to become more diffuse than normal,
    losing its human-shaped coherence and instead becoming a formless and invisible
    wind. When an anemos enters wind form, it automatically escapes from any grapples
    or bindings that managed to hold it despite its freedom of movement, and gains
    the natural invisibility ability, but can't use aerokinesis or its spear attack.
  Wind Orchestra (Su): An anemos can use the winds themselves as wind instruments,
    which count as masterwork instruments for the purpose of its Perform (wind instruments)
    skill. It can use its winds to duplicate the effects of the countersong or dirge
    of doom bardic performances as if it were a bard with a number of rounds of bardic
    performance per day equal to its Charisma bonus. Beginning this performance is
    a swift action.
  Windblessed (Su): An anemos is like a god unto the wind, and the wind zealously
    protects it. It gains a deflection bonus to its AC equal to its Charisma bonus.
    An anemos is never affected by winds or weather effects unless it chooses to be.
desc_long: |-
  Anemoi are godlike beings from the Plane of Air, masters of the storm and sky. While an anemos appears humanoid in shape, even a cursory glance reveals that its humanlike appearance is a complete facade, for its 6-foot-tall body is composed of solidified air, has no vital organs, and is nearly weightless. The winds themselves obey an anemos, and greater sky deities often task four anemoi with controlling the wind patterns for an entire world on the Material Plane.

  Implacable but not malevolent, an anemos guides its winds along the paths dictated by nature, heedless of how the weather patterns help or harm the creatures in their paths, whether through drought, flood, tornadoes, or hurricanes. Mighty heroes sometimes trap an anemos in earth and force it to protect the heroes' allies or destroy their enemies in exchange for its freedom. While an anemos always honors such agreements, such heroes may find the weather turning against them at a crucial moment many years later.

  Anemoi generally have little to do with their own kind, though they may hold court with a plethora of lesser air creatures. Councils of anemoi occur perhaps once every millennium, when the four anemoi who oversee a particular world assemble to confer and debate. Their personalities take on aspects of the winds they guide, and such councils often end in duels of winds, though such duels are always nonlethal due to the anemoi's regeneration.

  Anemoi are particularly fond of music, particularly that of wind instruments, and each can perform as a full wind ensemble with its own winds simultaneously. They appreciate musical talent in their followers, allowing sirens and other creatures with musical skills to join their courts. Despite anemoi's aloofness, skilled mortal musicians can earn their way into the creatures' good graces, and romance between anemoi and mortals, while extraordinarily rare, is not impossible.

  Though they are beings of air, anemoi usually choose to appear in humanoid form. Many sylphs, sorcerers with an air elemental bloodline, and aerokineticists make grandiose claims about anemos descent, but only a handful have the pedigree to support those claims, and they tend to become notable heroes and villains in their own right.

---

# Anemos
Strong winds _[[items/Weapon/Whip|whip]]_ around this majestic being, and lightning crackles from her eyes and flickers along her skin.
**Source** Bestiary 5 pg. 20
**XP** 153,600

N Medium outsider (air, elemental, extraplanar)
**Init** +14; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +33

##### Defense

**AC** 34, touch 30, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+10 _[[spells/Deflection|deflection]]_, +10 Dex, +4 natural)
**hp** 341 (22d10+220); _[[universal monster rules/Regeneration|regeneration]]_ 15 (earth; see earthbane)
**Fort** +23, **Ref** +23, **Will** +17
**Defensive Abilities** windblessed; **DR** 15/—; **Immune** _[[spells/Daze|daze]]_, electricity, elemental traits; **Resist** cold 30, fire 30; **SR** 29
**Weaknesses** earthbane

##### Offense
**Speed** 30 ft., fly 480 ft. (perfect)
**Melee** +5 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon Magic Abilities/Thundering|thundering]]_ _[[items/Weapon/Spear|spear]]_ +31/+26/+21/+16 (1d8+11/19-20/×3 plus 1d6 electricity)
**Ranged** thunderstorm blast +32 (20d6+30/19-20 bludgeoning) or electric blast +32 touch (10d6+5/19-20 electricity) or air blast +32 (10d6+20/19-20 half bludgeoning and half electricity)
**Special Attacks** aerokinesis, infusions (chain, cloud, cyclone, extreme range, gusting infusion, pushing infusion, _thundering_ infusion), manifest thunderbolt, wind orchestra
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +30)
Constant—_[[spells/Fickle Winds|fickle winds]]_, _[[spells/Freedom of Movement|freedom of movement]]_
At will—_[[spells/Control Weather|control weather]]_, _[[spells/Control Winds|control winds]]_
1/day—_[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 29), _[[spells/Summon Monster IX|summon monster IX]]_ (1d3 elder air elementals only)

##### Statistics
**Str** 18, **Dex** 31, **Con** 30, **Int** 23, **Wis** 26, **Cha** 31
**Base Atk** +22; **CMB** +26; **CMD** 57
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (kinetic blast), _Improved Critical_ (_spear_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Acrobatics +35, Fly +43, Knowledge (geography) +31, Knowledge (nature) +31, Knowledge (planes) +31, Perception +33, Perform (wind instruments) +37, Sense Motive +33, Spellcraft +28, Stealth +35, Survival +30, Use Magic Device +35
**Languages** Aquan, Auran, Common, Ignan, Sylvan, Terran
**SQ** manifest thunderbolt, utility wild talents (air’s reach, greater windsight, ride the blast, windsight), wind form

##### Ecology

**Environment** any sky (Plane of Air or Material Plane)
**Organization** solitary or council (4)
**Treasure** triple

### Special Abilities

**Aerokinesis (Sp, Su)** An _[[monsters/Anemos|anemos]]_ has access to a variety of air wild talents as if it were a 20th-level _[[classes/Kineticist|kineticist]]_. As a being of pure wind, it can perform the air and electric simple blasts and the thunderstorm composite blast at no _[[universal monster rules/Burn|burn]]_ cost. The _anemos_ gains infusions and utility talents listed under its other special abilities, but doesn’t gain any other abilities of a 20th-level _kineticist_.

**Earthbane** An _anemos_’s windblessed ability and _regeneration_ are suppressed whenever any part of the creature is submerged at least 1 inch into earth (including dirt, mud, or _[[items/Mundane/Clay|clay]]_). While an _anemos_ is airborne, only pure elemental earth attacks (like an earth simple blast or an earth elemental’s slam attack) can suppress the _anemos_’s _regeneration_.

**Infusions (Su)** An _anemos_ has access to the _kineticist_ form and substance infusions listed in its Special Attacks entry, which it can apply to any of the blasts granted by its aerokinesis ability without needing to accept _burn_. This applies to only the base _burn_ cost; an _anemos_ can’t accept additional _burn_ to gain a greater effect with infusions such as pushing infusion.

**Manifest Thunderbolt (Su)** An _anemos_’s _spear_ is an actual thunderbolt, which it can form at will as a free action.

**Utility Wild Talents (Sp, Su**) An _anemos_ gains access to the _kineticist_ utility wild talents listed in its SQ entry.

**Wind Form (Ex)** An _anemos_ can cause its body to become more diffuse than normal, losing its human-shaped coherence and instead becoming a formless and _[[conditions/Invisible|invisible]]_ wind. When an _anemos_ enters wind form, it automatically escapes from any grapples or bindings that managed to hold it despite its _freedom of movement_, and gains the _[[universal monster rules/Natural Invisibility|natural invisibility]]_ ability, but can’t use aerokinesis or its _spear_ attack.

**Wind Orchestra (Su)** An _anemos_ can use the winds themselves as wind instruments, which count as masterwork instruments for the purpose of its Perform (wind instruments) skill. It can use its winds to duplicate the effects of the countersong or dirge of _[[spells/Doom|doom]]_ bardic performances as if it were a _[[classes/Bard|bard]]_ with a number of rounds of bardic performance per day equal to its Charisma bonus. Beginning this performance is a swift action.

**Windblessed (Su)** An _anemos_ is like a god unto the wind, and the wind zealously protects it. It gains a _deflection_ bonus to its AC equal to its Charisma bonus. An _anemos_ is never affected by winds or weather effects unless it chooses to be.

##### Description

Anemoi are godlike beings from the Plane of Air, masters of the storm and sky. While an _anemos_ appears humanoid in shape, even a cursory glance reveals that its humanlike appearance is a complete facade, for its 6-foot-tall body is composed of solidified air, has no vital organs, and is nearly weightless. The winds themselves obey an _anemos_, and greater sky deities often task four anemoi with controlling the wind patterns for an entire world on the Material Plane.

Implacable but not _[[items/Armor Magic Abilities/Malevolent|malevolent]]_, an _anemos_ guides its winds along the paths dictated by nature, heedless of how the weather patterns help or _[[spells/Harm|harm]]_ the creatures in their paths, whether through drought, flood, tornadoes, or hurricanes. Mighty heroes sometimes trap an _anemos_ in earth and force it to protect the heroes’ allies or destroy their enemies in exchange for its _[[spells/Freedom|freedom]]_. While an _anemos_ always honors such agreements, such heroes may find the weather turning against them at a crucial moment many years later.

Anemoi generally have little to do with their own kind, though they may hold court with a plethora of lesser air creatures. Councils of anemoi occur perhaps once every millennium, when the four anemoi who oversee a particular world assemble to confer and debate. Their personalities take on aspects of the winds they guide, and such councils often end in duels of winds, though such duels are always nonlethal due to the anemoi’s _regeneration_.

Anemoi are particularly fond of music, particularly that of wind instruments, and each can perform as a full wind _[[feats/Ensemble|ensemble]]_ with its own winds simultaneously. They appreciate musical talent in their followers, allowing sirens and other creatures with musical skills to join their courts. Despite anemoi’s aloofness, skilled mortal musicians can earn their way into the creatures’ good graces, and romance between anemoi and mortals, while extraordinarily rare, is not impossible.

Though they are beings of air, anemoi usually choose to appear in humanoid form. Many sylphs, sorcerers with an air elemental bloodline, and aerokineticists make grandiose claims about _anemos_ descent, but only a handful have the pedigree to support those claims, and they tend to become notable heroes and villains in their own right.