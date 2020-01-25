# ****H.W****

## Exercise 1
The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc. But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one". 
In this mission you’ll get your chance.

Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. 

This class should have a few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".

##### Dialog for the human should be displayed like this:
(human name) said: message text
(robot serial number): message text

For the robot:
(human name) said: 11100100011
(robot serial number) said: 100011100101
Interlocutors should have a send() method for sending messages to the dialog.

Example:
chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi!...


## Exercise 2

### Part I - “The Warriors”Part I - “The Warriors”
One day, on a typical spring afternoon, Sir Ronald has been looking around his land, riding a horse. Nothing foretold troubles, when suddenly Sir Ronald heard a scream for help, coming from somewhere nearby: 
- "Help! Help!" - shouted a piercing young girl's voice. 
As a true knight, Sir Ronald couldn’t stay away and went to the lady’s rescue. Rushing in the direction from which the cry came, he saw a carriage. The girl peered out the window hoping to see someone who could help her. 
- "Stop!"- ordered Sir Ronald to the coachman. - "By what right are you on my land?" 
The coachman didn’t get a chance to open his mouth, as his master came out of the carriage. 
- "My respects, noble sir. I had no idea that this land is yours. My bride and I were just going to my estate, not wanting to give anyone any trouble. "
- "A flat-out lie! I'm not his bride!" - the girl exclaimed from the window. 
- "Explain yourself, Sir. What does that mean?",- said Sir Ronald. 
- "Of course. The king of a neighboring country has promised his daughter and half his kingdom to the one who’ll save her from the outlaws who took her. I’ve defeated those bastards and now I’m taking the princess to her father. "
- "It's not true! They were in on it together They’ve kidnapped me on his order! I saw how he paid them a bag of gold!" - The princess didn’t stop taking for a second, trying to quickly describe the situation to the miraculously appeared savior. 
- "Such behavior is unworthy of a knight! Prepare to die!",- exclaimed Sir Ronald, drawing his sword. - "Ha-ha-ha, simple-hearted nobleman! We’ll see about that..."
I'm sure that many of you have some experience with computer games. But have you ever wanted to change the game so that the characters or a game world would be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair" and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel. You need to create the class Warrior, the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a function fight(), which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
every turn one of the warriors will hit another one and the last will lose his health in the same value as the attack of the first warrior. After that, the second warrior will do the same to the first one.
If in the end of the turn the first warrior has > 0 health and the other one doesn’t, the function should return True, in the other case it should return False.

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
 
fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
Input: The warriors.
Output: The result of the duel (True or False).
How it is used: For computer games development.
Precondition: 2 types of units

## Part II - “Army Battles”
...Sir Ronald’s opponent - Umbert, has proved to be a very skillful warrior. In addition, he was a good fifteen years younger, which gave him a certain advantage. But Sir Ronald was also very strong - he had the experience of participation in many battles and in several major wars behind his back. And besides that, in his youth he was known as the best duelist in this land. 
Realizing that the forces are equal, each of them had followed the only course possible - to call for help. Umbert sent for the reinforcement his coachman on a horse, and Sir Ronald used a family horn that sounded more than once in hot battles. The knight's castle was close enough for the call to arms was heard back there. Nobody quite knew where the Umbert's accomplices were located, and this made it difficult to come up with a strategy for the battle ahead. 
Fortunately, the reinforcements for both sides arrived almost simultaneously. Now it was more than a question of the girl's honor. There was no peaceful solutions to this matter. One of the two armies must be destroyed.
In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the  fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.
Note that army 1 have the advantage...

## Part III: The Defenders, The Vampires, The Lancers, The Healers
...the clashes between different soldiers occurred here and there, and the new troops kept coming. The conflict gradually was starting to look more like a small war. 
"Knights, hear my command! Take your shields! Strengthen the armor! We are taking too much beating," - Sir Ronald shouted. 
Nobody’s expected that Umbert's soldiers could compete with the well-trained knights, so at the beginning of the battle the knights used exclusively two-handed swords - no one even thought of being on the defensive. But it seems that it's time to back down and take one-handed swords and shields instead of the former deadly weapons. This will slightly reduce the assault capacity of knights, but will allow them to better defend themselves against the dangerous attacks of enemy soldiers.
In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
 
fight(chuck, bruce) == True
fight(dave, carl) ==...
The warriors and armies.
The result of the battle (True or False).
For the computer games development.
From now on, the tests from "check" part will use another type of warrior: the rookie. Its code is
class Rookie(Warrior):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.health = 50
       self.attack = 1
The flocks of crows circled over the battlefield. Many brave warriors have fallen in this battle, many have continued to fight. 
"If this goes on, we’ll simply kill each other, and there will be no winners - we’ll all lose." - reflected Sir Ronald, watching a bleak picture in front of him. 
"I have to make an important decision. I know what it’ll cost, but now that’s the only thing that can save us all..." 
A long time ago, when he was often in search of trouble and adventure, he went to hunt a witch who had a huge bounty on her head. The bloody creature was able to save her life by persuading the knight to take a gift from her - a vial of vampire blood. This blood poured into the dying man’s mouth could bring him back to life in vampire form.
Is it really the day when he has to use it?.. 
It seemed to be the only way to win this battle. 
Sir Ronald began to lean over the barely living bodies of his knights, who were lying beside him. To each of them he said: 
- "Drink. You’ll be given a new life..."
So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
 
fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive...
... the vampires fought fiercely. Judging by the course of the battle, Sir Ronald made the right decision, although not very ethically ambiguous. 
Suddenly, new soldiers joined the Umbert’s ranks - has he really got an ace up his sleeve? Lancers presented the fresh forces, which made Sir Ronald’s position increasingly difficult, lancers could attack two soldiers at once with their long spears. Something needed to be done with that…
It seems that the Warrior, Knight, Defender and Vampire are not enough to win the battle. Let's add one more powerful unit type - the Lancer.
Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits the other unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower - consider this).
The basic parameters of the Lancer:
health = 50
attack = 6
 

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
freelancer = Lancer()
vampire = Vampire()
 
fight(chuck, bruce) == True
fight(dave,...
...the balance of power was once again not on the knights’ side. 
Sir Ronald used the horn one more time to summon the last hope for his army - the healers. The temple they lived in was even closer than the castle from which the first wave of reinforcements arrived. If the healers get here fast enough, they’ll save many lives and the knights will have a chance to win.
The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal the damage). But his role is also very important - every time the allied soldier hits the enemy, the Healer will heal the allie, standing right in front of him by +2 health points with the heal() method. Note that the health after healing can't be greater than the maximum health of the unit. For example, if the Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
freelancer = Lancer()
vampire = Vampire()
priest = Healer()
 
fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob,...

## Part IV - Straight Fight
...despite all of the tactical measures that have been undertaken, neither side still hasn’t had a victory. Therefore, the two army commanders decided to change tactics and immediately arrange a battle where all survived soldiers of one armie will be fighting all of the survivors of the other.
A new unit type won’t be added in this mission, but instead we’ll add a new tactic - straight_fight(army_1, army_2). It should be the method of the Battle class and it should work as follows:
at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against the first, the second against the second and so on). After that all dead soldiers will be removed and the process repeats until all soldiers of one of the armies will be dead. Armies might not have the same number of soldiers. If a warrior doesn’t have an opponent from the enemy army - we’ll automatically assume that he’s won a duel (for example - 9th and 10th units from the first army, if the second has only 8 soldiers).

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
freelancer = Lancer()
vampire = Vampire()
priest = Healer()
 
fight(chuck, bruce) == True
fight(dave,...

## Part V - The Weapons
... the battle lasted long enough and Sir Ronald have sent a messenger to the castle who had to deliver an order: "Open the weapons storehouse and bring everything to the battlefield." The last serious war has ended a long time ago, so the arsenal wasn’t too impressive, but one could find a few useful things, like better swords and shields, two-handed battle axes, and even the quite rare for these places, katana and wands. 
Perhaps, those weapons can turn the battle around...
In this mission you should create a new class Weapon(health, attack, defense, vampirism, heal_power) which will equip your soldiers with weapons. Every weapon's object will have the parameters that will show how the soldier's characteristics change while he uses this weapon. Assume that if the soldier doesn't have some of the characteristics (for example, defense or vampirism), but the weapon have those, these parameters don't need to be added to the soldier.
 
The parameters list:
health - add to the current health and the maximum health of the soldier this modificator;
attack - add to the soldier's attack this modificator;
defense - add to the soldier's defense this modificator;
vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
heal_power - increase the amount of health which the healer restore for the allied unit.
 
All parameters could be positive or negative, so when a negative modificator is being added to the soldier’s stats, they are decreasing, but none of them can be less than 0.
 
Let’s look at this example: vampire (basic parameters: health = 40, attack = 4, vampirism = 50%) equip the Weapon(20, 5, 2, -60, -1). The vampire has the health and the attack, so they will change - health will grow up to 60 (40 + 20), attack will be 9 (4 + 5). The vampire doesn’t have defense or the heal_power, so these weapon modificators will be ignored. The weapon's vampirism modificator -60% will work as well. The standard vampirism value is only 50%, so we’ll get -10%. But, as we said before, the parameters can’t be less than 0, so the vampirism after all manipulations will be just 0%.
 
Also you should create a few standard weapons classes, which should be the subclasses of the Weapon. Here’s their list:
Sword - health +5, attack +2
Shield - health +20, attack -1, defense +2
a - health -15, attack +5, defense -2, vampirism +10%
Katana - health -20, attack +6, defense -5, vampirism +50%
MagicWand - health +30, attack +3, heal_power +3
 
And finally, you should add an equip_weapon(weapon_name) method to all of the soldiers classes. It should equip the chosen soldier with the chosen weapon.
This method also should work for the units in the army. You should hold them in the list and use it like this:
my_army.units[0].equip_weapon(Sword()) - equip the first soldier with the sword.
 
Notes:
While healing (both vampirism and health restored by the healer), the health can’t be greater than the maximum amount of health for this unit (with consideration of all of the weapon's modificators).
If the heal from vampirism is float (for example 3.6, 1.1, 2.945), round it down in any case. So 3.6 = 3, 1.1 = 1, 2.945 = 2.
Every soldier can be equipped with any number of weapons and get all their bonuses, but if he wears too much weapons with the negative health modificator and his health is lower or equal 0 - he is as good as dead, which is actually pretty dead in this case.

Example:
ogre = Warrior()
lancelot = Knight()
richard = Defender()
eric = Vampire()
freelancer = Lancer()
priest = Healer()
 
sword = Sword()
shield = Shield()
axe = GreatAxe()
katana = Katana()
wand = MagicWand()
super_weapon = Weapon(50, 10, 5, 150, 8)
 
ogre.equip_weapon(sword)
ogre.equip_weapon(shield)
ogre.equip_weapon(super_weapon)
lancelot.equip_weapon(super_weapon)
richard.equip_weapon(shield)
eric.equip_weapon(super_weapon)
freelancer.equip_weapon(axe)
freelancer.equip_weapon(katana)
priest.equip_weapon(wand)
priest.equip_weapon(shield)
 
ogre.health == 125
lancelot.attack == 17
richard.defense == 4aa
eric.vampirism == 200
freelancer.health == 15
priest.heal_power...


## Part VI - The Walords

... after all the efforts, sir Ronald couldn't win the battle. He finally realized that this isn’t just a small fight, but a full-fledged battle, and he needs to apply all his experience to effectively manage his army.
It looks like this time the outcome of the battle will be decided once and for all.
In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the next characteristics:
health = 100
attack = 4
defense = 2
 
Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which allows to rearrange the units of that army for the better battle result. The rearrangement is done not only before the battle, but during the battle too, each time the allied units die. The rules for the rearrangement are as follow:
If there are Lancers in the army, they should be placed in front of everyone else.
If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight. If the number of Healers is > 1, all of them should be placed right behind the first Healer.
If there are no more Lancers in the army, but there are other soldiers who...

