---
cssclass: [monsters]
title1: Demon Lord, Baphomet
desc_short: Fire burns on the central horn and in the rheumy eyes of this bestial
  winged demon, who stands more than twice a human's height.
title2: Baphomet
CR: 27
sources:
- name: 'Pathfinder #77: Herald of the Ivory Labyrinth'
  page: 88
  link: http://paizo.com/products/btpy92lh?Pathfinder-Adventure-Path-77-Herald-of-the-Ivory-Labyrinth
XP: 3276800
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 23
senses:
  darkvision: 60
  detect good: true
  detect law: true
  see in darkness: true
  true seeing: true
auras:
- name: frightful presence
  radius: 180
  DC: 38
- name: unholy aura
  DC: 30
AC:
  AC: 45
  touch: 34
  flat_footed: 45
  components:
    deflection: 4
    dex: 11
    natural: 11
    profane: 10
    size: -1
HP:
  HP: 643
  long: 33d10+462
saves:
  fort: 36
  ref: 26
  will: 31
defensive_abilities:
- Abyssal resurrection
- freedom of movement
- supernatural cunning
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage
- ability drain
- charm and compulsion effects
- death effects
- electricity
- energy drain
- fire
- maze
- petrification
- poison
resistances:
  acid: 30
  cold: 30
SR: 38
speeds:
  base: 50
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: Aizerghaul +52/+47/+42/+37 (2d8+28/19-20/×3)
      entries:
      - - damage: 2d8+28
          crit_range: 19-20
          crit_multiplier: 3
      attack: Aizerghaul
      bonus:
      - 52
      - 47
      - 42
      - 37
    - text: gore +40 (2d8+6 plus 2d6 fire plus burn)
      entries:
      - - damage: 2d8+6
        - damage: 2d6
          type: fire
        - effect: burn
      attack: gore
      bonus:
      - 40
    - text: bite +40 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 40
  special:
  - burn (4d6 fire, DC 40)
  - glaive mastery
  - powerful charge (gore, 4d8+19 plus 2d6 fire and burn)
  - scroll use
space: 10
reach: 10
reach_other: 20 ft. with glaive
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
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 30
  - name: astral projection
    source: default
    freq: At will
  - name: baleful polymorph
    source: default
    freq: At will
    DC: 27
  - name: blasphemy
    source: default
    freq: At will
    DC: 29
  - name: desecrate
    source: default
    freq: At will
  - name: dominate person
    source: default
    freq: At will
    DC: 27
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 27
  - name: shapechange
    source: default
    freq: At will
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 26
  - name: quickened greater dispel magic
    source: default
    freq: 3/day
  - name: maze
    source: default
    freq: 3/day
  - name: summon demons
    source: default
    freq: 3/day
  - name: summon minotaurs
    source: default
    freq: 3/day
  - name: symbol of persuasion
    source: default
    freq: 3/day
    DC: 28
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 31
  - name: mass charm monster
    source: default
    freq: 1/day
    DC: 30
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 27
ability_scores:
  STR: 36
  DEX: 32
  CON: 38
  INT: 37
  WIS: 29
  CHA: 35
BAB: 33
CMB: 47
CMB_other: +51 bull rush
CMD: 82
CMD_other: 84 vs. bull rush
feats:
- name: Combat Reflexes
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Weapon Focus (glaive)
- name: Greater Weapon Specialization (glaive)
- name: Improved Bull Rush
- name: Improved Critical (glaive)
- name: Improved Initiative
- name: Power Attack
- name: Quicken Spell-Like Ability (greater dispel magic)
- name: Scribe Scroll
- name: Staggering Critical
- name: Weapon Focus (glaive)
- name: Weapon Specialization (glaive)
skills:
  Acrobatics: 44
  Bluff: 48
  Diplomacy: 48
  Fly: 49
  Handle Animal: 45
  Intimidate: 45
  Knowledge (arcana): 49
  Knowledge (dungeoneering): 46
  Knowledge (geography): 46
  Knowledge (history): 46
  Knowledge (nobility): 46
  Knowledge (planes): 49
  Knowledge (religion): 49
  Linguistics: 46
  Perception: 53
  Sense Motive: 45
  Spellcraft: 49
  Stealth: 43
  Use Magic Device: 45
  _racial_mods:
    Perception:
      _: 8
languages:
- all languages
- speak with animals
- telepathy 300 ft.
special_qualities:
- change shape (any animal, magical beast, or minotaur; greater polymorph)
- infernal brand
- language mastery
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - Aizerghaul
  - 2d6 scrolls
  - other treasure
special_abilities:
  Aizerghaul: Aizerghaul (Abyssal for ”Labyrinth's Final Edge”) is a uniquely shaped
    glaive, the head of which consists of a double blade akin to a crescent moon.
    This blade is made of ivory, but is razor sharp and as hard as adamantine (and
    possesses all the qualities of that material). It is a +5 lawful-outsider- bane
    unholy wounding glaive capable of inflicting particularly horrible and painful
    wounds on good-aligned targets and devils alike. Such a creature must succeed
    at a DC 38 Fortitude save each time it's wounded by Aizerghaul or be sickened
    with pain for as long as the damage caused by the wound persists. Whether the
    save succeeds or fails, these wounds don't heal naturally and resist magical healing.
    A character attempting to heal these wounds must succeed at a DC 32 caster level
    check or the healing has no effect on the injured creature.
  Glaive Mastery (Ex): Baphomet is exceptionally skilled at fighting with a glaive.
    He is treated as a 20th-level fighter for the purposes of fulfilling any feat
    prerequisites, such as that for Weapon Specialization.
  Infernal Brand (Su): The mark of Asmodeus is branded on Baphomet's brow, yet this
    is no mark of fealty or servitude. Rather, Baphomet has claimed the pentagram-a
    remnant of the time he spend as the archdevil's prisoner-and now draws power from
    it. The brand grants him his devil-like abilities of fire immunity and see in
    darkness. In addition, all devils and worshipers of devils take a -2 penalty on
    saving throws against Baphomet's special attacks and spell-like abilities. He
    gains a +4 bonus on caster level checks to penetrate a devil's spell resistance,
    and automatically penetrates a devil's damage reduction with his glaive and natural
    attacks.
  Language Mastery (Ex): Baphomet can speak, read, and understand all languages.
  Scroll Use (Ex): Baphomet can cast spells from any scroll as if he possessed the
    spell on a spell list. Spells he casts from scrolls always resolve at caster level
    27th.
  Summon Minotaurs (Sp): Baphomet can summon half-fiend minotaurs, labyrinth minotaurs
    (see page 90), and mythic minotaurs as if casting a summon monster spell. He can
    summon eight half-fiend minotaurs three times per day, and four mythic minotaurs
    or one labyrinth minotaur once per day. This ability functions as a swift action,
    but otherwise works like the summon universal monster rule with 100% chance of
    success and counts as a 9th-level spell effect.
  Supernatural Cunning (Su): Baphomet is never caught flat-footed and gains a +8 bonus
    on initiative checks. In addition, he's immune to maze spells and can never become
    lost. He always knows the shortest, most direct route through any maze. After
    spending 1 minute in any maze, he understands its entire layout implicitly and
    can teleport to any location using his greater teleport spell-like ability.
desc_long: |-
  Baphomet-Lord of the Minotaurs-was created by Lamashtu from the soul of the first minotaur. In those days, he was a powerfully muscled specimen, and the Queen of Demons kept him as a consort until the day Baphomet stole away from her palace in Yanaron, seeking to gain even greater favor by claiming a legendary trophy. Baphomet's ambition was as great as his folly, and he invaded the deepest layer of Hell, intent on stealing Asmodeus's ruby rod for his mistress. Needless to say, he was swiftly caught. Lamashtu claimed no allegiance to him, and Asmodeus imprisoned Baphomet in a devious maze the archdevil proclaimed to be unsolvable, even by the first minotaur. The archdevil also carved his own symbol into Baphomet's brow with the nail of his index finger in an attempt to fully subjugate the minotaur.

  But in this attempt, it was Asmodeus who overstepped his bounds. Not only did Baphomet solve the seemingly unsolvable maze after a mere decade, but as he escaped, he also took the world-sized labyrinth with him. Baphomet had changed over that time, becoming almost emaciated in his build, yet growing much wiser. He did not return to Lamashtu's side, but instead took the archdevil's infernal maze and made it his own as he claimed a portion of the Abyss as his realm.

  This was eons ago, and now Baphomet is a powerful demon lord in his own right. He has forgiven Lamashtu, and serves as her lover now and then, yet he's no longer her direct subservient minion. He works to increase the inf luence of his cult on countless worlds, building his forces so that one day he might again invade Hell. But this time, Baphomet plans on taking much more than Asmodeus's weapon-he intends to take Asmodeus's life!

---

# Demon Lord, Baphomet
Fire burns on the central horn and in the rheumy eyes of this bestial winged demon, who stands more than twice a human’s height.
**Source** Pathfinder #77: Herald of the Ivory Labyrinth pg. 88
**XP** 3,276,800
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +23; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +53
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 38), _[[spells/Unholy Aura|unholy aura]]_ (DC 30)

##### Defense

**AC** 45, touch 34, _[[conditions/Flat-Footed|flat-footed]]_ 45 (+4 deflection, +11 Dex, +11 natural, +10 profane, –1 size)
**hp** 643 (33d10+462)
**Fort** +36, **Ref** +26, **Will** +31
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, _[[spells/Freedom of Movement|freedom of movement]]_, supernatural _[[items/Weapon Magic Abilities/Cunning|cunning]]_; **DR** 20/cold iron, epic, and good; **Immune** ability damage, ability drain, charm and compulsion effects, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, fire, _[[spells/Maze|maze]]_, petrification, poison; **Resist** acid 30, cold 30; **SR** 38

##### Offense
**Speed** 50 ft., fly 50 ft. (good)
**Melee** Aizerghaul +52/+47/+42/+37 (2d8+28/19–20/×3), gore +40 (2d8+6 plus 2d6 fire plus _[[universal monster rules/Burn|burn]]_), bite +40 (1d8+6)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _[[items/Weapon/Glaive|glaive]]_)
**Special Attacks** _burn_ (4d6 fire, DC 40), _glaive_ mastery, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d8+19 plus 2d6 fire and _burn_), scroll use
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th)
Constant—_detect good_, _detect law_, _freedom of movement_, _[[spells/Speak with Animals|speak with animals]]_, _true seeing_, _unholy aura_ (DC 30)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 27), _[[spells/Blasphemy|blasphemy]]_ (DC 29), _[[spells/Desecrate|desecrate]]_, _[[spells/Dominate Person|dominate person]]_ (DC 27), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Telekinesis|telekinesis]]_ (DC 27), _[[spells/Shapechange|shapechange]]_, _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 26)
3/day—quickened greater _[[spells/Dispel Magic|dispel magic]]_, _maze_, _[[universal monster rules/Summon|summon]]_ demons, _summon_ minotaurs, _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 28)
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 31), mass _[[spells/Charm Monster|charm monster]]_ (DC 30), _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 36, **Dex** 32, **Con** 38, **Int** 37, **Wis** 29, **Cha** 35
**Base Atk** +33; **CMB** +47 (+51 bull rush); **CMD** 82 (84 vs. bull rush)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_glaive_), _[[feats/Greater Weapon Specialization|Greater Weapon Specialization]]_ (_glaive_), _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_glaive_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (greater _dispel magic_), _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_glaive_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_glaive_)
**Skills** Acrobatics +44, Bluff +48, Diplomacy +48, Fly +49, Handle Animal +45, Intimidate +45, Knowledge (arcana) +49, Knowledge (dungeoneering) +46, Knowledge (geography) +46, Knowledge (history) +46, Knowledge (nobility) +46, Knowledge (planes) +49, Knowledge (religion) +49, Linguistics +46, Perception +53, Sense Motive +45, Spellcraft +49, Stealth +43, Use Magic Device +45; **Racial Modifiers** +8 Perception
**Languages** all languages; _speak with animals_; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any animal, magical beast, or _[[monsters/Minotaur|minotaur]]_; greater _[[spells/Polymorph|polymorph]]_), infernal _[[spells/Brand|brand]]_, language mastery

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple (Aizerghaul, 2d6 scrolls, other treasure)

### Special Abilities

**Aizerghaul **Aizerghaul (Abyssal for ”Labyrinth’s Final Edge”) is a uniquely shaped _glaive_, the head of which consists of a double blade akin to a crescent moon. This blade is made of ivory, but is razor sharp and as hard as adamantine (and possesses all the qualities of that material). It is a +5 lawful-outsider- _[[spells/Bane|bane]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _glaive_ capable of inflicting particularly horrible and painful wounds on good-aligned targets and devils alike. Such a creature must succeed at a DC 38 Fortitude save each time it’s wounded by Aizerghaul or be _[[conditions/Sickened|sickened]]_ with pain for as long as the damage caused by the wound persists. Whether the save succeeds or fails, these wounds don’t _[[spells/Heal|heal]]_ naturally and resist magical healing. A character attempting to _heal_ these wounds must succeed at a DC 32 caster level check or the healing has no effect on the injured creature.

**_Glaive_ Mastery (Ex)** Baphomet is exceptionally skilled at fighting with a _glaive_. He is treated as a 20th-level _[[classes/Fighter|fighter]]_ for the purposes of fulfilling any feat prerequisites, such as that for _Weapon Specialization_.

**Infernal _Brand_ (Su)** The mark of Asmodeus is branded on Baphomet’s brow, yet this is no mark of fealty or servitude. Rather, Baphomet has claimed the pentagram—a remnant of the time he spend as the archdevil’s prisoner—and now draws power from it. The _brand_ grants him his devil-like abilities of fire _[[universal monster rules/Immunity|immunity]]_ and _see in darkness_. In addition, all devils and worshipers of devils take a –2 penalty on saving throws against Baphomet’s special attacks and _spell-like abilities_. He gains a +4 bonus on caster level checks to penetrate a devil’s _[[universal monster rules/Spell Resistance|spell resistance]]_, and automatically penetrates a devil’s _[[universal monster rules/Damage Reduction|damage reduction]]_ with his _glaive_ and _[[universal monster rules/Natural Attacks|natural attacks]]_.

**Language Mastery (Ex)** Baphomet can speak, read, and understand all languages.
**Scroll Use (Ex)** Baphomet can cast spells from any scroll as if he possessed the spell on a spell list. Spells he casts from scrolls always resolve at caster level 27th.
**_Summon_ Minotaurs (Sp)** Baphomet can _summon_ half-fiend minotaurs, labyrinth minotaurs (see page 90), and mythic minotaurs as if casting a _summon_ monster spell. He can _summon_ eight half-fiend minotaurs three times per day, and four mythic minotaurs or one labyrinth _minotaur_ once per day. This ability functions as a swift action, but otherwise works like the _summon_ universal monster rule with 100% chance of success and counts as a 9th-level spell effect.
**Supernatural _Cunning_ (Su)** Baphomet is never caught _flat-footed_ and gains a +8 bonus on initiative checks. In addition, he’s immune to _maze_ spells and can never become lost. He always knows the shortest, most direct route through any _maze_. After spending 1 minute in any _maze_, he understands its entire layout implicitly and can teleport to any location using his greater teleport spell-like ability.

##### Description

Baphomet—Lord of the Minotaurs—was created by Lamashtu from the soul of the first _minotaur_. In those days, he was a powerfully muscled specimen, and the Queen of Demons kept him as a consort until the day Baphomet stole away from her palace in Yanaron, seeking to gain even greater favor by claiming a legendary trophy. Baphomet’s ambition was as great as his folly, and he invaded the deepest layer of Hell, intent on stealing Asmodeus’s ruby rod for his mistress. Needless to say, he was swiftly caught. Lamashtu claimed no allegiance to him, and Asmodeus imprisoned Baphomet in a devious _maze_ the archdevil proclaimed to be unsolvable, even by the first _minotaur_. The archdevil also carved his own symbol into Baphomet’s brow with the nail of his index finger in an attempt to fully subjugate the _minotaur_.

But in this attempt, it was Asmodeus who overstepped his bounds. Not only did Baphomet solve the seemingly unsolvable _maze_ after a mere decade, but as he escaped, he also took the world-sized labyrinth with him. Baphomet had changed over that time, becoming almost emaciated in his build, yet _[[items/Weapon Magic Abilities/Growing|growing]]_ much wiser. He did not return to Lamashtu’s side, but instead took the archdevil’s infernal _maze_ and made it his own as he claimed a portion of the Abyss as his realm.

This was eons ago, and now Baphomet is a powerful demon lord in his own right. He has forgiven Lamashtu, and serves as her lover now and then, yet he’s no longer her direct subservient minion. He works to increase the inf luence of his cult on countless worlds, building his forces so that one day he might again invade Hell. But this time, Baphomet plans on taking much more than Asmodeus’s weapon—he intends to take Asmodeus’s life!