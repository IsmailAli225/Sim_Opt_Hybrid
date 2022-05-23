import random
import pandas as pd
from javaconnectormulti import *
import GA_Functions
import time
import copy


## Intital Parameters
Num_runs = 30
min_year = "1/1/2019"
max_year = "1/1/2028"
n = 5
N = 30  # Length of the solution
nPOP = 10  # Length of the Population
record = []
cr = 0.5
f = 0.7
num_generations = 5000  # Total number of Generation
Best_ResScore = []
Best_ResWeek = []
Best_ResSol = []
model = CapabilityModelMultiRunConnector()
# Available assets for each solution in the population presented by 3-d array
Vol, w, h = 4, 21, Num_runs
Avail_Assets_RUN = [[[0 for k in range(Vol)] for j in range(w)] for i in range(h)]  # Level of Runs
for run in range(Num_runs):
    # INPUT
    # # In this Array, all available assets will be listed...
    # # The array is updated during the running to reflect changes occured by each action.
    # ACQUISITION will add assets to its particular B and config.
    # UPGRADE and RETIREMENT will reduce assets from its particular B and config.

    ######  EXAMPLE     #######################################
    #             B1_UNASSIGNED     B2_UNASSIGNED   B3_UNASSIGNED       ENABLING_B1_UNASSIGNED
    # A TROOP           10                 10              10                   10
    # A C2              6                   6               6                   12
    # OLD TANK          2                   2               2                   0
    # ADD ROW AS NEW CONFIGURATION IS ACQUIRED
    w, h = 4, 21
    Initial_Avail_Assets = [[0 for x in range(w)] for y in range(h)]
    ## ADD INITIAL ASSETS [IF ANY....]
    start_time = time.time()
    # A TROOP 1 -- 0
    Initial_Avail_Assets[0][0] = 10
    Initial_Avail_Assets[0][1] = 10
    Initial_Avail_Assets[0][2] = 10
    Initial_Avail_Assets[0][3] = 10
    # A TROOP 2 -- 1
    # A TROOP 3 -- 2
    # A C2 1 -- 3
    Initial_Avail_Assets[3][0] = 6
    Initial_Avail_Assets[3][1] = 6
    Initial_Avail_Assets[3][2] = 6
    Initial_Avail_Assets[3][3] = 12
    # A C2 2 -- 4
    # A C2 3 -- 5
    # A AMB 1 -- 6
    # A AMB 2 -- 7
    # A RECON 1 -- 8
    # A RECON 2 -- 9
    # B TROOP 1 -- 10
    # B TROOP 2 -- 11
    # B C2 1 -- 12
    # B C2 2 -- 13
    # B AMB 1 -- 14
    # B AMB 2 -- 15
    # B RECON 1 -- 16
    # B RECON 2 -- 17
    # OLD TANK -- 18
    Initial_Avail_Assets[18][0] = 2
    Initial_Avail_Assets[18][1] = 2
    Initial_Avail_Assets[18][2] = 2
    # NEW TANK -- 19
    # NEW TANK 2 -- 20
    # Defining the population size.
    pop_size = (nPOP, N)
    random.seed(64 + run)
    #####-----Population Generation------#####
    #  Creating the initial population
    nPop1 = 1
    nPop2 = nPOP - nPop1
    pop1 = GA_Functions.generateIndividual2(min_year, max_year, N, nPop1)
    pop2 = GA_Functions.generateIndividual002(min_year, max_year, N, 0, nPOP)
    #  pop2 = GA_Functions.generateIndividual2(min_year, max_year, N, nPOP)

    pop = pop2
    # df141 = pd.DataFrame(pop1[0][:])
    # df141.to_csv('OrigBestSOLUTION122222222 -Run ' + str(run + 1) + '.csv')
    # Available assets for each solution in the population presented by 3-d array
    Vol, w, h = 4, 21, nPOP
    Avail_Assets_SOL = [[[0 for k in range(Vol)] for j in range(w)] for i in range(h)]  # Level of population
    # Available assets for each solution in the population presented by 3-d array
    Vol, w, h = 4, 21, num_generations
    Avail_Assets_GEN = [[[0 for k in range(Vol)] for j in range(w)] for i in range(h)]  # Level of Generations
    ## Repair solutions' configurations

    pop = GA_Functions.RepairOperations(pop, nPOP, N)

    pop = GA_Functions.RepairSol(pop, nPOP, N)
    # df11 = pd.DataFrame(pop[0][:])
    # df11.to_csv('OrigBestSOLUTION1222 -Run ' + str(run + 1) + '.csv')
    # Evaluate the fitness of the initial population
    VIO1, Avail_Assets_SOL, pop, Cost = GA_Functions.check_constraints(pop, nPOP, N, Initial_Avail_Assets,
                                                                      Avail_Assets_SOL)
    # df11 = pd.DataFrame(pop[0][:])
    # df11.to_csv('OrigBestSOLUTION12222425222222 -Run ' + str(run + 1) + '.csv')

    Fit, FitWeek, FitScore, Errs = GA_Functions.fitness(model, pop, nPOP, N)
    VIO = Errs
    # Sorting the Initial population
    fit, weeks, pop, FitWeek, FitScore, VIO, Avail_Assets_SOL, Cost = GA_Functions.sorting(pop, Fit, nPOP, FitWeek,
                                                                                           FitScore, VIO,
                                                                                           Avail_Assets_SOL, Cost)
    Fit = [weeks, fit, VIO, Cost]
    FIT = [Fit[0][0][0], Fit[1][0][0], Fit[2][0], Fit[3][0]]
    ResGen_fit = []
    ResGen_week = []
    Best_score = []
    Best_week = []
    colScore = list(zip(*FitScore))
    colWeek = list(zip(*FitWeek))
    Best_score.append(colScore[0])
    Best_week.append(colWeek[0])
    Time = []
    Time.append(time.time() - start_time)
    # Repair the best solution
   # Repair_sol=Repair(pop[0])
    print("Initial population: AVG: Best result : Score: Week: Vio: Cost:", FIT )
    print("Initial population: Best result B1, B2, B3 : Score:", colScore[0], "Week: ", colWeek[0], "Vio:", VIO[0])
    ResGen_fit.append(FIT)  # Fit to the best solution
    #  ResGen_week.append(weeks[0])
    df_av_assets = pd.DataFrame(Avail_Assets_SOL[0])  # Available assets to the best solution
    df_av_assets.columns = ["B1_UNASSIGNED", "B2_UNASSIGNED", "B3_UNASSIGNED", "ENABLING_B1_UNASSIGNED"]
    df_av_assets.index = ["A TROOP 1", "A TROOP 2", "A TROOP 3", "A C2 1", "A C2 2", "A C2 3", "A AMB 1", "A AMB 2",
                          "A RECON 1", "A RECON 2", "B TROOP 1", "B TROOP 2", "B C2 1", "B C2 2", "B AMB 1", "B AMB 2",
                          "B RECON 1", "B RECON 2", "OLD TANK", "NEW TANK", "NEW TANK 2"]
    df_av_assets.to_csv('Initial_assets.csv')

    for generation in range(0, num_generations - 1):
        OldPop = copy.deepcopy(pop)
        OldAvail_Assets_SOL = copy.deepcopy(Avail_Assets_SOL)
        # df1 = pd.DataFrame(OldPop[0][:])
        # df1.to_csv('OLDBestSOLUTION ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
        # OldAvail_Assets_SOL = copy.deepcopy(Avail_Assets_SOL)
        NewPop = GA_Functions.crossover(pop, cr, nPOP, N, pop1)
        # Adding some variations to the offsrping using mutation.
        MutPop = GA_Functions.mutation(NewPop, f, nPOP, N, min_year, max_year)
        # nVIO, Avail_Assets, MutPop = GA_Functions.check_constraints(MutPop, nPOP, N, Avail_Assets)
        MutPop = GA_Functions.RepairOperations(MutPop, nPOP, N)
        MutPop = GA_Functions.RepairSol(MutPop, nPOP, N)

        #  Re-evaluate the fitness functions
        nVIO1, NAvail_Assets_SOL, MutPop, NCost = GA_Functions.check_constraints(MutPop, nPOP, N, Initial_Avail_Assets,
                                                                                Avail_Assets_SOL)

        NewFit, NFitWeek, NFitScore, NErrs = GA_Functions.fitness(model, MutPop, nPOP, N)
        nVIO = NErrs
        #  print("STOP HERE")
        NewFit, NewWeek, NewPOP, FitWeek, FitScore, VIO, Avail_Assets_SOL, Cost = GA_Functions.Selection(OldPop, MutPop,
                                                                                                         Fit, NewFit,
                                                                                                         nPOP, FitWeek,
                                                                                                         FitScore,
                                                                                                         NFitWeek,
                                                                                                         NFitScore, VIO,
                                                                                                         nVIO,
                                                                                                         OldAvail_Assets_SOL,
                                                                                                         NAvail_Assets_SOL,
                                                                                                         Cost, NCost)
        # Fit = [NewWeek, NewFit]
        fit, weeks, pop, FitWeek, FitScore, VIO, Avail_Assets_SOL, Cost = GA_Functions.sorting(NewPOP, Fit, nPOP,
                                                                                               FitWeek, FitScore, VIO,
                                                                                               Avail_Assets_SOL, Cost)
        Fit = [weeks, fit, VIO, Cost]
        FIT = [Fit[0][0][0], Fit[1][0][0], Fit[2][0], Fit[3][0]]
        # The best result in the current iteration.
        print("Generation: ", generation, "Best result : AVG Score: Week: Vio: Cost:", FIT)
        #  print("Generation: ", generation, "Best result B1: Score:", FitScore[0][0], "Week: ", FitWeek[0][0])
        ResGen_fit.append(FIT)
        # ResGen_fit.append(fit[0])
        # ResGen_week.append(FIT[0])
        colScore = list(zip(*FitScore))
        colWeek = list(zip(*FitWeek))
        Best_score.append(colScore[0])
        Best_week.append(colWeek[0])
        Time.append(time.time() - start_time)
        # df1 = pd.DataFrame(pop[0][:])
        # df1.to_csv('BestSOLUTION ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
        Avail_Assets_GEN[generation] = Avail_Assets_SOL[0]
        if ((generation + 1) % 500) == 0:
            df1 = pd.DataFrame(ResGen_fit)
            df1.to_csv('AvgRes_Gen ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            df2 = pd.DataFrame(Time)
            df2.to_csv('CPU Time ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            df3 = pd.DataFrame(pop[0][:])
            df3.to_csv('SolRes_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            df4 = pd.DataFrame(Best_score)
            df4.to_csv('Bs_Scores_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            df5 = pd.DataFrame(Best_week)
            df5.to_csv('Bs_Weeks_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            df_av_assets = pd.DataFrame(Avail_Assets_GEN[generation])
            df_av_assets.columns = ["B1_UNASSIGNED", "B2_UNASSIGNED", "B3_UNASSIGNED", "ENABLING_B1_UNASSIGNED"]
            df_av_assets.index = ["A TROOP 1", "A TROOP 2", "A TROOP 3", "A C2 1", "A C2 2", "A C2 3", "A AMB 1",
                                  "A AMB 2",
                                  "A RECON 1", "A RECON 2", "B TROOP 1", "B TROOP 2", "B C2 1", "B C2 2", "B AMB 1",
                                  "B AMB 2",
                                  "B RECON 1", "B RECON 2", "OLD TANK", "NEW TANK", "NEW TANK 2"]
            # df_av_assets.to_csv('Initial_assets.csv')
            df_av_assets.to_csv('Avail_assets in GEN_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
            print("--- %s seconds ---" % (time.time() - start_time))

    Avail_Assets_RUN[run] = Avail_Assets_GEN[generation]
    Best_ResScore.append(ResGen_fit[-1])
    # Best_ResWeek.append(ResGen_week[-1])
    # BestRes = [Best_ResScore, Best_ResWeek]
    Best_ResSol.append(pop[0][:])
    Time.append(time.time() - start_time)
    df1 = pd.DataFrame(ResGen_fit)
    df1.to_csv('AvgRes_Gen ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
    df2 = pd.DataFrame(Time)
    df2.to_csv('CPU Time ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
    df3 = pd.DataFrame(pop[0][:])
    df3.to_csv('SolRes_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
    df4 = pd.DataFrame(Best_score)
    df4.to_csv('Bs_Scores_ ' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
    df5 = pd.DataFrame(Best_week)
    df5.to_csv('Bs_Weeks_  -Run ' + str(run + 1) + '.csv')
    df_av_assets = pd.DataFrame(Avail_Assets_RUN[run])
    df_av_assets.columns = ["B1_UNASSIGNED", "B2_UNASSIGNED", "B3_UNASSIGNED", "ENABLING_B1_UNASSIGNED"]
    df_av_assets.index = ["A TROOP 1", "A TROOP 2", "A TROOP 3", "A C2 1", "A C2 2", "A C2 3", "A AMB 1", "A AMB 2",
                          "A RECON 1", "A RECON 2", "B TROOP 1", "B TROOP 2", "B C2 1", "B C2 2", "B AMB 1", "B AMB 2",
                          "B RECON 1", "B RECON 2", "OLD TANK", "NEW TANK", "NEW TANK 2"]
    df_av_assets.to_csv('Avail_assets  -Run ' + str(run + 1) + '.csv')
    df_BestRes = pd.DataFrame(Best_ResScore)
    df_BestRes.to_csv('Best_Results  -Run ' + str(run + 1) + '.csv')
    df_BestSol = pd.DataFrame(Best_ResSol)
    df_BestSol.to_csv('Best_Sol' + str(generation + 1) + ' -Run ' + str(run + 1) + '.csv')
    print("--- %s seconds ---" % (time.time() - start_time))
