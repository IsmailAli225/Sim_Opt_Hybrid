import numpy
# generate random integer values
from datetime import datetime, timedelta
from random import seed, random
import random
from random import randint
import numpy
# generate random integer values
import numpy as np
import time
import pandas as pd

from javaconnectormulti import *
import csv
import pandas

AssetClassID_A = ["A TROOP", "A AMB", "A C2", "A RECON"]  # 4
AssetClassID_B = ["B TROOP", "B AMB", "B C2", "B RECON"]  # 4
AssetClassID_TANK = ["OLD TANK"]  # , "NEW TANK"]  # 2
AssetClassID_C = ["C RECON"]  # 1

ConfID_A = ["A TROOP 1", "A TROOP 2", "A TROOP 3"]

ConfID_A1 = ["A TROOP 1", "A TROOP 2", "A TROOP 3"]
ConfID_A2 = ["A AMB 1", "A AMB 2"]
ConfID_A3 = ["A C2 1", "A C2 2", "A C2 3"]
ConfID_A4 = ["A RECON 1", "A RECON 2"]  # 10

ConfID_B = ["B TROOP 1", "B TROOP 2"]

ConfID_B1 = ["B TROOP 1", "B TROOP 2"]
ConfID_B2 = ["B AMB 1", "B AMB 2"]
ConfID_B3 = ["B C2 1", "B C2 2"]
ConfID_B4 = ["B RECON 1", "B RECON 2"]  # 8

ConfID_TANK = ["OLD TANK", "NEW TANK", "NEW TANK 2"]  # 3

Project = ["PMICA", "JP9141-1", "JP9141-2", "LAND1", "PROJECT4"]  # 5
# Project = ["PMICA", "JP9141-1", "JP9141-2", "LAND1", "PROJECT4"]  # 5
Dest_Pool = ["B1_UNASSIGNED", "B2_UNASSIGNED", "B3_UNASSIGNED"]  # 3

Source_Pool = ["B1_UNASSIGNED", "B2_UNASSIGNED", "B3_UNASSIGNED", "ENABLING_B1_UNASSIGNED"]  # 5
Upgrade_Type = ["ACQUISITION", "UPGRADE", "UPGRADEWITHMODULES", "RETIREMENT",
                "RETIREMENTWITHMODULES"]  # , "TRANSFER"]  # 6
New_Upg_Type = ["ACQUISITION", "UPGRADE", "UPGRADEWITHMODULES"]
Upgrade_TypeII = ["UPGRADE", "UPGRADEWITHMODULES", "RETIREMENT", "RETIREMENTWITHMODULES"]  # , "TRANSFER"]  # 6
Initial_Assets = ["A TROOP 1", "A C2 1", "OLD TANK"]
AllConfig = ["A TROOP 1", "A TROOP 2", "A TROOP 3", "A C2 1", "A C2 2", "A C2 3", "A AMB 1", "A AMB 2", "A RECON 1",
             "A RECON 2", "B TROOP 1", "B TROOP 2", "B C2 1", "B C2 2", "B AMB 1", "B AMB 2", "B RECON 1", "B RECON 2",
             "OLD TANK", "NEW TANK", "NEW TANK 2"]
Upg_age = np.full((1, len(AllConfig)), random.randint(2, 4))
Ret_age = np.full((1, len(AllConfig)), random.randint(5, 7))

## Population Generation

# Generate solution from scenario-based examples:
def generateIndividual2(min_year, max_year, N, nPOP):
    individual = generateMatchedIndividual(min_year, max_year, N, nPOP)
    return individual  # creator.Individual(individual)
# Generate solution Randomly
def generateIndividual002(min_year, max_year, N, nPOP1, nPOP):
    individual = generateIndividual(min_year, max_year, N, nPOP1, nPOP)
    return individual  # creator.Individual(individual)


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)



print(random_date("1/1/2008", "1/1/2009", random.random()))


# Generate individuals with some fixed parts (read from CSV file) to test one or some other decision variables
def generateMatchedIndividual(min_year, max_year, N, nPOP):
    with open('NEWORIGIN.csv', 'r') as file:

        # with open('D:\Capability Model\Connector\OrigSchedwith1.csv', 'r') as file:
        OrigSc = csv.reader(file)
        dataOrig = []
        for row in OrigSc:
            dataOrig.append(row)
    FullIndv = []
    for s in range(nPOP):
        MatchIndv = []
        # , dataOrig[ro][2], dataOrig[ro][3], dataOrig[ro][4], dataOrig[ro][5], dataOrig[ro][6], int(dataOrig[ro][7]), dataOrig[ro][8], dataOrig[ro][9], int(dataOrig[ro][10]), int(dataOrig[ro][11])
        for i in range(17):
            Sol = [  # random_date(min_year, max_year, random.random()),
                pd.to_datetime(dataOrig[i][0], format="%d/%m/%Y"),
                dataOrig[i][1],
                dataOrig[i][2],
                dataOrig[i][3],
                dataOrig[i][4],
                dataOrig[i][5],
                dataOrig[i][6],
                int(dataOrig[i][7]),
                dataOrig[i][8],
                dataOrig[i][9],
                int(dataOrig[i][10]),
                int(dataOrig[i][11]),
            ]
            # print(Sol)
            MatchIndv.append(Sol)

        for i in range(17, 23):
            Sol = [  # random_date(min_year, max_year, random.random()),
                pd.to_datetime(dataOrig[i][0], format="%d/%m/%Y"),
                dataOrig[i][1],
                dataOrig[i][2],
                dataOrig[i][3],
                dataOrig[i][4],
                dataOrig[i][5],
                dataOrig[i][6],
                int(dataOrig[i][7]),
                dataOrig[i][8],
                dataOrig[i][9],
                int(dataOrig[i][10]),
                int(dataOrig[i][11]),
            ]
            # print(Sol)
            MatchIndv.append(Sol)

        for i in range(23, 30):
            Sol = [  # random_date(min_year, max_year, random.random()),
                pd.to_datetime(dataOrig[i][0], format="%d/%m/%Y"),
                dataOrig[i][1],
                dataOrig[i][2],
                dataOrig[i][3],
                dataOrig[i][4],
                dataOrig[i][5],
                dataOrig[i][6],
                int(dataOrig[i][7]),
                dataOrig[i][8],
                dataOrig[i][9],
                int(dataOrig[i][10]),
                int(dataOrig[i][11]),
            ]
            # print(MatchIndv)
            MatchIndv.append(Sol)
            # print(MatchIndv)
        FullIndv.append(MatchIndv)
    return FullIndv


# Generate Individual with RANDOM selected values for ALL decision variables
def generateIndividual(min_year, max_year, N, nPOP1, nPOP):
    # Upgrade_Type = ["ACQUISITION", "RETIREMENT", "RETIREMENTWITHMODULES", "TRANSFER", "UPGRADE",
    # "UPGRADEWITHMODULES"]  # 6

    FullIndv = []
    for s in range(nPOP1, nPOP):
        Indv = []
       # Qunty = [4, 3, 3, 5, 5, 3, 3, 5, 5, 3, 3, 6, 10, 3, 3, 3, 3, 10, 6, 10, 6, 10, 6, 4, 4, 4, 2, 2, 2, 4]
        for i in range(17): #pd.to_datetime(dataOrig[i][0], format="%d/%m/%Y")
            Sol = [pd.to_datetime(random_date(min_year, max_year, random.random()), format="%d/%m/%Y"),
                   random.choice(AssetClassID_A),
                   random.choice(ConfID_A),
                   random.choice(Project),  #Project[0], #
                   random.choice(Dest_Pool),
                   random.choice(Source_Pool),
                   random.choice(New_Upg_Type),
                   int(randint(2, 10)),
                   # Qunty[i],
                   "",
                   random.choice(ConfID_A),
                   int(randint(5, 15)),
                   # randint(0, 1),
                   0]
            # print(Sol)
            Indv.append(Sol)

        for i in range(17, 23):
            Sol = [pd.to_datetime(random_date(min_year, max_year, random.random()), format="%d/%m/%Y"),
                   random.choice(AssetClassID_B),
                   random.choice(ConfID_B),
                   random.choice(Project),  #Project[4], #
                   random.choice(Dest_Pool),
                   random.choice(Source_Pool),
                   random.choice(New_Upg_Type),
                   # Qunty[i],
                   int(randint(2, 10)),
                   "",
                   random.choice(ConfID_B),
                   int(randint(5, 15)),
                   # randint(0, 1),
                   0]
            # print(Sol)
            Indv.append(Sol)

        for i in range(23, 30):
            Sol = [pd.to_datetime(random_date(min_year, max_year, random.random()), format="%d/%m/%Y"),
                   random.choice(AssetClassID_TANK),
                   random.choice(ConfID_TANK),
                   random.choice(Project),  #Project[3], #
                   random.choice(Dest_Pool),
                   random.choice(Source_Pool),
                   random.choice(New_Upg_Type),
                   int(randint(2, 10)),
                   # Qunty[i],
                   "",
                   random.choice(ConfID_TANK),
                   int(randint(5, 15)),
                   # randint(0, 1),
                   0]
            Indv.append(Sol)
        # if s == 1:
        #      FullIndv = Indv
        # else:
        FullIndv.append(Indv)
    return FullIndv


# Type= ["UPGRADEWITHMODULES", "UPGRADE",	"UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADE", "UPGRADEWITHMODULES", "ACQUISITION", "UPGRADEWITHMODULES", "UPGRADEWITHMODULES", "UPGRADEWITHMODULES", "UPGRADEWITHMODULES", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "ACQUISITION", "RETIREMENT", "RETIREMENT", "RETIREMENT", "UPGRADEWITHMODULES"]
### Selection Mating

def sorting(pop, fitness, nPOP, FitWeek, FitScore, vio, Avail_Assets_SOL, Cost):
    # fit = fitness[1][0]
    # if fit.size == 1: # Second iteration
    # fit = FitScore  # fitness[1]
    # week = FitWeek  # fitness[0]
    # else:
    fit = fitness[1]
    week = fitness[0]

    for i in range(0, nPOP - 1):
        for s in range(i + 1, nPOP):
            # check if better (e.g. perform a tournament)
            if (vio[i] > vio[s]) or (vio[i] == vio[s] and fit[0][i] < fit[0][s]) or (
                    vio[i] == vio[s] and fit[0][i] == fit[0][s] and week[0][i] > week[0][s] or (
                    vio[i] == vio[s] and fit[0][i] == fit[0][s] and week[0][i] == week[0][s] and Cost[i] > Cost[s])):  # s is better?!
                fit[0][i], fit[0][s] = fit[0][s], fit[0][i]
                week[0][i], week[0][s] = week[0][s], week[0][i]
                #    FitWeek[i], FitWeek[s] = FitWeek[s], FitWeek[i]
                vio[i], vio[s] = vio[s], vio[i]
                Cost[i], Cost[s] = Cost[s], Cost[i]
                #    FitWeek[i], FitWeek[s] = FitWeek[s], FitWeek[i]
                #  vio[i], vio[s] = vio[s], vio[i]
                FitWeek[0][i], FitWeek[0][s] = FitWeek[0][s], FitWeek[0][i]
                FitWeek[1][i], FitWeek[1][s] = FitWeek[1][s], FitWeek[1][i]
                FitWeek[2][i], FitWeek[2][s] = FitWeek[2][s], FitWeek[2][i]
                # FitScore[i], FitScore[s] = FitScore[s], FitScore[i]
                FitScore[0][i], FitScore[0][s] = FitScore[0][s], FitScore[0][i]
                FitScore[1][i], FitScore[1][s] = FitScore[1][s], FitScore[1][i]
                FitScore[2][i], FitScore[2][s] = FitScore[2][s], FitScore[2][i]
                Avail_Assets_SOL[i][:][:], Avail_Assets_SOL[s][:][:] = Avail_Assets_SOL[s][:][:], Avail_Assets_SOL[i][
                                                                                                  :][:]
                pop[i][:], pop[s][:] = pop[s][:], pop[i][:]
                vio = vio
    return fit, week, pop, FitWeek, FitScore, vio, Avail_Assets_SOL, Cost


##-----Crossover
def crossover(pop, cr, nPOP, N, BestInd):
    n = 12
    for r in range(0, nPOP-1, 2):
        p1 = pop[r]
        # p2 = pop[r + 1][:]
        if random.random() <= 0.3:
            Indv = random.randint(0, nPOP - 1)
            p2 = pop[Indv]
        elif 0.3 < random.random() <= 0.6:
            Indv = r+1
            p2 = pop[Indv]
        else:
            Indv = r + 1
            p2 = BestInd[0]

        if random.random() <= cr:
            #for w in range(0, 3):
                #random.random() <= cr:
            s = random.randint(0, N/2)
            sn = random.randint((N/2)+1, N-1)
            swap = p1[s:sn]
            p1[s:sn] = p2[s:sn]
            p2[s:sn] = swap
                # c = random.randint(0, n - (n / 2))
                # d = random.randint(c + 1, n - 1)
                #
                # # c = random.randint(0, N - (N / 2))
                # # d = random.randint(c + 1, N - 1)
            # swap = c1
            # p1[s][s * n:(s * n) + n] = c2
            # p2[s][s * n:(s * n) + n] = c1
                # swap = p1[c:d]
                    # p1[c:d] = p2[c:d]
                    # p2[c:d] = swap
            pop[r] = p1
            pop[Indv] = p2
    return pop


# ##-----Crossover
# def crossover(pop, cr, nPOP, N):
#     for r in range(0, nPOP, 2):
#         p1 = pop[r][:]
#         #p2 = pop[r + 1][:]
#         p2 = pop[random.randint(0, nPOP - 1)][:]
#         if random.random() <= cr:
#             c = random.randint(0, N - (N / 2))
#             d = random.randint(c + 1, N - 1)
#             swap = p1[c:d]
#             p1[c:d] = p2[c:d]
#             p2[c:d] = swap
#         pop[r][:] = p1
#         pop[r + 1][:] = p2
#         return pop


##---Mutation
def mutation(pop, f, nPOP, N, min_year, max_year):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(nPOP - 1):
        # The random value to be added to the gene.
        for ind in range(N-1):
            if random.random() <= f:
                if random.random()<= 0.4:
                    pop[idx][ind][0] = pd.to_datetime(random_date(min_year, max_year, random.random()), format="%d/%m/%Y") # Date
                elif random.random()>0.4: # and random.random()<=0.7:
                    pop[idx][ind][7] = randint(2, 10) # Quantity
                # elif random.random()>0.7:# and random.random()<=0.6:
                #     pop[idx][ind][2] = random.choice(AllConfig)

    return pop


def Selection(pop, NewPop, fitness, NewFit, nPOP, FitWeek, FitScore, NFitWeek, NFitScore, vio, nvio, Avail_Assets_SOL,
              NAvail_Assets_SOL, Cost, NCost):
    # fit = FitScore  #fitness[1]
    # week = FitWeek  # fitness[0]
    fit = fitness[1][0]
    week = fitness[0][0]
    Nfit = NewFit[1][0]  # [1]#[1][0]
    Nweek = NewFit[0][0]  # [0]#[0][0]
    New_Fit = fit
    New_Week = week
    New_Pop = pop

    for i in range(0, nPOP):
        # check if better (e.g. perform a tournament)
        if (vio[i] > nvio[i]) or (vio[i] == nvio[i] and fit[i] < Nfit[i]) or (
                vio[i] == nvio[i] and fit[i] == Nfit[i] and week[i] > Nweek[i]) or (
                vio[i] == nvio[i] and fit[i] == Nfit[i] and week[i] == Nweek[i] and Cost[i] > NCost[
            i]):  # s is better?!
            New_Fit[i] = Nfit[i]
            New_Week[i] = Nweek[i]
            New_Pop[i][:] = NewPop[i][:]
            # FitWeek[i] = NFitWeek[i]
            vio[i] = nvio[i]
            Cost[i] = NCost[i]
            FitWeek[0][i] = NFitWeek[0][i]
            FitWeek[1][i] = NFitWeek[1][i]
            FitWeek[2][i] = NFitWeek[2][i]
            # FitScore[i] = NFitScore[i]
            FitScore[0][i] = NFitScore[0][i]
            FitScore[1][i] = NFitScore[1][i]
            FitScore[2][i] = NFitScore[2][i]
            Avail_Assets_SOL[i][:][:] = NAvail_Assets_SOL[i][:][:]
    return New_Fit, New_Week, New_Pop, FitWeek, FitScore, vio, Avail_Assets_SOL, Cost


###-----------FITNESS FUNCTION--------#####
def fitness(MainModel, individual, nPOP, N):
    # Not sure about adding below part!!!
    # change the configuration
    # cm_connector.origin_conf.addInitialAssetsToGroup("DIV_UNASSIGNED","TROOP(A)","A TROOP 1", 5 );
    ResScore, ResScoreB1, ResScoreB2, ResScoreB3 = ([] for i in range(4))
    ResWeek, ResWeekB1, ResWeekB2, ResWeekB3 = ([] for i in range(4))
    replication = []
    AllErrs=[]
    for R in range(0, nPOP):
        MainModel.load_config("conf/testbignewEmpty.xlsx")  # reads excel for each indivudal
        IndivN = []
        IndivN.append(individual[R])
        INV = pd.DataFrame.from_records(IndivN[0])
        rep = MainModel.add_replication()
        # replication.append(rep)
        #  print('R= ' + str(R))
        for S in range(N):

            IndivSol = []
            sol = INV.iloc[S]
          #  sol[0] =  sol[0].to_pydatetime()#datetime.strptime(str(sol[0]), '%d/%m/%Y')
           # sol[0]
#pd.to_datetime(sol[0] , format="%d/%m/%Y") #s
            # for sol in IndivSol:
            rep.getConf().addAssetEvent(sol[0].strftime("%d/%m/%Y %H:%M:%S"), sol[1], sol[2], sol[3], sol[4], sol[5], sol[6], sol[7], sol[8],
                                        sol[9], sol[10], sol[11])
            # print([sol[0], sol[1], sol[2], sol[3], sol[4], sol[5], sol[6], sol[7], sol[8],
            #      sol[9], sol[10], sol[11]])
        # run the replications for this iteration
        # print(sol)
        MainModel.run_multi()
       # print(sol)
        ## GET THE RESULTS
        # for rep_idx in range(0, N):
        # get replication from list
        # rep = replication[R]
        # get the roorFactor that contains the results
        rootFactor = rep.getMain().rootFactor

        b1 = rep.getMain().rootFactor.organisation.get_from_all_groups("B1")
        b2 = rep.getMain().rootFactor.organisation.get_from_all_groups("B2")
        b3 = rep.getMain().rootFactor.organisation.get_from_all_groups("B 3")

        # print("Assets in B1", b1.assets.size())
        b1sol = b2sol = b3sol = 0
        SolDetB1 = b1.ds_monthly_configScore.getData()
        SolDetB2 = b2.ds_monthly_configScore.getData()
        SolDetB3 = b3.ds_monthly_configScore.getData()

        AllSizeB1 = SolDetB1.size() - 1
        AllSizeB2 = SolDetB2.size() - 1
        AllSizeB3 = SolDetB3.size() - 1
        while b1sol <= AllSizeB1:
            if SolDetB1.get(b1sol).yval == 1:
                break
            elif b1sol == AllSizeB1:
                break
            else:
                b1sol += 1
        idx1 = b1sol
        while b2sol <= AllSizeB2:
            if SolDetB2.get(b2sol).yval == 1:
                break
            elif b2sol == AllSizeB2:
                break
            else:
                b2sol += 1
        idx2 = b2sol
        while b3sol <= AllSizeB3:
            if SolDetB3.get(b3sol).yval == 1:
                break
            elif b3sol == AllSizeB3:
                break
            else:
                b3sol += 1
        idx3 = b3sol

        ResWeekB1.append(b1.ds_monthly_configScore.getData().get(idx1).xval)
        ResScoreB1.append(b1.ds_monthly_configScore.getData().get(idx1).yval)

        ResWeekB2.append(b2.ds_monthly_configScore.getData().get(idx2).xval)
        ResScoreB2.append(b2.ds_monthly_configScore.getData().get(idx2).yval)

        ResWeekB3.append(b3.ds_monthly_configScore.getData().get(idx3).xval)
        ResScoreB3.append(b3.ds_monthly_configScore.getData().get(idx3).yval)
#        dis(R)
        if rep.anyErrorsOrWarnings():
        #   print("There are Errors or Warnings")
            err_list = rep.getAllErrorsAndWarnings()
            Errs = len(err_list)
            # for emsg in err_list:
            #     print(emsg)
        else:
            Errs = 0

        AllErrs.append(Errs)
    # ## Calculate the average as the fitness
    ResWeek.append(np.mean(np.array([ ResWeekB1, ResWeekB2, ResWeekB3 ]), axis=0 ))
    ResScore.append(np.mean(np.array([ ResScoreB1, ResScoreB2, ResScoreB3 ]), axis=0 ))
    # ResWeek.append(ResWeekB1)
    # ResScore.append(ResScoreB1)

    # ResProg.append(b1.ds_monthly_configScore.getData().get(idx))
    # Res.append(b1.ds_monthly_configScore.getData())
    #   print(Res)
    AllResWeek = [ResWeekB1  , ResWeekB2, ResWeekB1]
    AllResScore = [ResScoreB1  , ResScoreB2, ResScoreB3]
    AllAvgRes = [ResWeek, ResScore]
    return AllAvgRes, AllResWeek, AllResScore, AllErrs  # , ResProg

## Repair Operations
def RepairOperations(pop, nPOP, N):
    for I in range(0, nPOP):
        SOL = pop[I]
       # SOL[:][0] = datetime.strptime('01/01/2021', '%d %m %y')
        df1 = pd.DataFrame(SOL)
        df1.columns = ["date", "Config", "Config_sub", "Project", "Dest", "Source", "Type", "Quantity", "Re",
                       "re-Config", "Cost", "Delay"]
        df1["date"] = pd.to_datetime(df1["date"])
        SOL = df1.sort_values(by="date")
        nSOL = SOL
        Indx = SOL.index
        i=0
        for i in range(N):
            Flag = 0
            Ind = SOL.iloc[i]
            # type_count = Ind['Type'].str.contains('RETIREMENT').sum()
            # type_count1 = Ind['Type'].str.contains('RETIREMENTWITHMODULES').sum()
            # if (type_count > 0) or (type_count1 > 0):
            if i == 0 and Ind.iloc[6] == 'ACQUISITION':
                if Ind.iloc[2] in Initial_Assets:
                    Ind.at['Type'] = 'UPGRADE'
            elif i == 0 and (Ind.iloc[6] == 'UPGRADE' or Ind.iloc[6] == 'UPGRADEWITHMODULES') :
                if Ind.iloc[2] not in Initial_Assets:
                    Ind.at['Type'] = 'ACQUISITION'
            elif i == 0 and (Ind.iloc[6] == 'RETIREMENT' or Ind.iloc[6] == 'RETIREMENTWITHMODULES') :
                if Ind.iloc[2] not in Initial_Assets:
                    Ind.at['Type'] = 'ACQUISITION'
                else:
                    Ind.at['Type'] = 'UPGRADE'
            elif i > 0 and Ind.iloc[6] == 'ACQUISITION':
                curDF = SOL.iloc[0:i]
                type_count22 = curDF[curDF['Config_sub'] == Ind.iloc[2]].index.values
                type_count222 = curDF[curDF['Source'] == Ind.iloc[5]].index.values
                type_count = list(set(type_count22) & set(type_count222)) # Find config_sub with same config and pool
                type_count = np.array(type_count)
                type_count_sub1 = curDF[curDF['re-Config'] == Ind.iloc[2]].index.values
                type_count_sub = list(set(type_count_sub1) & set(type_count222)) # Find re-config with same config and pool
                type_count_sub = np.array(type_count_sub)
                fl = 0
                if len(type_count) > 0:
                    type_count2 = max(type_count)
                    fl = 1  # Sub-config
                elif len(type_count_sub) > 0:
                    type_count2 = max(type_count_sub)
                    fl = 2  # Re-config
                else:
                    type_count2 = type_count
                if type_count2 >= 0:
                    if fl == 1:
                        LastConfig = SOL.loc[type_count2]['Config_sub']
                    elif fl == 2:
                        LastConfig = SOL.loc[type_count2]['re-Config']
                    LastDest = SOL.loc[type_count2]['Source']
                    if LastConfig == Ind.iloc[2] and LastDest == Ind.iloc[5]:
                        LastDate = SOL.loc[type_count2]['date']
                        currDate = Ind.iloc[0]
                        #age_count = Ret_age.index(Ind.iloc[2])
                        RetAge = 6 #Ret_age[age_count]
                        UpgAge = 4 #Upg_age[age_count]
                        NewRetDate = addYears(LastDate, RetAge)
                        NewUpgDate = addYears(LastDate, UpgAge)
                        if currDate >= NewRetDate:
                            Ind.at['Type'] = 'RETIREMENT'
                        elif currDate >= NewUpgDate:
                            Ind.at['Type'] = 'UPGRADE'
                            Flag = 1
                        else:
                            Ind.at['Config_sub'] = random.choice(AllConfig)
            elif (i > 0 and (Ind.iloc[6] == 'RETIREMENT' or Ind.iloc[6] == 'RETIREMENTWITHMODULES')):
                curDF = SOL.iloc[0:i]
                type_count22 = curDF[curDF['Config_sub'] == Ind.iloc[2]].index.values
                type_count222 = curDF[curDF['Source'] == Ind.iloc[5]].index.values
                type_count = list(set(type_count22) & set(type_count222)) # Find config_sub with same config and pool
                type_count = np.array(type_count)
                type_count_sub1 = curDF[curDF['re-Config'] == Ind.iloc[2]].index.values
                type_count_sub = list(set(type_count_sub1) & set(type_count222)) # Find re-config with same config and pool
                type_count_sub = np.array(type_count_sub)
                fl = 0
                if len(type_count) > 0:
                    type_count2 = max(type_count)
                    fl = 1  # Sub-config
                elif len(type_count_sub) > 0:
                    type_count2 = max(type_count_sub)
                    fl = 2  # Re-config
                else:
                    type_count2 = type_count
                if type_count2 >= 0:
                    if fl == 1:
                        LastConfig = SOL.loc[type_count2]['Config_sub']
                    elif fl == 2:
                        LastConfig = SOL.loc[type_count2]['re-Config']
                    LastDest = SOL.loc[type_count2]['Source']
                    if LastConfig == Ind.iloc[2] and LastDest == Ind.iloc[5]:
                        LastDate = SOL.loc[type_count2]['date']
                        currDate = Ind.iloc[0]
                        #age_count = Ret_age.index(Ind.iloc[2])
                        RetAge = 6 #Ret_age[age_count]
                        UpgAge = 4 #Upg_age[age_count]
                        NewRetDate = addYears(LastDate, RetAge)
                        NewUpgDate = addYears(LastDate, UpgAge)
                        if currDate < NewRetDate:
                            Ind.at['Type'] = 'UPGRADE'
                            Flag = 1
                else:
                    Ind.at['Type'] = 'ACQUISITION'
            elif (i > 0 and (Ind.iloc[6] == 'UPGRADE' or Ind.iloc[6] == 'UPGRADEWITHMODULES')) or (Flag==1):
                curDF = SOL.iloc[0:i]
                type_count22 = curDF[curDF['Config_sub'] == Ind.iloc[2]].index.values
                type_count222 = curDF[curDF['Source'] == Ind.iloc[5]].index.values
                type_count = list(set(type_count22) & set(type_count222)) # Find config_sub with same config and pool
                type_count = np.array(type_count)
                type_count_sub1 = curDF[curDF['re-Config'] == Ind.iloc[2]].index.values
                type_count_sub = list(set(type_count_sub1) & set(type_count222)) # Find re-config with same config and pool
                type_count_sub = np.array(type_count_sub)
                fl = 0
                if len(type_count) > 0:
                    type_count2 = max(type_count)
                    fl = 1  # Sub-config
                elif len(type_count_sub) > 0:
                    type_count2 = max(type_count_sub)
                    fl = 2  # Re-config
                else:
                    type_count2 = type_count
                if type_count2 >= 0:
                    if fl == 1:
                        LastConfig = SOL.loc[type_count2]['Config_sub']
                    elif fl == 2:
                        LastConfig = SOL.loc[type_count2]['re-Config']
                    LastDest = SOL.loc[type_count2]['Source']
                    if LastConfig == Ind.iloc[2] and LastDest == Ind.iloc[5]:
                        LastDate = SOL.loc[type_count2]['date']
                        currDate = Ind.iloc[0]
                      #  age_count = Ret_age.index(Ind.iloc[2])
                        RetAge = 6#Ret_age[age_count]
                       # UpgAge = Upg_age[age_count]
                        NewRetDate = addYears(LastDate, RetAge)
                       # NewUpgDate = addYears(LastDate, UpgAge)
                        if currDate >= NewRetDate:
                            Ind.at['Type'] = 'RETIREMENT'
                        else:
                            Ind.at['Config_sub'] = random.choice(AllConfig)
                            # Repeat above Upgrade code again
                            curDF = SOL.iloc[0:i]
                            type_count22 = curDF[curDF['Config_sub'] == Ind.iloc[2]].index.values
                            type_count222 = curDF[curDF['Source'] == Ind.iloc[5]].index.values
                            type_count = list(
                                set(type_count22) & set(type_count222))  # Find config_sub with same config and pool
                            type_count = np.array(type_count)
                            type_count_sub1 = curDF[curDF['re-Config'] == Ind.iloc[2]].index.values
                            type_count_sub = list(
                                set(type_count_sub1) & set(type_count222))  # Find re-config with same config and pool
                            type_count_sub = np.array(type_count_sub)
                            fl = 0
                            if len(type_count) > 0:
                                type_count2 = max(type_count)
                                fl = 1  # Sub-config
                            elif len(type_count_sub) > 0:
                                type_count2 = max(type_count_sub)
                                fl = 2  # Re-config
                            else:
                                type_count2 = type_count
                            if type_count2 >= 0:
                                if fl == 1:
                                    LastConfig = SOL.loc[type_count2]['Config_sub']
                                elif fl == 2:
                                    LastConfig = SOL.loc[type_count2]['re-Config']
                                LastDest = SOL.loc[type_count2]['Source']
                                if LastConfig == Ind.iloc[2] and LastDest == Ind.iloc[5]:
                                    LastDate = SOL.loc[type_count2]['date']
                                    currDate = Ind.iloc[0]
                                    #  age_count = Ret_age.index(Ind.iloc[2])
                                    RetAge = 6  # Ret_age[age_count]
                                    # UpgAge = Upg_age[age_count]
                                    NewRetDate = addYears(LastDate, RetAge)
                                    # NewUpgDate = addYears(LastDate, UpgAge)
                                    if currDate >= NewRetDate:
                                        Ind.at['Type'] = 'RETIREMENT'
                                    else: #elif Ind.iloc[2] not in Initial_Assets and len(type_count22)<=0:
                                        Ind.at['Type'] = 'ACQUISITION'
                            else:  # elif Ind.iloc[2] not in Initial_Assets and len(type_count22)<=0:
                                Ind.at['Type'] = 'ACQUISITION'
                elif Ind.iloc[2] not in Initial_Assets:
                    Ind.at['Type'] = 'ACQUISITION'
            # if Flag == 0:
            #     i = i + 1

            nSOL.at[Indx[i]] = Ind
        SolArr = nSOL.values.tolist()
        pop[I] = SolArr
    return pop
import datetime
from datetime import date
def addYears(d, years):
    try:
#Return same day of the current year
        return d.replace(year = d.year + years)
    except ValueError:
#If not same day, it will return other, i.e.  February 29 to March 1 etc.
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


### Repair Solutions
def RepairSol(pop, nPOP, N):
    for R in range(0, nPOP):
        for S in range(N):
            sol = pop[R][S]
            # CHECK THE UPGRADE TYPE VALIDITY
            if sol[6] == "UPGRADE" or sol[6] == "UPGRADEWITHMODULES":  # No Dest Pool
                sol[4] = ''
                if sol[5] == '':
                    sol[5] = random.choice(Source_Pool)
                if sol[9] == '':
                    sol[9] = random.choice(ConfID_A1)
            # if not sol[1] in Initial_Assets:
            elif sol[6] == "ACQUISITION":  # No Source Pool AND No Upgraded Config.
                sol[5] = ''
                sol[9] = ''
                if sol[4] == '':
                    sol[4] = random.choice(Dest_Pool)
            elif sol[6] == "RETIREMENT" or sol[6] == "RETIREMENTWITHMODULES":  # No Dest Pool AND NO Upgraded Config.
                sol[4] = ''
                sol[9] = ''
                if sol[5] == '':
                    sol[5] = random.choice(Source_Pool)
            # elif sol[6] == "TRANSFER":  # Source Pool AND Dest Pool AND Upgraded Config. must be there.
            #     if sol[4] == '':
            #         sol[4] = random.choice(Dest_Pool)
            #     if sol[5] == '':
            #         sol[5] = random.choice(Source_Pool)

            # CHECK THE GROUP AND SUB-GROUP OF ASSETS CLASS ID
            if sol[2] in ConfID_A1:
                sol[1] = "A TROOP"
                # if not sol[2] in ConfID_A1:
                #     sol[2] = random.choice(ConfID_A1)
                if (not sol[9] in ConfID_A1 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_A1)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_A1)
            elif sol[2] in ConfID_A2:
                sol[1] = "A AMB"
                # if not sol[2] in ConfID_A2:
                #     sol[2] = random.choice(ConfID_A2)
                if (not sol[9] in ConfID_A2 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_A2)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_A2)
            elif sol[2] in ConfID_A3:
                sol[1] = "A C2"
                # if not sol[2] in ConfID_A3:
                #     sol[2] = random.choice(ConfID_A3)
                if (not sol[9] in ConfID_A3 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_A3)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_A3)
            elif sol[2] in ConfID_A4:
                sol[1] = "A RECON"
                # if not sol[2] in ConfID_A4:
                #     sol[2] = random.choice(ConfID_A4)
                if (not sol[9] in ConfID_A4 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_A4)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_A4)
            elif sol[2] in ConfID_B1:
                sol[1] = "B TROOP"
                # if not sol[2] in ConfID_B1:
                #     sol[2] = random.choice(ConfID_B1)
                if (not sol[9] in ConfID_B1 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_B1)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_B1)
            elif sol[2] in ConfID_B2:
                sol[1] = "B AMB"
                # if not sol[2] in ConfID_B2:
                #     sol[2] = random.choice(ConfID_B2)
                if (not sol[9] in ConfID_B2 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_B2)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_B2)
            elif sol[2] in ConfID_B3:
                sol[1] = "B C2"
                # if not sol[2] in ConfID_B3:
                #     sol[2] = random.choice(ConfID_B3)
                if (not sol[9] in ConfID_B3 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_B3)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_B3)
            elif sol[2] in ConfID_B4:
                sol[1] = "B RECON"
                # if not sol[2] in ConfID_B4:
                #     sol[2] = random.choice(ConfID_B4)
                if (not sol[9] in ConfID_B4 and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_B4)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_B4)
            elif sol[2] in ConfID_TANK:
                sol[1] = "OLD TANK"
                # if not sol[2] in ConfID_TANK:
                #     sol[2] = random.choice(ConfID_TANK)
                if (not sol[9] in ConfID_TANK and sol[9] != '') or sol[9] == sol[2]:
                    sol[9] = random.choice(ConfID_TANK)
                    while sol[9] == sol[2]:
                        sol[9] = random.choice(ConfID_TANK)
            pop[R][S] = sol
    return pop


def check_constraints(pop, nPOP, N, Orig_Avail_Asset, Avail_Assets_SOL):
    Acq_cost = 100
    # Acq_cost = [100 for i in range(21)]
    Upg_cost = 25
    # Orig_Avail_Asset = Avail_Assets
    #   Upg_cost = [25 for i in range(21)]
    VIO = [0] * nPOP
    Cost = [0] * nPOP
    for R in range(0, nPOP):
        # Sort POP with date of action (first column)
        SOL = pop[R]
      #  SOL[:][0] = datetime.strptime('01/01/2021', '%d %m %y')
        df1 = pd.DataFrame(SOL)
        df1.columns = ["date", "Config", "Config_sub", "Project", "Dest", "Source", "Type", "Quantity", "Re",
                       "re-Config", "Cost", "Delay"]
      #   df1["date"] = pd.to_datetime(df1.date)
      # #  df1["date"] = pd.to_datetime(df1["date"])
      #   df1["date"] = df1["date"].dt.strftime('%d/%m/%Y')

        SOL = df1.sort_values(by="date")
       # nSOL = SOL
       # Indx = SOL.index
        Vio = 0
        # Check the type of each schedule from    nSOL = SOL
        #  Reset the Initial Available Assets for each Individual
        w, h = 4, 21
        Local_Avail_Assets = [[0 for x in range(w)] for y in range(h)]
        Local_Avail_Assets[0][0] = 10
        Local_Avail_Assets[0][1] = 10
        Local_Avail_Assets[0][2] = 10
        Local_Avail_Assets[0][3] = 10
        Local_Avail_Assets[3][0] = 6
        Local_Avail_Assets[3][1] = 6
        Local_Avail_Assets[3][2] = 6
        Local_Avail_Assets[3][3] = 12
        Local_Avail_Assets[18][0] = 2
        Local_Avail_Assets[18][1] = 2
        Local_Avail_Assets[18][2] = 2
        # Local_Avail_Assets = Initial_Avail_Assets
        cost = 0
        for S in range(N):
            #  SolArr = SOL.to_numpy()
            sol = SOL.loc[S]

            if sol.iloc[6] == "UPGRADE" or sol.iloc[6] == "UPGRADEWITHMODULES":
                # Check if it is eligible for upgrade...

                # If applicable: Add the quantity to the re-config sol[9] and remove it from the config sol[2]
                Avail_qnty = check_quantity_UPG(sol, Local_Avail_Assets)
                vio = Avail_qnty - sol.iloc[7]
                if vio >= 0:
                    Local_Avail_Assets = remove_quantity(sol, Local_Avail_Assets, sol.iloc[7])
                    Local_Avail_Assets = add_quantity(sol, Local_Avail_Assets, sol.iloc[7])
                    if sol.iloc[2] not in Initial_Assets:
                        cost = cost + (Upg_cost * sol.iloc[7])
                elif Avail_qnty > 0:
                    sol.at['Quantity'] = Avail_qnty  # randint(1, Avail_qnty)
                    # sol.iloc[7] = randint(1, Avail_qnty)
                    Local_Avail_Assets = remove_quantity(sol, Local_Avail_Assets, Avail_qnty)
                    Local_Avail_Assets = add_quantity(sol, Local_Avail_Assets, Avail_qnty)
                    if sol.iloc[2] not in Initial_Assets:
                        cost = cost + (Upg_cost * Avail_qnty)
                # # elif random.random() <= 0.5:  # if not sol[1] in Initial_Assets: RETURN VIO
                # #     sol.at['Type'] = 'ACQUISITION'
                #    # sol.iloc[6] == "ACQUISITION"
                else:
                    sol.at['Quantity'] = sol.iloc[7]  # randint(1, Avail_qnty)
                    # sol.iloc[7] = randint(1, Avail_qnty)
                    Local_Avail_Assets = remove_quantity(sol, Local_Avail_Assets, -vio)
                    Local_Avail_Assets = add_quantity(sol, Local_Avail_Assets, -vio)
                    cost = cost + (Upg_cost * Avail_qnty)
                    Vio = Vio + vio

            elif sol.iloc[6] == "RETIREMENT" or sol.iloc[
                6] == "RETIREMENTWITHMODULES":  # Remove the quantity from the config sol[2]
                Avail_qnty = check_quantity_UPG(sol, Local_Avail_Assets)
                vio = Avail_qnty - sol.iloc[7]
                if vio >= 0:
                    Local_Avail_Assets = remove_quantity(sol, Local_Avail_Assets, sol.iloc[7])
                elif Avail_qnty > 0:
                    sol.at['Quantity'] = Avail_qnty  # randint(1, Avail_qnty)
                    Local_Avail_Assets = remove_quantity(sol, Local_Avail_Assets, Avail_qnty)
                else:
                    Vio = Vio + vio

            elif sol.iloc[6] == "ACQUISITION":  # No Source Pool AND No Upgraded Config.
                Avail_qnty = check_quantity_Acq(sol, Local_Avail_Assets)
                if Avail_qnty <= 0:
                    Local_Avail_Assets = add_quantity(sol, Local_Avail_Assets, sol.iloc[7])
                    cost = cost + (Acq_cost * sol.iloc[7])
                else:
                    Local_Avail_Assets = add_quantity(sol, Local_Avail_Assets, sol.iloc[7])
                    cost = cost + (Acq_cost * sol.iloc[7]) * 1000  # Prevent any redundant operations

            #nSOL.at[Indx[S]] = sol
            SOL.loc[S] = sol
        Cost[R] = cost
        SolArr = SOL.values.tolist()
        pop[R] = SolArr
        VIO[R] = Vio
        # print(R)
        Avail_Assets_SOL[R] = Local_Avail_Assets
    return VIO, Avail_Assets_SOL, pop, Cost


def check_quantity_Acq(sol, avail_mat):  # Check "Dest Pool" --> sol[4]
    ConInx = AllConfig.index(sol[2])
    if sol[4] == "B1_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][0]
    elif sol[4] == "B2_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][1]
    elif sol[4] == "B3_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][2]
    elif sol[4] == "ENABLING_B1_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][3]
    return Avail_quantity


def check_quantity_UPG(sol, avail_mat):  # Check "Source Pool" --> sol[5]
    # Avail_quantity = 0
    if sol[6] == "UPGRADE" or sol[6] == "UPGRADEWITHMODULES":
        ConInx = AllConfig.index(sol[2])
    elif sol[6] == "RETIREMENT" or sol[6] == "RETIREMENTWITHMODULES":
        ConInx = AllConfig.index(sol[2])
    # ConInx = AllConfig.index(sol[9])
    if sol[5] == "B1_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][0]
    elif sol[5] == "B2_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][1]
    elif sol[5] == "B3_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][2]
    elif sol[5] == "ENABLING_B1_UNASSIGNED":
        Avail_quantity = avail_mat[ConInx][3]
    # else:
    #     Avail_quantity = 0
    return Avail_quantity


def remove_quantity(sol, avail_mat, qnity):  # Check "Source Pool" --> sol[5]
    if sol[6] == "UPGRADE" or sol[6] == "UPGRADEWITHMODULES":
        ConInx = AllConfig.index(sol[2])
    elif sol[6] == "RETIREMENT" or sol[6] == "RETIREMENTWITHMODULES":
        ConInx = AllConfig.index(sol[2])
    if qnity >= 0:
        if sol[5] == "B1_UNASSIGNED":
            avail_mat[ConInx][0] = avail_mat[ConInx][0] - qnity
        elif sol[5] == "B2_UNASSIGNED":
            avail_mat[ConInx][1] = avail_mat[ConInx][1] - qnity
        elif sol[5] == "B3_UNASSIGNED":
            avail_mat[ConInx][2] = avail_mat[ConInx][2] - qnity
        elif sol[5] == "ENABLING_B1_UNASSIGNED":
            avail_mat[ConInx][3] = avail_mat[ConInx][3] - qnity

    return avail_mat


def add_quantity(sol, avail_mat, qnity):

    # Check the Pool [Destination or Source]
    if sol[6] == "UPGRADE" or sol[6] == "UPGRADEWITHMODULES":
        PoolInx = sol[5]  # Source Pool
        ConInx = AllConfig.index(sol[9])
    elif sol[6] == "ACQUISITION":
        PoolInx = sol[4]  # Destination Pool
        ConInx = AllConfig.index(sol[2])

    if PoolInx == "B1_UNASSIGNED":
        avail_mat[ConInx][0] = avail_mat[ConInx][0] + qnity
    elif PoolInx == "B2_UNASSIGNED":
        avail_mat[ConInx][1] = avail_mat[ConInx][1] + qnity
    elif PoolInx == "B3_UNASSIGNED":
        avail_mat[ConInx][2] = avail_mat[ConInx][2] + qnity
    elif PoolInx == "ENABLING_B1_UNASSIGNED":
        avail_mat[ConInx][3] = avail_mat[ConInx][3] + qnity
    return avail_mat
