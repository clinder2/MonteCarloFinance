import numpy as np

def optionCalc(numTrades, tradeData):
    winning = 0
    losing = 0
    tot_gain = 0
    tot_loss = 0
    ave_gain = 0
    ave_loss = 0
    max_loss = 0
    for t in tradeData:
        if t > 0:
            winning = winning + 1
            tot_gain = tot_gain + t
        else:
            losing = losing + 1
            tot_loss = tot_loss + t
            if t < max_loss:
                tot_loss = tot_loss - t + max_loss
                max_loss = t
    ave_gain = tot_gain/winning
    ave_loss = tot_loss/losing
    gamma = ave_gain/ave_loss # take ave_loss excluding max_loss as size of bet
    lambda_max = max_loss/ave_loss
    E = (winning * 1/numTrades)*gamma - (losing * 1/numTrades) - (1/numTrades)*lambda_max # expected gain
    return [gamma, 1, lambda_max, E]