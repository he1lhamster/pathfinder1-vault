---
cssclass: [monsters]
title1: Nightripper
desc_short: Twin talons attached to grotesque back-appendages drip blood from this
  hideously emaciated, jackal-legged albino demon.
title2: Nightripper
CR: 24
sources:
- name: Inner Sea Bestiary
  page: 34
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 1228800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: unholy aura
  DC: 25
AC:
  AC: 42
  touch: 25
  flat_footed: 31
  components:
    deflection: 4
    dex: 11
    natural: 17
HP:
  HP: 526
  long: 27d10+378
  regeneration: 15
  regeneration_weakness: good weapons or spells
saves:
  fort: 27
  ref: 30
  will: 25
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- charm and compulsion effects
- death effects
- electricity
- poison
resistances:
  acid: 30
  cold: 30
  fire: 30
SR: 35
speeds:
  base: 60
attacks:
  melee:
  - - text: +5 vorpal bastard sword +43/+38/+33/+28 (1d10+18/17-20)
      entries:
      - - damage: 1d10+18
          crit_range: 17-20
      attack: +5 vorpal bastard sword
      bonus:
      - 43
      - 38
      - 33
      - 28
    - text: claw +31 (2d6+4/19-20 plus 2d6 bleed)
      entries:
      - - damage: 2d6+4
          crit_range: 19-20
        - damage: 2d6
          type: bleed
      attack: claw
      bonus:
      - 31
    - text: 2 talons +31 (1d6+4/19-20 plus 2d6 bleed)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
        - damage: 2d6
          type: bleed
      count: 2
      attack: talons
      bonus:
      - 31
  special:
  - curse of living death
  - slowing gaze
  - sneak attack +3d6
  - swift cuts
  - sword mastery
space: 5
reach: 5
reach_other: 15 ft. with talons
spell_like_abilities:
  entries:
  - name: airwalk
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 25
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: phantasmal killer
    source: default
    freq: At will
    DC: 21
  - superscripts:
    - APG
    name: spiked pit
    source: default
    freq: At will
    DC: 20
  - name: telekinesis
    source: default
    freq: At will
    DC: 22
  - superscripts:
    - APG
    name: acid pit
    source: default
    freq: 3/day
    DC: 21
  - name: quickened blade barrier
    source: default
    freq: 3/day
    DC: 23
  - name: harm
    source: default
    freq: 3/day
    DC: 23
  - superscripts:
    - APG
    name: hungry pit
    source: default
    freq: 3/day
    DC: 22
  - name: reverse gravity
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any demon
    - name: combination of demons whose total combined CR is 20
    - name: lower
      chance: 100%
  - name: time stop
    source: default
    freq: 1/day
  - name: weird
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 29
  DEX: 32
  CON: 39
  INT: 18
  WIS: 23
  CHA: 24
BAB: 27
CMB: 36
CMD: 61
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dazzling Display
- name: Deadly Stroke
- is_bonus: true
  name: Exotic Weapon Proficiency (bastard sword)
- name: Greater Feint
- is_bonus: true
  name: Greater Weapon Focus (bastard sword)
- is_bonus: true
  name: Greater Weapon Specialization (bastard sword)
- name: Improved Critical (bastard sword)
- name: Improved Critical (claw)
- name: Improved Critical (talon)
- name: Improved Disarm
- name: Improved Feint
- name: Power Attack
- name: Quick Draw
- name: Quicken Spell- Like Ability (blade barrier)
- name: Shatter Defenses
- is_bonus: true
  name: Weapon Focus (bastard sword)
- is_bonus: true
  name: Weapon Specialization (bastard sword)
skills:
  Acrobatics: 41
  Intimidate: 37
  Knowledge (history): 31
  Knowledge (local): 31
  Knowledge (religion): 31
  Knowledge (nobility): 34
  Perception: 36
  Sense Motive: 36
  Stealth: 41
  Use Magic Device: 37
languages:
- Abyssal
- Celestial
- Common
- Draconic
- telepathy 300 ft.
special_qualities:
- nascent demon lord traits
ecology:
  environment: any (Kurnugia)
  organization: solitary
  treasure_type: triple
  treasure:
  - +5 keen vorpal bastard sword
  - other treasure
special_abilities:
  Curse of Living Death (Su): Once per round, as a free action as he kills a living
    creature, Nightripper can choose to afflict that target with the curse of living
    death. The target can resist this curse with a successful DC 30 Will save right
    before it dies, allowing the victim to die normally. If the victim fails its save,
    it enters a sort of half-living state; it becomes completely helpless, unable
    to take any actions whatsoever, but remains conscious and aware of the world,
    and of the pain in its body. It cannot be resurrected or otherwise restored to
    life until the curse is lifted. While the curse remains in effect, the victim
    takes 1d4 points of Intelligence, Wisdom, and Charisma drain every day as any
    lingering shreds of sanity are blasted away. When each ability score is drained
    to zero, the DC of the curse increases by +4. A character suffering the curse
    of living death can remain in this state forever, but as long as any one of her
    mental ability scores is at zero, she is capable only of enduring pain and cannot
    observe the world around her. Even if the character's body is destroyed, the cursed
    victim's consciousness remains as a disembodied and invisible presence at the
    site of this destruction, and cannot be resurrected or released to the afterlife.
    The save DC is Charisma-based.
  Nascent Demon Lord Traits: A nascent demon lord is a powerful demon that has not
    yet made the full transition from unique demon to full demon lord of an Abyssal
    realm. They have several traits, as summarized here. Immunity to charm and compulsion
    effects, death effects, electricity, and poison.Resistance to acid 30, cold 30,
    and fire 30.Summon (Sp) Once per day, Nightripper can summon any demon or combination
    of demons whose total combined CR is 20 or lower. This ability always works, and
    is equivalent to a 9th-level spell.Telepathy 300 feet.Nightripper's natural weapons,
    as well as any weapon he wields, are treated as chaotic, epic, and evil for the
    purpose of overcoming damage reduction.Nightripper can grant spells to his worshipers.
    He grants access to the domains of Chaos, Darkness, Evil, and Strength. His favored
    weapon is the bastard sword.
  Slowing Gaze (Su): Slowed (as the slow spell) for 1 round, 30 feet, Will DC 30 negates.
    The save DC is Charisma-based.
  Swift Cuts (Ex): As long as he is attacking with a sword, Nightripper treats foes
    who are staggered, nauseated, or under the effects of a slow spell (or similar
    effects, such as his gaze) as if they were flat-footed.
  Sword Mastery (Ex): Nightripper possesses several sword-related bonus feats normally
    restricted to fighters.
desc_long: |-
  Even today, centuries after his 13th and final execution, memories of Riktus Scroon continue to haunt the nightmares of those who live along the northern coastlines of the Inner Sea. During his reign of horror, the man who would come to be known as the Nightripper used his position in the now disbanded Graven Guard of Taldor to move along the shipping lanes with ease. His position among the mercenary company afforded him time in countless settlements from Golisfar to Corentyn, and in these unsuspecting towns he hunted. Scroon preferred young victims, that their vanishing would cause the most distress possible-his favorites were young adults freshly in love, although he seemed to have had no preference between man or woman. He abducted his victims with astonishing skill, tormenting them for hours with his blades before leaving them broken and bleeding to death at the bottom of a specially prepared pit far outside of town. The mass murderer was finally captured by Cesandra Dayne, an obsessed priest of Sarenrae who had lost her fiancee and her father to Scroon. Only by forsaking the teachings of her church was she able to trap the murderer in the slums of Almas, and although the resulting fight saw the death of a dozen innocent bystanders, in the end Cesandra had her man alive.

  After Scroon was turned over to the law in his hometown of Oppara, the authorities thought to prosecute him for the deaths of no fewer than 46 known victims. When Scroon gleefully bragged of having murdered nearly a thousand men, women, and children, the authorities were eager to write off his ravings, yet after Scroon provided exacting details to the sites of 953 victims, and one after the other his directions led to actual graves, the killer's sentencing was hastened-death by hanging. Yet Scroon survived. One after the other, attempts to execute the Nightripper failed-headsmen died of fright as they lifted the axe, guillotines malfunctioned, magic failed. Each botched execution left Scroon more disfigured, but his legend grew. The 13th and final execution put the man down once and for all-or so it was hoped.

  Scroon's soul went to the Boneyard, where something amazing happened-he passed through to the Abyss with his mind and memories intact. So remarkable was his retention of his identity that it drew the attention of Lamashtu herself, who pulled the killer's soul from the shuddersome bosom of the Abyss and made him her personal assassin, raising him from a broken shell of a soul to a nascent demon lord with greater power than he'd ever hoped for in life. His form had changed, transforming into a shape more befitting one of his horrific nature, yet his mind remained sharp and clear. Nightripper harbors a strong desire for revenge, but for now he serves dutifully as Lamashtu's favored torturer and assassin and as the lord of the dungeons below her palace in the Abyssal realm of Kurnugia. But it is said that someday, when he has repaid his debt to the Mother of Demons for his ascension and rescue from the dregs of the Abyss, the Nightripper will return to his old haunts. Only this time, it will not be individuals he breaks and bleeds and buries in his pits-it will be entire cities.

---

# Nightripper
Twin talons attached to grotesque back-appendages drip blood from this hideously emaciated, jackal-legged albino demon.
**Source** Inner Sea Bestiary pg. 34
**XP** 1,228,800
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +36
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 25)

##### Defense

**AC** 42, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+4 _[[spells/Deflection|deflection]]_, +11 Dex, +17 natural)
**hp** 526 (27d10+378); _[[universal monster rules/Regeneration|regeneration]]_ 15 (good weapons or spells)
**Fort** +27, **Ref** +30, **Will** +25
**DR** 15/cold iron and good; **Immune** charm and compulsion effects, death effects, electricity, poison; **Resist** acid 30, cold 30, fire 30; **SR** 35

##### Offense
**Speed** 60 ft.
**Melee** +5 _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ _[[items/Weapon/Bastard sword|bastard sword]]_ +43/+38/+33/+28 (1d10+18/17–20), claw +31 (2d6+4/19–20 plus 2d6 _[[universal monster rules/Bleed|bleed]]_), 2 talons +31 (1d6+4/19–20 plus 2d6 _bleed_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with talons)
**Special Attacks** curse of living death, slowing _[[universal monster rules/Gaze|gaze]]_, sneak attack +3d6, swift cuts, sword mastery
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—airwalk, _detect good_, _detect law_, _[[spells/Freedom of Movement|freedom of movement]]_, _true seeing_, _unholy aura_ (DC 25)
At will—greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/Spiked Pit|spiked pit]]_ (DC 20), _[[spells/Telekinesis|telekinesis]]_ (DC 22)
3/day—_[[spells/Acid Pit|acid pit]]_ (DC 21), quickened _[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Harm|harm]]_ (DC 23), _[[spells/Hungry Pit|hungry pit]]_ (DC 22)
1/day—_[[spells/Reverse Gravity|reverse gravity]]_, _[[universal monster rules/Summon|summon]]_ (level 9, any demon or combination of demons whose total combined CR is 20 or lower 100%), _[[spells/Time Stop|time stop]]_, _[[spells/Weird|weird]]_ (DC 26)

##### Statistics
**Str** 29, **Dex** 32, **Con** 39, **Int** 18, **Wis** 23, **Cha** 24
**Base Atk** +27; **CMB** +36; **CMD** 61
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Deadly Stroke|Deadly Stroke]]_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (_bastard sword_), _[[feats/Greater Feint|Greater Feint]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_bastard sword_), _[[feats/Greater Weapon Specialization|Greater Weapon Specialization]]_ (_bastard sword_), _[[feats/Improved Critical|Improved Critical]]_ (_bastard sword_, claw, talon), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, Quicken Spell- Like Ability (_blade barrier_), _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_bastard sword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_bastard sword_)
**Skills** Acrobatics +41, Intimidate +37, Knowledge (history, local, religion) +31, Knowledge (nobility) +34, Perception +36, Sense Motive +36, Stealth +41, Use Magic Device +37
**Languages** Abyssal, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** nascent demon lord traits

##### Ecology

**Environment** any (Kurnugia)
**Organization** solitary
**Treasure** triple (+5 _[[items/Weapon Magic Abilities/Keen|keen]]_ _vorpal_ _bastard sword_, other treasure)

### Special Abilities

**Curse of Living Death (Su)** Once per round, as a free action as he kills a living creature, _[[monsters/Nightripper|Nightripper]]_ can choose to afflict that target with the curse of living death. The target can resist this curse with a successful DC 30 Will save right before it dies, allowing the victim to die normally. If the victim fails its save, it enters a sort of half-living state; it becomes completely _[[conditions/Helpless|helpless]]_, unable to take any actions whatsoever, but remains conscious and aware of the world, and of the pain in its body. It cannot be resurrected or otherwise restored to life until the curse is lifted. While the curse remains in effect, the victim takes 1d4 points of Intelligence, Wisdom, and Charisma drain every day as any lingering shreds of sanity are blasted away. When each ability score is drained to zero, the DC of the curse increases by +4. A character suffering the curse of living death can remain in this state forever, but as long as any one of her mental ability scores is at zero, she is capable only of enduring pain and cannot observe the world around her. Even if the character’s body is destroyed, the cursed victim’s consciousness remains as a disembodied and _[[conditions/Invisible|invisible]]_ presence at the site of this _[[spells/Destruction|destruction]]_, and cannot be resurrected or released to the afterlife. The save DC is Charisma-based.

**Nascent Demon Lord Traits** A nascent demon lord is a powerful demon that has not yet made the full transition from unique demon to full demon lord of an Abyssal realm. They have several traits, as summarized here.

* _[[universal monster rules/Immunity|Immunity]]_ to charm and compulsion effects, death effects, electricity, and poison.
* _[[universal monster rules/Resistance|Resistance]]_ to acid 30, cold 30, and fire 30.
* _Summon_ (Sp) Once per day, _Nightripper_ can _summon_ any demon or combination of demons whose total combined CR is 20 or lower. This ability always works, and is equivalent to a 9th-level spell.
* _Telepathy_ 300 feet.
* _Nightripper_’s natural weapons, as well as any weapon he wields, are treated as chaotic, epic, and evil for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.
* _Nightripper_ can grant spells to his worshipers. He grants access to the domains of Chaos, _[[spells/Darkness|Darkness]]_, Evil, and Strength. His favored weapon is the _bastard sword_.
**Slowing _Gaze_ (Su)** Slowed (as the _[[spells/Slow|slow]]_ spell) for 1 round, 30 feet, Will DC 30 negates. The save DC is Charisma-based.
**Swift Cuts (Ex)** As long as he is attacking with a sword, _Nightripper_ treats foes who are _[[conditions/Staggered|staggered]]_, _[[conditions/Nauseated|nauseated]]_, or under the effects of a _slow_ spell (or similar effects, such as his _gaze_) as if they were _flat-footed_.
**Sword Mastery (Ex) **_Nightripper_ possesses several sword-related bonus feats normally restricted to fighters.

##### Description

Even today, centuries after his 13th and final execution, memories of Riktus Scroon continue to haunt the nightmares of those who live along the northern coastlines of the Inner Sea. During his reign of horror, the man who would come to be known as the _Nightripper_ used his position in the now disbanded Graven _[[npcs/Guard|Guard]]_ of Taldor to move along the shipping lanes with ease. His position among the mercenary company afforded him time in countless settlements from Golisfar to Corentyn, and in these unsuspecting towns he hunted. Scroon preferred young victims, that their vanishing would cause the most distress possible—his favorites were young adults freshly in love, although he seemed to have had no preference between man or woman. He abducted his victims with astonishing skill, tormenting them for hours with his blades before leaving them _[[conditions/Broken|broken]]_ and bleeding to death at the bottom of a specially prepared pit far outside of town. The mass murderer was finally captured by Cesandra Dayne, an obsessed priest of Sarenrae who had lost her fiancee and her father to Scroon. Only by forsaking the teachings of her church was she able to trap the murderer in the slums of Almas, and although the resulting fight _[[items/Mundane/Saw|saw]]_ the death of a dozen innocent bystanders, in the end Cesandra had her man alive.

After Scroon was turned over to the law in his hometown of Oppara, the authorities thought to prosecute him for the deaths of no fewer than 46 known victims. When Scroon gleefully bragged of having murdered nearly a thousand men, women, and children, the authorities were eager to write off his ravings, yet after Scroon provided exacting details to the sites of 953 victims, and one after the other his directions led to actual graves, the killer’s sentencing was hastened—death by hanging. Yet Scroon survived. One after the other, attempts to execute the _Nightripper_ failed—headsmen died of fright as they lifted the axe, guillotines malfunctioned, magic failed. Each botched execution left Scroon more disfigured, but his legend grew. The 13th and final execution put the man down once and for all—or so it was hoped.

Scroon’s soul went to the Boneyard, where something amazing happened—he passed through to the Abyss with his mind and memories intact. So remarkable was his retention of his identity that it drew the attention of Lamashtu herself, who pulled the killer’s soul from the shuddersome bosom of the Abyss and made him her personal assassin, raising him from a _broken_ shell of a soul to a nascent demon lord with greater power than he’d ever hoped for in life. His form had changed, transforming into a shape more befitting one of his horrific nature, yet his mind remained sharp and clear. _Nightripper_ harbors a strong desire for revenge, but for now he serves dutifully as Lamashtu’s favored torturer and assassin and as the lord of the dungeons below her palace in the Abyssal realm of Kurnugia. But it is said that someday, when he has repaid his debt to the Mother of Demons for his _[[spells/Ascension|ascension]]_ and rescue from the dregs of the Abyss, the _Nightripper_ will return to his old haunts. Only this time, it will not be individuals he breaks and bleeds and buries in his pits—it will be entire cities.