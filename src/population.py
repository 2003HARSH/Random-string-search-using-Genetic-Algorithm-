import random
from src.dna import Dna

class Population:
    def __init__(self,target_string,mutation_rate,n,number_of_parents) -> None:
        self.target_string=target_string
        self.mutation_rate=mutation_rate
        self.n=n
        self.best_fitness_score=0
        self.most_fit_element=''
        self.number_of_parents=number_of_parents
    
    def generate_population(self):
        l=[]
        for i in range(self.n):
            dna=Dna(len(self.target_string))
            l.append(dna.word)
        return l

    def calculate_fitness(self,population_list):
        fitness_scores=[]
        for j in range(self.n):
            score=0.0
            for i in range(0,len(self.target_string)):
                if population_list[j][i]==self.target_string[i] :
                    score+=1.0
            if score==len(self.target_string):
                print("Match Found : ",population_list[j])
                return -1

            fitness_scores.append((score/len(self.target_string)*10))
        return fitness_scores

    def natural_selection(self,population_list,fitness_scores):
        mating_pool=[]
        self.best_fitness_score=max(fitness_scores)
        for i in range(int(self.number_of_parents)):
          ele=max(fitness_scores)
          ind=fitness_scores.index(ele)
          app_ele=population_list[ind]
          mating_pool.append(app_ele)
          population_list.pop(ind)
          fitness_scores.pop(ind)

        if len(mating_pool)==0:
            mating_pool=population_list
        return mating_pool

    def generate_new_population(self,mating_pool):
        new_population=[]
        for i in range(self.n):
            parent1=mating_pool[random.randint(0,len(mating_pool)-1)]
            parent2=mating_pool[random.randint(0,len(mating_pool)-1)]
            child=Dna.crossover(parent1,parent2)
            new_child=Dna.mutation(child,self.mutation_rate)
            new_population.append(new_child)
        return new_population