---
cssclass: [monsters]
title1: Empyreal Lord, Korada
desc_short: This serene, acrobatic man has stiff sideburns, a beard like a monkey,
  and three golden-furred tails.
title2: Korada
CR: 26
sources:
- name: Bestiary 4
  page: 90
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 2457600
alignment: NG
size: Large
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: 22
senses:
  blindsense: 60
  darkvision: 60
  detect evil: true
  detect thoughts: true
  low-light vision: true
auras:
- name: primal
  radius: 30
AC:
  AC: 45
  touch: 40
  flat_footed: 36
  other: never flat-footed
  components:
    dex: 10
    dodge: 1
    insight: 2
    natural: 13
    size: -1
    sacred: 6
    wis: 12
HP:
  HP: 528
  long: 32d10+352
  regeneration: 10
  regeneration_weakness: evil artifacts, effects, and spells
saves:
  fort: 21
  ref: 30
  will: 30
defensive_abilities:
- never surprised
DR:
- amount: 10
  weakness: epic and evil
immunities:
- ability damage
- ability drain
- charm effects
- compulsion effects
- death effects
- disease
- electricity
- energy drain
- petrification
- poison
resistances:
  cold: 30
  sonic: 30
SR: 37
speeds:
  base: 90
  climb: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: unarmed strike +31/+36/+31/+26 (2d10+8)
      entries:
      - - damage: 2d10+8
      attack: unarmed strike
      bonus:
      - 31
      - 36
      - 31
      - 26
  - - text: +5 quarterstaff +44/+39/+34/+29 (1d8+13)
      entries:
      - - damage: 1d8+13
      attack: +5 quarterstaff
      bonus:
      - 44
      - 39
      - 34
      - 29
  - - text: flurry of blows +38/+38/+33/+33/+28/+28/+23 (2d10+8)
      entries:
      - - damage: 2d10+8
      attack: flurry of blows
      bonus:
      - 38
      - 38
      - 33
      - 33
      - 28
      - 28
      - 23
  special:
  - shatter spells
  - stunning fist (8/day, DC 22)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: Constant
  - name: foresight
    source: default
    freq: Constant
  - name: sanctuary
    source: default
    freq: Constant
    DC: 25
  - name: water walk
    source: default
    freq: Constant
  - name: augury
    source: default
    freq: At will
  - name: bless
    source: default
    freq: At will
  - name: calm animals
    source: default
    freq: At will
    DC: 25
  - name: calm emotions
    source: default
    freq: At will
    DC: 26
  - name: cure serious wounds
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: mirror image
    source: default
    freq: At will
  - name: divination
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: mad monkeys
    source: default
    freq: 3/day
  - name: quickened mirror image
    source: default
    freq: 3/day
  - name: neutralize poison
    source: default
    freq: 3/day
  - name: true seeing
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  - name: antimagic field
    source: default
    freq: 1/day
  - name: moment of prescience
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 34
ability_scores:
  STR: 26
  DEX: 30
  CON: 33
  INT: 25
  WIS: 35
  CHA: 38
BAB: 32
CMB: 41
CMB_other: +43 disarm or grapple, +45 trip
CMD: 84
CMD_other: 86 vs. disarm, grapple, or trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Greater Trip
- name: Improved Disarm
- name: Improved Grapple
- name: Improved Initiative
- name: Improved Trip
- is_bonus: true
  name: Improved Unarmed Strike
- name: Lunge
- name: Mobility
- name: Quicken Spell-Like Ability (mirror image)
- name: Scorpion Style
- name: Snatch Arrows
- name: Spring Attack
- name: Step Up
- is_bonus: true
  name: Stunning Fist
- name: Weapon Finesse
skills:
  Acrobatics: 44
    when jumping: 68
  Bluff: 32
  Climb: 50
  Diplomacy: 45
  Disguise: 32
  Escape Artist: 26
  Fly: 8
  Heal: 27
  Knowledge (arcana): 23
  Knowledge (geography): 23
  Knowledge (history): 23
  Knowledge (nature): 23
  Knowledge (local): 22
  Knowledge (planes): 41
  Knowledge (religion): 41
  Perception: 46
  Sense Motive: 46
  Spellcraft: 22
  Stealth: 40
  _racial_mods:
    Acrobatics:
      when jumping: 24
languages:
- Celestial
- Infernal
- speak with animals
- truespeech
special_qualities:
- abundant step
- change shape (avoral or any humanoid, shapechange)
- combat style master
- empyreal lord traits
- ki pool (22 points; adamantine, epic, good, lawful, magic, mythic, silver)
- lay on hands (15d6, 29/day)
- seed of life
- tranquil master
ecology:
  environment: any forests or mountains (Nirvana)
  organization: unique
  treasure_type: standard
  treasure:
  - +5 quarterstaff
  - other treasure
special_abilities:
  Combat Style Master (Ex): Korada can attack with unarmed strikes and perform flurry
    of blows as a 20th-level monk. Like a monk, he adds his Wisdom bonus to his AC
    and CMD. As a swift action, Korada may enter the basic stance of any combat style
    feat (such as Crane StyleUC, Monkey StyleUC, and so on) as if he had the first
    feat in the feat path for that combat style. By expending 2 points of ki, he may
    use any two feats from his current combat style's feat path for the next minute;
    if he changes his stance, the previous stance's feats become unavailable but he
    may use feats from the new stance.
  Primal Aura (Su): Korada's primal aura radiates calm and tranquility, automatically
    suppressing any non-mythic charm or compulsion effect on any creature within its
    area. Any creature in his aura (including him) can deal nonlethal damage with
    weapons without taking the -4 penalty on attack rolls for doing so.
  Shatter Spells (Su): Korada can destroy a magical effect (whether it's on a creature
    or an independent effect such as a wall of fire) by attacking it with an unarmed
    strike. He must succeed at a melee touch attack against the creature or effect
    and expend 2 points of ki. If the attack hits, the creature or effect is subject
    to targeted greater dispel magic (CL 20th). If he dispels an effect, he suffer
    no harmful effects from touching it. If the effect is on a creature, the creature
    takes 1 point of damage per spell level of each effect dispelled.
  Tranquil Master (Su): Korada may attack without breaking his sanctuary spell-like
    ability so long as he only attempts to deal nonlethal damage.
desc_long: |-
  Korada is the champion of peace, kindness, and forgiveness. While he loves and respects his fellow empyreal lords for their tireless fight against wickedness, Korada believes good's final triumph will come from the redemption of evil creatures rather than their destruction. Honest, joyful, and clever, the Open Hand of Harmony dispenses wisdom with warmth and humility, and freely shares the secrets he has amassed over ages of study and meditation. Korada's dedication to philosophy and introspection have garnered him the ability to read the diverse threads of the world, see their nearly limitless connections, and then act on them with uncanny foresight. With neither the naïvety of youth nor the jaded weariness of age, Korada is a perfect balance of sentient intelligence and animal instinct, at home wherever he is.

  Though he can assume many forms, Korada's true appearance is a slender, athletic man wearing a simple monk's robe. He has a golden monkey-like beard and sideburns, three monkey tails, and a light layer of downy golden fur covering the rest of his body.

  On Nirvana, Korada dwells in the Dream Lotus, a serene palace city whose blossoming violet walls always drip with cool, golden nectar that is said to calm even the wildest of spirits. It's a place of refuge and healing, and no violence is allowed within its walls; those with problems controlling their anger are sent to meditate at one of its many calming sacred pools.

  Korada is said to possess the gift of foresight, but he rarely acts on these strange visions. He believes the struggle to change is always worthwhile, even if such a journey does not always end in success. It's the process, not the result, that matters most to Korada.

  Despite his staunch dedication to peace, Korada's skill in battle is respected, and he's able to utilize almost any fighting style without a second's pause. He may be responsible for inspiring or teaching the animal combat styles to mortals, using various guises over the course of history on many worlds-or he may even have persuaded the creator gods to give the animals their instincts and talents for fighting, which led to mortals studying and emulating animal combat styles.

  Korada's reputation for peace and martial skill earned him the role of the diplomat of the empyreal lords and their celestial armies. Balor lords, demodand warlords, and even infernal dukes have (temporarily) abandoned their dreams of conquest and warmongering when the Open Hand of Harmony has arrived-alone-in their court to suggest that they consider a different path. These visits always leave behind a path of dazed and stunned fiends, surprised and awed by how easily he defeated them; most silently suffer this indignation and plan vengeance for the next time he appears.

  Although Korada is usually serene and gentle, he has a mischievous side and has been known to poke fun at or harass his opponents like a capricious monkey. He combines his skill in battle and gift for trickery to lead dangerous opponents away from innocents or into places where they can more easily be captured or subdued.

  That said, Korada abhors violence, and he prefers to make nonlethal attacks (using his primal aura and tranquil master abilities), disabling foes so he can speak to them of their weakness. He dispatches mindless opponents without hesitation, not wanting to waste energy debating or persuading a thing empty of thoughts and incapable of making moral choices. He challenges enemy leaders to single combat if doing so would prevent violence between other combatants.

---

# Empyreal Lord, Korada
This serene, _[[feats/Acrobatic|acrobatic]]_ man has stiff sideburns, a beard like a monkey, and three golden-furred tails.
**Source** Bestiary 4 pg. 90
**XP** 2,457,600

NG Large outsider (agathion, extraplanar, good)
**Init** +22; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Thoughts|detect thoughts]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +46
**Aura** primal (30 ft.)

##### Defense

**AC** 45, touch 40, _[[conditions/Flat-Footed|flat-footed]]_ 36 (+10 Dex, +1 dodge, +2 insight, +13 natural, –1 size, +6 _[[items/Weapon Magic Abilities/Sacred|sacred]]_, +12 Wis); never _flat-footed_
**hp** 528 (32d10+352); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil artifacts, effects, and spells)
**Fort** +21, **Ref** +30, **Will** +30
**Defensive Abilities** never surprised; **DR** 10/epic and evil; **Immune** ability damage, ability drain, charm effects, compulsion effects, death effects, disease, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification, poison; **Resist** cold 30, sonic 30; **SR** 37

##### Offense
**Speed** 90 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 60 ft. (average)
**Melee** unarmed strike +31/+36/+31/+26 (2d10+8) or +5 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +44/+39/+34/+29 (1d8+13) or flurry of blows +38/+38/+33/+33/+28/+28/+23 (2d10+8)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Shatter|shatter]]_ spells, _[[feats/Stunning Fist|stunning fist]]_ (8/day, DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +34)
Constant—_detect evil_, _detect thoughts_, _[[spells/Foresight|foresight]]_*, _[[spells/Sanctuary|sanctuary]]_* (DC 25), _[[spells/Water Walk|water walk]]_
At will—_[[spells/Augury|augury]]_, _[[spells/Bless|bless]]_*, _[[spells/Calm Animals|calm animals]]_ (DC 25), _[[spells/Calm Emotions|calm emotions]]_ (DC 26), _[[spells/Cure Serious Wounds|cure serious wounds]]_*, greater teleport, _[[spells/Mirror Image|mirror image]]_*
3/day—_[[spells/Divination|divination]]_, _[[spells/Mad Monkeys|mad monkeys]]_, quickened _mirror image_*, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/True Seeing|true seeing]]_, _[[spells/Wall Of Force|wall of force]]_*
1/day—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Moment of Prescience|moment of prescience]]_
* Korada can use the mythic version of this ability in his realm.

##### Statistics
**Str** 26, **Dex** 30, **Con** 33, **Int** 25, **Wis** 35, **Cha** 38
**Base Atk** +32; **CMB** +41 (+43 disarm or grapple, +45 _[[universal monster rules/Trip|trip]]_); **CMD** 84 (86 vs. disarm, grapple, or _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_mirror image_), _[[feats/Scorpion Style|Scorpion Style]]_, _[[feats/Snatch Arrows|Snatch Arrows]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Step Up|Step Up]]_, _Stunning Fist_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +44 (+68 when jumping), Bluff +32, _Climb_ +50, Diplomacy +45, Disguise +32, Escape Artist +26, Fly +8, _[[spells/Heal|Heal]]_ +27, Knowledge (arcana, geography, history, nature) +23, Knowledge (local) +22, Knowledge (planes, religion) +41, Perception +46, Sense Motive +46, Spellcraft +22, Stealth +40; **Racial Modifiers** +24 Acrobatics when jumping
**Languages** Celestial, Infernal; _[[spells/Speak with Animals|speak with animals]]_, truespeech
**SQ** abundant step, _[[universal monster rules/Change Shape|change shape]]_ (avoral or any humanoid, _[[spells/Shapechange|shapechange]]_), _[[feats/Combat Style Master|combat style master]]_, _[[universal monster rules/Empyreal Lord Traits|empyreal lord traits]]_, ki pool (22 points; adamantine, epic, good, lawful, magic, mythic, silver), lay on hands (15d6, 29/day), seed of life, tranquil master

##### Ecology

**Environment** any forests or mountains (Nirvana)
**Organization** unique
**Treasure** standard (+5 _quarterstaff_, other treasure)

### Special Abilities

**_Combat Style Master_ (Ex)** Korada can attack with unarmed strikes and perform flurry of blows as a 20th-level _[[classes/Monk|monk]]_. Like a _monk_, he adds his Wisdom bonus to his AC and CMD. As a swift action, Korada may enter the basic stance of any combat style feat (such as _[[feats/Crane Style|Crane Style]]_, _[[feats/Monkey Style|Monkey Style]]_, and so on) as if he had the first feat in the feat path for that combat style. By expending 2 points of ki, he may use any two feats from his current combat style’s feat path for the next minute; if he changes his stance, the previous stance’s feats become unavailable but he may use feats from the new stance.

**Primal Aura (Su)** Korada’s primal aura radiates calm and tranquility, automatically suppressing any non-mythic charm or compulsion effect on any creature within its area. Any creature in his aura (including him) can deal nonlethal damage with weapons without taking the –4 penalty on attack rolls for doing so.
**_Shatter_ Spells (Su)** Korada can destroy a magical effect (whether it’s on a creature or an independent effect such as a _[[spells/Wall Of Fire|wall of fire]]_) by attacking it with an unarmed strike. He must succeed at a melee touch attack against the creature or effect and _[[spells/Expend|expend]]_ 2 points of ki. If the attack hits, the creature or effect is subject to targeted greater _[[spells/Dispel Magic|dispel magic]]_ (CL 20th). If he dispels an effect, he suffer no harmful effects from touching it. If the effect is on a creature, the creature takes 1 point of damage per spell level of each effect dispelled.

**Tranquil Master (Su)** Korada may attack without _[[items/Weapon Magic Abilities/Breaking|breaking]]_ his _sanctuary_ spell-like ability so long as he only attempts to deal nonlethal damage.

##### Description

Korada is the _[[items/Armor Magic Abilities/Champion|champion]]_ of peace, kindness, and forgiveness. While he loves and respects his fellow empyreal lords for their tireless fight against wickedness, Korada believes good’s final triumph will come from the _[[feats/Redemption|redemption]]_ of evil creatures rather than their _[[spells/Destruction|destruction]]_. Honest, joyful, and clever, the Open Hand of Harmony dispenses wisdom with warmth and humility, and freely shares the secrets he has amassed over ages of study and meditation. Korada’s dedication to philosophy and introspection have garnered him the ability to read the diverse threads of the world, see their nearly limitless connections, and then act on them with uncanny _foresight_. With neither the naïvety of youth nor the jaded weariness of age, Korada is a perfect balance of sentient intelligence and animal instinct, at home wherever he is.

Though he can assume many forms, Korada’s true appearance is a slender, _[[feats/Athletic|athletic]]_ man wearing a simple _monk_’s robe. He has a golden monkey-like beard and sideburns, three monkey tails, and a light layer of downy golden fur covering the rest of his body.

On Nirvana, Korada dwells in the _[[spells/Dream|Dream]]_ Lotus, a serene palace city whose blossoming violet walls always drip with cool, golden nectar that is said to calm even the wildest of spirits. It’s a place of _[[spells/Refuge|refuge]]_ and healing, and no violence is allowed within its walls; those with problems controlling their anger are sent to meditate at one of its many _[[items/Armor Magic Abilities/Calming|calming]]_ _sacred_ pools.

Korada is said to possess the gift of _foresight_, but he rarely acts on these strange visions. He believes the struggle to change is always worthwhile, even if such a journey does not always end in success. It’s the process, not the result, that matters most to Korada.

Despite his staunch dedication to peace, Korada’s skill in battle is respected, and he’s able to utilize almost any fighting style without a second’s pause. He may be responsible for inspiring or teaching the animal combat styles to mortals, using various guises over the course of history on many worlds—or he may even have persuaded the creator gods to give the animals their instincts and talents for fighting, which led to mortals studying and emulating animal combat styles.

Korada’s reputation for peace and martial skill earned him the role of the _[[npcs/Diplomat|diplomat]]_ of the empyreal lords and their celestial armies. Balor lords, demodand warlords, and even infernal dukes have (temporarily) abandoned their dreams of conquest and warmongering when the Open Hand of Harmony has arrived—alone—in their court to suggest that they consider a different path. These visits always leave behind a path of _[[conditions/Dazed|dazed]]_ and _[[conditions/Stunned|stunned]]_ fiends, surprised and awed by how easily he defeated them; most silently suffer this indignation and plan _[[feats/Vengeance|vengeance]]_ for the next time he appears.

Although Korada is usually serene and gentle, he has a mischievous side and has been known to poke fun at or harass his opponents like a capricious monkey. He combines his skill in battle and gift for trickery to lead dangerous opponents away from innocents or into places where they can more easily be captured or subdued.

That said, Korada abhors violence, and he prefers to make nonlethal attacks (using his primal aura and tranquil master abilities), disabling foes so he can speak to them of their weakness. He dispatches mindless opponents without hesitation, not wanting to waste energy debating or persuading a thing empty of thoughts and incapable of making moral choices. He challenges enemy leaders to single combat if doing so would prevent violence between other combatants.