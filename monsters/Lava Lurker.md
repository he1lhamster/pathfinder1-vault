---
cssclass: [monsters]
title1: Lava Lurker
desc_short: Spatters of magma sear everything that comes near this vaguely humanoid
  mass of endlessly melting and reforming rock.
title2: Lava Lurker
CR: 9
sources:
- name: The Emerald Spire Superdungeon
  page: 155
  link: http://paizo.com/products/btpy8yqx?Pathfinder-Module-The-Emerald-Spire-Superdungeon
XP: 6400
alignment: N
size: Medium
type: outsider
subtypes:
- elemental
- extraplanar
- fire
initiative:
  bonus: 5
senses:
  darkvision: 60
  tremorsense: 60
AC:
  AC: 22
  touch: 11
  flat_footed: 21
  components:
    dex: 1
    natural: 11
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 12
  ref: 9
  will: 4
immunities:
- electricity
- elemental traits
- fire
weaknesses:
- vulnerable to cold
- vulnerable to water
speeds:
  base: 30
  swim: 30
  swim_other: in molten rock only
attacks:
  melee:
  - - text: 2 slams +20 (1d6+8 plus burn)
      entries:
      - - damage: 1d6+8
        - effect: burn
      count: 2
      attack: slams
      bonus:
      - 20
  ranged:
  - - text: magma ball +14 (1d6+8 plus burn)
      entries:
      - - damage: 1d6+8
        - effect: burn
      attack: magma ball
      bonus:
      - 14
  special:
  - burn (1d6 fire, DC 20)
  - death throes
ability_scores:
  STR: 26
  DEX: 13
  CON: 18
  INT: 5
  WIS: 10
  CHA: 11
BAB: 12
CMB: 20
CMD: 31
feats:
- name: Combat Reflexes
- name: Deadly Aim
- name: Improved Initiative
- name: Power Attack
- name: Stand Still
- name: Weapon Focus (magma ball)
skills:
  Perception: 15
  Stealth: 16
    in magma: 20
  Swim: 31
  _racial_mods:
    Stealth:
      in magma: 4
languages:
- Ignan
ecology:
  environment: any volcano or underground
  organization: solitary, pair, or flow (3-6)
  treasure_type: incidental
special_abilities:
  Death Throes (Ex): |-
    When a lava lurker is slain, its body implodes, creating an extinguishing vacuum. All creatures within a 5-foot-radius burst take 8d6 points of cold damage (Reflex DC 20 half). In addition to the damage, every affected square is targeted by quench (CL 10th). This also targets all fire effects and magic items that create and control flame.

    If the lava lurker is killed in a pool of magma, it solidifies the rock within the area of effect, though in an active magma flow or similar natural and nearly endless supply of molten rock, cooled rock might melt again after only a few moments. The save DC is Constitution-based.
  Vulnerable to Water (Ex): If a significant amount of water- such as the contents
    of a large bucket, the liquid created by a create water spell, or a blow from
    a water elemental- strikes a lava lurker, the lava lurker must succeed at a DC
    20 Fortitude save or be staggered for 2d4 rounds. A lava lurker that is immersed
    in water is automatically staggered and must succeed at a DC 20 Fortitude save
    each round or be petrified (this DC increases by 1 on each subsequent round),
    reverting to its molten stone form once the water is gone.
desc_long: |-
  Territorial swimmers through the molten veins that crisscross the hottest depths of mortal worlds and the Elemental Plane of Earth, lava lurkers claim active magma flows and the fiery lakes within smoldering volcanoes as their homes. Most are content to stay within such burning depths, threatening only those foolish enough to wander close to such obviously deadly natural hazards. But occasionally, during volcanic eruptions or other explosive geological events, lava lurkers are forced from their comfortable homes, becoming unwilling riders on blazing rapids. While these disasters rarely threaten lava lurkers' elemental forms, they do often force the creatures into-or worse, strand them in-areas they find uncomfortably cool.

  Dull-witted lava lurkers eagerly sow fires and throw magma as they wander semi-aimlessly, doing what they can to create more comfortable surroundings or seeking other nearby warm places-like furnaces or bonfires-as they try to find their way back to active volcanic flows. They care little for non-elemental creatures, being baffled and annoyed by the shrill noises such creatures make when they're exposed to even the slightest fleck of molten rock.

  Though lava lurkers live in earth and flame, they die with a chilling inward gasp. If slain, the final surge of a lava lurker's animating fires consumes the nearby air, creating a momentary vacuum that extinguishes surrounding flames. This instantly transforms a lava lurker's body into a perfectly cool hunk of rock and often quells lesser flames nearby, if only temporarily.

---

# Lava Lurker
Spatters of magma sear everything that comes near this vaguely humanoid mass of endlessly melting and reforming rock.
**Source** The Emerald Spire Superdungeon pg. 155
**XP** 6,400

N Medium outsider (elemental, extraplanar, fire)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +15

##### Defense

**AC** 22, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+1 Dex, +11 natural)
**hp** 114 (12d10+48)
**Fort** +12, **Ref** +9, **Will** +4
**Immune** electricity, elemental traits, fire
**Weaknesses** vulnerable to cold, vulnerable to water

##### Offense
**Speed** 30 ft., swim 30 ft. (in molten rock only)
**Melee** 2 slams +20 (1d6+8 plus _[[universal monster rules/Burn|burn]]_)
**Ranged** magma ball +14 (1d6+8 plus _burn_)
**Special Attacks** _burn_ (1d6 fire, DC 20), death throes

##### Statistics
**Str** 26, **Dex** 13, **Con** 18, **Int** 5, **Wis** 10, **Cha** 11
**Base Atk** +12; **CMB** +20; **CMD** 31
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (magma ball)
**Skills** Perception +15, Stealth +16 (+20 in magma), Swim +31; **Racial Modifiers** +4 Stealth in magma
**Languages** Ignan

##### Ecology

**Environment** any volcano or underground
**Organization** solitary, pair, or flow (3–6)
**Treasure** incidental

### Special Abilities

**Death Throes (Ex)** When a _[[monsters/Lava Lurker|lava lurker]]_ is slain, its body implodes, creating an extinguishing vacuum. All creatures within a 5-foot-radius burst take 8d6 points of cold damage (Reflex DC 20 half). In addition to the damage, every affected square is targeted by _[[spells/Quench|quench]]_ (CL 10th). This also targets all fire effects and magic items that create and control flame.

If the _lava lurker_ is killed in a pool of magma, it solidifies the rock within the area of effect, though in an active magma flow or similar natural and nearly endless supply of molten rock, cooled rock might melt again after only a few moments. The save DC is Constitution-based.

**Vulnerable to Water (Ex)** If a significant amount of water— such as the contents of a large _[[items/Mundane/Bucket|bucket]]_, the liquid created by a _[[spells/Create Water|create water]]_ spell, or a blow from a water elemental— strikes a _lava lurker_, the _lava lurker_ must succeed at a DC 20 Fortitude save or be _[[conditions/Staggered|staggered]]_ for 2d4 rounds. A _lava lurker_ that is immersed in water is automatically _staggered_ and must succeed at a DC 20 Fortitude save each round or be _[[conditions/Petrified|petrified]]_ (this DC increases by 1 on each subsequent round), reverting to its molten stone form once the water is gone.

##### Description

Territorial swimmers through the molten veins that crisscross the hottest depths of mortal worlds and the Elemental Plane of Earth, lava lurkers claim active magma flows and the fiery lakes within smoldering volcanoes as their homes. Most are content to stay within such _[[items/Weapon Magic Abilities/Burning|burning]]_ depths, threatening only those foolish enough to wander close to such obviously _[[items/Weapon Magic Abilities/Deadly|deadly]]_ natural hazards. But occasionally, during _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ eruptions or other explosive geological events, lava lurkers are forced from their comfortable homes, becoming unwilling riders on blazing rapids. While these disasters rarely threaten lava lurkers’ elemental forms, they do often force the creatures into—or worse, strand them in—areas they find uncomfortably cool.

Dull-witted lava lurkers eagerly sow fires and throw magma as they wander semi-aimlessly, doing what they can to create more comfortable surroundings or seeking other nearby warm places—like furnaces or bonfires—as they try to find their way back to active _volcanic_ flows. They care little for non-elemental creatures, being baffled and annoyed by the shrill noises such creatures make when they’re exposed to even the slightest fleck of molten rock.

Though lava lurkers live in earth and flame, they die with a chilling inward gasp. If slain, the final surge of a _lava lurker_’s animating fires consumes the nearby air, creating a momentary vacuum that extinguishes surrounding flames. This instantly transforms a _lava lurker_’s body into a perfectly cool hunk of rock and often quells lesser flames nearby, if only temporarily.