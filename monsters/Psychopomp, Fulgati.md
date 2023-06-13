---
cssclass: [monsters]
title1: Psychopomp, Fulgati
desc_short: This towering, muscular, female figure wears an iron, ram-headed mask.
  Four stout arms crackle with primal energies, while four additional arms emerge
  from her hips, supporting her bulk in place of legs.
title2: Fulgati
CR: 18
sources:
- name: Concordance of Rivals
  page: 60
  link: https://paizo.com/products/btq01x4d?Pathfinder-Campaign-Setting-Concordance-of-Rivals
XP: 153600
alignment: N
size: Colossal
type: outsider
subtypes:
- extraplanar
- psychopomp
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  spiritsense: true
  true seeing: true
auras:
- name: calamity
  radius: 300
AC:
  AC: 32
  touch: 5
  flat_footed: 29
  components:
    dex: 3
    natural: 27
    size: -8
HP:
  HP: 312
  long: 25d10+175
  regeneration: 10
  regeneration_weakness: artifacts, epic, or mythic
saves:
  fort: 21
  ref: 11
  will: 20
defensive_abilities:
- poisonous blood
DR:
- amount: 10
  weakness: adamantine
immunities:
- cold
- death effects
- disease
- electricity
- poison
resistances:
  fire: 15
  sonic: 15
SR: 29
speeds:
  base: 50
  other_semicolon: air walk
  burrow: 20
  climb: 50
attacks:
  melee:
  - - text: gore +31 (3d6+14/19-20)
      entries:
      - - damage: 3d6+14
          crit_range: 19-20
      attack: gore
      bonus:
      - 31
    - text: 4 slams +31 (2d6+14)
      entries:
      - - damage: 2d6+14
      count: 4
      attack: slams
      bonus:
      - 31
  ranged:
  - - text: rock +29 (4d6+14)
      entries:
      - - damage: 4d6+14
      attack: rock
      bonus:
      - 29
  special:
  - rend (2 slams, 2d8+21)
  - rock throwing (240 ft.)
space: 30
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: align weapon
    source: default
    freq: 3/day
    other: self only
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 21
  - name: greater shout
    source: default
    freq: 3/day
    DC: 20
  - name: plane shift
    source: default
    freq: 3/day
    DC: 21
  - name: undeath to death
    source: default
    freq: 3/day
    DC: 19
  - name: control water
    source: default
    freq: 1/day
  - name: control weather
    source: default
    freq: 1/day
  - name: creeping doom
    source: default
    freq: 1/day
    DC: 20
  - name: earthquake
    source: default
    freq: 1/day
  - name: epidemic
    source: default
    freq: 1/day
  - name: incendiary cloud
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 25
    concentration: 28
ability_scores:
  STR: 39
  DEX: 16
  CON: 24
  INT: 7
  WIS: 19
  CHA: 16
BAB: 25
CMB: 47
CMB_other: +51 bull rush, sunder
CMD: 60
CMD_other: 62 vs. bull rush or sunder, 64 vs. trip
feats:
- name: Awesome Blow
- name: Cleave
- name: Greater Bull Rush
- name: Greater Sunder
- name: Improved Bull Rush
- name: Improved Critical (gore)
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- name: Spell Focus (conjuration)
- name: Spell Focus (evocation)
- name: Sundering Strike
skills:
  Acrobatics: 3
    when jumping: 11
  Climb: 22
  Intimidate: 31
  Perception: 32
  Sense Motive: 32
  Survival: 32
languages:
- Abyssal
- Celestial
- Infernal
special_qualities:
- paramnesia
- spirit touch
ecology:
  environment: any (Boneyard)
  organization: solitary
  treasure_type: none
special_abilities:
  Aura of Calamity (Ex): 'A fulgati's presence warps probability and makes tragedy
    more likely. Any result of a natural 1 on a d20 roll within 300 feet of a fulgati
    results in a reversal of the desired effect: a successful Diplomacy check makes
    the target a hated enemy, an attack roll injures the attacker or an ally, a failed
    saving throw against a spell increases the damage or duration by 50%, and a successful
    concentration check turns the spell's effects back upon the caster. Psychopomps
    are immune to this effect. A fulgati cannot suppress this ability.'
  Paramnesia (Ex): Fulgatis are anathema to life, and mortal minds reflexively attempt
    to wipe away all memory of their presence. Living creatures that travel more than
    1,000 feet from a fulgati must succeed at a DC 25 Will save or forget all experiences
    of their interactions with the creature, per modify memory. A creature that succeeds
    at this saving throw is permanently immune to the individual fulgati's paramnesia
    ability. The save DC is Charisma-based.
  Poisonous Blood (Ex): |-
    Any attack with a piercing or slashing melee or natural weapon that damages the fulgati exposes the attacker to this poison. The space a fulgati occupied when it was attacked is also tainted and rendered supernaturally unable to support plant life for 5 years per Hit Die of the injured fulgati (125 years for most). The fulgati's poison has its full effect on undead as well, even those normally immune to poison, dealing Charisma damage in place of Constitution damage.
     Fulgati Blood: Spray-contact; save Fort DC 29, frequency 1/minute for 10 minutes, effect 1d4 Con damage, cure 2 consecutive saves.
  Quintessence (Su): A fulgati absorbs the motivating force of dying victims, collecting
    1 Quintessence Point for every Hit Die of a creature that dies within 50 feet
    of it. As a standard action, it can cast animate object as a spell-like ability,
    treating its current Quintessence Point total as its caster level. After using
    this ability, the fulgati's Quintessence Point total resets to 0. Objects animated
    by a fulgati remain active and hostile until destroyed. A fulgati can store a
    maximum number of Quintessence Points equal to double its Hit Dice (50 for most
    fulgatis).
desc_long: |-
  The monolithic outsiders known as fulgatis reap not souls but entire cultures. They tread upon the land when a civilization that has reached the end of days must be wiped away for new things to grow from its corpse. Their arrival heralds the end of cities, nations, and even entire species. They are simpleminded, loyal, and utterly devoid of the compassion that defines so many other psychopomps-terrible things created and directed with terrible purpose. Legends claim that Pharasma bore these creatures herself, rather than forging them from once-mortal souls, lending some clarity to the usher Atropos's title as the “Last Sister.”

   Clad in iron masks resembling rams and bulls, fulgatis serve as little more than beasts of burden. While most psychopomps are artisans in death, honing and crafting it with purpose and applying it only when needed, fulgatis are fonts. Death itself pumps through their veins and unravels creations where they step, leaving the ground fallow so immediate survivors of their attacks have no chance to rebuild. While intelligent enough to speak and read, they lack the intellect and forceful personalities of most powerful outsiders, instead serving as the penultimate enforcers of the Boneyard's will-second only to Pharasma herself.

   These titanic psychopomps are too aggressive to collect souls, and instead rend souls free and allow their lesser kin-always close at hand when fulgatis march-to shepherd their victims to the Boneyard. What fulgatis do collect is the motivating life force, or quintessence, of the creatures they slay, pooling it until they invest it into the rubble around them to animate earth and stone as minions to assist in their destruction. These animated soldiers sometimes remain active for decades or even centuries after the psychopomps' grim work is done, tearing down what ruins remain and ensuring no trace of a destroyed civilization can ever be reclaimed.

   Fearsome psychopomps of last resort, a dozen known fulgatis slumber in isolated sepulchres deep within the Spire, awaiting those rare occasions when Pharasma herself has no need for subtlety or patience. Many more guard Pharasma's Palace, likewise held in deep sleep until released and directed against the Boneyard's enemies. Many psychopomps note that the structures housing the fulgatis continue far down along the Spire's length, well beyond the reaches of where they are permitted to travel, and it is possible that more of these powerful reapers-or even more powerful manifestations of their kind-slumber at the Spire's base, waiting to tear it down at the end of the cosmos as Pharasma brushes away the last traces of the multiverse.

   The fulgatis' ability to cast plane shift means the willful among them can escape and even hide for centuries at a time, reaping not at the Lady of Graves' command, but at whim. Teams of psychopomps relentlessly hunt these wayward destroyers, but few among their number, save the legendary yamarajes, can stand to the reapers of realms. Some psychopomps compare these wild fulgatis and their lust for random destruction to the spawn of Rovagug, but others believe Pharasma fashioned her own killers in response to Rovagug's arrival in the multiverse, likely to reap his divine spawn. Other claim that the souls of Rovagug's offspring are too terrible to exist freely, and so the Gray Lady devours them and rebirths them as new monsters-ones she alone can control.

   Despite the fulgatis' incredible power, few outside the courts of the Boneyard are even aware they exist. The mortal need to turn away from death is so powerful that living minds often wipe clean any encounter with a fulgati, leaving survivors to rationalize the destruction and death left in their wake as terrible accidents and natural disasters. Because of this, mortal scholars are unsure how often-or even if-the fulgatis have ever been unleashed upon the Material Plane. The reapers may be unleashed upon the world every few centuries, or they may simply slumber and exist only in nightmares and legend.

   Fulgatis resemble massive, female forms bearing eight stout arms, four of which serve them in place of legs. Their unusual locomotion allows them to climb and burrow with ease, even springing forth from the earth in the midst of their targets. While they wear no clothing, their flesh resembles worked metal and stone carved into elaborate whorls and patterns, giving the illusion of magnificent armor. The horns they bear are perfectly functional and deadly in close combat.

   A fulgati stands 80 feet tall and weighs 150-175 tons.

---

# Psychopomp, Fulgati
This towering, muscular, female figure wears an iron, ram-headed _[[items/Mundane/Mask|mask]]_. Four stout arms crackle with primal energies, while four additional arms emerge from her hips, supporting her bulk in place of legs.
**Source** Concordance of Rivals pg. 60
**XP** 153,600

N Colossal outsider (extraplanar, psychopomp)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, spiritsense, _[[spells/True Seeing|true seeing]]_; Perception +32
**Aura** calamity (300 ft.)

##### Defense

**AC** 32, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+3 Dex, +27 natural, –8 size)
**hp** 312 (25d10+175); _[[universal monster rules/Regeneration|regeneration]]_ 10 (artifacts, epic, or mythic)
**Fort** +21, **Ref** +11, **Will** +20
**Defensive Abilities** _[[universal monster rules/Poisonous Blood|poisonous blood]]_; **DR** 10/adamantine; **Immune** cold, death effects, disease, electricity, poison; **Resist** fire 15, sonic 15; **SR** 29

##### Offense
**Speed** 50 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.; _[[spells/Air Walk|air walk]]_
**Melee** gore +31 (3d6+14/19–20), 4 slams +31 (2d6+14)
**Ranged** rock +29 (4d6+14)
**Space** 30 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 slams, 2d8+21), _[[universal monster rules/Rock Throwing|rock throwing]]_ (240 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +28)
Constant—_air walk_, _[[spells/Mind Blank|mind blank]]_, _true seeing_
 3/day—_[[spells/Align Weapon|align weapon]]_ (self only), _[[spells/Chain Lightning|chain lightning]]_ (DC 21), greater _[[spells/Shout|shout]]_ (DC 20), _[[spells/Plane Shift|plane shift]]_ (DC 21), _[[spells/Undeath to Death|undeath to death]]_ (DC 19)
 1/day—_[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Creeping Doom|creeping doom]]_ (DC 20), _[[spells/Earthquake|earthquake]]_, _[[spells/Epidemic|epidemic]]_, _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 22)

##### Statistics
**Str** 39, **Dex** 16, **Con** 24, **Int** 7, **Wis** 19, **Cha** 16
**Base Atk** +25; **CMB** +47 (+51 bull rush, sunder); **CMD** 60 (62 vs. bull rush or sunder, 64 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (gore), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _Spell Focus_ (evocation), _[[feats/Sundering Strike|Sundering Strike]]_
**Skills** Acrobatics +3 (+11 when jumping), _Climb_ +22, Intimidate +31, Perception +32, Sense Motive +32, Survival +32
**Languages** Abyssal, Celestial, Infernal
**SQ** paramnesia, spirit touch

##### Ecology

**Environment** any (Boneyard)
**Organization** solitary
**Treasure** none

### Special Abilities

**Aura of Calamity (Ex)** A fulgati’s presence warps probability and makes tragedy more likely. Any result of a natural 1 on a d20 roll within 300 feet of a fulgati results in a reversal of the desired effect: a successful Diplomacy check makes the target a hated enemy, an attack roll injures the attacker or an ally, a failed saving throw against a spell increases the damage or duration by 50%, and a successful concentration check turns the spell’s effects back upon the caster. Psychopomps are immune to this effect. A fulgati cannot suppress this ability.
 **Paramnesia (Ex)** Fulgatis are anathema to life, and mortal minds reflexively attempt to wipe away all memory of their presence. Living creatures that travel more than 1,000 feet from a fulgati must succeed at a DC 25 Will save or forget all experiences of their interactions with the creature, per _[[spells/Modify Memory|modify memory]]_. A creature that succeeds at this saving throw is permanently immune to the individual fulgati’s paramnesia ability. The save DC is Charisma-based.
 **_Poisonous Blood_ (Ex)** Any attack with a piercing or slashing melee or natural weapon that damages the fulgati exposes the attacker to this poison. The space a fulgati occupied when it was attacked is also tainted and rendered supernaturally unable to support plant life for 5 years per Hit Die of the injured fulgati (125 years for most). The fulgati’s poison has its full effect on undead as well, even those normally immune to poison, dealing Charisma damage in place of Constitution damage.
 Fulgati Blood: Spray—contact; save Fort DC 29, frequency 1/minute for 10 minutes, effect 1d4 Con damage, cure 2 consecutive saves.
 **_[[spells/Quintessence|Quintessence]]_ (Su)** A fulgati absorbs the motivating force of _[[conditions/Dying|dying]]_ victims, collecting 1 _Quintessence_ Point for every Hit Die of a creature that dies within 50 feet of it. As a standard action, it can cast animate object as a spell-like ability, treating its current _Quintessence_ Point total as its caster level. After using this ability, the fulgati’s _Quintessence_ Point total resets to 0. Objects _[[items/Armor Magic Abilities/Animated|animated]]_ by a fulgati remain active and hostile until destroyed. A fulgati can store a maximum number of _Quintessence_ Points equal to double its Hit Dice (50 for most fulgatis).

##### Description

The monolithic outsiders known as fulgatis reap not souls but entire cultures. They tread upon the land when a civilization that has reached the end of days must be wiped away for new things to grow from its corpse. Their arrival heralds the end of cities, nations, and even entire species. They are simpleminded, loyal, and utterly devoid of the compassion that defines so many other psychopomps—terrible things created and directed with terrible purpose. Legends claim that Pharasma bore these creatures herself, rather than forging them from once-mortal souls, lending some _[[items/Weapon/Clarity|clarity]]_ to the usher Atropos’s title as the “Last Sister.”
 Clad in iron masks resembling rams and bulls, fulgatis serve as little more than beasts of burden. While most psychopomps are artisans in death, honing and crafting it with purpose and applying it only when needed, fulgatis are fonts. Death itself pumps through their veins and unravels creations where they step, leaving the ground fallow so immediate survivors of their attacks have no chance to rebuild. While intelligent enough to speak and read, they lack the intellect and forceful personalities of most powerful outsiders, instead serving as the penultimate enforcers of the Boneyard’s will—second only to Pharasma herself.

These _[[items/Armor Magic Abilities/Titanic|titanic]]_ psychopomps are too aggressive to collect souls, and instead _rend_ souls free and allow their lesser kin—always close at hand when fulgatis march—to shepherd their victims to the Boneyard. What fulgatis do collect is the motivating life force, or _quintessence_, of the creatures they slay, pooling it until they invest it into the rubble around them to animate earth and stone as minions to assist in their _[[spells/Destruction|destruction]]_. These _animated_ soldiers sometimes remain active for decades or even centuries after the psychopomps’ grim work is done, tearing down what ruins remain and ensuring no trace of a destroyed civilization can ever be reclaimed.

Fearsome psychopomps of last resort, a dozen known fulgatis slumber in isolated sepulchres deep within the Spire, awaiting those rare occasions when Pharasma herself has no need for subtlety or patience. Many more _[[npcs/Guard|guard]]_ Pharasma’s Palace, likewise held in deep sleep until released and directed against the Boneyard’s enemies. Many psychopomps note that the structures housing the fulgatis continue far down along the Spire’s length, well beyond the reaches of where they are permitted to travel, and it is possible that more of these powerful reapers—or even more powerful manifestations of their kind—slumber at the Spire’s base, waiting to tear it down at the end of the cosmos as Pharasma brushes away the last traces of the multiverse.

The fulgatis’ ability to cast _plane shift_ means the willful among them can escape and even hide for centuries at a time, reaping not at the Lady of Graves’ _[[spells/Command|command]]_, but at whim. Teams of psychopomps relentlessly hunt these wayward destroyers, but few among their number, save the legendary yamarajes, can stand to the reapers of realms. Some psychopomps compare these wild fulgatis and their lust for random _destruction_ to the spawn of Rovagug, but others believe Pharasma fashioned her own killers in response to Rovagug’s arrival in the multiverse, likely to reap his divine spawn. Other claim that the souls of Rovagug’s offspring are too terrible to exist freely, and so the _[[monsters/Gray|Gray]]_ Lady devours them and rebirths them as new monsters—ones she alone can control.

Despite the fulgatis’ incredible power, few outside the courts of the Boneyard are even aware they exist. The mortal need to turn away from death is so powerful that living minds often wipe clean any encounter with a fulgati, leaving survivors to rationalize the _destruction_ and death left in their wake as terrible accidents and natural disasters. Because of this, mortal scholars are unsure how often—or even if—the fulgatis have ever been unleashed upon the Material Plane. The reapers may be unleashed upon the world every few centuries, or they may simply slumber and exist only in nightmares and legend.

Fulgatis resemble massive, female forms bearing eight stout arms, four of which serve them in place of legs. Their unusual locomotion allows them to _climb_ and _burrow_ with ease, even springing forth from the earth in the midst of their targets. While they wear no clothing, their flesh resembles worked metal and stone carved into elaborate whorls and patterns, giving the illusion of magnificent armor. The horns they bear are perfectly functional and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ in close combat.

A fulgati stands 80 feet tall and weighs 150–175 tons.

**Name****CR**Ahmuuth4Algea11Calaca8Catrina5Ember Weaver8Esobok3Fulgati18Kere10Memitim15Morbai6Morrigna13Nosoi2Olethros17Shoki9Vanth7Viduus4Yamaraj20

**Source** Bestiary 4 pg. 217
All life has its beginning and its end. From the moment of birth, everything that shrieks and struggles upon the Material Plane crawls toward a singular finale, that fatal climax that grants passage into the unimaginable infinities of the afterlife. As the spirits of the deceased flow from the _[[spells/Confusion|confusion]]_ of mortality to their ultimate fates, they are each judged by the gods of death, who assure that all who die reach their prescribed afterlife. Yet with all the worlds of the Material Plane, the countless faces and exceptions of mortality, and all those who would turn fate and finality to their own devices, death as a system and institution requires more agents than a single deity or pantheon to uphold. These agents are the psychopomps—denizens of Purgatory and the dispassionate stewards, chroniclers, and guides of all that die.

Psychopomps preside over the flow of life. Their primary concerns focus upon souls in the vulnerable transition between death and their final destinations upon the planes. Psychopomps carry out their duties with the dispassion of veterans and cynics. In terms of service measuring in ages, psychopomps meet countless souls from innumerable worlds, and soon nearly every story, fate, plea, and exception becomes all too familiar. They care little for the histories or personalities of the souls that pass them by, concerned only for the efficient and unvaried processing of each spirit to its final unremarkable eternity. _[[spells/Damnation|Damnation]]_ and paradise are the same to them, as are heroes and villains, and no psychopomp cares one jot for great deeds left undone, other fates hanging in the balance, or bribes worth even a world’s ransom. But while drudgery is the lot of many psychopomps—interrupted only by the diversions they sometimes create for themselves—their system is not without flaws. There are creatures who would seek to deny the natural order of death—fiends that prey upon souls, spirits lost in their migration, and undead abominations. To counter such abnormalities and _[[spells/Preserve|preserve]]_ the flow of souls as the multiverse requires, numerous specialized psychopomps exist to protect the dead and counter any who would seek to pervert the state of death to their own ends.

Noteworthy among psychopomps are their masks. Many who have dealings with the living wear some manner of grim face covering or funerary _mask_. While these masks are not part of a psychopomp’s body and grant them no special abilities, the legends of numerous cultures suggest that for a living creature to see a psychopomp’s unmasked countenance invites a premature death. Those psychopomps who deal predominately with the dead typically eschew such marks of station except as a formality.

As psychopomps help convey souls to all of the Outer Planes, and thus provide petitioners equally to each of those realms, they enjoy a special _[[spells/Status|status]]_ among many _[[items/Weapon Magic Abilities/Planar|planar]]_ races as respected neutrals. As such, most other _planar_ races grant them a wide berth, with even archons and demons going out of their ways to avoid interfering with death’s emissaries. Soul-hungry daemons and reality-violating qlippoth are among the only races that actively oppose psychopomps. Consequently, the deadlier classes of psychopomps watch for and hunt _[[feats/Disruptive|disruptive]]_ members of these races, seeking to expunge the paths between the planes of any that would impede the certain cycle of death.

The death gods create the weakest psychopomps out of mortal souls, usually those who served Purgatory in life or worshiped deities of judgment. The gods may transform psychopomps which perform exemplary service into greater members of their kind, though rarely an exceptional hero or _[[items/Armor Magic Abilities/Champion|champion]]_ of Purgatory may become a superior psychopomp when she dies. There is little competitiveness or jealousy among the ranks of these creatures, as their primary motivation is fulfillment of their eternal duties, and there is little point in coveting another’s rewards and responsibilities.

The following are the most common types of psychopomps. Other varieties exist, tasked with more obscure duties for the gods of death, or responsible for alien worlds where the native creatures have radically different life cycles and outlooks compared to humanoids.

## Psychopomp Ushers

Beings ancient and dispassionate rise above the psychopomp droves, emissaries of death who have presided over the dooms of whole nations, races, and worlds. These eldest and most efficient servants of death hold great respect for the gods of death, but are not necessarily their minions, striving to fulfill their own visions of death’s ultimate purpose and process over all other objectives.

Atropos the Last Sister
 Barzahk the Passage
 Ceyanan the Shepherd
 Dammar the Denied
 Imot the Symbol of _[[spells/Doom|Doom]]_
 Mother _[[monsters/Vulture|Vulture]]_
 Mrtyu, Death’s Consort
 Narakaas the Cleansing Sentence
 The Pale _[[monsters/Horse|Horse]]_
 Phlegyas, Consoler of Atheists
 Saloc, Minder of Immortals
 Teshallas the Primordial Poison
 Vale the Court of Ancestors