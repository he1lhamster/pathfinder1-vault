---
cssclass: [monsters]
title1: Hollow Serpent
desc_short: An unseen breeze stirs the desiccated scales of this immense snakeskin,
  causing the shedding's frayed, dried edges to flutter with a semblance of life.
  Pinpoints of unholy green light flare behind the intact eye lenses as the head starts
  to rise. The same glow behind those long-dead eyes illuminates a gaping mouth and
  bony fangs. Then a terrifying, painful hiss assaults your mind as the serpent slithers
  forward with a silent, unearthly grace.
title2: Hollow Serpent
CR: 16
sources:
- name: 'Pathfinder #42: Sanctum of the Serpent God'
  page: 86
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/serpentsSkull/v5748btpy8ihw
- name: Bestiary 3
  page: 149
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 76800
alignment: NE
size: Large
type: undead
subtypes:
- reptilian
initiative:
  bonus: 9
senses:
  darkvision: 60
  lifesense: true
auras:
- name: desiccation
  radius: 30
  other:
  - 1d4 Cha damage
  DC: 26
  DC_type: Fort
AC:
  AC: 31
  touch: 19
  flat_footed: 21
  components:
    dex: 9
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 230
  long: 20d8+140
  fast_healing: 10
saves:
  fort: 14
  ref: 17
  will: 18
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: magic and silver
immunities:
- undead traits
SR: 27
speeds:
  base: 50
  climb: 50
attacks:
  melee:
  - - text: bite +23 (4d10+10 plus grab)
      entries:
      - - damage: 4d10+10
        - effect: grab
      attack: bite
      bonus:
      - 23
  special:
  - channel negative energy (8d6, DC 24, 9/day)
  - constrict (4d10+10 plus energy drain)
  - dissonant hiss
  - energy drain (1 level, DC 26)
  - life-stealing coils
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 24
  - name: waves of exhaustion
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 22
ability_scores:
  STR: 25
  DEX: 29
  CON:
  INT: 6
  WIS: 19
  CHA: 22
BAB: 15
CMB: 25
CMB_other: +29 grapple
CMD: 43
CMD_other: can't be tripped
feats:
- name: Agile Maneuvers
- name: Channel Smite
- name: Dodge
- name: Great Fortitude
- name: Iron Will
- name: Lightning Reflexes
- name: Lunge
- name: Toughness
- name: Vital Strike
- name: Weapon Finesse
skills:
  Climb: 28
  Escape Artist: 19
  Perception: 17
  Stealth: 18
languages:
- Aklo
- telepathy 100 ft.
ecology:
  environment: underground
  organization: solitary, pair, or nest (3-8)
  treasure:
  - double standard
special_abilities:
  Channel Negative Energy (Su): As a standard action, a hollow serpent can channel
    negative energy in a 30-foot burst just like a 16th-level cleric of an evil deity.
    This ability requires no divine focus. The save DC is Charisma-based.
  Desiccation Aura (Su): A cloud of negatively charged dust fills the air in a 30-foot
    radius around the body of a hollow serpent, causing living creatures within the
    area to make a DC 26 Fortitude save or take 1d6 points of Charisma damage. Whether
    or not the save is successful, a creature cannot be affected again by the same
    hollow serpent's desiccation aura for 24 hours. The save DC is Constitution-based.
  Life-Draining Coils (Su): A hollow serpent seethes with negative energy capable
    of draining the life force of creatures trapped within its coils. While holding
    such victims, the hollow serpent's constrict ability bestows one negative level
    per round. The hollow serpent also gains 5 temporary hit points for each negative
    level it bestows.
  Lifesense (Su): A hollow serpent notices and locates living creatures within 60
    feet, just as if it possessed the blindsight ability.
desc_long: |-
  Among the many manifestations of serpentfolk faith, the hollow serpent represents one of the most horrific harbingers of doom. Serpentfolk legend suggests Ydersius created the first hollow serpents as protectors and guardians for their underground enclaves. But serpentfolk priests soon learned how to make more, worshiping and cultivating the skin sheddings of monstrously giant snakes with rituals to turn them into engines of destruction. Capable of laying waste to entire regions, the hollow serpents used their life-draining coils to slay the enemies of the serpentfolk, proving particularly effective against the Azlanti empire in the early years of the serpentfolk's age-long struggle against humanity. Eventually, however, the Azlanti learned to combat these skins with positive energy and fire. With the retreat of the mighty snake-god and his people into the shadows of the Darklands, serpentfolk priests have hoarded the most potent of these defenders as guardians of the hibernation chambers of the serpentfolk elite.

  A typical hollow serpent measures a little over 15 feet long and weighs 500 pounds. A lesser hollow serpent is 7 feet long and weighs just 90 pounds.

---

# Hollow Serpent
An _[[items/Weapon Magic Abilities/Unseen|unseen]]_ _[[spells/Breeze|breeze]]_ stirs the desiccated scales of this immense snakeskin, causing the shedding’s frayed, dried edges to flutter with a semblance of life. Pinpoints of _[[items/Weapon Magic Abilities/Unholy|unholy]]_ green light _[[spells/Flare|flare]]_ behind the intact eye lenses as the head starts to rise. The same glow behind those long-dead eyes illuminates a gaping mouth and bony fangs. Then a terrifying, painful hiss assaults your mind as the serpent slithers forward with a silent, unearthly _[[spells/Grace|grace]]_.
**Source** Pathfinder #42: Sanctum of the Serpent God pg. 86, Bestiary 3 pg. 149
**XP** 76,800

NE Large undead (reptilian)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +17
**Aura** desiccation (30 ft., 1d4 Cha damage, Fort DC 26 negates)

##### Defense

**AC** 31, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+9 Dex, +1 dodge, +12 natural, -1 size)
**hp** 230 (20d8+140); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +14, **Ref** +17, **Will** +18
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/magic and silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 27

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** bite +23 (4d10+10 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy (8d6, DC 24, 9/day), _[[universal monster rules/Constrict|constrict]]_ (4d10+10 plus _[[universal monster rules/Energy Drain|energy drain]]_), dissonant hiss, _energy drain_ (1 level, DC 26), life-stealing coils
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +22)
Constant - _[[spells/Deathwatch|deathwatch]]_, _[[spells/Freedom of Movement|freedom of movement]]_
1/day - _[[spells/Horrid Wilting|horrid wilting]]_ (DC 24), _[[spells/Waves of Exhaustion|waves of exhaustion]]_

##### Statistics
**Str** 25, **Dex** 29, **Con** —, **Int** 6, **Wis** 19, **Cha** 22
**Base Atk** +15; **CMB** +25 (+29 grapple); **CMD** 43 (can't be tripped)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Channel Smite|Channel Smite]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _Climb_ +28, Escape Artist +19, Perception +17, Stealth +18
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** underground
**Organization** solitary, pair, or nest (3-8)
**Treasure** double standard

### Special Abilities

**Channel Negative Energy (Su)** As a standard action, a _[[monsters/Hollow Serpent|hollow serpent]]_ can channel negative energy in a 30-foot burst just like a 16th-level _[[classes/Cleric|cleric]]_ of an evil deity. This ability requires no divine focus. The save DC is Charisma-based.

**Desiccation Aura (Su)** A cloud of negatively charged dust fills the air in a 30-foot radius around the body of a _hollow serpent_, causing living creatures within the area to make a DC 26 Fortitude save or take 1d6 points of Charisma damage. Whether or not the save is successful, a creature cannot be affected again by the same _hollow serpent_’s desiccation aura for 24 hours. The save DC is Constitution-based.

**Life-Draining Coils (Su)** A _hollow serpent_ seethes with negative energy capable of draining the life force of creatures trapped within its coils. While holding such victims, the _hollow serpent_’s _constrict_ ability bestows one negative level per round. The _hollow serpent_ also gains 5 temporary hit points for each negative level it bestows.

**_Lifesense_ (Su)** A _hollow serpent_ notices and locates living creatures within 60 feet, just as if it possessed the _[[universal monster rules/Blindsight|blindsight]]_ ability.

##### Description

Among the many manifestations of _[[monsters/Serpentfolk|serpentfolk]]_ faith, the _hollow serpent_ represents one of the most horrific harbingers of _[[spells/Doom|doom]]_. _Serpentfolk_ legend suggests Ydersius created the first hollow serpents as protectors and guardians for their underground enclaves. But _serpentfolk_ priests soon learned how to make more, worshiping and cultivating the skin sheddings of monstrously giant snakes with rituals to turn them into engines of _[[spells/Destruction|destruction]]_. Capable of laying waste to entire regions, the hollow serpents used their life-draining coils to slay the enemies of the _serpentfolk_, proving particularly effective against the Azlanti empire in the early years of the _serpentfolk_’s age-long struggle against humanity. Eventually, however, the Azlanti learned to combat these skins with positive energy and fire. With the retreat of the mighty snake-god and his people into the shadows of the Darklands, _serpentfolk_ priests have hoarded the most _[[items/Weapon Magic Abilities/Potent|potent]]_ of these defenders as guardians of the hibernation chambers of the _serpentfolk_ elite.

A typical _hollow serpent_ measures a little over 15 feet long and weighs 500 pounds. A lesser _hollow serpent_ is 7 feet long and weighs just 90 pounds.