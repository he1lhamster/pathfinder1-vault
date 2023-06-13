---
cssclass: [monsters]
title1: Blighted Fey (Satyr)
desc_short: Ropes of fungus and patches of sickly mold cover this wan satyr.
title2: Blighted Fey (Satyr)
CR: 6
sources:
- name: Inner Sea Bestiary
  page: 6
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 2400
alignment: CE
size: Medium
type: fey
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    dex: 2
    dodge: 1
    natural: 7
HP:
  HP: 76
  long: 8d8+40
saves:
  fort: 6
  ref: 8
  will: 8
defensive_abilities:
- fungal rejuvenation
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- disease
- paralysis
- poison
- polymorph
resistances:
  cold: 10
  electricity: 10
SR: 17
speeds:
  base: 40
attacks:
  melee:
  - - text: dagger +6 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 6
    - text: horns +1 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: horns
      bonus:
      - 1
  ranged:
  - - text: shortbow +6 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 6
  special:
  - parasitic bond
  - pipes
  - thorn throw
spell_like_abilities:
  entries:
  - name: charm person
    source: default
    freq: At will
    DC: 16
  - name: dancing lights
    source: default
    freq: At will
  - name: ghost sound
    source: default
    freq: At will
    DC: 15
  - name: sleep
    source: default
    freq: At will
    DC: 16
  - name: suggestion
    source: default
    freq: At will
    DC: 17
  - name: fear
    source: default
    freq: 1/day
    DC: 18
  - name: summon nature's ally III
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 8
    concentration: 13
ability_scores:
  STR: 18
  DEX: 15
  CON: 19
  INT: 12
  WIS: 14
  CHA: 21
BAB: 4
CMB: 8
CMD: 21
feats:
- name: Dodge
- name: Mobility
- name: Skill Focus (Perception)
- is_bonus: true
  name: Toughness
- name: Weapon Finesse
skills:
  Bluff: 16
  Diplomacy: 16
  Disguise: 10
  Intimidate: 10
  Knowledge (nature): 12
  Perception: 20
  Perform (wind): 20
  Stealth: 19
  Survival: 7
  _racial_mods:
    Knowledge (nature):
      _: 2
    Perception:
      _: 6
    Perform (wind):
      _: 4
    Stealth:
      _: 6
languages:
- Common
- Sylvan
special_qualities:
- Cyth-V'sug's unity
- tainted blood
ecology:
  environment: temperate forests (Nirmathas)
  organization: solitary, pair, band (3-6), or orgy (7-11)
  treasure_type: standard
  treasure:
  - dagger
  - shortbow plus 20 arrows
  - masterwork panpipes
  - other treasure
special_abilities:
  Pipes (Su): A satyr can focus and empower his magic by playing haunting melodies
    on his panpipes. When he plays, all creatures within a 60-foot radius must make
    a successful DC 18 Will save or be affected by charm person, fear, sleep, or suggestion,
    depending on which tune the satyr chooses. A creature that successfully saves
    against any of the pipes' effects cannot be affected by the same set of pipes
    for 24 hours, but can still be affected by the satyr's other spell-like abilities
    as normal. The satyr's use of his pipes does not count toward his uses per day
    of his spell-like abilities, and if separated from them, he may continue to use
    his standard abilities. The pipes themselves are masterwork, and a satyr can craft
    a replacement with 1 week of labor. The save DC is Charisma-based.
desc_long: |-
  The forest of Fangwood dominates the nation of Nirmathas. The country depends on the mighty wood for its security and economy, yet in its thick and shadowy depths lurks an oppressive curse. Where the pine trees grow tall and thick, the dryad Arlantia reigns. A pawn of the demon lord Cyth-V'sug, she is infected by the insidious tendrils of the Prince of the Blasted Heath. A magical breach forged by this curse connects the demon lord's realm, the Jeharlu, to Golarion and to the First World itself. Arlantia infects trees with demonic ichor that warps the fey creatures who reside in the heart of Fangwood, and she takes advantage of the conf lict and war that wracks Nirmathas to create an army of thorncrowned daughters and other rot-infested horrors to consume the forest from within.

  The blight manifests as a black and greasy fungal rot that moves and sways tree branches and limbs where no wind propels them, and a mystic network of fell power extends an unnatural awareness between nearby blighted fey. Dryads are by far the most insidious of the corrupted fey; they lure humanoids to literally and spiritually dark places to beget more daughters from their dark embrace- and further spread the disease. The dryads connect through a unified but tainted mystic field that transcends their ordinary limitations and permits them to treat every infected tree as if it were their own bonded tree.

  Only magic such as miracle, limited wish, or wish can sever the connection to the Jeharlu and cure a blighted fey. Some speculate that a magical linchpin exists within Fangwood, which if destroyed would end this hideous plague.

---

# Blighted Fey (Satyr)
Ropes of fungus and patches of sickly mold cover this wan _[[monsters/Satyr|satyr]]_.
**Source** Inner Sea Bestiary pg. 6
**XP** 2,400
CE Medium fey
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 76 (8d8+40)
**Fort** +6, **Ref** +8, **Will** +8
**Defensive Abilities** fungal rejuvenation; **DR** 10/cold iron and good; **Immune** disease, _[[universal monster rules/Paralysis|paralysis]]_, poison, _[[spells/Polymorph|polymorph]]_; **Resist** cold 10, electricity 10; **SR** 17

##### Offense
**Speed** 40 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +6 (1d4+4/19–20), horns +1 (1d6+2)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +6 (1d6/×3)
**Special Attacks** parasitic bond, pipes, thorn throw
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +13)
At will—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), sleep (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 17)
1/day—_[[universal monster rules/Fear|fear]]_ (DC 18), _[[universal monster rules/Summon|summon]]_ nature’s ally III

##### Statistics
**Str** 18, **Dex** 15, **Con** 19, **Int** 12, **Wis** 14, **Cha** 21
**Base Atk** +4; **CMB** +8; **CMD** 21
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +16, Diplomacy +16, Disguise +10, Intimidate +10, Knowledge (nature) +12, Perception +20, Perform (wind) +20, Stealth +19, Survival +7; **Racial Modifiers** +2 Knowledge (nature), +6 Perception, +4 Perform (wind), +6 Stealth
**Languages** Common, Sylvan
**SQ** Cyth-V’sug’s unity, tainted blood

##### Ecology

**Environment** temperate forests (Nirmathas)
**Organization** solitary, pair, band (3–6), or orgy (7–11)
**Treasure** standard (_dagger_, _shortbow_ plus 20 arrows, masterwork panpipes, other treasure)

### Special Abilities

**Pipes (Su)** A _satyr_ can focus and empower his magic by playing haunting melodies on his panpipes. When he plays, all creatures within a 60-foot radius must make a successful DC 18 Will save or be affected by _charm person_, _fear_, sleep, or _suggestion_, depending on which tune the _satyr_ chooses. A creature that successfully saves against any of the pipes’ effects cannot be affected by the same set of pipes for 24 hours, but can still be affected by the _satyr_’s other _spell-like abilities_ as normal. The _satyr_’s use of his pipes does not count toward his uses per day of his _spell-like abilities_, and if separated from them, he may continue to use his standard abilities. The pipes themselves are masterwork, and a _satyr_ can craft a replacement with 1 week of labor. The save DC is Charisma-based.

##### Description

The forest of Fangwood dominates the nation of Nirmathas. The country depends on the mighty wood for its security and economy, yet in its thick and shadowy depths lurks an oppressive curse. Where the pine trees grow tall and thick, the _[[monsters/Dryad|dryad]]_ Arlantia reigns. A pawn of the demon lord Cyth-V’sug, she is infected by the insidious tendrils of the Prince of the Blasted Heath. A magical breach forged by this curse connects the demon lord’s realm, the Jeharlu, to Golarion and to the First World itself. Arlantia infects trees with demonic ichor that warps the fey creatures who reside in the heart of Fangwood, and she takes advantage of the conf lict and war that wracks Nirmathas to create an army of thorncrowned daughters and other rot-infested horrors to consume the forest from within.

The _[[spells/Blight|blight]]_ manifests as a black and greasy fungal rot that moves and sways tree branches and limbs where no wind propels them, and a mystic network of fell power extends an unnatural awareness between nearby blighted fey. Dryads are by far the most insidious of the corrupted fey; they lure humanoids to literally and spiritually dark places to beget more daughters from their dark embrace— and further spread the disease. The dryads connect through a unified but tainted mystic field that transcends their ordinary limitations and permits them to treat every infected tree as if it were their own bonded tree.

Only magic such as _[[spells/Miracle|miracle]]_, _[[spells/Limited Wish|limited wish]]_, or _[[spells/Wish|wish]]_ can sever the connection to the Jeharlu and cure a blighted fey. Some speculate that a magical linchpin exists within Fangwood, which if destroyed would end this hideous plague.