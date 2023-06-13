---
cssclass: [monsters]
title1: Sphinx, Elder Sphinx
desc_short: The brooding face of this towering limestone statue of a gynosphinx reflects
  a harsh wisdom acquired through untold ages of experience.
title2: Elder Sphinx
CR: 16
sources:
- name: 'Pathfinder #83: The Slave Trenches of Hakotep'
  page: 90
  link: http://paizo.com/products/btpy97at?Pathfinder-Adventure-Path-83-The-Slave-Trenches-of-Hakotep
XP: 76800
alignment: N
size: Gargantuan
type: magical beast
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 29
  touch: 7
  flat_footed: 28
  components:
    dex: 1
    natural: 22
    size: -4
HP:
  HP: 241
  long: 21d10+126
saves:
  fort: 18
  ref: 15
  will: 19
defensive_abilities:
- enciphered mind
- DR 15/adamantine and magic
immunities:
- petrification
SR: 27
speeds:
  base: 40
  fly: 60
  fly_maneuverability: poor
attacks:
  melee:
  - - text: 2 claws +31 (2d6+14)
      entries:
      - - damage: 2d6+14
      count: 2
      attack: claws
      bonus:
      - 31
    - text: 2 wings +26 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: wings
      bonus:
      - 26
  special:
  - litany of riddles
  - pounce
  - rake (2 claws +31, 2d6+14)
  - trample (2d6+21, DC 34)
space: 20
reach: 15
spell_like_abilities:
  entries:
  - name: comprehend languages
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: nondetection
    source: default
    freq: Constant
  - name: read magic
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: 3/day
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: hallucinatory terrain
    source: default
    freq: 3/day
    DC: 21
  - name: locate object
    source: default
    freq: 3/day
  - name: remove curse
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: sirocco
    source: default
    freq: 3/day
    DC: 23
  - name: commune
    source: default
    freq: 1/day
  - name: contact other plane
    source: default
    freq: 1/day
  - name: legend lore
    source: default
    freq: 1/day
  - symbols_special: true
    name: symbol of fear
    source: default
    freq: 1/week
    DC: 22
  - symbols_special: true
    name: symbol of persuasion
    source: default
    freq: 1/week
    DC: 23
  - symbols_special: true
    name: symbol of sleep
    source: default
    freq: 1/week
    DC: 23
  - symbols_special: true
    name: symbol of vulnerability
    source: default
    freq: 1/week
    DC: 26
  - symbols_special: true
    name: symbol of weakness
    source: default
    freq: 1/week
    DC: 24
  sources:
  - name: default
    CL: 20
    concentration: 27
  symbols_special:
    max_duration: 1 week
    num_selected: one
ability_scores:
  STR: 39
  DEX: 12
  CON: 23
  INT: 26
  WIS: 30
  CHA: 25
BAB: 21
CMB: 39
CMB_other: +41 bull rush
CMD: 50
CMD_other: 52 vs. bull rush, 54 vs. trip
feats:
- name: Alertness
- name: Awesome Blow
- name: Flyby Attack
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Diplomacy: 20
  Fly: 8
  Intimidate: 15
  Knowledge (arcana): 20
  Knowledge (dungeoneering): 20
  Knowledge (engineering): 15
  Knowledge (geography): 20
  Knowledge (history): 20
  Knowledge (local): 20
  Knowledge (nature): 20
  Knowledge (nobility): 20
  Knowledge (planes): 20
  Knowledge (religion): 20
  Linguistics: 15
  Perception: 27
  Sense Motive: 24
  Spellcraft: 28
  Use Magic Device: 20
languages:
- Abyssal
- Aquan
- Ancient Osiriani
- Auran
- Celestial
- Common
- Draconic
- Giant
- Ignan
- Infernal
- Jistka
- Sphinx
- Sylvan
- Tekritanin
- Terran
- telepathy 100 ft.
special_qualities:
- enigma
- sphinx monolith
ecology:
  environment: warm deserts
  organization: solitary
  treasure_type: standard
special_abilities:
  Enciphered Mind (Su): The forbidden knowledge elder sphinxes have accumulated is
    etched on their psyches, and it causes great harm to those who attempt to make
    psychic contact. Any creature attempting to contact an elder sphinx's mind or
    read its thoughts with a divination spell or similar ability must succeed at a
    DC 27 Will save or be overwhelmed by the chaos and vast scope of the knowledge
    within. Those who fail are affected by feeblemind. An elder sphinx can willingly
    suppress this ability at will as a free action. This is a mind-affecting effect,
    and the save DC is Charisma-based.
  Enigma (Su): Elder sphinxes have removed themselves from the mundane world to contemplate
    the mysteries of the universe-and beyond. To facilitate this, they possess an
    uncanny ability to elude detection and discovery by those that could possibly
    interrupt their meditations. Any creature (other than another sphinx), that leaves
    line of sight of an elder sphinx for more than 1 hour must succeed at a DC 27
    Will save or be unable to recall details of the encounter, as if the sphinx cast
    modify memory to eliminate all recollection of itself. The exact details of this
    memory loss are decided by the elder sphinx subconsciously during the encounter
    and it may eliminate up to an hour of memories. This is a mind-affecting compulsion
    effect and the save DC is Charisma-based.
  Litany of Riddles (Su): As a standard action, an elder sphinx can telepathically
    project a befuddling series of riddles, puzzles, and logic paradoxes at all creatures
    in a 60-foot cone. Creatures caught in this effect must succeed at a DC 27 Will
    save or be stunned for 1d4 rounds. Creatures that succeed against this effect
    glean snippets of lore from this brush with the sphinx's mind, granting them a
    +5 insight bonus on all Knowledge checks for 1 hour and the ability to attempt
    Knowledge checks with a DC higher than 10 untrained. Once a creature successfully
    saves against this ability, it can't be affected by the same elder sphinx's litany
    of riddles for 24 hours. This is a mind-affecting effect and the save DC is Charisma-based.
  Sphinx Monolith (Su): An elder sphinx can enter a state of suspended animation and
    transform its massive body into a stone monument. This transformation takes 1
    minute to complete, during which the elder sphinx is immobile. Once it transforms
    into its monolith form, the elder sphinx's body hardens to stone, granting it
    hardness 30 and 350 hit points. If the elder sphinx's stony body is reduced to
    0 hit points, it is destroyed and the elder sphinx is slain. While transformed,
    an elder sphinx doesn't need to breathe, eat, drink, or sleep. The elder sphinx
    is aware of its surroundings and it can use astral projection at will when in
    this form. Anytime an elder sphinx's body takes damage while using astral projection,
    its astral form immediately becomes aware that it is in danger and can, as a free
    action, end the astral projection and begin reverting back to its natural form
    (though the process still takes 1 minute). When an elder sphinx ends its transformation,
    it is immediately healed of all hit point damage it may have sustained while transformed.
    An elder sphinx can remain in its sphinx monolith form indefinitely.
desc_long: Older than most modern civilizations, elder sphinxes are the wisest and
  most venerable of sphinx kind. Though they have long since calcified into creatures
  of living limestone, these ancient creatures serve eternally as guardians, not of
  temples or other such terrestrial sites, but of forbidden knowledge and lore, much
  of which is beyond the understanding of lesser beings. Elder sphinxes are highly
  protective of the vast wealth of information they possess and strive to defend it
  from those they deem unworthy.

---

# Sphinx, Elder Sphinx
The brooding face of this towering limestone _[[spells/Statue|statue]]_ of a gynosphinx reflects a harsh wisdom acquired through untold ages of experience.
**Source** Pathfinder #83: The Slave Trenches of Hakotep pg. 90
**XP** 76,800

N Gargantuan magical beast
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +27

##### Defense

**AC** 29, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+1 Dex, +22 natural, –4 size)
**hp** 241 (21d10+126)
**Fort** +18, **Ref** +15, **Will** +19
**Defensive Abilities** enciphered mind, DR 15/adamantine and magic; **Immune** petrification; **SR** 27

##### Offense
**Speed** 40 ft., fly 60 ft. (poor)
**Melee** 2 claws +31 (2d6+14), 2 wings +26 (2d6+7)
**Space** 20 ft., **Reach** 15 ft.
**Special Attacks** litany of riddles, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +31, 2d6+14), _[[universal monster rules/Trample|trample]]_ (2d6+21, DC 34)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Nondetection|nondetection]]_, _[[spells/Read Magic|read magic]]_, _true seeing_
3/day—clairaudience/clairvoyance, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 21), _[[spells/Locate Object|locate object]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Sirocco|sirocco]]_ (DC 23)
1/day—_[[spells/Commune|commune]]_, _[[spells/Contact Other Plane|contact other plane]]_, _[[spells/Legend Lore|legend lore]]_
1/week—any one of the following: _[[spells/Symbol of Fear|symbol of fear]]_ (DC 22), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 23), _[[spells/Symbol of Sleep|symbol of sleep]]_ (DC 23), _[[spells/Symbol of Vulnerability|symbol of vulnerability]]_ (DC 26), _[[spells/Symbol Of Weakness|symbol of weakness]]_ (DC 24); all symbols last for 1 week maximum

##### Statistics
**Str** 39, **Dex** 12, **Con** 23, **Int** 26, **Wis** 30, **Cha** 25
**Base Atk** +21; **CMB** +39 (+41 bull rush); **CMD** 50 (52 vs. bull rush, 54 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Diplomacy +20, Fly +8, Intimidate +15, Knowledge (arcana) +20, Knowledge (dungeoneering) +20, Knowledge (engineering) +15, Knowledge (geography) +20, Knowledge (history) +20, Knowledge (local) +20, Knowledge (nature) +20, Knowledge (nobility) +20, Knowledge (planes) +20, Knowledge (religion) +20, Linguistics +15, Perception +27, Sense Motive +24, Spellcraft +28, Use Magic Device +20
**Languages** Abyssal, Aquan, Ancient Osiriani, Auran, Celestial, Common, Draconic, Giant, Ignan, Infernal, Jistka, Sphinx, Sylvan, Tekritanin, Terran; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** enigma, sphinx monolith

##### Ecology

**Environment** warm deserts
**Organization** solitary
**Treasure** standard

### Special Abilities

**Enciphered Mind (Su)** The forbidden knowledge elder sphinxes have accumulated is etched on their psyches, and it causes great _[[spells/Harm|harm]]_ to those who attempt to make _[[classes/Psychic|psychic]]_ contact. Any creature attempting to contact an elder sphinx’s mind or read its thoughts with a _[[spells/Divination|divination]]_ spell or similar ability must succeed at a DC 27 Will save or be overwhelmed by the chaos and vast scope of the knowledge within. Those who fail are affected by _[[spells/Feeblemind|feeblemind]]_. An elder sphinx can willingly suppress this ability at will as a free action. This is a mind-affecting effect, and the save DC is Charisma-based.

**Enigma (Su)** Elder sphinxes have removed themselves from the mundane world to contemplate the mysteries of the universe—and beyond. To facilitate this, they possess an uncanny ability to elude detection and discovery by those that could possibly interrupt their meditations. Any creature (other than another sphinx), that leaves line of sight of an elder sphinx for more than 1 hour must succeed at a DC 27 Will save or be unable to recall details of the encounter, as if the sphinx cast _[[spells/Modify Memory|modify memory]]_ to eliminate all recollection of itself. The exact details of this memory loss are decided by the elder sphinx subconsciously during the encounter and it may eliminate up to an hour of memories. This is a mind-affecting compulsion effect and the save DC is Charisma-based.

**Litany of Riddles (Su)** As a standard action, an elder sphinx can telepathically project a befuddling series of riddles, puzzles, and logic paradoxes at all creatures in a 60-foot cone. Creatures caught in this effect must succeed at a DC 27 Will save or be _[[conditions/Stunned|stunned]]_ for 1d4 rounds. Creatures that succeed against this effect glean snippets of lore from this brush with the sphinx’s mind, granting them a +5 insight bonus on all Knowledge checks for 1 hour and the ability to attempt Knowledge checks with a DC higher than 10 untrained. Once a creature successfully saves against this ability, it can’t be affected by the same elder sphinx’s litany of riddles for 24 hours. This is a mind-affecting effect and the save DC is Charisma-based.
**Sphinx Monolith (Su)** An elder sphinx can enter a state of suspended animation and transform its massive body into a stone monument. This _[[spells/Transformation|transformation]]_ takes 1 minute to complete, during which the elder sphinx is immobile. Once it transforms into its monolith form, the elder sphinx’s body hardens to stone, granting it hardness 30 and 350 hit points. If the elder sphinx’s stony body is reduced to 0 hit points, it is destroyed and the elder sphinx is slain. While transformed, an elder sphinx doesn’t need to breathe, eat, drink, or sleep. The elder sphinx is aware of its surroundings and it can use _[[spells/Astral Projection|astral projection]]_ at will when in this form. Anytime an elder sphinx’s body takes damage while using _astral projection_, its astral form immediately becomes aware that it is in danger and can, as a free action, end the _astral projection_ and begin reverting back to its natural form (though the process still takes 1 minute). When an elder sphinx ends its _transformation_, it is immediately healed of all hit point damage it may have sustained while transformed. An elder sphinx can remain in its sphinx monolith form indefinitely.

##### Description

Older than most modern civilizations, elder sphinxes are the wisest and most venerable of sphinx kind. Though they have long since calcified into creatures of living limestone, these ancient creatures serve eternally as guardians, not of temples or other such terrestrial sites, but of forbidden knowledge and lore, much of which is beyond the understanding of lesser beings. Elder sphinxes are highly protective of the vast wealth of information they possess and strive to defend it from those they deem unworthy.