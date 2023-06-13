---
cssclass: [monsters]
title1: Ilzunae, the Gloom Widow
desc_short: This lithe, shadowy creature is obviously feminine, yet the talons and
  horns leave no doubt as to her fiendish nature.
title2: Ilzunae, the Gloom Widow
CR: 19
sources:
- name: Demons Revisited
  page: 32
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 204800
race: Female
classes:
- shadow demon cleric of Nocticula 15 (Pathfinder RPG Bestiary 67)
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- incorporeal
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 33
  touch: 25
  flat_footed: 27
  components:
    armor: 8
    deflection: 8
    dex: 5
    dodge: 1
    insight: 1
HP:
  HP: 274
  long: 7d10+15d8+169
  HD: 22
saves:
  fort: 17
  ref: 16
  will: 19
  other: +4 vs. blindness and charm
defensive_abilities:
- incorporeal
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- cold
- electricity
- poison
resistances:
  acid: 10
  fire: 10
SR: 17
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +24 (1d6 plus 1d6 cold)
      entries:
      - - damage: 1d6
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 24
    - text: 2 claws +24 (1d4 plus 1d6 cold)
      entries:
      - - damage: 1d4
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 24
  special:
  - channel negative energy 11/day (DC 25, 8d6)
  - pounce
  - shadow blend
  - sprint
spell_like_abilities:
  entries:
  - name: quickened blindness/deafness
    source: default
    freq: 3/day
    DC: 20
  - name: charm person
    source: default
    freq: 3/day
    DC: 19
  - name: dominate thrall
    source: default
    freq: 1/day
  - name: charming smile
    source: domain
    freq: At Will
    other: 15 rounds
    DC: 17
  - name: dazing touch
    source: domain
    freq: 8/day
  - name: touch of darkness
    source: domain
    freq: 8/day
    other: 7 rounds
  - name: deeper darkness
    source: invidiak
    freq: At will
  - name: fear
    source: invidiak
    freq: At will
    DC: 22
  - name: greater teleport
    source: invidiak
    freq: At will
    other: self only
  - name: telekinesis
    source: invidiak
    freq: At will
    DC: 23
  - name: shadow conjuration
    source: invidiak
    freq: 3/day
    DC: 22
  - name: shadow evocation
    source: invidiak
    freq: 3/day
    DC: 23
  - name: magic jar
    source: invidiak
    freq: 1/day
    DC: 23
  - name: summon
    source: invidiak
    freq: 1/day
    level: 3
    summons:
    - name: shadow demon
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 22
    concentration: 30
  - name: domain
    CL: 15
    concentration: 20
  - name: invidiak
    CL: 10
    concentration: 18
spells:
  entries:
  - is_domain_spell: true
    name: demand
    source: Cleric
    level: 8
    DC: 23
  - superscripts:
    - BOTD2
    name: rift of ruin
    source: Cleric
    level: 8
    DC: 23
  - name: quickened cure critical wounds
    source: Cleric
    level: 7
  - name: destruction
    source: Cleric
    level: 7
    DC: 22
  - is_domain_spell: true
    name: power word blind
    source: Cleric
    level: 7
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 21
  - name: quickened death knell
    source: Cleric
    level: 6
    DC: 17
  - is_domain_spell: true
    name: geas/quest
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: quickened command
    source: Cleric
    level: 5
    DC: 16
  - name: flame strike
    source: Cleric
    level: 5
    DC: 20
  - name: greater command
    source: Cleric
    level: 5
    DC: 20
  - name: slay living
    source: Cleric
    level: 5
    DC: 20
  - is_domain_spell: true
    name: summon monster V
    source: Cleric
    level: 5
    other: summons 1d3 shadows
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: discern lies
    source: Cleric
    level: 4
    DC: 19
  - name: poison
    source: Cleric
    level: 4
    DC: 19
  - name: sending
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: shadow conjuration
    source: Cleric
    level: 4
    DC: 19
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - name: cure serious wounds
    source: Cleric
    level: 3
    count: 2
  - name: dispel magic
    source: Cleric
    level: 3
  - name: speak with dead
    source: Cleric
    level: 3
    DC: 18
  - is_domain_spell: true
    name: suggestion
    source: Cleric
    level: 3
    DC: 18
  - is_domain_spell: true
    name: blindness/deafness
    source: Cleric
    level: 2
    DC: 17
    other: only to cause blindness
  - name: cure moderate wounds
    source: Cleric
    level: 2
    count: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - name: undetectable alignment
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: charm person
    source: Cleric
    level: 1
    DC: 16
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 5
  - name: divine favor
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 15
    concentration: 20
    slots:
      0: at-will
    domains:
    - charm
    - darkness
ability_scores:
  STR:
  DEX: 22
  CON: 22
  INT: 14
  WIS: 20
  CHA: 26
BAB: 18
CMB: 24
CMD: 44
feats:
- name: Blind-Fight
- name: Combat Expertise
- superscripts:
  - BOTD2
  name: Demonic Obedience
- name: Dodge
- name: Eschew Materials
- name: Improved Possession
- name: Lightning Stance
- name: Mobility
- name: Quicken Spell
- name: Spring Attack
- name: Toughness
- name: Wind Stance
skills:
  Bluff: 33
  Diplomacy: 33
  Fly: 32
  Knowledge (planes): 20
  Knowledge (religion): 17
  Perception: 31
  Sense Motive: 23
languages:
- Abyssal
- Draconic
- telepathy 100 ft.
special_qualities:
- eyes of darkness (7 rounds/day)
gear:
  gear:
  - +5 glamered ghost touch studded leather
  - deep red sphere ioun stone
  - dusty rose prism ioun stone
  - pink and green sphere ioun stone
  - pink rhomboid ioun stone
  - manual of bodily health +1 (used)
special_abilities:
  Dominate Thrall (Sp): Once per day, Ilzunae may cast dominate monster. She may only
    have one creature dominated at a time via this effect, but the effects are permanent
    until she dominates a new target, at which point the previous target is released
    from domination but is stunned for 1d4 rounds.
desc_long: |-
  Not all of Nocticula's favored servants are succubi. Ever since her slaughter of the demon lord Vyriavaxus, she has also been served by the invidiaks. Some of these demons, of course, turned away from the murderer of their patron and have gone on to serve other demon lords or even to strike out on their own, but those who became loyal to her found that their new mistress was every bit as dangerous as their old lord of shadows, and quite a bit more forthcoming at rewarding those who served her well.

  Ilzunae is the first of these shadow demons to have been awarded stewardship of one of the many Midnight Isles of Nocticula's Abyssal realm. Kovalarue is one of the realm's smaller islands, but in some ways is one of its most beautiful, consisting of rolling hills covered with wildflowers and idyllic streams and lakes. That those flowers drink blood and that those lakes can pull those who look into their waters below to drown them does not mar this beauty, and Ilzunae has proven more than a capable keeper of this land.

  The Gloom Widow earned her appellation as a result of her preferred method of preying upon mortals. When she finds herself on the Material Plane, she seeks out young couples who are too shy or hesitant to make the first steps toward forming a relationship, then possesses one of their friends. Using that friend as a proxy, she arranges for the couple to meet, fall in love, and eventually wed, retaining control of the friend the whole time. During the honeymoon, Ilzunae brings the friend to a distant city via teleportation, informs the friend of her plans before releasing him, then teleports back to the honeymooners, where she possesses one of them to enjoy their first night of wedded bliss. The nonpossessed spouse never survives until the dawn, and if they are lucky, Ilzunae waits until the final hour of the night to shift from sharing bliss to giving pain. She then abandons the possessed widow or widower with a message that all this was made possible through the jealousy of the friend, who has fled to a distant city. In most cases, the surviving spouse either commits suicide or seeks out the “friend” to murder them, and when she can, Ilzunae enjoys intercepting those sinful lost souls when they come to the Abyss so she can harvest and keep them in gilt bird cages in her palace as trophies.

  Ilzunae prefers promises of time left to her own devices on the Material Plane, but will accept the bodies of grieving widows or widowers as well. It's a DC 29 check to research the Gloom Widow.

---

# Ilzunae, the Gloom Widow
This lithe, shadowy creature is obviously feminine, yet the talons and horns leave no doubt as to her fiendish nature.
**Source** Demons Revisited pg. 32
**XP** 204,800
Female _[[items/Armor Magic Abilities/Shadow|shadow]]_ demon _[[classes/Cleric|cleric]]_ of Nocticula 15 (Pathfinder RPG Bestiary 67)
CE Medium outsider (chaotic, demon, evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +31

##### Defense

**AC** 33, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+8 armor, +8 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +1 insight)
**hp** 274 (22 HD; 7d10+15d8+169)
**Fort** +17, **Ref** +16, **Will** +19; +4 vs. blindness and charm
**Defensive Abilities** _incorporeal_; **DR** 10/cold iron or good; **Immune** cold, electricity, poison; **Resist** acid 10, fire 10; **SR** 17

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** bite +24 (1d6 plus 1d6 cold), 2 claws +24 (1d4 plus 1d6 cold)
**Special Attacks** channel negative energy 11/day (DC 25, 8d6), _[[universal monster rules/Pounce|pounce]]_, _shadow_ _[[spells/Blend|blend]]_, sprint
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 22nd; concentration +30)
3/day—quickened blindness/deafness (DC 20), _[[spells/Charm Person|charm person]]_ (DC 19)
1/day—dominate thrall
**Domain _Spell-Like Abilities_ **(CL 15th; concentration +20)
At Will—charming smile (15 rounds, DC 17)
8/day—dazing touch, touch of _[[spells/Darkness|darkness]]_ (7 rounds)
**Invidiak _Spell-Like Abilities_ **(CL 10th; concentration +18)
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[universal monster rules/Fear|fear]]_ (DC 22), greater teleport (self only), _[[spells/Telekinesis|telekinesis]]_ (DC 23)
3/day—_[[spells/Shadow Conjuration|shadow conjuration]]_ (DC 22), _[[spells/Shadow Evocation|shadow evocation]]_ (DC 23)
1/day—_[[spells/Magic Jar|magic jar]]_ (DC 23), _[[universal monster rules/Summon|summon]]_ (level 3, 1 _shadow_ demon 50%)
**_Cleric_ Spells Prepared **(CL 15th; concentration +20)
8th—_[[spells/Demand|demand]]_ (DC 23), _[[spells/Rift Of Ruin|rift of ruin]]_ (DC 23)
7th—quickened _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Destruction|destruction]]_ (DC 22), _[[spells/Power Word Blind|power word blind]]_
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 21), quickened _[[spells/Death Knell|death knell]]_ (DC 17), geas/quest, _[[spells/Heal|heal]]_
5th—_[[spells/Breath Of Life|breath of life]]_, quickened _[[spells/Command|command]]_ (DC 16), _[[spells/Flame Strike|flame strike]]_ (DC 20), greater _command_ (DC 20), _[[spells/Slay Living|slay living]]_ (DC 20), _[[spells/Summon Monster V|summon monster V]]_ (summons 1d3 shadows)
4th—_cure critical wounds_, _[[spells/Discern Lies|discern lies]]_ (DC 19), poison (DC 19), _[[spells/Sending|sending]]_, _shadow conjuration_ (DC 19), _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Speak with Dead|speak with dead]]_ (DC 18), _[[spells/Suggestion|suggestion]]_ (DC 18)
2nd—blindness/deafness (DC 17, only to cause blindness), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Silence|silence]]_ (DC 17), _[[spells/Undetectable Alignment|undetectable alignment]]_
1st—_charm person_ (DC 16), _command_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_ (5), _[[spells/Divine Favor|divine favor]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domains **Charm, _Darkness_

##### Statistics
**Str** —, **Dex** 22, **Con** 22, **Int** 14, **Wis** 20, **Cha** 26
**Base Atk** +18; **CMB** +24; **CMD** 44
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Demonic Obedience|Demonic Obedience]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Possession|Improved Possession]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Bluff +33, Diplomacy +33, Fly +32, Knowledge (planes) +20, Knowledge (religion) +17, Perception +31, Sense Motive +23
**Languages** Abyssal, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** eyes of _darkness_ (7 rounds/day)
**Gear** +5 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ studded leather, _[[items/Wondrous Item/Deep Red Sphere Ioun Stone|deep red sphere ioun stone]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Pink and Green Sphere Ioun Stone|pink and green sphere ioun stone]]_, _[[items/Wondrous Item/Pink Rhomboid Ioun Stone|pink rhomboid ioun stone]]_, _[[items/Wondrous Item/Manual of Bodily Health +1|manual of bodily health +1]]_ (used)

### Special Abilities

**Dominate Thrall (Sp)** Once per day, Ilzunae may cast _[[spells/Dominate Monster|dominate monster]]_. She may only have one creature dominated at a time via this effect, but the effects are permanent until she dominates a new target, at which point the previous target is released from domination but is _[[conditions/Stunned|stunned]]_ for 1d4 rounds.

##### Description

Not all of Nocticula’s favored servants are succubi. Ever since her slaughter of the demon lord Vyriavaxus, she has also been served by the invidiaks. Some of these demons, of course, turned away from the murderer of their patron and have gone on to serve other demon lords or even to strike out on their own, but those who became loyal to her found that their new mistress was every bit as dangerous as their old lord of shadows, and quite a bit more forthcoming at rewarding those who served her well.

Ilzunae is the first of these _shadow_ demons to have been awarded stewardship of one of the many Midnight Isles of Nocticula’s Abyssal realm. Kovalarue is one of the realm’s smaller islands, but in some ways is one of its most beautiful, consisting of rolling hills covered with wildflowers and idyllic streams and lakes. That those flowers drink blood and that those lakes can _[[universal monster rules/Pull|pull]]_ those who look into their waters below to drown them does not mar this beauty, and Ilzunae has proven more than a capable keeper of this land.

The Gloom Widow earned her appellation as a result of her preferred method of preying upon mortals. When she finds herself on the Material Plane, she seeks out young couples who are too shy or hesitant to make the first steps toward forming a relationship, then possesses one of their friends. Using that friend as a proxy, she arranges for the couple to meet, fall in love, and eventually wed, retaining control of the friend the whole time. During the honeymoon, Ilzunae brings the friend to a distant city via teleportation, informs the friend of her plans before releasing him, then teleports back to the honeymooners, where she possesses one of them to enjoy their first night of wedded bliss. The nonpossessed spouse never survives until the dawn, and if they are _[[feats/Lucky|lucky]]_, Ilzunae waits until the final hour of the night to shift from sharing bliss to giving pain. She then abandons the possessed widow or widower with a _[[spells/Message|message]]_ that all this was made possible through the jealousy of the friend, who has fled to a distant city. In most cases, the surviving spouse either commits suicide or seeks out the “friend” to murder them, and when she can, Ilzunae enjoys intercepting those sinful lost souls when they come to the Abyss so she can harvest and keep them in gilt bird cages in her palace as trophies.

Ilzunae prefers promises of time left to her own devices on the Material Plane, but will accept the bodies of grieving widows or widowers as well. It’s a DC 29 check to research the Gloom Widow.