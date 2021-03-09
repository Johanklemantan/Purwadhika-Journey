class Hero:
    Round = 1
    def __init__(self, name ,Health, Serangan, Defense):
        self.nama = name
        self.health = Health
        self.serangan = Serangan
        self.defense = Defense

 
    def attacked(self,lawannya_siapa,attack_yang_nyerang_berapa):
        Damage = attack_yang_nyerang_berapa/self.defense
        print('Damage:', round(Damage,0))
        print('Attacker HP Left: ',(round(lawannya_siapa.health,0)))
        self.health -= Damage
        print('Opponent HP Left: ',(round(self.health,0)))
        return Damage

    def attack(self,lawannya_siapa):
        # Damage = lawannya_siapa.attacked(self,self.serangan)
        # battlereport = Hero.battlereport(self,lawannya_siapa,Damage)
        print('Attacker :',self.nama)
        print('Opponent :',lawannya_siapa.nama)
        # Attacker = self.name
        # print(Saitama.serangan)
        # print(Genos.defense)
        lawannya_siapa.attacked(self,self.serangan)
        # return battlereport

    # @classmethod
    # @property
    def battlereport(self,lawannya_siapa):
        battlereport={
            # 'Hari ini' :'Lalala'
            'Round' : Hero.Round-1,
            'Attacker': self.nama,
            'Opponent': lawannya_siapa.nama,
            # # 'Damage' : self.Damage,
            'Attacker HP Left':round(self.health,0),
            'Opponent HP Left':round(lawannya_siapa.health,0)
        }
        return battlereport

    def game(self,lawannya_siapa):
        print(self.nama,':',self.health)
        print('')
        print('')
        print('VS')
        print('')
        print('')
        print(lawannya_siapa.nama,':',lawannya_siapa.health)
        print('')
        print('')
        bl = []
        while self.health>=0 and lawannya_siapa.health>=0:
            print('Ronde ke', Hero.Round)
            self.attack(lawannya_siapa)
            Hero.Round +=1
            bl.append(Hero.battlereport(self,lawannya_siapa))
            # Hero.battlereport(self,lawannya_siapa)
            print('')
            print('Ronde ke', Hero.Round)
            lawannya_siapa.attack(self)
            Hero.Round +=1
            bl.append(Hero.battlereport(self,lawannya_siapa))
            # Hero.battlereport(self,lawannya_siapa)
            if self.health<0:
                print(lawannya_siapa.nama,',WIN! After',Hero.Round,'Rounds')
            elif lawannya_siapa.health<0:
                print(self.nama,',WIN! After',Hero.Round,'Rounds')
            print('')
        # print('b1',bl)
        # return bl
        zz = int(input('Which round do you want to see the report ?:'))
        print(bl[zz])
    


Saitama = Hero('Saitama',5000,5000,300)
Genos = Hero('Genos',5000,2000,150)
Atomic_Samurai = Hero('Atomic Samurai',5000,3000,175)      



    # Saitama.attack(Genos)
    # print('')
    # Genos.attack(Saitama)
print('### Welcome to One Punch Man 1v1 ###')
print(f'Hero Available: (1) Saitama; (2) Genos; (3) Atomic Samurai')
a = int(input('Choose Your First Hero!:'))
if a > 3:
    print('Invalid Input')   
b = int(input('Choose Your Second Hero!:'))
if b > 3:
    print('Invalid Input')
x = Saitama.nama
y = Genos.nama
z = Atomic_Samurai.nama
if a == 1 and b == 2:
    print(f'My name is',x,'I am a hero!\nMy name is',y,'I am a Hero!' )
    Hero.game(Saitama,Genos)
elif a == 1 and b == 3:
    print(f'My name is',x,'I am a hero!\nMy name is',z,'I am a Hero!' )
    Hero.game(Saitama,Atomic_Samurai)
elif a == 2 and b == 1:
    print(f'My name is',y,'I am a hero!\nMy name is',x,'I am a Hero!' )
    Hero.game(Genos,Saitama)
elif a == 2 and b == 3:
    print(f'My name is',y,'I am a hero!\nMy name is',z,'I am a Hero!' )
    Hero.game(Genos,Atomic_Samurai)
elif a == 3 and b == 1:
    print(f'My name is',z,'I am a hero!\nMy name is',x,'I am a Hero!' )
    Hero.game(Atomic_Samurai,Saitama)
elif a == 3 and b == 2:
    print(f'My name is',z,'I am a hero!\nMy name is',y,'I am a Hero!' )
    Hero.game(Atomic_Samurai,Genos)


# Hero.manggil(zz)
    