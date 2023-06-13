---
cssclass: [monsters]
title1: Daemonic Harbinger, Braismois
desc_short: This humanoid fiend has an overly long torso, black eyes, and a mouth
  full of razor-sharp teeth. It wears black robes that cover most of its rotting,
  frostbitten flesh.
title2: Braismois
CR: 22
sources:
- name: Druma, Profit and Prophecy
  page: 58
  link: https://paizo.com/products/btq01zow
XP: 614400
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 15
senses:
  darkvision: 60
  true seeing: true
auras:
- name: fine print
  radius: 120
AC:
  AC: 40
  touch: 28
  flat_footed: 30
  components:
    deflection: 8
    dex: 10
    natural: 12
HP:
  HP: 377
  long: 26d10+234
saves:
  fort: 17
  ref: 25
  will: 24
DR:
- amount: 20
  weakness: good and silver
immunities:
- acid
- charm
- compulsion
- death effects
- disease
- emotion
- enchantments
- mind-reading
- poison
resistances:
  cold: 30
  electricity: 30
  fire: 30
SR: 33
speeds:
  base: 30
  burrow: 60
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: toxic quill +41/+36/+31/+26 (3d6+15/17-20 plus poison)
      entries:
      - - damage: 3d6+15
          crit_range: 17-20
        - effect: poison
      attack: toxic quill
      bonus:
      - 41
      - 36
      - 31
      - 26
  ranged:
  - - text: toxic quill +41 (3d6+15/17-20 plus poison)
      entries:
      - - damage: 3d6+15
          crit_range: 17-20
        - effect: poison
      attack: toxic quill
      bonus:
      - 41
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
  - name: mirror image
    source: default
    freq: At will
  - name: displacement
    source: default
    freq: 3/day
  - name: quickened mirror image
    source: default
    freq: 3/day
  - name: power word blind
    source: default
    freq: 3/day
  - name: power word stun
    source: default
    freq: 3/day
  - name: symbol of insanity
    source: default
    freq: 3/day
    DC: 27
  - name: symbol of persuasion
    source: default
    freq: 3/day
    DC: 25
  - name: symbol of strife
    source: default
    freq: 3/day
    DC: 28
  - name: symbol of stunning
    source: default
    freq: 3/day
    DC: 26
  - name: quickened mass hold person
    source: default
    freq: 1/day
    DC: 26
  - name: overwhelming presence
    source: default
    freq: 1/day
    DC: 28
  - name: quickened power word kill
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 26
    concentration: 35
ability_scores:
  STR: 21
  DEX: 30
  CON: 28
  INT: 25
  WIS: 28
  CHA: 29
BAB: 26
CMB: 31
CMD: 59
feats:
- name: Ability Focus
- name: Combat Casting
- name: Combat Expertise
- name: Deadly Aim
- name: Greater Vital Strike
- name: Improved Critical (dagger)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Quicken Spell-Like Ability (mass hold person)
- name: Quicken Spell-Like Ability (mirror image)
- name: Quicken Spell-Like Ability (power word kill)
- name: Vital Strike
- name: Weapon Finesse
skills:
  Appraise: 20
  Bluff: 38
  Diplomacy: 38
  Disguise: 35
  Fly: 34
  Intimidate: 38
  Knowledge (history): 20
  Knowledge (nobility): 33
  Knowledge (planes): 23
  Linguistics: 36
  Perception: 38
  Profession (barrister): 38
  Sense Motive: 38
  Spellcraft: 33
  Stealth: 39
languages:
- Abyssal
- Common
- Dwarven
- Elven
- Gnome
- Halfling
- Infernal
- telepathy 300 ft.
special_qualities:
- daemonic harbinger traits
- deft of hand
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: triple
special_abilities:
  Daemonic Harbinger Traits: A daemonic harbinger is a powerful daemon that has not
    yet made the full transition from unique daemon to a horseman. It has several
    traits, as summarized here. Immunity to acid, charm and compulsion effects, death
    effects, disease, and poison. Resistance to cold 30, electricity 30, and fire
    30. Telepathy 300 feet. The harbinger's natural weapons, as well as any weapon
    it wields, are treated as evil for the purpose of overcoming damage reduction.
    The harbinger can grant spells to its worshipers. Granting spells does not require
    any specific action on its behalf. Braismois grants access to the domains of Evil,
    Knowledge, Rune and Trickery. His favored weapon is the light mace.
  Deft of Hand (Ex): Braismois wields his quill as both an instrument of ensnarement
    and a deadly weapon. He always adds his Dexterity bonus to damage rolls with his
    toxic quill. In addition, Braismois can add his Dexterity bonus to any skill check
    related to writing. As a swift action, Braismois can attempt a Profession (barrister)
    check to write a full contract for any situation. The result of this check is
    the DC for creatures attempting a Linguistics or Profession (barrister) check
    to identify loopholes or flaws within the contract in Braismois's favor.
  Fine Print Aura (Su): All written texts within the radius of this aura become unintelligibly
    dense and convoluted. Scrolls used within the aura automatically risk a mishap;
    the DC of the Wisdom check required to negate the mishap is 15 instead of DC 5.
    A scroll's user can spend a move action to attempt a DC 30 Linguistics or Profession
    (barrister) check to parse the text and use the scroll normally; failing this
    check results in a mishap.
  Toxic Quill (Su): "Braismois's quill is a manifestation of his spirit and is treated\
    \ as a +5 dagger that functions as a natural attack and deals 3d6 points of piercing\
    \ damage on a hit. Braismois can throw the quill as a ranged attack against any\
    \ creature within 120 feet. As a full-round action, he can instead make a ranged\
    \ attack against all foes within 60 feet. Braismois can instantly re-form his\
    \ toxic quill as a free action. For each attack Braismois makes with the quill,\
    \ he can select one of the following poisons to apply to the attack. If the attack\
    \ is a confirmed critical hit, the DC of the poison increases by 6 and can affect\
    \ creatures with poison immunity. The save DCs are Constitution-based. Broken\
    \ Oath: injury; save Fort DC 32; frequency 1/minute for 10 minutes; effect 1d6\
    \ Wis and controlled by Braismois as per dominate monster for the duration of\
    \ the poison; cure 2 consecutive saves. Promise of Power: injury; save Fort DC\
    \ 32; frequency 2/round for 3 rounds; effect 2d6 Str; cure 2 consecutive saves\
    \ or agree to telepathically transmitted contract with Braismois, which acts as\
    \ a geas and instantly heals the applied ability damage. Silence: injury; save\
    \ Fort DC 32; frequency 1/round for 6 rounds; effect 2d4 Con damage and cannot\
    \ speak until the ability damage is healed; cure 2 consecutive saves."
desc_long: |-
  Braismois, the Silent Quill, sometimes referred to as the Toxic Quill by those misinterpreting his weapon as his title, is the daemonic harbinger of broken deals, fine print, and unfair bargains. A being of immense power, Braismois currently serves Trelmarixian, the Horseman of Famine, though only to fulfill an ongoing contract with the horseman. Braismois appears as a frostbitten human with weasel-like features, bedecked in ink-smeared clothing. His followers are generally administrators, barristers, clerks, or those highly placed in judicial or political environments. Braismois preys on mortals unable to fully grasp his contracts, though he enjoys a challenge and seeks out haughty nobles or intellectuals who believe themselves immune to such treachery. He frequently appears to powerful and influential mortals to seed contracts and deals across the Material Plane.

   The harbinger of broken deals rules from the Silent Nation, an expansive set of tunnels dug into the bottom of a glacier in Abaddon. Deep within the glacier, Braismois maintains a vast library of all the contacts and documentation on his various schemes throughout the cosmos, with each plane and world tended to by its own unique bibliodaemon caretaker. Braismois also keeps the true versions of many historical records that he and his agents have altered or replaced over the years as vainglorious trophies within his archival sanctum.

   Those who serve Braismois in life end up as hunted petitioners doomed to roam the mazelike tunnels of the Silent Nation's lowest depths. Petitioners struggle eternally to decipher detailed but purposely inaccurate directions carved into the walls; those who fail to recognize the directions as falsehoods wander forever, those who recognize them as lies are quickly consumed by warden daemons, and those who put up misleading directions of their own to lead others into harm are elevated to the ranks of lesser daemonhood.

   Over a century ago, Braismois turned his attention to the nation of Druma and its Kalistocracy. A member of the esteemed Petronax family had come to learn the truth of the Kalistocracy's promised afterlife and saw it as little more than delaying an inevitable judgment by Pharasma. This prophet betrayed the Kalistocracy and, using ancient Kellid rituals and profane tools uncovered in the Palakar Forest, communed with Braismois to share the discovery. Braismois fumed at the Kalistocracy's subversion of death, as any daemon would in their role as the wouldbe enders of all life. Having learned one of the greatest secrets on Golarion, Braismois has kept the information to himself, using the well-positioned Petronax family to weaken the Kalistocracy and pave the way for a daemonic incursion into the heart of the nation. It is through this culminating scheme that Braismois hopes to unearth the hidden tombs of Kalistrade's prophets and gorge on the untold number of souls removed from the cycle of death-an act that Braismois hopes will grant him enough power to challenge and supplant Charon as the Horseman of Death.

---

# Daemonic Harbinger, Braismois
This humanoid fiend has an overly long torso, black eyes, and a mouth full of razor-sharp teeth. It wears black robes that cover most of its rotting, frostbitten flesh.
**Source** Druma, Profit and Prophecy pg. 58
**XP** 614,400

NE Medium outsider (daemon, evil, extraplanar)
**Init** +15; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +38
**Aura** fine print (120 ft.)

##### Defense

**AC** 40, touch 28, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+8 _[[spells/Deflection|deflection]]_, +10 Dex, +12 natural)
**hp** 377 (26d10+234)
**Fort** +17, **Ref** +25, **Will** +24
**DR** 20/good and silver; **Immune** acid, charm, compulsion, death effects, disease, emotion, enchantments, mind-reading, poison; **Resist** cold 30, electricity 30, fire 30; **SR** 33

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 60 ft., fly 60 ft. (perfect)
**Melee** _[[items/Weapon Magic Abilities/Toxic|toxic]]_ quill +41/+36/+31/+26 (3d6+15/17–20 plus poison)
**Ranged** _toxic_ quill +41 (3d6+15/17–20 plus poison)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 26th; concentration +35)
Constant—_true seeing_ 
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Mirror Image|mirror image]]_ 
3/day—_[[spells/Displacement|displacement]]_, quickened _mirror image_, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 27), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 25), _[[spells/Symbol of Strife|symbol of strife]]_ (DC 28), _[[spells/Symbol of Stunning|symbol of stunning]]_ (DC 26) 
1/day—quickened mass _[[spells/Hold Person|hold person]]_ (DC 26), _[[spells/Overwhelming Presence|overwhelming presence]]_ (DC 28), quickened _[[spells/Power Word Kill|power word kill]]_

##### Statistics
**Str** 21, **Dex** 30, **Con** 28, **Int** 25, **Wis** 28, **Cha** 29
**Base Atk** 26; **CMB** 31; **CMD** 59
**Feats** _[[feats/Ability Focus|Ability Focus]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Dagger|dagger]]_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (mass _hold person_), _Quicken Spell-Like Ability_ (_mirror image_), _Quicken Spell-Like Ability_ (_power word kill_), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Appraise +20, Bluff +38, Diplomacy +38, Disguise +35, Fly +34, Intimidate +38, Knowledge (history) +20, Knowledge (nobility) +33, Knowledge (planes) +23, Linguistics +36, Perception +38, Profession (barrister) +38, Sense Motive +38, Spellcraft +33, Stealth +39
**Languages** Abyssal, Common, Dwarven, Elven, Gnome, Halfling, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** daemonic harbinger traits, deft of hand

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** triple

### Special Abilities

**Daemonic Harbinger Traits** A daemonic harbinger is a powerful daemon that has not yet made the full transition from unique daemon to a horseman. It has several traits, as summarized here.

* _[[universal monster rules/Immunity|Immunity]]_ to acid, charm and compulsion effects, death effects, disease, and poison. 
* _[[universal monster rules/Resistance|Resistance]]_ to cold 30, electricity 30, and fire 30. 
* _Telepathy_ 300 feet. 
* The harbinger's natural weapons, as well as any weapon it wields, are treated as evil for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. 
* The harbinger can grant spells to its worshipers. Granting spells does not require any specific action on its behalf. Braismois grants access to the domains of Evil, Knowledge, Rune and Trickery. His favored weapon is the _[[items/Weapon/Light mace|light mace]]_.

**Deft of Hand (Ex)** Braismois wields his quill as both an instrument of ensnarement and a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ weapon. He always adds his Dexterity bonus to damage rolls with his _toxic_ quill. In addition, Braismois can add his Dexterity bonus to any skill check related to writing. As a swift action, Braismois can attempt a Profession (barrister) check to write a full contract for any situation. The result of this check is the DC for creatures attempting a Linguistics or Profession (barrister) check to _[[spells/Identify|identify]]_ loopholes or flaws within the contract in Braismois's favor.

**Fine Print Aura (Su)** All written texts within the radius of this aura become unintelligibly dense and convoluted. Scrolls used within the aura automatically risk a mishap; the DC of the Wisdom check required to negate the mishap is 15 instead of DC 5. A scroll's user can spend a move action to attempt a DC 30 Linguistics or Profession (barrister) check to parse the text and use the scroll normally; failing this check results in a mishap.

**_Toxic_ Quill (Su)** Braismois's quill is a manifestation of his spirit and is treated as a +5 _dagger_ that functions as a natural attack and deals 3d6 points of piercing damage on a hit. Braismois can throw the quill as a ranged attack against any creature within 120 feet. As a full-round action, he can instead make a ranged attack against all foes within 60 feet. Braismois can instantly re-form his _toxic_ quill as a free action. For each attack Braismois makes with the quill, he can select one of the following poisons to apply to the attack. If the attack is a confirmed critical hit, the DC of the poison increases by 6 and can affect creatures with poison _immunity_. The save DCs are Constitution-based.

* _[[conditions/Broken|Broken]]_ Oath: injury; save Fort DC 32; frequency 1/minute for 10 minutes; effect 1d6 Wis and controlled by Braismois as per _[[spells/Dominate Monster|dominate monster]]_ for the duration of the poison; cure 2 consecutive saves. 
* Promise of Power: injury; save Fort DC 32; frequency 2/round for 3 rounds; effect 2d6 Str; cure 2 consecutive saves or agree to telepathically transmitted contract with Braismois, which acts as a geas and instantly heals the applied ability damage. 
* _[[spells/Silence|Silence]]_: injury; save Fort DC 32; frequency 1/round for 6 rounds; effect 2d4 Con damage and cannot speak until the ability damage is healed; cure 2 consecutive saves.

##### Description

Braismois, the Silent Quill, sometimes referred to as the _Toxic_ Quill by those misinterpreting his weapon as his title, is the daemonic harbinger of _broken_ deals, fine print, and unfair bargains. A being of immense power, Braismois currently serves Trelmarixian, the Horseman of _[[curses/Famine|Famine]]_, though only to fulfill an ongoing contract with the horseman. Braismois appears as a frostbitten human with weasel-like features, bedecked in ink-smeared clothing. His followers are generally administrators, barristers, clerks, or those highly placed in judicial or political environments. Braismois preys on mortals unable to fully _[[spells/Grasp|grasp]]_ his contracts, though he enjoys a challenge and seeks out haughty nobles or intellectuals who believe themselves immune to such treachery. He frequently appears to powerful and influential mortals to seed contracts and deals across the Material Plane.

The harbinger of _broken_ deals rules from the Silent Nation, an expansive set of tunnels dug into the bottom of a glacier in Abaddon. Deep within the glacier, Braismois maintains a vast library of all the contacts and documentation on his various schemes throughout the cosmos, with each plane and world tended to by its own unique bibliodaemon caretaker. Braismois also keeps the true versions of many historical records that he and his agents have altered or replaced over the years as vainglorious trophies within his archival sanctum.

Those who serve Braismois in life end up as hunted petitioners doomed to roam the mazelike tunnels of the Silent Nation’s lowest depths. Petitioners struggle eternally to decipher detailed but purposely inaccurate directions carved into the walls; those who fail to recognize the directions as falsehoods wander forever, those who recognize them as lies are quickly consumed by warden daemons, and those who put up misleading directions of their own to lead others into _[[spells/Harm|harm]]_ are elevated to the ranks of lesser daemonhood.

Over a century ago, Braismois turned his attention to the nation of Druma and its Kalistocracy. A member of the esteemed Petronax family had come to learn the truth of the Kalistocracy’s promised afterlife and _[[items/Mundane/Saw|saw]]_ it as little more than delaying an inevitable judgment by Pharasma. This _[[feats/Prophet|prophet]]_ _[[feats/Betrayed|betrayed]]_ the Kalistocracy and, using ancient Kellid rituals and profane tools uncovered in the Palakar Forest, communed with Braismois to share the discovery. Braismois fumed at the Kalistocracy’s subversion of death, as any daemon would in their role as the wouldbe enders of all life. Having learned one of the greatest secrets on Golarion, Braismois has kept the information to himself, using the well-positioned Petronax family to weaken the Kalistocracy and pave the way for a daemonic incursion into the heart of the nation. It is through this culminating scheme that Braismois hopes to unearth the hidden tombs of Kalistrade’s prophets and gorge on the untold number of souls removed from the cycle of death—an act that Braismois hopes will grant him enough power to challenge and supplant Charon as the Horseman of Death.