---
cssclass: [monsters]
title1: Hag, Dreamthief Hag
desc_short: This hideously gaunt woman has tangled white hair, goatlike horns, and
  menacing eyes that blaze with green light.
title2: Dreamthief Hag
CR: 11
sources:
- name: Occult Bestiary
  page: 22
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 12800
alignment: NE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  see alignment: true
AC:
  AC: 27
  touch: 16
  flat_footed: 21
  components:
    dex: 6
    natural: 11
HP:
  HP: 149
  long: 13d10+78
saves:
  fort: 14
  ref: 10
  will: 12
DR:
- amount: 10
  weakness: cold iron and magic
immunities:
- cold
- fire
- mind-affecting effects
SR: 26
speeds:
  base: 30
  other_semicolon: fly 20 ft. (clumsy)
attacks:
  melee:
  - - text: bite +20 (2d10+6/19-20 plus mind block)
      entries:
      - - damage: 2d10+6
          crit_range: 19-20
        - effect: mind block
      attack: bite
      bonus:
      - 20
    - text: 2 claws +14 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: claws
      bonus:
      - 14
  special:
  - dream theft
  - mind block
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - superscripts:
    - UC
    name: see alignment
    source: default
    freq: Constant
  - name: deep slumber
    source: default
    freq: At will
    DC: 18
  - name: etherealness
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: magic missile
    source: default
    freq: At will
  sources:
  - name: default
    CL: 10
    concentration: 15
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: dream council
    PE: 5
    DC: 20
  - superscripts:
    - OA
    name: dream scan
    PE: 5
    DC: 20
  - superscripts:
    - OA
    name: dream travel
    PE: 6
  sources:
  - name: default
    CL: 10
    concentration: 15
  PE: 15
ability_scores:
  STR: 23
  DEX: 23
  CON: 22
  INT: 20
  WIS: 18
  CHA: 21
BAB: 13
CMB: 19
CMD: 35
feats:
- name: Combat Casting
- name: Deceitful
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Mounted Combat
- name: Trample
- name: Weapon Focus (bite)
skills:
  Bluff: 25
  Diplomacy: 21
  Disguise: 25
  Fly: -2
  Intimidate: 21
  Knowledge (arcana): 21
  Knowledge (planes): 21
  Perception: 20
  Ride: 19
  Sense Motive: 20
  Spellcraft: 18
  Stealth: 22
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Infernal
special_qualities:
- change shape (any humanoid or cat; alter self or beast shape II)
- dreamstone
ecology:
  environment: any (Dimension of Dreams)
  organization: solitary, mounted (1 plus 1 advanced nightmare), or coven (1 plus
    2 hags of any type)
  treasure_type: standard
special_abilities:
  Dream Theft (Su): While in the same space as a dreaming creature, or when touching
    the boundary of a dreamscape, the hag can force the dreaming creature into a lucid
    body and enter its dreamscape-this is a full-round action that provokes attacks
    of opportunity. If the hag deals enough damage to kill the lucid body (despite
    the dreamer's ability to perform impossible deeds), instead of the dreamer waking
    up harmlessly, the hag can trap the creature's dreaming mind in her dreamstone
    (see below), causing its body to remain in a mindless coma indefinitely (even
    magic like miracle and wish can at best transport the caster to the location of
    the trapped mind).
  Dreamstone (Su): Every dreamthief hag carries a dreamstone-a gemstone crafted from
    the petrified tears of a dream dragon and worth at least 2,200 gp. The stone is
    psychically attuned by the hag's spirit and proximity. If the hag dies or is no
    longer in possession of her stone, it remains attuned for only 24 hours. The dreamstone
    can hold up to 20 dreaming minds stolen by the hag. A dreamthief hag can release
    a stored mind, sifting out its essence, to regain 2 PE. The mind then returns
    to its body, but the hag's tampering usually inflicts deep mental scars, resulting
    in new phobias, nervous ticks, or sleep disorders. A dreamthief hag can use her
    dream theft ability and etherealness only if she has her dreamstone.
  Mind Block (Su): A creature bitten by a dreamthief hag cannot cast spells or attempt
    Intelligence checks or Intelligence-based skill checks for 1 round. Creatures
    with at least 1 mythic rank are immune to this ability. This is a poison effect.
desc_long: |-
  These more powerful cousins of night hags often wander the Dimension of Dreams, stealing dreaming minds, trapping them within dreamstones, and selling them to the highest bidder. While few denizens of any plane trust dreamthief hags, some welcome them as merchants. Many powerful evil beings find captured minds to be useful components in dark rituals or profane research.

  Even those who hold dreamthief hags in contempt are careful not to offend them, for their bite contains a venom capable of temporarily paralyzing a victim's mind, and the hags have few scruples about capturing even longtime commercial partners' minds if the hags feel they have been disrespectful. While it's difficult to determine exactly what harm befalls the minds in dreamthief hags' care, those who have been released by them are never quite the same, and rarely have a nightmare-free night of sleep again.

---

# Hag, Dreamthief Hag
This hideously gaunt woman has tangled white hair, goatlike horns, and _[[items/Weapon Magic Abilities/Menacing|menacing]]_ eyes that blaze with green light.
**Source** Occult Bestiary pg. 22
**XP** 12,800

NE Medium outsider (evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; _[[spells/See Alignment|see alignment]]_; Perception +20

##### Defense

**AC** 27, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+6 Dex, +11 natural)
**hp** 149 (13d10+78)
**Fort** +14, **Ref** +10, **Will** +12
**DR** 10/cold iron and magic; **Immune** cold, fire, mind-affecting effects; **SR** 26

##### Offense
**Speed** 30 ft.; fly 20 ft. (clumsy)
**Melee** bite +20 (2d10+6/19–20 plus mind block), 2 claws +14 (2d6+6)
**Special Attacks** _[[spells/Dream|dream]]_ theft, mind block
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +15)
Constant—_[[spells/Detect Magic|detect magic]]_, _see alignment_
At will—_[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Etherealness|etherealness]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Magic Missile|magic missile]]_
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 10th; concentration +15)
15 PE—_[[spells/Dream Council|dream council]]_ (5 PE, DC 20), _[[spells/Dream Scan|dream scan]]_ (5 PE, DC 20), _[[spells/Dream Travel|dream travel]]_ (6 PE)

##### Statistics
**Str** 23, **Dex** 23, **Con** 22, **Int** 20, **Wis** 18, **Cha** 21
**Base Atk** +13; **CMB** +19; **CMD** 35
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Mounted Combat|Mounted Combat]]_, _[[universal monster rules/Trample|Trample]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +25, Diplomacy +21, Disguise +25, Fly –2, Intimidate +21, Knowledge (arcana) +21, Knowledge (planes) +21, Perception +20, Ride +19, Sense Motive +20, Spellcraft +18, Stealth +22
**Languages** Abyssal, Aklo, Celestial, Common, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid or cat; _[[spells/Alter Self|alter self]]_ or _[[spells/Beast Shape II|beast shape II]]_), dreamstone

##### Ecology

**Environment** any (Dimension of Dreams)
**Organization** solitary, mounted (1 plus 1 advanced _[[spells/Nightmare|nightmare]]_), or coven (1 plus 2 hags of any type)
**Treasure** standard

### Special Abilities

**_Dream_ Theft (Su)** While in the same space as a dreaming creature, or when touching the boundary of a dreamscape, the hag can force the dreaming creature into a lucid body and enter its dreamscape—this is a full-round action that provokes attacks of opportunity. If the hag deals enough damage to kill the lucid body (despite the dreamer’s ability to perform impossible deeds), instead of the dreamer waking up harmlessly, the hag can trap the creature’s dreaming mind in her dreamstone (see below), causing its body to remain in a mindless coma indefinitely (even magic like _[[spells/Miracle|miracle]]_ and _[[spells/Wish|wish]]_ can at best transport the caster to the location of the trapped mind).

**Dreamstone (Su)** Every dreamthief hag carries a dreamstone—a gemstone crafted from the _[[conditions/Petrified|petrified]]_ tears of a _dream_ dragon and worth at least 2,200 gp. The stone is psychically attuned by the hag’s spirit and proximity. If the hag dies or is no longer in _[[spells/Possession|possession]]_ of her stone, it remains attuned for only 24 hours. _[[items/Wondrous Item/The Dreamstone|The dreamstone]]_ can hold up to 20 dreaming minds stolen by the hag. A dreamthief hag can release a stored mind, sifting out its essence, to regain 2 PE. The mind then returns to its body, but the hag’s tampering usually inflicts deep mental scars, resulting in new phobias, nervous ticks, or sleep disorders. A dreamthief hag can use her _dream_ theft ability and _etherealness_ only if she has her dreamstone.

**Mind Block (Su)** A creature bitten by a dreamthief hag cannot cast spells or attempt Intelligence checks or Intelligence-based skill checks for 1 round. Creatures with at least 1 mythic rank are immune to this ability. This is a poison effect.

##### Description

These more powerful cousins of night hags often wander the Dimension of Dreams, stealing dreaming minds, trapping them within dreamstones, and selling them to the highest bidder. While few denizens of any plane trust dreamthief hags, some welcome them as merchants. Many powerful evil beings find captured minds to be useful components in dark rituals or profane research.

Even those who hold dreamthief hags in contempt are careful not to offend them, for their bite contains a venom capable of temporarily paralyzing a victim’s mind, and the hags have few scruples about capturing even longtime commercial partners’ minds if the hags feel they have been disrespectful. While it’s difficult to determine exactly what _[[spells/Harm|harm]]_ befalls the minds in dreamthief hags’ care, those who have been released by them are never quite the same, and rarely have a nightmare-free night of sleep again.