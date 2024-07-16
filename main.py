from src.population import Population

def founder(Target_string,Mutation_rate,Population_size,No_of_generations,number_of_parents):
    ppl=Population(Target_string,Mutation_rate,Population_size,number_of_parents)
    ppl_list=ppl.generate_population()
    for i in range(No_of_generations):
        print("\n\n#######################################\n\n")
        ppl_fitness=ppl.calculate_fitness(ppl_list)
        if ppl_fitness==-1:
          print("Generation :",i)
          print("Population Size :",ppl.n)
          print("Mutation rate :",ppl.mutation_rate*100,"%")
          break
        ppl_mating_pool=ppl.natural_selection(ppl_list,ppl_fitness)
        new_ppl_list=ppl.generate_new_population(ppl_mating_pool)
        for j in (new_ppl_list):
            print("Generation : ",i,"\t Variant : ",j,"\tBest fitness Score ",ppl.best_fitness_score)
        ppl_list=new_ppl_list

Mutation_rate=0.1
Population_size=200
Target_string="Harsh is a data enthusiast"
No_of_generations=10000
Number_of_parents=2
founder(Target_string,Mutation_rate,Population_size,No_of_generations,Number_of_parents)