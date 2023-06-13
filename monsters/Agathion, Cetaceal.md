---
cssclass: [monsters]
title1: Agathion, Cetaceal
desc_short: 'This mermaid-like creature has the torso and head of a long-haired woman
  and the lower half of a sleek killer whale. '
title2: Cetaceal
CR: 15
sources:
- name: Bestiary 2
  page: 17
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 51200
alignment: NG
size: Medium
type: outsider
subtypes:
- agathion
- aquatic
- extraplanar
- good
initiative:
  bonus: 8
senses:
  blindsense: 60
  darkvision: 60
  low-light vision: true
auras:
- name: protective aura
  radius: 20
AC:
  AC: 30
  touch: 15
  flat_footed: 25
  components:
    dex: 4
    dodge: 1
    natural: 15
    deflection vs. evil: 4
HP:
  HP: 212
  long: 17d10+119
  regeneration: 5
  regeneration_weakness: evil weapons and spells
saves:
  fort: 17
  ref: 16
  will: 9
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 10
  weakness: evil and silver
immunities:
- cold
- electricity
- petrification
resistances:
  sonic: 10
SR: 26
speeds:
  base: 10
  swim: 80
attacks:
  melee:
  - - text: +1 shocking burst shortspear +28/+23/+18/+13 (1d6+14 plus 1d6 electricity)
      entries:
      - - damage: 1d6+14
        - damage: 1d6
          type: electricity
      attack: +1 shocking burst shortspear
      bonus:
      - 28
      - 23
      - 18
      - 13
    - text: tail slap +22 (1d6+4 plus push and stun)
      entries:
      - - damage: 1d6+4
        - effect: push
        - effect: stun
      attack: tail slap
      bonus:
      - 22
  special:
  - shockwave
  - push (tail slap, 10 ft.)
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: light
    source: default
    freq: At will
  - name: lightning bolt
    source: default
    freq: At will
    DC: 16
  - name: hold monster
    source: default
    freq: At will
    DC: 18
  - name: message
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: break enchantment
    source: default
    freq: 7/day
  - name: cure serious wounds
    source: default
    freq: 7/day
  - name: neutralize poison
    source: default
    freq: 7/day
  - name: remove disease
    source: default
    freq: 7/day
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 18
  - name: cure critical wounds
    source: default
    freq: 3/day
  - name: greater restoration
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 3/day
  - name: awaken
    source: default
    freq: 1/day
  - name: summon monster VIII
    source: default
    freq: 1/day
    other: water elementals only
  sources:
  - name: default
    CL: 15
    concentration: 18
ability_scores:
  STR: 29
  DEX: 19
  CON: 24
  INT: 14
  WIS: 18
  CHA: 17
BAB: 17
CMB: 26
CMD: 41
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
- name: Spell Penetration
- name: Weapon Focus (shortspear)
- name: Weapon Focus (tail slap)
- name: Wind Stance
skills:
  Diplomacy: 12
  Handle Animal: 14
  Heal: 21
  Knowledge (arcana): 22
  Knowledge (nature): 19
  Knowledge (planes): 22
  Perception: 28
  Sense Motive: 24
  Stealth: 24
  Swim: 17
  _racial_mods:
    Perception:
      _: 4
languages:
- Celestial
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- amphibious
- lay on hands (8d6, 11/day, as a 17th-level paladin)
ecology:
  environment: any water (Nirvana)
  organization: solitary, pair, or pod (3-6)
  treasure_type: double
  treasure:
  - +1 shocking burst shortspear
  - other treasure
special_abilities:
  Protective Aura (Su): Against attacks made or effects created by evil creatures,
    this ability provides a +4 deflection bonus to AC and a +4 resistance bonus on
    saving throws to anyone within 20 feet of the cetaceal. Otherwise, it functions
    as a magic circle against evil effect and a lesser globe of invulnerability, both
    with a radius of 20 feet (caster level equals cetaceal's HD). The defensive benefits
    from the circle are not included in the above stat block.
  Shockwave (Su): Once per day, a cetaceal can release a 100-foot-radius burst of
    energy. All creatures in the area take 17d6 damage; half of this damage is cold,
    and half is electricity (DC 25 Reflex save halves). The save DC is Constitution-based.
  Stun (Ex): Any creature moved by a cetaceal's push attack must make a DC 25 Fortitude
    saving throw or be stunned for 1 round. The DC is Constitution-based.
desc_long: |-
  Cetaceals are great water-dwelling agathions who swim the planar seas and commune with the creatures of the deeps. Rarely seen by landwalkers, they defend the waters against aquatic evils such as aboleths. Their spirits usually were those of great mortal leaders of aquatic or coastal tribes, or good folk who died underwater serving some great cause, reborn in a celestial form that is part humanoid, part orca. They are social beings and develop close friendships with other celestials and marine creatures. 

  A cetaceal is 8 feet long and weighs 400 pounds, although some grow quite a bit larger than that.

---

# Agathion, Cetaceal
This mermaid-like creature has the torso and head of a long-haired woman and the lower half of a sleek killer _[[monsters/Whale|whale]]_.

**Source** Bestiary 2 pg. 17
**XP** 51,200

NG Medium outsider (agathion, aquatic, extraplanar, good)
**Init** +8; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +28
**Aura** protective aura (20 ft.)

##### Defense

**AC** 30, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +15 natural; +4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 212 (17d10+119); _[[universal monster rules/Regeneration|regeneration]]_ 5 (evil weapons and spells)
**Fort** +17, **Ref** +16, **Will** +9; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 10/evil and silver; **Immune** cold, electricity, petrification; **Resist** sonic 10; **SR** 26

##### Offense
**Speed** 10 ft., swim 80 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Shocking Burst|shocking burst]]_ _[[items/Weapon/Shortspear|shortspear]]_ +28/+23/+18/+13 (1d6+14 plus 1d6 electricity), tail slap +22 (1d6+4 plus push and stun)
**Special Attacks** shockwave, push (tail slap, 10 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
Constant—_[[spells/Speak with Animals|speak with animals]]_ 
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), light, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 16), _[[spells/Hold Monster|hold monster]]_ (DC 18), _[[spells/Message|message]]_, greater teleport (self plus 50 lbs. of objects only) 
7/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Disease|remove disease]]_ 
3/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 18), _[[spells/Cure Critical Wounds|cure critical wounds]]_, greater _[[spells/Restoration|restoration]]_, _[[spells/Heal|heal]]_ 
1/day—_[[spells/Awaken|awaken]]_, _[[spells/Summon Monster VIII|summon monster VIII]]_ (water elementals only)

##### Statistics
**Str** 29, **Dex** 19, **Con** 24, **Int** 14, **Wis** 18, **Cha** 17
**Base Atk** +17; **CMB** +26; **CMD** 41 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_shortspear_, tail slap), _[[feats/Wind Stance|Wind Stance]]_
**Skills** Diplomacy +12, Handle Animal +14, _Heal_ +21, Knowledge (arcana) +22, Knowledge (nature) +19, Knowledge (planes) +22, Perception +28, Sense Motive +24, Stealth +24, Swim +17; **Racial Modifiers** +4 Perception
**Languages** Celestial, Draconic, Infernal; _speak with animals_, truespeech
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, lay on hands (8d6, 11/day, as a 17th-level _[[classes/Paladin|paladin]]_)

##### Ecology

**Environment** any water (Nirvana)
**Organization** solitary, pair, or pod (3–6)
**Treasure** double (+1 _shocking burst_ _shortspear_, other treasure)

### Special Abilities

**Protective Aura (Su)** Against attacks made or effects created by evil creatures, this ability provides a +4 _deflection_ bonus to AC and a +4 _resistance_ bonus on saving throws to anyone within 20 feet of the cetaceal. Otherwise, it functions as a _[[spells/Magic Circle against Evil|magic circle against evil]]_ effect and a lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, both with a radius of 20 feet (caster level equals cetaceal’s HD). The defensive benefits from the circle are not included in the above stat block.
**Shockwave (Su)** Once per day, a cetaceal can release a 100-foot-radius burst of energy. All creatures in the area take 17d6 damage; half of this damage is cold, and half is electricity (DC 25 Reflex save halves). The save DC is Constitution-based.
**Stun (Ex) **Any creature moved by a cetaceal’s push attack must make a DC 25 Fortitude saving throw or be _[[conditions/Stunned|stunned]]_ for 1 round. The DC is Constitution-based.

##### Description

Cetaceals are great water-dwelling agathions who swim the _[[items/Weapon Magic Abilities/Planar|planar]]_ seas and _[[spells/Commune|commune]]_ with the creatures of the deeps. Rarely seen by landwalkers, they defend the waters against aquatic evils such as aboleths. Their spirits usually were those of great mortal leaders of aquatic or coastal tribes, or good folk who died _[[items/Weapon Magic Abilities/Underwater|underwater]]_ serving some great cause, reborn in a celestial form that is part humanoid, part orca. They are social beings and develop close friendships with other celestials and marine creatures.

A cetaceal is 8 feet long and weighs 400 pounds, although some grow quite a bit larger than that.