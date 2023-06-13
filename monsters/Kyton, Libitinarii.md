---
cssclass: [monsters]
title1: Kyton, Libitinarii
desc_short: This willowy, blue-skinned figure wears robes of draped chains. Its exposed
  skin is pierced with lengths of razor-sharp, bloodstained icicles.
title2: Libitinarii
CR: 13
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 84
  link: https://paizo.com/products/btq01vak
XP: 25600
alignment: LE
size: Medium
type: outsider
subtypes:
- cold
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 11
senses:
  darkvision: 60
AC:
  AC: 28
  touch: 17
  flat_footed: 21
  components:
    dex: 7
    natural: 11
HP:
  HP: 184
  long: 16d10+96
  regeneration: 5
  regeneration_weakness: good weapons and spells, silver weapons
saves:
  fort: 16
  ref: 17
  will: 13
defensive_abilities:
- icy fiend
DR:
- amount: 10
  weakness: good or silver
immunities:
- cold
SR: 24
speeds:
  base: 30
  other_semicolon: air walk
attacks:
  melee:
  - - text: 2 claws +22 (2d6+6 plus 2d6 cold)
      entries:
      - - damage: 2d6+6
        - damage: 2d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 22
    - text: 2 chains +22 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: chains
      bonus:
      - 22
  ranged:
  - - text: 4 icicles +23 (1d8+6/19-20/×3 plus 2d6 cold)
      entries:
      - - damage: 1d8+6
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 2d6
          type: cold
      count: 4
      attack: icicles
      bonus:
      - 23
  special:
  - perfect freeze
  - unnerving gaze (30 ft., DC 21)
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: plane shift
    source: default
    freq: At will
    paren_text: from Material Plane to Shadow Plane only, self only
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 18
  - name: dimension door
    source: default
    freq: 3/day
  - name: ice storm
    source: default
    freq: 3/day
  - name: polar ray
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
    concentration: 16
ability_scores:
  STR: 23
  DEX: 24
  CON: 22
  INT: 15
  WIS: 22
  CHA: 17
BAB: 16
CMB: 22
CMD: 39
feats:
- name: Alertness
- name: Combat Reflexes
- name: Deadly Aim
- name: Improved Critical (icicles)
- name: Improved Initiative
- name: Iron Will
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Intimidate: 22
  Knowledge (local): 21
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 29
  Sense Motive: 29
  Stealth: 26
  Survival: 25
languages:
- Common
- Infernal
- Shadowtongue
ecology:
  environment: any (Shadow Plane)
  organization: solitary, pair, or shiver (2-5)
  treasure_type: standard
special_abilities:
  Icicles (Ex): A libitinarii can use the icicles embedded into its flesh as thrown
    ranged weapons, with a range increment of 20 feet. It can retrieve up to four
    of these icicles per round as a free action. These icicles deal piercing damage
    equal to 1d8 plus the libitinarii's Strength modifier (usually +6) plus 2d6 points
    of cold damage; they deal triple damage on a critical hit (although the cold damage
    is not increased). The icicles aren't considered magic weapons, but they are supernaturally
    hardened and count as adamantine for the purpose of overcoming damage reduction.
    Once the libitinarii has retrieved icicles from its flesh, new icicles immediately
    form as a free action. If the libitinarii's regeneration is suppressed, it also
    can't form new icicles. A libitinarii typically has 24 icicles embedded in its
    flesh at any time.
  Icy Fiend (Ex): A libitinarii's body is made from an unholy union of soulstuff and
    the icy essence of the coldest reaches of the Shadow Plane. As such, the libitinarii
    is immune to cold, and it can treat any difficult terrain that results from magical
    or mundane ice as normal terrain, such as the icy terrain of the Frozen Tears,
    realm of the kyton demagogue Inkariax.
  Perfect Freeze (Su): A libitinarii can harness the power of absolute zero and impose
    it upon the body of a living creature with a touch. The libitinarii can use this
    ability three times per day as a standard action that doesn't provoke attacks
    of opportunity. If the libitinarii's touch attack is successful, the target takes
    2d6 points of cold damage and 2d6 points of evil-aligned magic damage. A successful
    DC 23 Fortitude saving throw halves each type of damage. Additionally, creatures
    that fail this saving throw must immediately attempt a DC 23 Will saving throw.
    Failing this second saving throw means that a creature has been frozen solid and
    has become a supernaturally frozen, mindless, inert statue and is considered petrified,
    per flesh to stone (if the creature is not made of flesh, this secondary ability
    has no effect). The creature can't be turned back to flesh by casting stone to
    flesh spell, but it can be restored via casting break enchantment. If the creature
    isn't returned to flesh after a number of hours equal to the creature's Hit Dice,
    the creature dies and remains a frozen statue. It can be returned to life normally
    by casting raise dead or similar spells. This is a cold effect. The save DCs are
    Constitution-based.
  Unnerving Gaze (Ex): A creature that succumbs to a libitinarii's unnerving gaze
    becomes staggered for 1 round as it feels itself slowly freezing from the inside
    out.
desc_long: |-
  Libitinariis form from the souls of cold-obsessed spellcasters, wicked taxidermists, torturers partial to using frostbite to torment their victims, and other evil beings obsessed with inflicting pain through the perfect preservation of cold. They roam the Shadow Planes' frozen reaches seeking to further their craft. Most serve Inkariax, the kyton demagogue known as the White Death, who seeks to preserve the fleetingness of perfection with his icy-fingered grasp. Indeed, the demagogue's favored servants almost entirely consist of libitinariis.

   Other libitinariis serve Doloras, the demigoddess of dispassion, detachment, and pain, who many kytons believe was the infernal patroness that released their kind from Hell eons ago. In some cases, libitinariis pay homage to both unholy deities, for the two churches share more in common than not. Certainly Inkariax and his worshippers pay homage to the fell queen, and so many libitinariis consider deference to her a matter of course.

   Libitinariis' bodies seem humanoid, though their skin ranges in color from powder to navy blue. Their lips, ears, fingers, and toes are deep black, as if horribly frostbitten. Libitinariis often wear robes of draping chains, though most prominent on their persons are the horrific icicles that pierce their flesh. Although they are as adept at wielding traditional weapons as any humanoid, they typically favor using these icicles as thrown weapons.

   Libitinariis are roughly 5 feet tall and typically weight from 90 to 140 pounds.

---

# Kyton, Libitinarii
This willowy, blue-skinned figure wears robes of draped chains. Its exposed skin is pierced with lengths of razor-sharp, bloodstained icicles.
**Source** Pathfinder #137: The City Outside of Time pg. 84
**XP** 25,600

LE Medium outsider (cold, evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +29

##### Defense

**AC** 28, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 Dex, +11 natural)
**hp** 184 (16d10+96); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons and spells, silver weapons)
**Fort** +16, **Ref** +17, **Will** +13
**Defensive Abilities** icy fiend; **DR** 10/good or silver; **Immune** cold; **SR** 24

##### Offense
**Speed** 30 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 2 claws +22 (2d6+6 plus 2d6 cold), 2 chains +22 (1d8+6)
**Ranged** 4 icicles +23 (1d8+6/19–20/×3 plus 2d6 cold)
**Special Attacks** perfect _[[universal monster rules/Freeze|freeze]]_, unnerving _[[universal monster rules/Gaze|gaze]]_ (30 ft., DC 21)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +16)
Constant—_air walk_ 
At will—_[[spells/Plane Shift|plane shift]]_ (from Material Plane to _[[items/Armor Magic Abilities/Shadow|Shadow]]_ Plane only, self only) 
3/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 18), _[[spells/Dimension Door|dimension door]]_, _[[spells/Ice Storm|ice storm]]_ 
1/day—_[[spells/Polar Ray|polar ray]]_

##### Statistics
**Str** 23, **Dex** 24, **Con** 22, **Int** 15, **Wis** 22, **Cha** 17
**Base Atk** +16; **CMB** +22; **CMD** 39
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Improved Critical|Improved Critical]]_ (icicles), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Intimidate +22, Knowledge (local) +21, Knowledge (planes) +21, Knowledge (religion) +21, Perception +29, Sense Motive +29, Stealth +26, Survival +25
**Languages** Common, Infernal, Shadowtongue

##### Ecology

**Environment** any (_Shadow_ Plane)
**Organization** solitary, pair, or shiver (2-5)
**Treasure** standard

### Special Abilities

**Icicles (Ex)** A libitinarii can use the icicles embedded into its flesh as thrown ranged weapons, with a range increment of 20 feet. It can retrieve up to four of these icicles per round as a free action. These icicles deal piercing damage equal to 1d8 plus the libitinarii’s Strength modifier (usually +6) plus 2d6 points of cold damage; they deal triple damage on a critical hit (although the cold damage is not increased). The icicles aren’t considered magic weapons, but they are supernaturally hardened and count as adamantine for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. Once the libitinarii has retrieved icicles from its flesh, new icicles immediately form as a free action. If the libitinarii’s _regeneration_ is suppressed, it also can’t form new icicles. A libitinarii typically has 24 icicles embedded in its flesh at any time.

**Icy Fiend (Ex)** A libitinarii’s body is made from an _[[items/Weapon Magic Abilities/Unholy|unholy]]_ union of soulstuff and the icy essence of the coldest reaches of the _Shadow_ Plane. As such, the libitinarii is immune to cold, and it can treat any difficult terrain that results from magical or mundane ice as normal terrain, such as the icy terrain of the Frozen Tears, realm of the _kyton_ demagogue Inkariax.

**Perfect _Freeze_ (Su)** A libitinarii can harness the power of absolute zero and impose it upon the body of a living creature with a touch. The libitinarii can use this ability three times per day as a standard action that doesn’t provoke attacks of opportunity. If the libitinarii’s touch attack is successful, the target takes 2d6 points of cold damage and 2d6 points of evil-aligned magic damage. A successful DC 23 Fortitude saving throw halves each type of damage. Additionally, creatures that fail this saving throw must immediately attempt a DC 23 Will saving throw. Failing this second saving throw means that a creature has been frozen solid and has become a supernaturally frozen, mindless, inert _[[spells/Statue|statue]]_ and is considered _[[conditions/Petrified|petrified]]_, per _[[spells/Flesh to Stone|flesh to stone]]_ (if the creature is not made of flesh, this secondary ability has no effect). The creature can’t be turned back to flesh by casting _[[spells/Stone to Flesh|stone to flesh]]_ spell, but it can be restored via casting _[[spells/Break Enchantment|break enchantment]]_. If the creature isn’t returned to flesh after a number of hours equal to the creature’s Hit Dice, the creature dies and remains a frozen _statue_. It can be returned to life normally by casting _[[spells/Raise Dead|raise dead]]_ or similar spells. This is a cold effect. The save DCs are Constitution-based.

**Unnerving _Gaze_ (Ex)** A creature that succumbs to a libitinarii’s unnerving _gaze_ becomes _[[conditions/Staggered|staggered]]_ for 1 round as it feels itself slowly freezing from the inside out.

##### Description

Libitinariis form from the souls of cold-obsessed spellcasters, wicked taxidermists, torturers partial to using _[[spells/Frostbite|frostbite]]_ to torment their victims, and other evil beings obsessed with inflicting pain through the perfect preservation of cold. They roam the _Shadow_ Planes’ frozen reaches seeking to further their craft. Most serve Inkariax, the _kyton_ demagogue known as the White Death, who seeks to _[[spells/Preserve|preserve]]_ the fleetingness of perfection with his icy-fingered _[[spells/Grasp|grasp]]_. Indeed, the demagogue’s favored servants almost entirely consist of libitinariis.

Other libitinariis serve Doloras, the demigoddess of dispassion, detachment, and pain, who many kytons believe was the infernal patroness that released their kind from Hell eons ago. In some cases, libitinariis pay homage to both _unholy_ deities, for the two churches share more in common than not. Certainly Inkariax and his worshippers pay homage to the fell queen, and so many libitinariis consider deference to her a matter of course.

Libitinariis’ bodies seem humanoid, though their skin ranges in color from _[[items/Mundane/Powder|powder]]_ to navy blue. Their lips, ears, fingers, and toes are deep black, as if horribly frostbitten. Libitinariis often wear robes of draping chains, though most prominent on their persons are the horrific icicles that pierce their flesh. Although they are as adept at wielding _[[feats/Traditional Weapons|traditional weapons]]_ as any humanoid, they typically favor using these icicles as thrown weapons.

Libitinariis are roughly 5 feet tall and typically weight from 90 to 140 pounds.