---
cssclass: [monsters]
title1: Shamira
desc_short: This crimson-haired demonic woman has wings of fire. She carries a slender
  bow made of flames.
title2: Shamira
CR: 25
sources:
- name: 'Pathfinder #76: The Midnight Isles'
  page: 74
  link: http://paizo.com/products/btpy92lf?Pathfinder-Adventure-Path-76-The-Midnight-Isles
XP: 1638400
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- fire
initiative:
  bonus: 11
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: unholy aura (DC 31),
AC:
  AC: 42
  touch: 35
  flat_footed: 31
  components:
    deflection: 4
    dex: 11
    natural: 7
    profane: 10
HP:
  HP: 553
  long: 27d10+405
  regeneration: 15
  regeneration_weakness: good
saves:
  fort: 28
  ref: 30
  will: 26
defensive_abilities:
- fire shield
- freedom of movement
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- charm and compulsion effects
- death effects
- disease
- fire
- electricity
- poison
resistances:
  acid: 30
  cold: 30
SR: 36
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 80
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +36 (1d8+9 plus 4d6 fire and burn)
      entries:
      - - damage: 1d8+9
        - damage: 4d6
          type: fire
        - effect: burn
      count: 2
      attack: claws
      bonus:
      - 36
    - text: tail slap +31 (2d6+4 plus 4d6 fire, burn, and grab)
      entries:
      - - damage: 2d6+4
        - damage: 4d6
          type: fire
        - effect: burn
        - effect: grab
      attack: tail slap
      bonus:
      - 31
    - text: 2 wings +31 (1d8+4 plus 4d6 fire and burn)
      entries:
      - - damage: 1d8+4
        - damage: 4d6
          type: fire
        - effect: burn
      count: 2
      attack: wings
      bonus:
      - 31
  ranged:
  - - text: firebow +43/+38/+33/+28 (1d8+14/19-20/×3 plus 1d6 fire and burn)
      entries:
      - - damage: 1d8+14
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: fire
        - effect: burn
      attack: firebow
      bonus:
      - 43
      - 38
      - 33
      - 28
  special:
  - burn (8d6 fire, DC 38)
  - constrict (2d6+13 plus 4d6 fire and burn)
  - dream haunting
  - energy drain
  - fiery passion
  - profane benediction
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: fire shield
    source: default
    freq: Constant
    other: warm shield only
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 31
  - name: charm monster
    source: default
    freq: At will
    DC: 27
  - name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: mass suggestion
    source: default
    freq: At will
    DC: 29
  - name: telekinesis
    source: default
    freq: At will
    DC: 28
  - name: unholy blight
    source: default
    freq: At will
    DC: 27
  - name: empowered delayed blast fireball
    source: default
    freq: 3/day
    DC: 30
  - name: quickened dominate person
    source: default
    freq: 3/day
    DC: 28
  - name: symbol of persuasion
    source: default
    freq: 3/day
    DC: 29
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 32
  - name: nightmare
    source: default
    freq: 1/day
    DC: 28
  - name: summon demons
    source: default
    freq: 1/day
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
ability_scores:
  STR: 29
  DEX: 32
  CON: 40
  INT: 28
  WIS: 25
  CHA: 37
BAB: 27
CMB: 36
CMB_other: +40 grapple
CMD: 71
feats:
- name: Blinding Critical
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Deadly Aim
- name: Empower Spell-Like Ability (delayed blast fireball)
- name: Improved Critical (composite longbow)
- name: Improved Precise Shot
- name: Pinpoint Targeting
- name: Point-Blank Shot
- name: Precise Shot
- name: Quicken Spell-Like Ability (dominate person)
- name: Rapid Shot
skills:
  Acrobatics: 41
  Bluff: 51
  Diplomacy: 40
  Disguise: 43
  Fly: 49
  Intimidate: 40
  Knowledge (planes): 39
  Knowledge (religion): 39
  Perception: 45
  Perform (dance): 40
  Sense Motive: 37
  Sleight of Hand: 38
  Spellcraft: 36
  Stealth: 41
  Use Magic Device: 43
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Ignan
- telepathy 300 ft.
special_qualities:
- change shape (any humanoid; alter self)
- divine deception
- nascent demon lord traits
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Divine Deception (Su): Once per day while Shamira uses her change shape ability,
    she can choose to emulate a different alignment for the purpose of divination
    spells that reveal auras (such as detect evil). This effect persists as long as
    she carries a holy symbol of a deity of the same alignment she wishes to emulate.
    This holy symbol must have been given to her within the previous hour by a worshiper
    of that deity; Shamira typically secures these symbols via mind control. This
    effect last for 2d6 hours, after which point the holy symbol crumbles to ashes.
    While it lasts, spells and other magical effects treat her alignment as if it
    were the feigned alignment, not her true alignment of chaotic evil. If she uses
    a symbol of Sarenrae to appear neutral good, this effect lasts for 24 hours before
    the symbol crumbles to dust.
  Dream Haunting (Su): Shamira can use her energy drain attack, mind-affecting spell-like
    abilities, and profane benediction abilities on any creature she successfully
    affects with her nightmare spell-like ability while that ability is in effect.
    Once she uses one of these abilities against her target, the nightmare spell ends-she
    can only use one of these abilities per use of nightmare.
  Energy Drain (Su): Shamira's energy drain ability functions like that of a succubus,
    except that it drains 2 levels per use. As a free action as part of this attack,
    she may choose use her burn special attack with her energy drain. With a successful
    DC 36 Will save, a character resists the suggestion implanted by this attack,
    and a successful DC 36 Fortitude save negates the negative level after 24 hours.
    The save DCs are Charisma-based.
  Fiery Passion (Su): Shamira's passions and fires are one. A creature must be immune
    to both fire and mind-affecting effects in order to be immune to fire damage caused
    by Shamira. Creatures immune only to fire instead take fire damage as if they
    instead had fire resistance 10. Creatures with fire resistance and no immunity
    to mind-affecting effects take fire damage from Shamira's attacks as if they had
    no fire resistance.
  Firebow (Su): As a swift action, Shamira can conjure a +5 flaming burst unholy composite
    longbow that creates arrows as she fires it. In addition, arrows fired from her
    firebow can inflict her burn special attack.
  Nascent Demon Lord Traits: In addition to many of the defenses and abilities incorporated
    into Shamira's statistics above, her weapons (natural and manufactured) are treated
    as chaotic, epic, and evil for the purpose of resolving damage reduction. Also,
    she can grant spells to her worshipers-she grants access to the domains of Chaos,
    Charm, Evil, and Nobility and the subdomains of Demon, Leadership, Love, and Lust.
  Profane Benediction (Su): This ability functions as the succubus's profane gift
    ability, except it grants a +4 profane bonus to an ability score of the target's
    choice rather than a +2 bonus. If the target is a worshiper of Sarenrae, the target
    also gains immunity to fire as long as the profane benediction persists, even
    if the worshiper at some point later abandons her faith in Sarenrae (as is often
    the case with those who are eager to keep their profane benedictions).
  Summon Demons (Sp): As a nascent demon lord, Shamira can summon any demon or combination
    of demons whose total combined CR is 20 or lower. This ability always works, and
    is equivalent to a 9th-level spell.
desc_long: |-
  Shamira, the Ardent Dream, is the nominal ruler of the isle of Alinythia, and by extension the city of Alushinyrra, but with the honor of ruling the largest of the Midnight Isles comes with an unwritten caveat-Nocticula's palace overlooks the city from its own isle. While this position is one that Shamira revels in, and one that has afforded her no small amount of inf luence (indeed, it's helped to propel her into the ranks of nascent demon lords), the Ardent Dream knows that her mistress watches over her always, and surely regards her not only as a valued lover, companion, and minion, but also as the closest thing Nocticula has to competition. Of course, Shamira does keep an eye out for any opportunity she has to erode some of Nocticula's power, for someday she hopes to wear Nocticula's crown.

  Shamira is unique in her appearance. Even before she became a nascent demon lord, her burning wings and flowing crimson hair marked her as a succubus of power. Close-lipped about her history, she appeared in Nocticula's palace one moonrise and seduced the Lady in Shadow, thus earning the position of Lady of Alinythia. (Nocticula banished Shamira's predecessor, an incubus named Ziforian, to the sewers below the city, where he may yet lurk.) None in the Abyss recall this majestic and unmistakable succubus in the city before her arrival in Nocticula's boudoir. Shamira does little to quell rumors that her previous home was a much loftier place than the Abyss, and her resemblance to the deity Sarenrae provides endless speculation.

---

# Shamira
This crimson-haired demonic woman has wings of fire. She carries a slender bow made of flames.
**Source** Pathfinder #76: The Midnight Isles pg. 74
**XP** 1,638,400
CE Medium outsider (chaotic, demon, evil, extraplanar, fire)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +45
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 31),

##### Defense

**AC** 42, touch 35, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+4 _[[spells/Deflection|deflection]]_, +11 Dex, +7 natural, +10 profane)
**hp** 553 (27d10+405); _[[universal monster rules/Regeneration|regeneration]]_ 15 (good)
**Fort** +28, **Ref** +30, **Will** +26
**Defensive Abilities** _[[spells/Fire Shield|fire shield]]_, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron and good; **Immune** charm and compulsion effects, death effects, disease, fire, electricity, poison; **Resist** acid 30, cold 30; **SR** 36
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft., fly 80 ft. (perfect)
**Melee** 2 claws +36 (1d8+9 plus 4d6 fire and _[[universal monster rules/Burn|burn]]_), tail slap +31 (2d6+4 plus 4d6 fire, _burn_, and _[[universal monster rules/Grab|grab]]_), 2 wings +31 (1d8+4 plus 4d6 fire and _burn_)
**Ranged** firebow +43/+38/+33/+28 (1d8+14/19–20/×3 plus 1d6 fire and _burn_)
**Special Attacks** _burn_ (8d6 fire, DC 38), _[[universal monster rules/Constrict|constrict]]_ (2d6+13 plus 4d6 fire and _burn_), _[[spells/Dream|dream]]_ haunting, _[[universal monster rules/Energy Drain|energy drain]]_, fiery passion, profane benediction
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th)
Constant—_detect good_, _detect law_, _fire shield_ (warm _[[spells/Shield|shield]]_ only), _freedom of movement_, _true seeing_, _unholy aura_ (DC 31)
At will—_[[spells/Charm Monster|charm monster]]_ (DC 27), _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, mass _[[spells/Suggestion|suggestion]]_ (DC 29), _[[spells/Telekinesis|telekinesis]]_ (DC 28), _[[spells/Unholy Blight|unholy blight]]_ (DC 27)
3/day—empowered _[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 30), quickened _[[spells/Dominate Person|dominate person]]_ (DC 28), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 29)
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 32), _[[spells/Nightmare|nightmare]]_ (DC 28), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 29, **Dex** 32, **Con** 40, **Int** 28, **Wis** 25, **Cha** 37
**Base Atk** +27; **CMB** +36 (+40 grapple); **CMD** 71
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_delayed blast fireball_), _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Composite longbow|composite longbow]]_), _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Pinpoint Targeting|Pinpoint Targeting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_), _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** Acrobatics +41, Bluff +51, Diplomacy +40, Disguise +43, Fly +49, Intimidate +40, Knowledge (planes, religion) +39, Perception +45, Perform (dance) +40, Sense Motive +37, Sleight of Hand +38, Spellcraft +36, Stealth +41, Use Magic Device +43; **Racial Modifiers** +8 Bluff, +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic, Ignan; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid; _[[spells/Alter Self|alter self]]_), _[[feats/Divine Deception|divine deception]]_, nascent demon lord traits

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**_Divine Deception_ (Su)** Once per day while _[[monsters/Shamira|Shamira]]_ uses her _change shape_ ability, she can choose to emulate a different alignment for the purpose of _[[spells/Divination|divination]]_ spells that reveal auras (such as _[[spells/Detect Evil|detect evil]]_). This effect persists as long as she carries a holy symbol of a deity of the same alignment she wishes to emulate. This holy symbol must have been given to her within the previous hour by a worshiper of that deity; _Shamira_ typically secures these symbols via mind control. This effect last for 2d6 hours, after which point the holy symbol crumbles to ashes. While it lasts, spells and other magical effects treat her alignment as if it were the feigned alignment, not her true alignment of chaotic evil. If she uses a symbol of Sarenrae to appear neutral good, this effect lasts for 24 hours before the symbol crumbles to dust.

**_Dream_ Haunting (Su)** _Shamira_ can use her _energy drain_ attack, mind-affecting _spell-like abilities_, and profane benediction abilities on any creature she successfully affects with her _nightmare_ spell-like ability while that ability is in effect. Once she uses one of these abilities against her target, the _nightmare_ spell ends—she can only use one of these abilities per use of _nightmare_.

**_Energy Drain_ (Su)** _Shamira_’s _energy drain_ ability functions like that of a succubus, except that it drains 2 levels per use. As a free action as part of this attack, she may choose use her _burn_ special attack with her _energy drain_. With a successful DC 36 Will save, a character resists the _suggestion_ implanted by this attack, and a successful DC 36 Fortitude save negates the negative level after 24 hours. The save DCs are Charisma-based.

**Fiery Passion (Su)** _Shamira_’s passions and fires are one. A creature must be immune to both fire and mind-affecting effects in order to be immune to fire damage caused by _Shamira_. Creatures immune only to fire instead take fire damage as if they instead had fire _[[universal monster rules/Resistance|resistance]]_ 10. Creatures with fire _resistance_ and no _[[universal monster rules/Immunity|immunity]]_ to mind-affecting effects take fire damage from _Shamira_’s attacks as if they had no fire _resistance_.

**Firebow (Su)** As a swift action, _Shamira_ can conjure a +5 _[[items/Weapon Magic Abilities/Flaming Burst|flaming burst]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _composite longbow_ that creates arrows as she fires it. In addition, arrows fired from her firebow can inflict her _burn_ special attack.

**Nascent Demon Lord Traits** In addition to many of the defenses and abilities incorporated into _Shamira_’s statistics above, her weapons (natural and manufactured) are treated as chaotic, epic, and evil for the purpose of resolving _[[universal monster rules/Damage Reduction|damage reduction]]_. Also, she can grant spells to her worshipers—she grants access to the domains of Chaos, Charm, Evil, and Nobility and the subdomains of Demon, _[[feats/Leadership|Leadership]]_, Love, and Lust.

**Profane Benediction (Su)** This ability functions as the succubus’s profane gift ability, except it grants a +4 profane bonus to an ability score of the target’s choice rather than a +2 bonus. If the target is a worshiper of Sarenrae, the target also gains _immunity_ to fire as long as the profane benediction persists, even if the worshiper at some point later abandons her faith in Sarenrae (as is often the case with those who are eager to keep their profane benedictions).
**_Summon_ Demons (Sp)** As a nascent demon lord, _Shamira_ can _summon_ any demon or combination of demons whose total combined CR is 20 or lower. This ability always works, and is equivalent to a 9th-level spell.

##### Description

_Shamira_, the Ardent _Dream_, is the nominal ruler of the isle of Alinythia, and by extension the city of Alushinyrra, but with the honor of ruling the largest of the Midnight Isles comes with an unwritten caveat—Nocticula’s palace overlooks the city from its own isle. While this position is one that _Shamira_ revels in, and one that has afforded her no small amount of inf luence (indeed, it’s helped to propel her into the ranks of nascent demon lords), the Ardent _Dream_ knows that her mistress watches over her always, and surely regards her not only as a valued lover, companion, and minion, but also as the closest thing Nocticula has to competition. Of course, _Shamira_ does keep an eye out for any opportunity she has to erode some of Nocticula’s power, for someday she hopes to wear Nocticula’s crown.

_Shamira_ is unique in her appearance. Even before she became a nascent demon lord, her _[[items/Weapon Magic Abilities/Burning|burning]]_ wings and flowing crimson hair marked her as a succubus of power. Close-lipped about her history, she appeared in Nocticula’s palace one moonrise and seduced the Lady in _[[items/Armor Magic Abilities/Shadow|Shadow]]_, thus earning the position of Lady of Alinythia. (Nocticula banished _Shamira_’s predecessor, an incubus named Ziforian, to the sewers below the city, where he may yet lurk.) None in the Abyss recall this majestic and unmistakable succubus in the city before her arrival in Nocticula’s boudoir. _Shamira_ does little to quell rumors that her previous home was a much loftier place than the Abyss, and her resemblance to the deity Sarenrae provides endless speculation.