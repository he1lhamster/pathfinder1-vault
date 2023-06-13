---
cssclass: [monsters]
title1: Dark Folk, Dark Slayer
desc_short: 'This small humanoid is clothed in tattered rags from head to foot. Only
  its sinister eyes and pale hands are visible. '
title2: Dark Slayer
CR: 3
sources:
- name: Bestiary 2
  page: 75
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 800
alignment: CE
size: Small
type: humanoid
subtypes:
- dark folk
initiative:
  bonus: 4
senses:
  detect magic: true
  see in darkness: true
AC:
  AC: 15
  touch: 15
  flat_footed: 11
  components:
    dex: 4
    size: 1
HP:
  HP: 22
  long: 4d8+4
saves:
  fort: 2
  ref: 8
  will: 1
weaknesses:
- light blindness
speeds:
  base: 30
attacks:
  melee:
  - - text: kukri +8 (1d3-1/18-20 plus black smear poison)
      entries:
      - - damage: 1d3-1
          crit_range: 18-20
        - effect: black smear poison
      attack: kukri
      bonus:
      - 8
  special:
  - death throes
  - poison use
  - sneak attack +2d6
  - soul harvest
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: bleed
    source: default
    freq: At will
    DC: 12
  - name: chill touch
    source: default
    freq: At will
    DC: 13
  - name: darkness
    source: default
    freq: At will
  - name: spectral hand
    source: default
    freq: At will
  - name: daze monster
    source: default
    freq: 3/day
    DC: 14
  - name: death knell
    source: default
    freq: 3/day
    DC: 14
  - name: inflict moderate wounds
    source: default
    freq: 3/day
    DC: 14
  sources:
  - name: default
    CL: 4
    concentration: 6
ability_scores:
  STR: 9
  DEX: 18
  CON: 12
  INT: 10
  WIS: 11
  CHA: 15
BAB: 3
CMB: 1
CMD: 15
feats:
- name: Skill Focus (Use Magic Device)
- name: Weapon Finesse
skills:
  Climb: 3
  Perception: 4
  Spellcraft: 7
  Stealth: 12
  Use Magic Device: 12
  _racial_mods:
    Climb:
      _: 4
    Stealth:
      _: 4
    Perception:
      _: 4
languages:
- Dark Folk
special_qualities:
- magical knack
ecology:
  environment: any underground
  organization: solitary, gang (1 dark slayer and 2-5 dark stalkers), or clan (20-80
    dark creepers plus 1 dark stalker or dark slayer per 20 dark creepers)
  treasure_type: standard
  treasure:
  - kukri
  - black smear [2 doses] [see Bestiary 54]
  - other gear
special_abilities:
  Death Throes (Su): When a dark slayer is slain, its body implodes violently into
    nothingness, leaving its gear in a heap on the ground. All creatures within a
    10-foot burst take 1d8 points of sonic damage and must make a DC 13 Fortitude
    save or be deafened for 2d4 rounds. The save DC is Constitution-based.
  Magical Knack (Ex): Spellcraft and Use Magic Device are always class skills for
    dark slayers.
  Soul Harvest (Su): When a dark slayer damages a flat-footed foe or a foe it is flanking
    with a melee touch spell or spell-like ability that deals hit point damage, the
    spell does an additional 1d6 points of damage and the dark slayer gains an equal
    amount of temporary hit points. These temporary hit points last for a maximum
    of 1 hour.
desc_long: |-
  Dark slayers are a relatively rare sub-race of the dark folk imbued with malign energies that grant them a suite of deadly spell-like abilities beyond those normally accessible to their kin. They are usually encountered leading small bands of dark creepers, and seethe with barely concealed envy of the dark stalkers, ever scheming to displace them and claim a dark folk tribe of their own. Dark stalkers direct the slayers for their own ends, grooming them for use against enemies, ever ready to sacrifice a slayer in battle for an advantage, however temporary. 

  Unlike other dark folk, dark slayers embrace their evil impulses. Their pleasures extend more to murder and pain than to theft or mayhem. Dark slayers are obsessed with magical trinkets, coveting them above all else. Sadly, their obsessive need to fiddle and tinker often leaves their pretties broken or depleted. 

  Dark slayers stand just short of 4 feet tall and weigh 50 pounds. Most have a persistent tremor visible in their hands, stilled only when fondling a newfound magic item. Their skin is dead white, dry, and hot to the touch; their eyes are dark and narrow. Dark slayers wear salvaged rags like dark creepers do, but they discard the rags when they grow too tattered or foul-smelling.

---

# Dark Folk, Dark Slayer
This small humanoid is clothed in tattered rags from head to foot. Only its sinister eyes and pale hands are visible.

**Source** Bestiary 2 pg. 75
**XP** 800
CE Small humanoid (dark folk)
**Init** +4; **Senses** _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +4

##### Defense

**AC** 15, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+4 Dex, +1 size)
**hp** 22 (4d8+4)
**Fort** +2, **Ref** +8, **Will** +1
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Kukri|kukri]]_ +8 (1d3–1/18–20 plus black smear poison)
**Special Attacks** death throes, poison use, sneak attack +2d6, soul harvest
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
Constant—_detect magic_
At will—_[[universal monster rules/Bleed|bleed]]_ (DC 12), _[[spells/Chill Touch|chill touch]]_ (DC 13), _[[spells/Darkness|darkness]]_, _[[spells/Spectral Hand|spectral hand]]_
3/day—_[[spells/Daze Monster|daze monster]]_ (DC 14), _[[spells/Death Knell|death knell]]_ (DC 14), _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 14)

##### Statistics
**Str** 9, **Dex** 18, **Con** 12, **Int** 10, **Wis** 11, **Cha** 15
**Base Atk** +3; **CMB** +1; **CMD** 15
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Use Magic Device), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +3, Perception +4, Spellcraft +7, Stealth +12, Use Magic Device +12; **Racial Modifiers** +4 _Climb_, +4 Stealth, +4 Perception
**Languages** Dark Folk
**SQ** magical knack

##### Ecology

**Environment** any underground
**Organization** solitary, gang (1 dark _[[classes/Slayer|slayer]]_ and 2–5 dark stalkers), or clan (20–80 dark creepers plus 1 dark stalker or dark _slayer_ per 20 dark creepers)
**Treasure** standard (_kukri_, black smear [2 doses] [see Bestiary 54], other gear)

### Special Abilities

**Death Throes (Su)** When a dark _slayer_ is slain, its body implodes violently into nothingness, leaving its gear in a heap on the ground. All creatures within a 10-foot burst take 1d8 points of sonic damage and must make a DC 13 Fortitude save or be _[[conditions/Deafened|deafened]]_ for 2d4 rounds. The save DC is Constitution-based.

**Magical Knack (Ex)** Spellcraft and Use Magic Device are always class skills for dark slayers.
**Soul Harvest (Su)** When a dark _slayer_ damages a _flat-footed_ foe or a foe it is flanking with a melee touch spell or spell-like ability that deals hit point damage, the spell does an additional 1d6 points of damage and the dark _slayer_ gains an equal amount of temporary hit points. These temporary hit points last for a maximum of 1 hour.

##### Description

Dark slayers are a relatively rare sub-race of the dark folk imbued with malign energies that grant them a suite of _[[items/Weapon Magic Abilities/Deadly|deadly]]_ _spell-like abilities_ beyond those normally accessible to their kin. They are usually encountered leading small bands of dark creepers, and seethe with barely _[[items/Weapon Magic Abilities/Concealed|concealed]]_ envy of the dark stalkers, ever scheming to displace them and claim a dark folk tribe of their own. Dark stalkers direct the slayers for their own ends, grooming them for use against enemies, ever ready to _[[spells/Sacrifice|sacrifice]]_ a _slayer_ in battle for an advantage, however temporary.

Unlike other dark folk, dark slayers embrace their evil impulses. Their pleasures extend more to murder and pain than to theft or mayhem. Dark slayers are obsessed with magical trinkets, coveting them above all else. Sadly, their obsessive need to fiddle and tinker often leaves their pretties _[[conditions/Broken|broken]]_ or depleted.

Dark slayers stand just short of 4 feet tall and weigh 50 pounds. Most have a persistent tremor visible in their hands, stilled only when fondling a newfound magic item. Their skin is dead white, dry, and hot to the touch; their eyes are dark and narrow. Dark slayers wear salvaged rags like dark creepers do, but they discard the rags when they grow too tattered or foul-smelling.