---
cssclass: [monsters]
title1: Keeper of the Yellow Sign
desc_short: This black-clad figure has a pale, puffy face from which its yellow-irised
  eyes glare with equal parts intensity and insanity.
title2: Keeper of the Yellow Sign
CR: 6
sources:
- name: 'Pathfinder #110: The Thrushmoor Terror'
  page: 88
  link: http://paizo.com/products/btpy9l3g
XP: 2400
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
auras:
- name: disquieting aura
  radius: 30
  DC: 17
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    dex: 2
    natural: 5
HP:
  HP: 66
  long: 7d8+35
saves:
  fort: 8
  ref: 4
  will: 5
defensive_abilities:
- channel resistance +2
DR:
- amount: 5
  weakness: magic or silver
immunities:
- undead traits
weaknesses:
- sunlight powerlessness
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 slams +12 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: slams
      bonus:
      - 12
  - - text: entropic drain +11 touch (energy drain)
      entries:
      - - effect: energy drain
      attack: entropic drain
      bonus:
      - 11
      touch: true
  special:
  - energy drain (1 level, DC 17)
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: 3/day
  - name: invisibility
    source: default
    freq: 3/day
    other: self only
  - name: bestow curse
    source: default
    freq: 1/day
    DC: 17
  - name: dream
    source: default
    freq: 1/day
    DC: 19
  - name: rusting grasp
    source: default
    freq: 1/day
  - name: warp wood
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 11
ability_scores:
  STR: 22
  DEX: 15
  CON:
  INT: 13
  WIS: 10
  CHA: 19
BAB: 5
CMB: 11
CMD: 23
feats:
- name: Great Fortitude
- name: Improved Initiative
- name: Toughness
- name: Weapon Focus (slams)
skills:
  Climb: 11
  Intimidate: 14
  Knowledge (arcana): 8
  Knowledge (religion): 8
  Perception: 10
  Sense Motive: 7
  Stealth: 12
languages:
- Aklo
- Common
special_qualities:
- Yellow Sign affinity
ecology:
  environment: any land
  organization: solitary, pair, or cult (3-6)
  treasure_type: standard
special_abilities:
  Disquieting Aura (Su): A keeper of the Yellow Sign is surrounded by an aura of gloom
    and repulsiveness. A creature that fails its saving throw against this aura takes
    a -1 penalty on attack rolls and on saving throws against fear effects while within
    the aura and for 7 minutes after leaving the affected area. Any creature that
    successfully saves against this power cannot be affected again by it for 24 hours.
    This is a mind-affecting fear effect, and the save DC is Charisma-based. A creature
    within range of a keeper's disquieting aura can be affected by its bestow curse
    spell-like ability from a distance (not only by touch). If a target of the aura
    has seen the Yellow Sign, it takes a -2 penalty on its saving throws against the
    aura and the keeper's bestow curse spell-like ability.
  Entropic Drain (Ex): A keeper's use of its energy draining ability can result in
    a surge of entropy that consumes its body and disrupts life all around it. Every
    time the keeper's entropic drain attack results in a creature's death, the keeper
    must succeed at a DC 17 Fortitude saving throw or be destroyed. If the keeper
    is destroyed, all sentient beings in a 15-foot radius around the keeper gain a
    negative level (Fortitude DC 17 negates). If any negative level bestowed by a
    keeper becomes permanent, the victim must succeed at a DC 17 Will saving throw
    or die after 1 hour of delirium. The save DCs are Charisma-based.
  Sunlight Powerlessness (Ex): A keeper of the Yellow Sign is powerless in natural
    sunlight (though not in an area of daylight or similar spells), and it cannot
    attack and is staggered. It can use its supernatural and spell-like abilities,
    but with a 50% failure chance.
  Yellow Sign Affinity (Su): When the keeper of the Yellow Sign stays within 1 mile
    of an active Yellow Sign for 24 hours, it gains a +2 profane bonus to its Armor
    Class and a +1 resistance bonus on all saving throws. An active Yellow Sign is
    either one that was created by Hastur or by the Yellow Sign spell (see page 72).
    If the keeper leaves this range, it loses the bonuses immediately and can regain
    them only after once more staying within 1 mile of an active Yellow Sign for 24
    hours.
desc_long: |-
  A keeper of the Yellow Sign is the undead form of a cultist of Hastur who willingly sacrificed his soul to rise as his god's servant after death. A quiet but relentless champion of the Unspeakable One, a keeper brings anxiety and woe to the lives of any infidel who comes too close to the secrets of its master. Like a vampire, a keeper can easily pass for a living human, if it so wishes, although it tends to have a pale, unhealthy look and a swollen face that can give away its true nature to those who know what to look for. Feeble and sluggish in the sunlight, a keeper can easily be mistaken for a sickly vagrant or even a leper if seen in the open during the day. In the darkness, however, a keeper grows supernaturally strong and attentive, and its eyes glow with a malignant, yellow luminescence.

  A keeper's primary purpose is to haunt and persecute unbelievers who witness the Yellow Sign or, worse, have a document or item that bears the dreaded symbol, such as a copy of The King in Yellow or another artifact of Hastur's cult. Against these favored victims, the keeper uses dream to create a sense of anticipation and awareness of its victim's forthcoming doom. Although a keeper's actions are mainly motivated by a sadistic eagerness to spread pain and misery, the creature can also perform special duties on behalf of a cleric of Hastur, such as slaying her personal enemies or harassing cultists she considers unworthy. These monsters also have an odd, morbid attraction for art in all its forms, favoring bizarre and decadent creations. Since a keeper's energy drain ability can cause its own destruction, one interested in prolonging its own existence uses its touch attack sparingly. Typically, a keeper switches to touch attacks when it faces heavily armored adversaries otherwise difficult to hit, when it is reduced to half hit points (and therefore already facing destruction), or when it simply feels the urge to “taste” the energy of a victim, usually one with artistic talent (such as anyone who demonstrates particular skill in the areas of Craft or Perform).

---

# Keeper of the Yellow Sign
This black-clad figure has a pale, puffy face from which its yellow-irised eyes glare with equal parts intensity and _[[spells/Insanity|insanity]]_.
**Source** Pathfinder #110: The Thrushmoor Terror pg. 88
**XP** 2,400
CE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10
**Aura** disquieting aura (30 ft., DC 17)

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +5 natural)
**hp** 66 (7d8+35)
**Fort** +8, **Ref** +4, **Will** +5
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **DR** 5/magic or silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** _[[universal monster rules/Sunlight Powerlessness|sunlight powerlessness]]_

##### Offense
**Speed** 30 ft.
**Melee** 2 slams +12 (1d6+6) or entropic drain +11 touch (_[[universal monster rules/Energy Drain|energy drain]]_)
**Special Attacks** _energy drain_ (1 level, DC 17)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +11)
3/day—_[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_ (self only)
1/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Dream|dream]]_ (DC 19), _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Warp Wood|warp wood]]_

##### Statistics
**Str** 22, **Dex** 15, **Con** —, **Int** 13, **Wis** 10, **Cha** 19
**Base Atk** +5; **CMB** +11; **CMD** 23
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slams)
**Skills** _[[universal monster rules/Climb|Climb]]_ +11, Intimidate +14, Knowledge (arcana) +8, Knowledge (religion) +8, Perception +10, Sense Motive +7, Stealth +12
**Languages** Aklo, Common
**SQ** _[[spells/Yellow Sign|Yellow Sign]]_ affinity

##### Ecology

**Environment** any land
**Organization** solitary, pair, or cult (3–6)
**Treasure** standard

### Special Abilities

**Disquieting Aura (Su)** A _[[monsters/Keeper of the Yellow Sign|keeper of the Yellow Sign]]_ is surrounded by an aura of gloom and repulsiveness. A creature that fails its saving throw against this aura takes a –1 penalty on attack rolls and on saving throws against _[[universal monster rules/Fear|fear]]_ effects while within the aura and for 7 minutes after leaving the affected area. Any creature that successfully saves against this power cannot be affected again by it for 24 hours. This is a mind-affecting _fear_ effect, and the save DC is Charisma-based. A creature within range of a keeper’s disquieting aura can be affected by its _bestow curse_ spell-like ability from a distance (not only by touch). If a target of the aura has seen the _Yellow Sign_, it takes a –2 penalty on its saving throws against the aura and the keeper’s _bestow curse_ spell-like ability.

**Entropic Drain (Ex)** A keeper’s use of its energy draining ability can result in a surge of entropy that consumes its body and disrupts life all around it. Every time the keeper’s entropic drain attack results in a creature’s death, the keeper must succeed at a DC 17 Fortitude saving throw or be destroyed. If the keeper is destroyed, all sentient beings in a 15-foot radius around the keeper gain a negative level (Fortitude DC 17 negates). If any negative level bestowed by a keeper becomes permanent, the victim must succeed at a DC 17 Will saving throw or die after 1 hour of delirium. The save DCs are Charisma-based.
**_Sunlight Powerlessness_ (Ex)** A _keeper of the Yellow Sign_ is powerless in natural sunlight (though not in an area of _[[spells/Daylight|daylight]]_ or similar spells), and it cannot attack and is _[[conditions/Staggered|staggered]]_. It can use its supernatural and _spell-like abilities_, but with a 50% failure chance.

**_Yellow Sign_ Affinity (Su)** When the _keeper of the Yellow Sign_ stays within 1 mile of an active _Yellow Sign_ for 24 hours, it gains a +2 profane bonus to its Armor Class and a +1 _[[universal monster rules/Resistance|resistance]]_ bonus on all saving throws. An active _Yellow Sign_ is either one that was created by Hastur or by the _Yellow Sign_ spell (see page 72). If the keeper leaves this range, it loses the bonuses immediately and can regain them only after once more staying within 1 mile of an active _Yellow Sign_ for 24 hours.

##### Description

A _keeper of the Yellow Sign_ is the undead form of a _[[npcs/Cultist|cultist]]_ of Hastur who willingly sacrificed his soul to rise as his god’s servant after death. A quiet but relentless _[[items/Armor Magic Abilities/Champion|champion]]_ of the Unspeakable One, a keeper brings anxiety and woe to the lives of any infidel who comes too close to the secrets of its master. Like a _[[monsters/Vampire|vampire]]_, a keeper can easily pass for a living human, if it so wishes, although it tends to have a pale, unhealthy look and a swollen face that can give away its true nature to those who know what to look for. Feeble and sluggish in the sunlight, a keeper can easily be mistaken for a sickly vagrant or even a leper if seen in the open during the day. In the _darkness_, however, a keeper grows supernaturally strong and attentive, and its eyes glow with a malignant, yellow luminescence.

A keeper’s primary purpose is to haunt and persecute unbelievers who _[[spells/Witness|witness]]_ the _Yellow Sign_ or, worse, have a document or item that bears the dreaded symbol, such as a copy of The _[[npcs/King|King]]_ in Yellow or another artifact of Hastur’s cult. Against these favored victims, the keeper uses _dream_ to create a sense of anticipation and awareness of its victim’s forthcoming _[[spells/Doom|doom]]_. Although a keeper’s actions are mainly motivated by a sadistic eagerness to spread pain and misery, the creature can also perform special duties on behalf of a _[[classes/Cleric|cleric]]_ of Hastur, such as slaying her personal enemies or harassing cultists she considers unworthy. These monsters also have an odd, morbid attraction for art in all its forms, favoring bizarre and decadent creations. Since a keeper’s _energy drain_ ability can cause its own _[[spells/Destruction|destruction]]_, one interested in prolonging its own existence uses its touch attack sparingly. Typically, a keeper switches to touch attacks when it faces heavily armored adversaries otherwise difficult to hit, when it is reduced to half hit points (and therefore already facing _destruction_), or when it simply feels the urge to “taste” the energy of a victim, usually one with artistic talent (such as anyone who demonstrates particular skill in the areas of Craft or Perform).