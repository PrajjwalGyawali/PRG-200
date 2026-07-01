def remmitance(original_amount,agent_percentage_charge):
    npr = 165 * original_amount
    final_fee = npr - (agent_percentage_charge*npr)
    return final_fee

print(remmitance(100, 0.05)) 