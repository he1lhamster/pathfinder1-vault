---
cssclass: [monsters]
title1: Kyton, Oitos
desc_short: The golden bones of this magnificent skeleton are clad in monstrous face-skins
  sewn into a cape and skirt adorned with gold pendants.
title2: Oitos
CR: 11
sources:
- name: Book of the Damned
  page: 249
  link: http://paizo.com/products/btpy9tok
XP: 12800
alignment: LE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    dex: 5
    natural: 10
HP:
  HP: 149
  long: 13d10+78
  regeneration: 5
  regeneration_weakness: good
saves:
  fort: 14
  ref: 11
  will: 15
DR:
- amount: 10
  weakness: bludgeoning and silver or bludgeoning and good
immunities:
- cold
SR: 22
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +17 (1d6+11/19-20 plus 2d6 cold)
      entries:
      - - damage: 1d6+11
          crit_range: 19-20
        - damage: 2d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 17
    - text: lash +17 (2d4+11 plus 2d6 cold)
      entries:
      - - damage: 2d4+11
        - damage: 2d6
          type: cold
      attack: lash
      bonus:
      - 17
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    paren_text: between the Material Plane, Shadow Plane, and evil-aligned planes
      only; lawful creatures only
  - name: speak with dead
    source: default
    freq: At will
    DC: 18
  - name: charm monster
    source: default
    freq: 3/day
    DC: 19
  - name: dimensional anchor
    source: default
    freq: 3/day
  - name: fabricate
    source: default
    freq: 3/day
  - name: shadow walk
    source: default
    freq: 3/day
  - name: eyebite
    source: default
    freq: 1/day
    DC: 21
  - name: summon monster V
    source: default
    freq: 1/day
    other: evil creatures only
  sources:
  - name: default
    CL: 11
    concentration: 16
ability_scores:
  STR: 19
  DEX: 20
  CON: 23
  INT: 19
  WIS: 20
  CHA: 20
BAB: 13
CMB: 17
CMB_other: +19 trip
CMD: 32
CMD_other: 34 trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Trip
- name: Iron Will
- name: Lightning Reflexes
skills:
  Appraise: 20
  Bluff: 21
  Craft (any one): 20
  Diplomacy: 21
  Fly: 14
  Intimidate: 21
  Knowledge (planes): 20
  Perception: 21
  Sense Motive: 21
  Spellcraft: 20
  Stealth: 21
languages:
- Common
- Infernal
- telepathy 100 ft.
special_qualities:
- dark traveler
ecology:
  environment: any (Shadow Plane)
  organization: solitary, pair, or delegation (1 plus 1d6 kytons)
  treasure_type: triple
special_abilities:
  Dark Traveler (Ex): When an oitos uses plane shift to travel to the Shadow Plane
    or an evil-aligned plane, it arrives at its intended destination with complete
    accuracy. When an oitos uses shadow walk, it moves at a rate of 100 miles per
    hour.
  Golden Bones (Su): |-
    On a critical hit, an oitos attempts to bless the damaged creature with inner beauty. If the target fails at a DC 21 Fortitude save, the oitos turns the creature's bones into magical, radiant gold. The target is immediately and permanently affected as per the spell faerie fire, and its Constitution is reduced by 4.

     At the start of every round this effect persists, the victim must succeed at a DC 21 Fortitude save or its eyes are burned out from the inside, resulting in permanent blindness. This is a curse effect; the effects do not stack. The cleaned bones of a Medium creature affected by this ability are worth 1,000 gp. This value doubles for each size category an affected creature is larger than Medium, and it is halved for each size category a creature is smaller than Medium. The save DC is Charisma-based.
  Lash (Su): An oitos can lash at foes with razor-sharp, animated strips of leather
    and silk. This is a primary natural attack that deals slashing damage.
  Unnerving Gaze (Ex): A creature that succumbs to an oitos's unnerving gaze becomes
    nauseated for 1 round. This is a mind-affecting fear effect. The save DC is Charisma-based.
desc_long: What is perfection without splendor? Oitos kytons know there is much more
  to seduction than audacities of the flesh. Oitoses tempt souls to drift willingly
  into their clutches. They have more discerning tastes than many of their brethren,
  though, seeking specific targets, whether those with a certain “flavor” of mortal
  experience or outsiders of particular magnificence. Tearing away their victims'
  tawdry flesh, they exalt in the clean grandeur of bone gilded with precious metals.
  They present themselves as living treasures-beings capable of fulfilling the promise
  of any reward and embodiments of glories to come.

---

# Kyton, Oitos
The golden bones of this magnificent skeleton are clad in monstrous face-skins sewn into a cape and skirt adorned with gold pendants.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 249
**XP** 12,800

LE Medium outsider (evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +21

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 Dex, +10 natural)
**hp** 149 (13d10+78); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good)
**Fort** +14, **Ref** +11, **Will** +15
**DR** 10/bludgeoning and silver or bludgeoning and good; **Immune** cold; **SR** 22

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** 2 claws +17 (1d6+11/19–20 plus 2d6 cold), lash +17 (2d4+11 plus 2d6 cold)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
Constant—fly
 At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Plane Shift|plane shift]]_ (between the Material Plane, _[[items/Armor Magic Abilities/Shadow|Shadow]]_ Plane, and evil-aligned planes only; lawful creatures only), _[[spells/Speak with Dead|speak with dead]]_ (DC 18)
 3/day—_[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Fabricate|fabricate]]_, _[[spells/Shadow Walk|shadow walk]]_
 1/day—_[[spells/Eyebite|eyebite]]_ (DC 21), _[[spells/Summon Monster V|summon monster V]]_ (evil creatures only)

##### Statistics
**Str** 19, **Dex** 20, **Con** 23, **Int** 19, **Wis** 20, **Cha** 20
**Base Atk** +13; **CMB** +17 (+19 _[[universal monster rules/Trip|trip]]_); **CMD** 32 (34 _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Appraise +20, Bluff +21, Craft (any one) +20, Diplomacy +21, Fly +14, Intimidate +21, Knowledge (planes) +20, Perception +21, Sense Motive +21, Spellcraft +20, Stealth +21
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** dark traveler

##### Ecology

**Environment** any (_Shadow_ Plane)
**Organization** solitary, pair, or delegation (1 plus 1d6 kytons)
**Treasure** triple

### Special Abilities

**Dark Traveler (Ex)** When an oitos uses _plane shift_ to travel to the _Shadow_ Plane or an evil-aligned plane, it arrives at its intended destination with complete accuracy. When an oitos uses _shadow walk_, it moves at a rate of 100 miles per hour.

**Golden Bones (Su)** On a critical hit, an oitos attempts to _[[spells/Bless|bless]]_ the damaged creature with inner beauty. If the target fails at a DC 21 Fortitude save, the oitos turns the creature’s bones into magical, _[[items/Armor Magic Abilities/Radiant|radiant]]_ gold. The target is immediately and permanently affected as per the spell _[[spells/Faerie Fire|faerie fire]]_, and its Constitution is reduced by 4.

At the start of every round this effect persists, the victim must succeed at a DC 21 Fortitude save or its eyes are burned out from the inside, resulting in permanent blindness. This is a curse effect; the effects do not stack. The cleaned bones of a _Medium_ creature affected by this ability are worth 1,000 gp. This value doubles for each size category an affected creature is larger than _Medium_, and it is halved for each size category a creature is smaller than _Medium_. The save DC is Charisma-based.

**Lash (Su)** An oitos can lash at foes with razor-sharp, _[[items/Armor Magic Abilities/Animated|animated]]_ strips of leather and silk. This is a primary natural attack that deals slashing damage.

**Unnerving _[[universal monster rules/Gaze|Gaze]]_ (Ex)** A creature that succumbs to an oitos’s unnerving _gaze_ becomes _[[conditions/Nauseated|nauseated]]_ for 1 round. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DC is Charisma-based.

##### Description

What is perfection without splendor? Oitos kytons know there is much more to seduction than audacities of the flesh. Oitoses tempt souls to drift willingly into their clutches. They have more discerning tastes than many of their brethren, though, seeking specific targets, whether those with a certain “flavor” of mortal experience or outsiders of particular magnificence. Tearing away their victims’ tawdry flesh, they exalt in the clean grandeur of bone gilded with precious metals. They present themselves as living treasures—beings capable of fulfilling the promise of any reward and embodiments of glories to come.