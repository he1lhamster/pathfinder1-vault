---
cssclass: [monsters]
title1: Great Old One, Ithaqua
desc_short: This looming humanoid shape has long, gangly limbs, glowing red eyes,
  and a gaping mouth full of fangs.
title2: Ithaqua
CR: 28
sources:
- name: 'Pathfinder #109: In Search of Sanity'
  page: 82
  link: http://paizo.com/products/btpy9nry?Pathfinder-Adventure-Path-109-In-Search-of-Sanity
XP: 4915200
alignment: CE
size: Gargantuan
type: monstrous humanoid
subtypes:
- air
- chaotic
- cold
- evil
- Great Old One
initiative:
  bonus: 24
senses:
  darkvision: 60
  low-light vision: true
  snow vision: true
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 36
AC:
  AC: 46
  touch: 27
  flat_footed: 35
  components:
    dex: 10
    dodge: 1
    insight: 10
    natural: 19
    size: -4
HP:
  HP: 688
  long: 32d10+512
  fast_healing: 25
saves:
  fort: 26
  ref: 30
  will: 28
defensive_abilities:
- immortality
- insanity (DC 36)
DR:
- amount: 15
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- energy drain
- mindaffecting effects
- paralysis
- petrification
- storms
resistances:
  electricity: 30
  sonic: 30
SR: 39
weaknesses:
- arctic bound
- vulnerable to fire
speeds:
  base: 60
  other:
  - air walk
attacks:
  melee:
  - - text: 2 slams +46 (4d6+18/19-20 plus grab)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: slams
      bonus:
      - 46
  ranged:
  - - text: 4 wind blasts +38 (8d6/19-20 plus hurl)
      entries:
      - - damage: 8d6
          crit_range: 19-20
        - effect: hurl
      count: 4
      attack: wind blasts
      bonus:
      - 38
  special:
  - arctic dreams
  - create wendigo
  - howl
  - mythic power (10/day, surge +1d12)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - is_mythic_spell: true
    name: control weather
    source: default
    freq: At will
    other: as druid
  - name: control winds
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - is_mythic_spell: true
    name: gust of wind
    source: default
    freq: At will
    DC: 22
  - is_mythic_spell: true
    name: ice storm
    source: default
    freq: At will
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 25
  - name: whispering wind
    source: default
    freq: At will
  - name: wind walk
    source: default
    freq: At will
    DC: 36
    other: see page 83
  - name: demand
    source: default
    freq: 3/day
    DC: 28
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 25
  - is_mythic_spell: true
    name: quickened gust of wind
    source: default
    freq: 3/day
    DC: 22
  - name: summon
    source: default
    freq: 3/day
    level: 9
    summons:
    - name: wendigos
      amount: 2d4
      chance: 100%
  - name: interplanetary teleport
    source: default
    freq: 1/day
    other: arctic regions only
  - is_mythic_spell: true
    name: storm of vengeance
    source: default
    freq: 1/day
    DC: 29
  - is_mythic_spell: true
    name: whirlwind
    source: default
    freq: 1/day
    DC: 28
  sources:
  - name: default
    CL: 28
    concentration: 38
ability_scores:
  STR: 46
  DEX: 31
  CON: 42
  INT: 29
  WIS: 31
  CHA: 30
BAB: 32
CMB: 54
CMB_other: +58 bull rush
CMD: 95
CMD_other: 97 vs. bull rush
feats:
- name: Awesome Blow
- name: Blinding Critical
- name: Critical Focus
- name: Dodge
- name: Greater Bull Rush
- name: Improved Bull Rush
- name: Improved Critical (slam)
- name: Improved Critical (wind blast)
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Quicken Spell-Like Ability (gust of wind)
- name: Spring Attack
skills:
  Acrobatics: 42
  Knowledge (arcana): 41
  Knowledge (geography): 41
  Knowledge (history): 41
  Knowledge (nature): 41
  Knowledge (planes): 41
  Knowledge (religion): 41
  Perception: 45
  Sense Motive: 42
  Spellcraft: 41
  Stealth: 33
  Survival: 45
  Use Magic Device: 42
languages:
- Aklo
- Aquan
- Giant
- telepathy 100 ft.
special_qualities:
- otherworldly insight
- wind walk
ecology:
  environment: any cold
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Arctic Bound (Ex): When Ithaqua is south of a planet's arctic circle or on a planet
    without a magnetic north, he is staggered.
  Arctic Dreams (Su): Any creature that has ever looked into Ithaqua's eyes or has
    committed cannibalism can be targeted by the Great Old One's arctic dreams regardless
    of distance, even across planar boundaries. If such a victim fails its save against
    Ithaqua's nightmare spell-like ability, the damage it takes from the ability is
    cold damage. Upon awakening, the victim is affected by a geas/quest to travel
    north beyond the arctic circle and, once there, await Ithaqua's arrival in a remote
    location. Whether or not the Great Old One comes to call is left to the GM to
    decide, but if Ithaqua does not visit within 1 month, the effects of the arctic
    dreams end.
  Create Wendigo (Su): |-
    By using wind walk with a creature or by affecting it with his unspeakable presence, Ithaqua afflicts the creature with an enhanced version of wendigo psychosis.

     Wendigo Psychosis: Curse-unspeakable presence or wind walk; save Will DC 36; onset immediate; frequency 1/hour; effect 1d6 Wis drain (minimum Wis 1). When a victim's Wisdom reaches 1, it seeks an individual of its race to kill and devour. After completing this act, the victim takes off at a run, and in 1d4 rounds sprints up into the sky at such a speed that its feet burn away into jagged stumps. The victim transforms into a wendigo (Pathfinder RPG Bestiary 2 281) over the next 1d4 minutes. Once the transformation is complete, the victim is effectively dead, replaced by a wendigo. Miracle, true resurrection, or wish can restore such a victim to life, yet doing so does not harm the new wendigo. The save DC is Charisma-based.
  Great Old One Traits: Rules for Great Old One traits like immortality, insanity,
    his mythic abilities, and otherworldly insight, and the base rules for unspeakable
    presence can be found on page 306 of Pathfinder RPG Bestiary 4.
  Howl (Su): Once every 1d4 rounds as a swift action, Ithaqua can emit a forlorn howl
    that can be heard up to 10 miles away. Any who hear the howl must make succeed
    at a DC 36 Will save to avoid becoming shaken for 24 hours. Creatures within 360
    feet of Ithaqua become panicked for 1d4+4 rounds, and those within 60 feet cower
    in fear for 1d4 rounds. Although this is a mind-affecting fear effect, immunity
    to fear does not offer full protection; a creature normally immune to fear must
    still succeed at a Will saving throw if within 60 feet to avoid becoming shaken
    for 1 hour (immunity to fear functions normally against Ithaqua's howl at greater
    distances). The save DC is Charisma-based.
  Immortality (Ex): If Ithaqua is slain, his body explodes in a burst of frozen wind
    that deals 20d6 points of cold damage to all creatures within a 60-foot spread
    (Reflex DC 42 half; the save DC is Constitution-based). Ithaqua reforms with full
    hit points 1 year later in another world's arctic region, but cannot return to
    the world on which he was slain via interplanetary teleport for another 10 years
    (or until outside agents allow for his travel to this world).
  Immune to Storms (Ex): Ithaqua is immune to the effects of any storm or storm-like
    condition unless he chooses otherwise. This includes being affected by high winds
    and by spells like ice storm and storm of vengeance.
  Snow Vision (Ex): Ithaqua can see perfectly well in snowy conditions, and does not
    take penalties on Perception checks when in snowy or blizzard conditions.
  Unspeakable Presence (Su): Failing a DC 36 Will saving throw against Ithaqua's unspeakable
    presence has two effects. First, it exposes the victim to Ithaqua's create wendigo
    ability (see page 82). In addition, the creature gains vulnerability to cold and
    loses any resistance or immunity to cold it had; this condition persists for 24
    hours. A creature that lacks any immunity or resistance to cold also becomes chilled
    by the Great Old One's presence, taking a -4 penalty on ranged attacks, initiative
    checks, Reflex saving throws, and Dexteritybased skill checks, as well as a -4
    penalty to Armor Class. These penalties last for 24 hours.
  Wind Walk (Sp): If Ithaqua pins a grappled foe, he can attempt to use wind walk
    with the grappled foe by using his spell-like ability-he automatically succeeds
    at all concentration checks made to use wind walk in this case. If the victim
    fails to resist the spell, Ithaqua hurtles into the sky with it. Each round, a
    victim can attempt a new DC 36 Will saving throw to turn solid again, but at this
    point it falls if it cannot fly. A creature affected by Ithaqua's wind walk in
    this way might begin transformation into a wendigo (see Create Wendigo on page
    82), and eventually Ithaqua strands the victim in some rural area, often miles
    or even worlds away from where it began. The save DC is Charisma-based.
desc_long: |-
  Also known as the Wind-Walker, Ithaqua has visited countless worlds during his travels throughout the universe. Whether he is able to visit only worlds with arctic circles and magnetic poles, or whether those worlds have such conditions because the Great Old One visited them in their earliest days is unclear.

  Ithaqua appears as a 50-foot-tall primitive humanoid with glowing red eyes and unnaturally long arms, yet his feet are always cloaked in blasts of thick snow-laden and freezing winds.

---

# Great Old One, Ithaqua
This looming humanoid shape has long, gangly limbs, glowing red eyes, and a gaping mouth full of fangs.
**Source** Pathfinder #109: In Search of Sanity pg. 82
**XP** 4,915,200
CE Gargantuan monstrous humanoid (air, chaotic, cold, evil, Great Old One)
**Init** +24; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, snow _[[spells/Vision|vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +45
**Aura** unspeakable presence (300 ft., DC 36)

##### Defense

**AC** 46, touch 27, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+10 Dex, +1 dodge, +10 insight, +19 natural, –4 size)
**hp** 688 (32d10+512); _[[universal monster rules/Fast Healing|fast healing]]_ 25
**Fort** +26, **Ref** +30, **Will** +28
**Defensive Abilities** immortality, _[[spells/Insanity|insanity]]_ (DC 36); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mindaffecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, storms; **Resist** electricity 30, sonic 30; **SR** 39
**Weaknesses** arctic bound, vulnerable to fire

##### Offense
**Speed** 60 ft., _[[spells/Air Walk|air walk]]_
**Melee** 2 slams +46 (4d6+18/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** 4 wind blasts +38 (8d6/19–20 plus hurl)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** arctic dreams, create _[[monsters/Wendigo|wendigo]]_, howl, mythic power (10/day, surge +1d12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 28th; concentration +38)
Constant—_air walk_, _true seeing_
At will—_[[spells/Control Weather|control weather]]_ (as _[[classes/Druid|druid]]_), _[[spells/Control Winds|control winds]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 22), _[[spells/Ice Storm|ice storm]]_, _[[spells/Nightmare|nightmare]]_ (DC 25), _[[spells/Whispering Wind|whispering wind]]_, _[[spells/Wind Walk|wind walk]]_ (DC 36; see page 83)
3/day—_[[spells/Demand|demand]]_ (DC 28), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 25), quickened _gust of wind_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 9, 2d4 wendigos 100%)
1/day—_[[spells/Interplanetary Teleport|interplanetary teleport]]_ (arctic regions only), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 29), _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 28)

##### Statistics
**Str** 46, **Dex** 31, **Con** 42, **Int** 29, **Wis** 31, **Cha** 30
**Base Atk** +32; **CMB** +54 (+58 bull rush); **CMD** 95 (97 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _Improved Critical_ (wind blast), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_, _gust of wind_), _[[feats/Spring Attack|Spring Attack]]_
**Skills** Acrobatics +42, Knowledge (arcana, geography, history, nature, planes, religion) +41, Perception +45, Sense Motive +42, Spellcraft +41, Stealth +33, Survival +45, Use Magic Device +42
**Languages** Aklo, Aquan, Giant; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** otherworldly insight, _wind walk_

##### Ecology

**Environment** any cold
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Arctic Bound (Ex)** When Ithaqua is south of a planet’s arctic circle or on a planet without a magnetic north, he is _[[conditions/Staggered|staggered]]_.

**Arctic Dreams (Su)** Any creature that has ever looked into Ithaqua’s eyes or has committed cannibalism can be targeted by the Great Old One’s arctic dreams regardless of distance, even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries. If such a victim fails its save against Ithaqua’s _nightmare_ spell-like ability, the damage it takes from the ability is cold damage. Upon awakening, the victim is affected by a geas/quest to travel north beyond the arctic circle and, once there, await Ithaqua’s arrival in a remote location. Whether or not the Great Old One comes to call is left to the GM to decide, but if Ithaqua does not visit within 1 month, the effects of the arctic dreams end.

**Create _Wendigo_ (Su)** By using _wind walk_ with a creature or by affecting it with his unspeakable presence, Ithaqua afflicts the creature with an enhanced version of _wendigo_ psychosis.

_Wendigo_ Psychosis: Curse—unspeakable presence or _wind walk_; save Will DC 36; onset immediate; frequency 1/hour; effect 1d6 Wis drain (minimum Wis 1). When a victim’s Wisdom reaches 1, it seeks an individual of its race to kill and devour. After completing this act, the victim takes off at a run, and in 1d4 rounds sprints up into the sky at such a speed that its feet _[[universal monster rules/Burn|burn]]_ away into jagged stumps. The victim transforms into a _wendigo_ (Pathfinder RPG Bestiary 2 281) over the next 1d4 minutes. Once the _[[spells/Transformation|transformation]]_ is complete, the victim is effectively dead, replaced by a _wendigo_. _[[spells/Miracle|Miracle]]_, _[[spells/True Resurrection|true resurrection]]_, or _[[spells/Wish|wish]]_ can restore such a victim to life, yet doing so does not _[[spells/Harm|harm]]_ the new _wendigo_. The save DC is Charisma-based.

**Great Old One Traits** Rules for Great Old One traits like immortality, _insanity_, his mythic abilities, and otherworldly insight, and the base rules for unspeakable presence can be found on page 306 of Pathfinder RPG Bestiary 4.

**Howl (Su)** Once every 1d4 rounds as a swift action, Ithaqua can emit a forlorn howl that can be heard up to 10 miles away. Any who hear the howl must make succeed at a DC 36 Will save to avoid becoming _[[conditions/Shaken|shaken]]_ for 24 hours. Creatures within 360 feet of Ithaqua become _[[conditions/Panicked|panicked]]_ for 1d4+4 rounds, and those within 60 feet cower in _[[universal monster rules/Fear|fear]]_ for 1d4 rounds. Although this is a mind-affecting _fear_ effect, _[[universal monster rules/Immunity|immunity]]_ to _fear_ does not offer full protection; a creature normally immune to _fear_ must still succeed at a Will saving throw if within 60 feet to avoid becoming _shaken_ for 1 hour (_immunity_ to _fear_ functions normally against Ithaqua’s howl at greater distances). The save DC is Charisma-based.

**Immortality (Ex)** If Ithaqua is slain, his body explodes in a burst of frozen wind that deals 20d6 points of cold damage to all creatures within a 60-foot spread (Reflex DC 42 half; the save DC is Constitution-based). Ithaqua reforms with full hit points 1 year later in another world’s arctic region, but cannot return to the world on which he was slain via _interplanetary teleport_ for another 10 years (or until outside agents allow for his travel to this world).

**Immune to Storms (Ex)** Ithaqua is immune to the effects of any storm or storm-like condition unless he chooses otherwise. This includes being affected by high winds and by spells like _ice storm_ and _storm of vengeance_.
**Snow _Vision_ (Ex)** Ithaqua can see perfectly well in snowy conditions, and does not take penalties on Perception checks when in snowy or blizzard conditions.

**Unspeakable Presence (Su)** Failing a DC 36 Will saving throw against Ithaqua’s unspeakable presence has two effects. First, it exposes the victim to Ithaqua’s create _wendigo_ ability (see page 82). In addition, the creature gains _[[curses/Vulnerability|vulnerability]]_ to cold and loses any _[[universal monster rules/Resistance|resistance]]_ or _immunity_ to cold it had; this condition persists for 24 hours. A creature that lacks any _immunity_ or _resistance_ to cold also becomes chilled by the Great Old One’s presence, taking a –4 penalty on ranged attacks, initiative checks, Reflex saving throws, and Dexteritybased skill checks, as well as a –4 penalty to Armor Class. These penalties last for 24 hours.

**_Wind Walk_ (Sp)** If Ithaqua pins a _[[conditions/Grappled|grappled]]_ foe, he can attempt to use _wind walk_ with the _grappled_ foe by using his spell-like ability—he automatically succeeds at all concentration checks made to use _wind walk_ in this case. If the victim fails to resist the spell, Ithaqua hurtles into the sky with it. Each round, a victim can attempt a new DC 36 Will saving throw to turn solid again, but at this point it falls if it cannot fly. A creature affected by Ithaqua’s _wind walk_ in this way might begin _transformation_ into a _wendigo_ (see Create _Wendigo_ on page 82), and eventually Ithaqua strands the victim in some rural area, often miles or even worlds away from where it began. The save DC is Charisma-based.

##### Description

Also known as the Wind-Walker, Ithaqua has visited countless worlds during his travels throughout the universe. Whether he is able to visit only worlds with arctic circles and magnetic poles, or whether those worlds have such conditions because the Great Old One visited them in their earliest days is unclear.

Ithaqua appears as a 50-foot-tall primitive humanoid with glowing red eyes and unnaturally long arms, yet his feet are always cloaked in blasts of thick snow-laden and freezing winds.