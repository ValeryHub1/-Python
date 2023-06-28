class Cassa:
    summa=45875

    def top_up(self, pokup):
        self.pokup=pokup
        pokup+=Cassa.summa
        return f"в кассе {pokup}"
    
    def count_1000(self):
        print(Cassa.summa//1000)

    def take_away(self, x):
        if x<=self.summa:
            self.summa-=x
        else:
            return f"не достаточно денег"
r=Cassa()
print(r.top_up(125))