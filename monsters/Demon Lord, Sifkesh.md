---
cssclass: [monsters]
title1: Demon Lord, Sifkesh
desc_short: This gaunt woman has blood-soaked hair, eyes and lips stitched shut with
  wire, and severed limbs that float nearby as if they were still attached.
title2: Sifkesh
CR: 28
sources:
- name: "Pathfinder #75: Demon's Heresy"
  page: 86
  link: http://paizo.com/products/btpy91dm?Pathfinder-Adventure-Path-75-Demons-Heresy
XP: 4915200
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 12
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 38
- name: unholy aura
  radius: 20
  DC: 31
AC:
  AC: 49
  touch: 43
  flat_footed: 36
  components:
    deflection: 4
    dex: 12
    dodge: 1
    natural: 6
    profane: 16
HP:
  HP: 666
  long: 31d10+496
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 30
  ref: 33
  will: 30
defensive_abilities:
- critical healing
- freedom of movement
- heretical
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage and drain
- bleed
- charm and compulsion effects
- death effects
- electricity
- energy drain
- petrification
- poison
- slashing weapons
resistances:
  acid: 30
  cold: 30
  fire: 30
SR: 39
speeds:
  base: 30
  fly: 120
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +5 unholy speed war razor +47/+42/+37/+32 (1d4+27/19-20)
      entries:
      - - damage: 1d4+27
          crit_range: 19-20
      attack: +5 unholy speed war razor
      bonus:
      - 47
      - 42
      - 37
      - 32
    - text: claw +42 (4d6+27/19-20 plus 1d4 Cha drain)
      entries:
      - - damage: 4d6+27
          crit_range: 19-20
        - damage: 1d4
          type: Cha drain
      attack: claw
      bonus:
      - 42
  special:
  - Charisma drain
  - despairing cry
  - precise cuts
  - suicide
space: 5
reach: 30
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: At will
    DC: 30
  - name: crushing despair
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
  - name: telekinesis
    source: default
    freq: At will
    DC: 28
  - name: shapechange
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 26
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 27
  - name: demand
    source: default
    freq: 3/day
    DC: 31
  - name: quickened dominate person
    source: default
    freq: 3/day
    DC: 28
  - name: quickened suggestion
    source: default
    freq: 3/day
    DC: 26
  - name: summon demons
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: symbol of strife
    source: default
    freq: 3/day
    DC: 32
  - name: sympathy
    source: default
    freq: 1/day
    DC: 31
  - name: time stop
    source: default
    freq: 1/day
  - name: weird
    source: default
    freq: 1/day
    DC: 32
  sources:
  - name: default
    CL: 28
    concentration: 41
ability_scores:
  STR: 32
  DEX: 35
  CON: 42
  INT: 33
  WIS: 29
  CHA: 36
BAB: 31
CMB: 42
CMD: 85
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Dodge
- name: Improved Critical (war razor)
- name: Improved Critical (claw)
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (dominate person)
- name: Quicken Spell-Like Ability (suggestion)
- name: Spring Attack
- name: Staggering Critical
- name: Whirlwind Attack
skills:
  Acrobatics: 46
  Bluff: 47
  Diplomacy: 47
  Fly: 54
  Intimidate: 44
  Knowledge (arcana): 42
  Knowledge (engineering): 42
  Knowledge (history): 42
  Knowledge (local): 42
  Knowledge (nobility): 45
  Knowledge (planes): 45
  Knowledge (religion): 42
  Perception: 51
  Sense Motive: 43
  Spellcraft: 45
  Stealth: 46
  Use Magic Device: 44
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal (can't speak)
- Celestial (can't speak)
- Common (can't speak)
- telepathy 300 ft.
special_qualities:
- demon lord traits
- detached limbs
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - +5 unholy speed war razor
  - other treasure
special_abilities:
  Charisma Drain (Su): Sifkesh's claw leaves hideous scars that resist healing even
    via magic; these scars manifest as Charisma drain. The more scars a victim gains
    in this manner, the more despondent and depressed its personality grows. A creature
    whose Charisma score is drained to 3 or lower by this attack automatically fails
    any Will save against any spell-like ability or supernatural attack made by Sifkesh.
    A successful DC 41 Will save resists the Charisma drain inflicted by this attack,
    and instead causes the victim to be sickened for 1 round. The save DC is Charisma-based.
  Critical Healing (Ex): Critical hits cause Sifkesh to experience a sudden rush of
    energy and healing. Any additional damage dealt to Sifkesh by a critical hit actually
    heals her of that amount of damage rather than harming her. This damage applies
    simultaneously to the attack's normal damage, and can prevent her from being slain
    if the damage from the normal attack would otherwise have been enough to kill
    her. Sifkesh takes no damage at all (but neither does she gain healing) from critical
    hits she or her allies deal to her-only attempts to actually damage her can heal
    her in this way. Whenever Sifkesh is healed of any damage in this manner, she
    becomes hasted for 1 round. Sifkesh takes normal damage from sneak attacks and
    other precision-based damage.
  Despairing Cry (Su): Once every 1d4 rounds as a swift action, Sifkesh can unleash
    a soul-rending mournful scream that affects all creatures in a 60-foot-radius
    spread. A creature in this area must attempt a successful DC 38 Will save or be
    overcome by suicidal despair-on a successful save, a creature is merely sickened
    for 1d4 rounds. A creature fully affected by this special attack takes a -6 penalty
    on attack rolls, saving throws, ability checks, skill checks, and weapon damage
    rolls, and cannot gain the benefit of any morale bonus for 24 hours. A creature
    that is normally immune to fear loses that ability while under the effects of
    despairing cry, and can be ordered to take obviously suicidal acts while under
    the influence of effects like charm person, dominate person, and suggestion. The
    effects of multiple despairing cries do not stack. This is a mindaffecting sonic
    curse effect. The save DC is Charisma-based.
  Detached Limbs (Su): Sifkesh's arms, legs, and head are not physically attached
    to her torso. Instead, they float in approximately the positions they would normally
    take up, but never quite perfectly aligned. She is immune to any effect that severs
    limbs or her head. In addition, when she attacks, her limbs can move with surprising
    speed, effectively granting her exceptional reach for a Medium creature.
  Heretical (Ex): Sifkesh's heretical persona protects her from servants of faith.
    Against any spell cast by a divine spellcaster, her Spell Resistance increases
    to 41, and she gains a +2 bonus on all saving throws against such spells. A divine
    spellcaster who willingly touches Sifkesh must succeed at a DC 38 Will save or
    be nauseated for 1d4 rounds. The save DC is Charisma-based.
  Immune to Edged Weapons (Ex): Sifkesh is immune to all forms of slashing damage
    and bleed effects.
  Precise Cuts (Ex): Sifkesh deals an amount of additional damage equal to her Intelligence
    bonus on any successful attack that deals slashing damage.
  Suicide (Su): Once per day as an immediate action, Sifkesh can drop her defenses
    when attacked by a foe. She is treated as flat-footed for this attack, loses her
    profane bonus to her AC and spell resistance, and automatically fails any saving
    throws against that attack. If this attack kills her, she immediately utters her
    despairing cry (even if she's already used it within the previous 1d4 rounds).
    Any creatures affected by this particular despairing cry are also stunned for
    1d4 rounds. One round after she commits suicide, Sifkesh automatically comes back
    to life, as if affected by true resurrection.
desc_long: |-
  Sifkesh, the Sacred Whore, is the demon lord of suicide, heresy, and hopeless despair. She rules the Abyssal realm of Vantian, the legendary City of Open Windows. The city itself is constantly destroying itself, as its buildings continually plummet into the churning surf along an eternally crumbling coastline.

  Sifkesh is among the most enigmatic of all demon lords, for she seems more diabolic or even daemonic in her personality and appearance. Planar scholars have long struggled to interpret the demon lord's position and power. The belief that Sif kesh rose from the animus of a heretical erinyes who became the first of Hell's heretics is correct, and she constantly works to seduce and lure additional powerful devils from their infernal roles, inviting some to join her as favored minions but leaving others in place so they can more easily work to subvert Hell's machinations.

---

# Demon Lord, Sifkesh
This gaunt woman has blood-soaked hair, eyes and lips stitched shut with _[[items/Mundane/Wire|wire]]_, and severed limbs that float nearby as if they were still attached.
**Source** Pathfinder #75: Demon's Heresy pg. 86
**XP** 4,915,200
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +51
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 38), _[[spells/Unholy Aura|unholy aura]]_ (20 ft., DC 31)

##### Defense

**AC** 49, touch 43, _[[conditions/Flat-Footed|flat-footed]]_ 36 (+4 _[[spells/Deflection|deflection]]_, +12 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural, +16 profane)
**hp** 666 (31d10+496); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +30, **Ref** +33, **Will** +30
**Defensive Abilities** critical healing, _[[spells/Freedom of Movement|freedom of movement]]_, _[[items/Weapon Magic Abilities/Heretical|heretical]]_; **DR** 20/cold iron, epic, and good; **Immune** _[[universal monster rules/Ability Damage and Drain|ability damage and drain]]_, _[[universal monster rules/Bleed|bleed]]_, charm and compulsion effects, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification, poison, slashing weapons; **Resist** acid 30, cold 30, fire 30; **SR** 39

##### Offense
**Speed** 30 ft., fly 120 ft. (perfect)
**Melee** +5 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ speed _[[items/Weapon/War razor|war razor]]_ +47/+42/+37/+32 (1d4+27/19–20), claw +42 (4d6+27/19–20 plus 1d4 Cha drain)
**Space** 5 ft., **Reach** 30 ft.
**Special Attacks** Charisma drain, despairing cry, precise cuts, suicide
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 28th; concentration +41)
Constant—_detect good_, _detect law_, _freedom of movement_, _true seeing_, _unholy aura_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_ (DC 30), _[[spells/Crushing Despair|crushing despair]]_ (DC 27), _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Telekinesis|telekinesis]]_ (DC 28), _[[spells/Shapechange|shapechange]]_, _[[spells/Suggestion|suggestion]]_ (DC 26), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 27)
3/day—_[[spells/Demand|demand]]_ (DC 31), quickened _[[spells/Dominate Person|dominate person]]_ (DC 28), quickened _suggestion_ (DC 26), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol of Strife|symbol of strife]]_ (DC 32)
1/day—_[[spells/Sympathy|sympathy]]_ (DC 31), _[[spells/Time Stop|time stop]]_, _[[spells/Weird|weird]]_ (DC 32)

##### Statistics
**Str** 32, **Dex** 35, **Con** 42, **Int** 33, **Wis** 29, **Cha** 36
**Base Atk** +31; **CMB** +42; **CMD** 85 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_war razor_), _Improved Critical_ (claw), _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_, _suggestion_), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +46, Bluff +47, Diplomacy +47, Fly +54, Intimidate +44, Knowledge (arcana) +42, Knowledge (engineering) +42, Knowledge (history) +42, Knowledge (local) +42, Knowledge (nobility) +45, Knowledge (planes) +45, Knowledge (religion) +42, Perception +51, Sense Motive +43, Spellcraft +45, Stealth +46, Use Magic Device +44; **Racial Modifiers** +8 Perception
**Languages** Abyssal (can’t speak), Celestial (can’t speak), Common (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** demon lord traits, detached limbs

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple (+5 _unholy_ speed _war razor_, other treasure)

### Special Abilities

**Charisma Drain (Su)** Sifkesh’s claw leaves hideous scars that resist healing even via magic; these scars manifest as Charisma drain. The more scars a victim gains in this manner, the more despondent and depressed its personality grows. A creature whose Charisma score is drained to 3 or lower by this attack automatically fails any Will save against any spell-like ability or supernatural attack made by Sifkesh. A successful DC 41 Will save resists the Charisma drain inflicted by this attack, and instead causes the victim to be _[[conditions/Sickened|sickened]]_ for 1 round. The save DC is Charisma-based.

**Critical Healing (Ex)** Critical hits cause Sifkesh to experience a sudden rush of energy and healing. Any additional damage dealt to Sifkesh by a critical hit actually heals her of that amount of damage rather than harming her. This damage applies simultaneously to the attack’s normal damage, and can prevent her from being slain if the damage from the normal attack would otherwise have been enough to kill her. Sifkesh takes no damage at all (but neither does she gain healing) from critical hits she or her allies deal to her—only attempts to actually damage her can _[[spells/Heal|heal]]_ her in this way. Whenever Sifkesh is healed of any damage in this manner, she becomes hasted for 1 round. Sifkesh takes normal damage from sneak attacks and other precision-based damage.

**Despairing Cry (Su)** Once every 1d4 rounds as a swift action, Sifkesh can unleash a soul-rending mournful scream that affects all creatures in a 60-foot-radius spread. A creature in this area must attempt a successful DC 38 Will save or be overcome by suicidal despair—on a successful save, a creature is merely _sickened_ for 1d4 rounds. A creature fully affected by this special attack takes a –6 penalty on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls, and cannot gain the benefit of any morale bonus for 24 hours. A creature that is normally immune to _[[universal monster rules/Fear|fear]]_ loses that ability while under the effects of despairing cry, and can be ordered to take obviously suicidal acts while under the influence of effects like _[[spells/Charm Person|charm person]]_, _dominate person_, and _suggestion_. The effects of multiple despairing cries do not stack. This is a mindaffecting sonic curse effect. The save DC is Charisma-based.

**Detached Limbs (Su)** Sifkesh’s arms, legs, and head are not physically attached to her torso. Instead, they float in approximately the positions they would normally take up, but never quite perfectly aligned. She is immune to any effect that severs limbs or her head. In addition, when she attacks, her limbs can move with surprising speed, effectively granting her exceptional reach for a _Medium_ creature.

**_Heretical_ (Ex)** Sifkesh’s _heretical_ persona protects her from servants of faith. Against any spell cast by a divine spellcaster, her _[[universal monster rules/Spell Resistance|Spell Resistance]]_ increases to 41, and she gains a +2 bonus on all saving throws against such spells. A divine spellcaster who willingly touches Sifkesh must succeed at a DC 38 Will save or be _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds. The save DC is Charisma-based.

**Immune to Edged Weapons (Ex)** Sifkesh is immune to all forms of slashing damage and _bleed_ effects.

**Precise Cuts (Ex)** Sifkesh deals an amount of additional damage equal to her Intelligence bonus on any successful attack that deals slashing damage.
**Suicide (Su)** Once per day as an immediate action, Sifkesh can drop her defenses when attacked by a foe. She is treated as _flat-footed_ for this attack, loses her profane bonus to her AC and _spell resistance_, and automatically fails any saving throws against that attack. If this attack kills her, she immediately utters her despairing cry (even if she’s already used it within the previous 1d4 rounds). Any creatures affected by this particular despairing cry are also _[[conditions/Stunned|stunned]]_ for 1d4 rounds. One round after she commits suicide, Sifkesh automatically comes back to life, as if affected by _[[spells/True Resurrection|true resurrection]]_.

##### Description

Sifkesh, the _[[items/Weapon Magic Abilities/Sacred|Sacred]]_ Whore, is the demon lord of suicide, heresy, and hopeless despair. She rules the Abyssal realm of Vantian, the legendary City of Open Windows. The city itself is constantly destroying itself, as its buildings continually plummet into the churning surf along an eternally crumbling coastline.

Sifkesh is among the most enigmatic of all demon lords, for she seems more diabolic or even daemonic in her personality and appearance. _[[items/Weapon Magic Abilities/Planar|Planar]]_ scholars have long struggled to interpret the demon lord’s position and power. The belief that Sif kesh rose from the animus of a _heretical_ erinyes who became the first of Hell’s heretics is correct, and she constantly works to seduce and lure additional powerful devils from their infernal roles, inviting some to join her as favored minions but leaving others in place so they can more easily work to subvert Hell’s machinations.