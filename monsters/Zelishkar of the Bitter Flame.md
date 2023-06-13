---
cssclass: [monsters]
title1: Zelishkar of the Bitter Flame
desc_short: This fiendish figure appears to be shaped from pure flame with a feline
  face. Three wicked tongues dart from the creature's mouth.
title2: Zelishkar of the Bitter Flame
CR: 21
sources:
- name: Inner Sea Bestiary
  page: 62
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 409600
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
- fire
initiative:
  bonus: 5
senses:
  darkvision: 60
  scent: true
  true seeing: true
auras:
- name: unholy aura
AC:
  AC: 39
  touch: 13
  flat_footed: 35
  components:
    armor: 11
    dex: 3
    dodge: 1
    natural: 15
    size: -1
HP:
  HP: 396
  long: 24d10+264
saves:
  fort: 19
  ref: 19
  will: 20
defensive_abilities:
- blur (20% miss chance)
immunities:
- ability damage
- acid
- charm and compulsion effects
- death effects
- disease
- fire
- poison
resistances:
  cold: 30
  electricity: 30
SR: 32
weaknesses:
- vulnerable to cold
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +34 (1d8+11 plus 2d6 fire)
      entries:
      - - damage: 1d8+11
        - damage: 2d6
          type: fire
      attack: bite
      bonus:
      - 34
    - text: 2 claws +35 (1d10+11/19-20 plus 2d6 fire)
      entries:
      - - damage: 1d10+11
          crit_range: 19-20
        - damage: 2d6
          type: fire
      count: 2
      attack: claws
      bonus:
      - 35
  special:
  - bitter flames
  - corpse cremation
  - incandescent body
  - incendiary grasp
  - pounce
  - rake (2 claws +35, 1d10+11 plus 2d6 fire)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 24
  - superscripts:
    - UC
    name: blistering invective
    source: default
    freq: At will
    DC: 18
  - name: dispel good
    source: default
    freq: At will
    DC: 21
  - name: fire shield
    source: default
    freq: At will
  - name: mass charm monster
    source: default
    freq: At will
    other: creatures of the fire subtype only
    DC: 24
  - name: empowered fire storm
    source: default
    freq: 3/day
    DC: 24
  - name: incendiary cloud
    source: default
    freq: 3/day
    DC: 24
  - superscripts:
    - APG
    name: quickened contagious flame
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: sirocco
    source: default
    freq: 3/day
    DC: 22
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: fiendish elder fire elementals
      amount: 2
    - name: any daemon of 20 Hit Dice
    - name: fewer
      chance: 100%
  sources:
  - name: default
    CL: 24
    concentration: 30
ability_scores:
  STR: 33
  DEX: 21
  CON: 32
  INT: 17
  WIS: 22
  CHA: 23
BAB: 24
CMB: 36
CMD: 52
feats:
- name: Blind-Fight
- superscripts:
  - APG
  name: Charge Through
- name: Combat Reflexes
- name: Dodge
- name: Empower Spell-Like Ability ( fire storm)
- name: Greater Overrun
- name: Improved Critical (claw)
- name: Improved Overrun
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (contagious flame)
- name: Weapon Focus (claw)
skills:
  Acrobatics: 29
  Bluff: 20
  Diplomacy: 20
  Fly: 26
  Intimidate: 33
  Knowledge (planes): 30
  Perception: 33
  Sense Motive: 29
  Spellcraft: 24
  Stealth: 25
  Survival: 27
languages:
- Abyssal
- Common
- Ignan
- Infernal
- telepathy 300 ft.
special_qualities:
- daemonic harbinger traits
ecology:
  environment: any (Osirion)
  organization: solitary
  treasure_type: triple
  treasure:
  - +5 breastplate
  - other treasure
special_abilities:
  Bitter Flames (Su): Whenever Zelishkar deals fire damage with any attack or effect,
    half of the damage is fire damage and the other half is untyped damage, similar
    to a flame strike spell. In addition, creatures that fail a save against any fire
    effect Zelishkar creates are sickened for 1 minute. Those damaged by his melee
    attacks or by fire effects that allow no save are instead sickened for 1 round
    per attack. This duration stacks.
  Corpse Cremation (Su): Whenever Zelishkar reduces a living creature to negative
    hit points, as a swift action he can turn its body to ashes and feed upon the
    target's life force, as death knell (Will DC 28 negates). Whenever Zelishkar slays
    a creature with any attack or ability, the creature's corpse is reduced to ashes
    (treat as disintegrate).
  Daemonic Harbinger Traits: A daemonic harbinger is a powerful daemon that has not
    yet made the full transition from unique daemon to a horseman. It possesses several
    traits, as summarized here. Immunity to acid, charm and compulsion effects, death
    effects, disease, and poison.Resistance to cold 30, electricity 30, and fire 30.Telepathy
    300 feet.The harbinger's natural weapons, as well as any weapon it wields, are
    treated as evil and lawful for the purpose of overcoming damage reduction.The
    harbinger can grant spells to its worshipers. Granting spells does not require
    any specific action on its behalf. Zelishkar grants access to the domains of Evil,
    Law, Magic, and Trickery. His favored weapon is the quarterstaff.
  Incandescent Body (Su): As a free action, Zelishkar can cause his body to erupt
    into white-hot flame. He sheds light as bright as a daylight spell, and dazzles
    any creature that does not avert its gaze. Creatures with the fire subtype are
    immune to this dazzling effect. Zelishkar can dim his flames to burning black
    shadows as a free action, suppressing the dazzling effect and allowing him to
    use Stealth without penalty.
  Incendiary Grasp (Su): If Zelishkar hits a target with more than one natural weapon
    in the same round, the fire damage from each hit is combined as if from a single
    attack for the purpose of overcoming effects that provide resistance to fire.
    In addition, if Zelishkar succeeds at a grapple combat maneuver, as a swift action
    he can suppress any fire resistance or immunity the target possesses until the
    beginning of Zelishkar's next turn. Creatures with the fire subtype are immune
    to this effect, unless that subtype is granted by a temporary magical effect or
    magic item.
desc_long: |-
  The dread Zelishkar of the Bitter Flame is a figure much feared on the crumbling plains of Abaddon and across the multiverse. A monstrous feline in shape but seemingly sculpted of lurid crimson flame, Zelishkar is girded with a crest and cuirass of infernally strengthened obsidian, shaved to razor thinness yet losing none of its terrible strength. His eyes are jet-black pits that mirror his armor, though pinpoints of awful orange radiance gleam deep within. He is surrounded always by a heat shimmer that diffuses his blinding radiance. Zelishkar is reputed to sense the presence of his prey by the tiniest variations in temperature, tracking the movements of creatures both seen and unseen before he pounces. His own fires burn with a hellish uncleanness, tainting even those who thought themselves proofed against his flames and rapidly consuming their body and soul, leaving nothing behind but befouled ashes.

  Zelishkar is feared as much for his incisive tactical acumen as for his dreadful and terrifying powers in close combat. He has single-handedly withered and despoiled cities and farmlands when summoned in the name of his daemonic mistress-Szuriel, patron of war and suffering. She forged Zelishkar's form in the deepest pits of the Cinder Furnace as her terrifying harbinger, embodying the hopeless misery of funeral pyres that consume and cremate the dead in the wake of the war that she brings. He proved so adept that she judged him worthy to transcend his purpose, and he has come to embody all of the hateful and sadistic purposes that fire serves. His name is invoked now by torturers and inquisitors alike as they consign their hapless captives to the ultimate agonies of being burned alive, and even by arsonists both petty and grand. All twisted souls who love nothing more than to see the world burn offer up silent praises to Zelishkar in their hearts; even if they never speak his name, the hate that burns within them is a sweet savor in his nostrils.

  Zelishkar was summoned to Golarion in ancient times, during the height of Osirion's empire, and he led legions of flaming minions against the enemies of the Pharaoh of Forgotten Plagues, notably the Jistka Imperium. In a twist of supreme hubris, the Pharaoh of Forgotten Plagues turned against his summoned ally after several successful campaigns, and chose Zelishkar to be the test subject of his grandest experiment yet. The Osirian king had just finished construction of a grand labyrinth south of the Alamein Peninsula, and in a display of prideful foolishness ordered Zelishkar to be imprisoned within to prove the infallibility of his maze. It took the efforts of an entire army of summoned genies to lock the daemonic harbinger away beneath the desert's churning sands, but his imprisonment was absolute with the aid of an ancient efreeti and a legendary artifact known as the Bottle of the Bound.

  Through all the long millennia since, Zelishkar and the remnant of his host have remained imprisoned beneath the Labyrinth of Shiman-Sekh, the city founded by the Song Pharaoh upon her victory over the Pharaoh of Forgotten Plagues years after Zelishkar's detention. He has emerged from his prison but once, when Szuriel and the ironically named Incorruptible Pharaoh joined to loose his fiery fury upon one of the sky-cities of Shory. His destructive rampage could not be contained, however, and he devastated several cities and oases of western Osirion before he and his host were finally bound back within their prison. There he remains, plotting burning vengeance upon Osirion and all of Golarion for his ages of durance vile.

---

# Zelishkar of the Bitter Flame
This fiendish figure appears to be shaped from pure flame with a feline face. Three wicked _[[spells/Tongues|tongues]]_ _[[items/Weapon/Dart|dart]]_ from the creature’s mouth.
**Source** Inner Sea Bestiary pg. 62
**XP** 409,600

NE Large outsider (daemon, evil, extraplanar, fire)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +33
**Aura** _[[spells/Unholy Aura|unholy aura]]_

##### Defense

**AC** 39, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+11 armor, +3 Dex, +1 dodge, +15 natural, –1 size)
**hp** 396 (24d10+264)
**Fort** +19, **Ref** +19, **Will** +20
**Defensive Abilities** _[[spells/Blur|blur]]_ (20% miss chance); **Immune** ability damage, acid, charm and compulsion effects, death effects, disease, fire, poison; **Resist** cold 30, electricity 30; **SR** 32
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** bite +34 (1d8+11 plus 2d6 fire), 2 claws +35 (1d10+11/19–20 plus 2d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[items/Armor Magic Abilities/Bitter|bitter]]_ flames, corpse cremation, incandescent body, incendiary _[[spells/Grasp|grasp]]_, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +35, 1d10+11 plus 2d6 fire)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +30)
Constant—_blur_, _true seeing_, _unholy aura_ (DC 24)
At will—_[[spells/Blistering Invective|blistering invective]]_ (DC 18), _[[spells/Dispel Good|dispel good]]_ (DC 21), _[[spells/Fire Shield|fire shield]]_, mass _[[spells/Charm Monster|charm monster]]_ (creatures of the fire subtype only) (DC 24)
3/day—empowered _[[spells/Fire Storm|fire storm]]_ (DC 24), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 24), quickened _[[spells/Contagious Flame|contagious flame]]_, _[[spells/Sirocco|sirocco]]_ (DC 22)
1/day—_[[universal monster rules/Summon|summon]]_ (level 9, 2 fiendish elder fire elementals or any daemon of 20 Hit Dice or fewer 100%)

##### Statistics
**Str** 33, **Dex** 21, **Con** 32, **Int** 17, **Wis** 22, **Cha** 23
**Base Atk** +24; **CMB** +36; **CMD** 52
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Charge Through|Charge Through]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ ( _fire storm_), _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_contagious flame_), _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +29, Bluff +20, Diplomacy +20, Fly +26, Intimidate +33, Knowledge (planes) +30, Perception +33, Sense Motive +29, Spellcraft +24, Stealth +25, Survival +27
**Languages** Abyssal, Common, Ignan, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** daemonic harbinger traits

##### Ecology

**Environment** any (Osirion)
**Organization** solitary
**Treasure** triple (+5 _[[items/Armor/Breastplate|breastplate]]_, other treasure)

### Special Abilities

**_Bitter_ Flames (Su)** Whenever Zelishkar deals fire damage with any attack or effect, half of the damage is fire damage and the other half is untyped damage, similar to a _[[spells/Flame Strike|flame strike]]_ spell. In addition, creatures that fail a save against any fire effect Zelishkar creates are _[[conditions/Sickened|sickened]]_ for 1 minute. Those damaged by his melee attacks or by fire effects that allow no save are instead _sickened_ for 1 round per attack. This duration stacks.

**Corpse Cremation (Su)** Whenever Zelishkar reduces a living creature to negative hit points, as a swift action he can turn its body to ashes and feed upon the target’s life force, as _[[spells/Death Knell|death knell]]_ (Will DC 28 negates). Whenever Zelishkar slays a creature with any attack or ability, the creature’s corpse is reduced to ashes (treat as _[[spells/Disintegrate|disintegrate]]_).

**Daemonic Harbinger Traits **A daemonic harbinger is a powerful daemon that has not yet made the full transition from unique daemon to a horseman. It possesses several traits, as summarized here.

* _[[universal monster rules/Immunity|Immunity]]_ to acid, charm and compulsion effects, death effects, disease, and poison.
* _[[universal monster rules/Resistance|Resistance]]_ to cold 30, electricity 30, and fire 30.
* _Telepathy_ 300 feet.
* The harbinger’s natural weapons, as well as any weapon it wields, are treated as evil and lawful for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.
* The harbinger can grant spells to its worshipers. Granting spells does not require any specific action on its behalf. Zelishkar grants access to the domains of Evil, Law, Magic, and Trickery. His favored weapon is the _[[items/Weapon/Quarterstaff|quarterstaff]]_.

**Incandescent Body (Su)** As a free action, Zelishkar can cause his body to erupt into white-hot flame. He sheds light as bright as a _[[spells/Daylight|daylight]]_ spell, and dazzles any creature that does not avert its _[[universal monster rules/Gaze|gaze]]_. Creatures with the fire subtype are immune to this dazzling effect. Zelishkar can dim his flames to _[[items/Weapon Magic Abilities/Burning|burning]]_ black shadows as a free action, suppressing the dazzling effect and allowing him to use Stealth without penalty.

**Incendiary _Grasp_ (Su)** If Zelishkar hits a target with more than one natural weapon in the same round, the fire damage from each hit is combined as if from a single attack for the purpose of overcoming effects that provide _resistance_ to fire. In addition, if Zelishkar succeeds at a grapple combat maneuver, as a swift action he can suppress any fire _resistance_ or _immunity_ the target possesses until the beginning of Zelishkar’s next turn. Creatures with the fire subtype are immune to this effect, unless that subtype is granted by a temporary magical effect or magic item.

##### Description

The dread _[[monsters/Zelishkar of the _Bitter_ Flame|Zelishkar of the _Bitter_ Flame]]_ is a figure much feared on the crumbling plains of Abaddon and across the multiverse. A monstrous feline in shape but seemingly sculpted of lurid crimson flame, Zelishkar is girded with a crest and cuirass of infernally strengthened obsidian, shaved to razor thinness yet losing none of its terrible strength. His eyes are jet-black pits that _[[items/Mundane/Mirror|mirror]]_ his armor, though pinpoints of awful orange _[[items/Weapon/Radiance|radiance]]_ gleam deep within. He is surrounded always by a _[[universal monster rules/Heat|heat]]_ shimmer that diffuses his _[[items/Armor Magic Abilities/Blinding|blinding]]_ _radiance_. Zelishkar is reputed to sense the presence of his prey by the tiniest variations in temperature, tracking the movements of creatures both _[[feats/Seen and Unseen|seen and unseen]]_ before he pounces. His own fires _[[universal monster rules/Burn|burn]]_ with a hellish uncleanness, tainting even those who thought themselves proofed against his flames and rapidly consuming their body and soul, leaving nothing behind but befouled ashes.

Zelishkar is feared as much for his incisive _[[spells/Tactical Acumen|tactical acumen]]_ as for his dreadful and terrifying powers in close combat. He has single-handedly withered and despoiled cities and farmlands when summoned in the name of his daemonic mistress—Szuriel, patron of war and suffering. She forged Zelishkar’s form in the deepest pits of the Cinder Furnace as her terrifying harbinger, embodying the hopeless misery of funeral pyres that consume and cremate the dead in the wake of the war that she brings. He proved so adept that she judged him worthy to transcend his purpose, and he has come to embody all of the hateful and sadistic purposes that fire serves. His name is invoked now by torturers and inquisitors alike as they consign their hapless captives to the ultimate agonies of being burned alive, and even by arsonists both petty and grand. All twisted souls who love nothing more than to see the world _burn_ offer up silent praises to Zelishkar in their hearts; even if they never speak his name, the hate that burns within them is a sweet savor in his nostrils.

Zelishkar was summoned to Golarion in ancient times, during the height of Osirion’s empire, and he led legions of _[[items/Weapon Magic Abilities/Flaming|flaming]]_ minions against the enemies of the Pharaoh of Forgotten Plagues, notably the Jistka Imperium. In a twist of supreme hubris, the Pharaoh of Forgotten Plagues turned against his summoned ally after several successful campaigns, and chose Zelishkar to be the test subject of his grandest experiment yet. The Osirian _[[npcs/King|king]]_ had just finished construction of a grand labyrinth south of the Alamein Peninsula, and in a display of prideful foolishness ordered Zelishkar to be imprisoned within to prove the infallibility of his _[[spells/Maze|maze]]_. It took the efforts of an entire army of summoned genies to lock the daemonic harbinger away beneath the desert’s churning sands, but his _[[spells/Imprisonment|imprisonment]]_ was absolute with the aid of an ancient efreeti and a legendary artifact known as the _[[items/Wondrous Item/Bottle of the Bound|Bottle of the Bound]]_.

Through all the long millennia since, Zelishkar and the remnant of his host have remained imprisoned beneath the Labyrinth of Shiman-Sekh, the city founded by the Song Pharaoh upon her victory over the Pharaoh of Forgotten Plagues years after Zelishkar’s detention. He has emerged from his prison but once, when Szuriel and the ironically named Incorruptible Pharaoh joined to loose his fiery fury upon one of the sky-cities of Shory. His destructive rampage could not be contained, however, and he devastated several cities and oases of western Osirion before he and his host were finally bound back within their prison. There he remains, plotting _burning_ _[[feats/Vengeance|vengeance]]_ upon Osirion and all of Golarion for his ages of durance vile.