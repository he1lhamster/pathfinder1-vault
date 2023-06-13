---
cssclass: [monsters]
title1: Sprite
desc_short: This lithe, diminutive creature looks like a humanoid with wispy, mothlike
  wings and long, thin ears.
title2: Sprite
CR: 1/3
sources:
- name: Bestiary 3
  page: 256
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 135
alignment: CN
size: Diminutive
type: fey
initiative:
  bonus: 3
senses:
  detect evil: true
  detect good: true
  low-light vision: true
AC:
  AC: 17
  touch: 17
  flat_footed: 14
  components:
    dex: 3
    size: 4
HP:
  HP: 3
  long: 1d6
saves:
  fort: 0
  ref: 5
  will: 2
DR:
- amount: 2
  weakness: cold iron
speeds:
  base: 15
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: short sword +0 (1d2-4/19-20)
      entries:
      - - damage: 1d2-4
          crit_range: 19-20
      attack: short sword
      bonus:
      - 0
  ranged:
  - - text: short bow +7 (1d2-4/x3)
      entries:
      - - damage: 1d2-4
          crit_multiplier: 3
      attack: short bow
      bonus:
      - 7
space: 1
reach: 0
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: daze
    source: default
    freq: At will
    DC: 10
  - name: color spray
    source: default
    freq: 1/day
    DC: 11
  sources:
  - name: default
    CL: 5
    concentration: 5
ability_scores:
  STR: 3
  DEX: 17
  CON: 10
  INT: 6
  WIS: 11
  CHA: 10
BAB: 0
CMB: -1
CMD: 5
feats:
- name: Alertness
skills:
  Escape Artist: 15
  Fly: 21
  Perception: 6
  Sense Motive: 6
  Stealth: 19
  _racial_mods:
    Escape Artist:
      _: 8
languages:
- Common
- Sylvan
special_qualities:
- luminous
ecology:
  environment: temperate forests
  organization: solitary, pair, troop (3-6), band (7-14), or tribe (15-40)
  treasure_type: standard
  treasure:
  - short sword
  - short bow with 20 arrows
  - other treasure
special_abilities:
  Luminous (Su): A sprite naturally sheds light equal to that provided by a torch.
    A sprite can control the color and intensity of the light as a swift action, reducing
    it to the dimness of a candle or even extinguishing its luminosity entirely if
    it wishes.
desc_long: |-
  Sprites gather in groups deep in forested lands, aligned to the cause of defending nature. Whole tribes of sprites deem themselves protectors of a certain person, place, or creature of importance in their lands, even if the being doesn't actually want or need protecting.

  A sprite's body is naturally luminous, although the sprite can vary the color and intensity of its body as it wishes. Shortly after death, a sprite's body simply melts away to a twinkling vapor. Sprites are among the smallest of fey, standing just over 9 inches in height and rarely weighing more than 1 or 2 pounds.

  Sprites are more primitive in many ways than most fey. They enjoy each other's company, but tend to be distrustful of other fey and assume any humanoids and any other creatures that they haven't expressly chosen to protect mean to do them ill. Even animals are generally regarded as dangerous. Much of this is due to sprites' diminutive size, which makes them popular targets for predators. As a result, a sprite's initial reaction to danger is typically to flee-it uses its spell-like abilities to delay or distract pursuers, and relies on its speed in flight and its size to allow it to escape in the end.

  While sprites themselves are relatively uncultured and savage in nature, they do have a healthy curiosity for all things magical in nature. They are particularly drawn to sites of great but latent magical power, such as the ruins of ancient temples. This curiosity makes them unusually receptive to roles as familiars as well. A 5th-level chaotic neutral spellcaster with the Improved Familiar feat can gain a sprite as a familiar.

---

# Sprite
This lithe, diminutive creature looks like a humanoid with wispy, mothlike wings and long, thin ears.
**Source** Bestiary 3 pg. 256
**XP** 135

CN Diminutive fey
**Init** +3; **Senses** _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +6

##### Defense

**AC** 17, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +4 size)
**hp** 3 (1d6)
**Fort** +0, **Ref** +5, **Will** +2
**DR** 2/cold iron

##### Offense
**Speed** 15 ft., fly 60 ft. (perfect)
**Melee** _[[items/Weapon/Short sword|short sword]]_ +0 (1d2–4/19–20)
**Ranged** short bow +7 (1d2–4/x3)
**Space** 1 ft., **Reach** 0 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +5)
Constant—_detect evil_, _detect good_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 10)
1/day—_[[spells/Color Spray|color spray]]_ (DC 11)

##### Statistics
**Str** 3, **Dex** 17, **Con** 10, **Int** 6, **Wis** 11, **Cha** 10
**Base Atk** +0; **CMB** –1; **CMD** 5
**Feats** _[[feats/Alertness|Alertness]]_
**Skills** Escape Artist +15, Fly +21, Perception +6, Sense Motive +6, Stealth +19; **Racial Modifiers** +8 Escape Artist
**Languages** Common, Sylvan
**SQ** luminous

##### Ecology

**Environment** temperate forests
**Organization** solitary, pair, troop (3–6), band (7–14), or tribe (15–40)
**Treasure** standard (_short sword_, short bow with 20 arrows, other treasure)

### Special Abilities

**Luminous (Su)** A _[[monsters/Sprite|sprite]]_ naturally sheds light equal to that provided by a _[[items/Mundane/Torch|torch]]_. A _sprite_ can control the color and intensity of the light as a swift action, reducing it to the dimness of a _[[items/Mundane/Candle|candle]]_ or even extinguishing its luminosity entirely if it wishes.

##### Description

Sprites gather in groups deep in forested lands, aligned to the cause of _[[items/Weapon Magic Abilities/Defending|defending]]_ nature. Whole tribes of sprites deem themselves protectors of a certain person, place, or creature of importance in their lands, even if the being doesn’t actually want or need protecting.

A _sprite_’s body is naturally luminous, although the _sprite_ can vary the color and intensity of its body as it wishes. Shortly after death, a _sprite_’s body simply melts away to a twinkling vapor. Sprites are among the smallest of fey, standing just over 9 inches in height and rarely weighing more than 1 or 2 pounds.

Sprites are more primitive in many ways than most fey. They enjoy each other’s company, but tend to be distrustful of other fey and assume any humanoids and any other creatures that they haven’t expressly chosen to protect mean to do them ill. Even animals are generally regarded as dangerous. Much of this is due to sprites’ diminutive size, which makes them popular targets for predators. As a result, a _sprite_’s initial reaction to danger is typically to flee—it uses its _spell-like abilities_ to delay or distract pursuers, and relies on its speed in _[[universal monster rules/Flight|flight]]_ and its size to allow it to escape in the end.

While sprites themselves are relatively uncultured and savage in nature, they do have a healthy curiosity for all things magical in nature. They are particularly drawn to sites of great but latent magical power, such as the ruins of ancient temples. This curiosity makes them unusually receptive to roles as familiars as well. A 5th-level chaotic neutral spellcaster with the _[[feats/Improved Familiar|Improved Familiar]]_ feat can gain a _sprite_ as a familiar.