---
cssclass: [monsters]
title1: Devil, Rust Devil (Ferrugon)
desc_short: This creature has curling ram's horns, metallic flesh that bears coiling
  ribbons of rust, and wings covered with rusty metallic feathers, each resembling
  a weathered dagger.
title2: Rust Devil (Ferrugon)
CR: 12
sources:
- name: 'Pathfinder #101: The Kintargo Contract'
  page: 82
  link: http://paizo.com/products/btpy9hdr?Pathfinder-Adventure-Path-101-The-Kintargo-Contract
XP: 19200
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect good: true
  see in darkness: true
AC:
  AC: 27
  touch: 15
  flat_footed: 22
  components:
    dex: 5
    natural: 12
HP:
  HP: 162
  long: 13d10+91
  regeneration: 5
  regeneration_weakness: good weapons, good spells, rust
saves:
  fort: 15
  ref: 13
  will: 10
DR:
- amount: 10
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 23
weaknesses:
- metallic
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 slams +19 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: slams
      bonus:
      - 19
    - text: 2 wings +19 (2d6+6/17-20 plus bleed and disease)
      entries:
      - - damage: 2d6+6
          crit_range: 17-20
        - effect: bleed
        - effect: disease
      count: 2
      attack: wings
      bonus:
      - 19
  ranged:
  - - text: 4 iron feathers +18 (1d6+6/19-20 plus disease)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
        - effect: disease
      count: 4
      attack: iron feathers
      bonus:
      - 18
  special:
  - bleed (1d4)
  - disease
  - iron feathers
  - slashing wings
  - vainglorious whispers
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: heat metal
    source: default
    freq: At will
    DC: 17
  - name: make whole
    source: default
    freq: At will
  - name: shatter
    source: default
    freq: At will
    DC: 17
  - name: shrink item
    source: default
    freq: At will
    DC: 18
  - name: fabricate
    source: default
    freq: 3/day
  - name: major creation
    source: default
    freq: 3/day
    other: iron objects only
  - name: rusting grasp
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  - name: wall of iron
    source: default
    freq: 3/day
  - name: flesh to iron
    source: default
    freq: 1/day
    DC: 21
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: barbed devil
      amount: 1
      chance: 50%
  - name: sympathetic vibration
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 17
ability_scores:
  STR: 23
  DEX: 20
  CON: 24
  INT: 18
  WIS: 19
  CHA: 21
BAB: 13
CMB: 19
CMB_other: +23 sunder
CMD: 34
CMD_other: 36 vs. sunder
feats:
- name: Combat Reflexes
- name: Greater Sunder
- name: Improved Critical (wing)
- name: Improved Sunder
- name: Infernal Legist (see page 64)
- name: Iron Will
- name: Power Attack
skills:
  Bluff: 21
  Disable Device: 21
  Fly: 25
  Intimidate: 21
  Knowledge (engineering): 20
  Knowledge (history): 17
  Knowledge (planes): 20
  Perception: 20
  Profession (architect): 20
  Sense Motive: 20
languages:
- Celestial
- Draconic
- Infernal
- Terran
- telepathy 100 ft.
special_qualities:
- slashing wings
ecology:
  environment: any (Hell)
  organization: solitary, pair, or company (3-7)
  treasure_type: standard
special_abilities:
  Disease (Ex): 'Scarlet Tetanus: Iron feather or wing-injury; save Fort DC 23; onset
    immediate; frequency 1/day; effect 1d4 Dex damage and 1 Con drain. Each time a
    victim takes Dexterity damage from scarlet tetanus, there is a 50% chance its
    jaw muscles and joints stiffen, preventing speech and the use of spells with verbal
    components for 24 hours; cure 2 consecutive saves. The save DC is Constitution-based.'
  Flesh to Iron (Sp): This spell-like ability functions as flesh to stone, save that
    it transforms the victim into iron, not stone. A victim turned to iron cannot
    be restored by stone to flesh, but break enchantment, polymorph any object, and
    similar spells can restore such a victim.
  Iron Feathers (Ex): With a flick of its wings, a rust devil can hurl a volley of
    four razor-sharp iron feathers at up to four targets as a standard action (make
    an attack roll for each feather). All targets must be within 30 feet of each other.
    This attack has a range increment of 40 feet, and threatens a critical hit on
    a result of 19-20. The rust devil's Strength modifier applies to the damage dealt
    by the feathers, as if the feathers were thrown weapons. The rust devil's feathers
    replenish instantly, allowing it to use this attack at will.
  Metallic (Ex): A rust devil's iron flesh makes it susceptible to rust attacks, such
    as those by a rust monster or a rusting grasp spell.
  Slashing Wings (Ex): A rust devil's wing attacks are primary attacks (except when
    it wields a manufactured weapon), and threaten a critical hit on a 19-20; most
    rust devils enhance this range to 17-20 with the Improved Critical feat.
  Vainglorious Whispers (Su): As a swift action, a rust devil can plant seeds of delusional
    pride in an adjacent target's mind by whispering to it. The target can resist
    the influence of these whispers with a successful DC 21 Will saving throw. On
    a failed save, the victim becomes overly confident in its abilities while in fact
    becoming less accomplished overall. The victim gains a +4 morale bonus on saving
    throws against fear effects but takes a -4 penalty on all attack rolls, weapon
    damage rolls, caster level checks, and skill checks. The victim cannot use the
    withdraw action, fight defensively, cast spells defensively, take the total defense
    action, or use healing magic or effects on itself. It can still accept healing
    from other sources, but must attempt saving throws to resist the effect if allowed.
    This is a mind-affecting, sonic, language-dependent effect, and the save DC is
    Charisma-based.
desc_long: |-
  A rust devil lives to sow the seeds of complacency, pride, and callous cynicism in the hearts of mortals. Also known as ferrugons, rust devils rarely attack first except when rising to defend buildings or other objects they have taken it upon themselves to protect. Rather than resorting to bloodshed, a rust devil instead seeks to bolster a mortal's pride and to convince him to undertake works of art, construction, or craft that are likely well beyond the mortal's skill. Nothing pleases a rust devil more than to see a mortal attempt something grand, fail spectacularly, and fall into a morass of depression, selfloathing, and jealousy for the rest of his life.

  In combat, a rust devil uses walls of iron to shape the battlefield to its advantage, and prefers to remain adjacent to foes so it can make full attacks on them and whisper in their ears. Against foes who wield weapons, rust devils almost always use Greater Sunder to damage weapons and foes alike. If faced with foes of particularly striking appearances (often those with a Charisma score of 15 or higher), a rust devil is likely to use its flesh to iron spell-like ability, then cast shrink item on the resulting statue to keep it as a decoration for its lair.

  A rust devil stands only 5 feet tall but weighs 900 pounds, because of its supernaturally dense metallic flesh.

---

# Devil, Rust Devil (Ferrugon)
This creature has curling ram’s horns, metallic flesh that bears coiling ribbons of rust, and wings covered with rusty metallic feathers, each resembling a weathered _[[items/Weapon/Dagger|dagger]]_.
**Source** Pathfinder #101: The Kintargo Contract pg. 82
**XP** 19,200

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +20

##### Defense

**AC** 27, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+5 Dex, +12 natural)
**hp** 162 (13d10+91); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells, rust)
**Fort** +15, **Ref** +13, **Will** +10
**DR** 10/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 23
**Weaknesses** metallic

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 slams +19 (1d8+6), 2 wings +19 (2d6+6/17–20 plus _[[universal monster rules/Bleed|bleed]]_ and disease)
**Ranged** 4 iron feathers +18 (1d6+6/19–20 plus disease)
**Special Attacks** _bleed_ (1d4), disease, iron feathers, slashing wings, vainglorious whispers
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
Constant—_detect good_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), greater teleport (self plus 50 lbs. of objects only), _[[spells/Heat Metal|heat metal]]_ (DC 17), _[[spells/Make Whole|make whole]]_, _[[spells/Shatter|shatter]]_ (DC 17), _[[spells/Shrink Item|shrink item]]_ (DC 18)
3/day—_[[spells/Fabricate|fabricate]]_, _[[spells/Major Creation|major creation]]_ (iron objects only), _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Wall of Iron|wall of iron]]_
1/day—flesh to iron (DC 21), _[[universal monster rules/Summon|summon]]_ (level 4, 1 barbed devil 50%), _[[spells/Sympathetic Vibration|sympathetic vibration]]_

##### Statistics
**Str** 23, **Dex** 20, **Con** 24, **Int** 18, **Wis** 19, **Cha** 21
**Base Atk** +13; **CMB** +19 (+23 sunder); **CMD** 34 (36 vs. sunder)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Critical|Improved Critical]]_ (wing), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Infernal Legist|Infernal Legist]]_ (see page 64), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +21, Disable Device +21, Fly +25, Intimidate +21, Knowledge (engineering) +20, Knowledge (history) +17, Knowledge (planes) +20, Perception +20, Profession (architect) +20, Sense Motive +20
**Languages** Celestial, Draconic, Infernal, Terran; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** slashing wings

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or company (3–7)
**Treasure** standard

### Special Abilities

**Disease (Ex)** Scarlet _[[diseases/Tetanus|Tetanus]]_: Iron feather or wing—injury; save Fort DC 23; onset immediate; frequency 1/day; effect 1d4 Dex damage and 1 Con drain. Each time a victim takes Dexterity damage from scarlet _tetanus_, there is a 50% chance its jaw muscles and joints stiffen, preventing speech and the use of spells with verbal components for 24 hours; cure 2 consecutive saves. The save DC is Constitution-based.

**Flesh to Iron (Sp)** This spell-like ability functions as _[[spells/Flesh to Stone|flesh to stone]]_, save that it transforms the victim into iron, not stone. A victim turned to iron cannot be restored by _[[spells/Stone to Flesh|stone to flesh]]_, but _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Polymorph Any Object|polymorph any object]]_, and similar spells can restore such a victim.

**Iron Feathers (Ex)** With a flick of its wings, a rust devil can hurl a volley of four razor-sharp iron feathers at up to four targets as a standard action (make an attack roll for each feather). All targets must be within 30 feet of each other. This attack has a range increment of 40 feet, and threatens a critical hit on a result of 19–20. The rust devil’s Strength modifier applies to the damage dealt by the feathers, as if the feathers were thrown weapons. The rust devil’s feathers replenish instantly, allowing it to use this attack at will.

**Metallic (Ex)** A rust devil’s iron flesh makes it susceptible to rust attacks, such as those by a _[[monsters/Rust Monster|rust monster]]_ or a _rusting grasp_ spell.
**Slashing Wings (Ex)** A rust devil’s wing attacks are primary attacks (except when it wields a manufactured weapon), and threaten a critical hit on a 19–20; most rust devils enhance this range to 17–20 with the _Improved Critical_ feat.

**Vainglorious Whispers (Su)** As a swift action, a rust devil can plant seeds of _[[spells/Delusional Pride|delusional pride]]_ in an adjacent target’s mind by whispering to it. The target can resist the influence of these whispers with a successful DC 21 Will saving throw. On a failed save, the victim becomes overly confident in its abilities while in fact becoming less accomplished overall. The victim gains a +4 morale bonus on saving throws against _[[universal monster rules/Fear|fear]]_ effects but takes a –4 penalty on all attack rolls, weapon damage rolls, caster level checks, and skill checks. The victim cannot use the withdraw action, fight defensively, cast spells defensively, take the total defense action, or use healing magic or effects on itself. It can still accept healing from other sources, but must attempt saving throws to resist the effect if allowed. This is a mind-affecting, sonic, language-dependent effect, and the save DC is Charisma-based.

##### Description

A rust devil lives to sow the seeds of complacency, pride, and callous cynicism in the hearts of mortals. Also known as ferrugons, rust devils rarely attack first except when rising to defend buildings or other objects they have taken it upon themselves to protect. Rather than resorting to bloodshed, a rust devil instead seeks to bolster a mortal’s pride and to convince him to undertake works of art, construction, or craft that are likely well beyond the mortal’s skill. Nothing pleases a rust devil more than to see a mortal attempt something grand, fail spectacularly, and fall into a morass of depression, selfloathing, and jealousy for the rest of his life.

In combat, a rust devil uses walls of iron to shape the battlefield to its advantage, and prefers to remain adjacent to foes so it can make full attacks on them and whisper in their ears. Against foes who wield weapons, rust devils almost always use _Greater Sunder_ to damage weapons and foes alike. If faced with foes of particularly striking appearances (often those with a Charisma score of 15 or higher), a rust devil is likely to use its flesh to iron spell-like ability, then cast _shrink item_ on the resulting _[[spells/Statue|statue]]_ to keep it as a decoration for its lair.

A rust devil stands only 5 feet tall but weighs 900 pounds, because of its supernaturally dense metallic flesh.