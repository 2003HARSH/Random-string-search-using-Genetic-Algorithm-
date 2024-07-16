import string
import random

class Dna:
    total_char=(string.ascii_letters+' 1234567890')
    def __init__(self,num) -> None:
        self.num=num
        self.word=self.generate()
    
    def generate(self): #generate a random string
        word=''
        for i in range(0,self.num):
            word=word+Dna.total_char[random.randint(0,len(Dna.total_char)-1)]
        return word

    @staticmethod
    def crossover(parent1,parent2):
        length=len(parent1)
        length_2=int((len(parent1))/2)        
        return (parent1[0: length_2]  +  parent2[length_2:length])
    
    @staticmethod
    def mutation(child,mutation_rate):
        total_char=(string.ascii_letters+' 1234567890')
        new_child=''
        for i in range(len(child)):   
            if random.random()<mutation_rate:
                new_child+=total_char[random.randint(0,len(total_char)-1)]
            else:
                new_child+=child[i]
        return new_child