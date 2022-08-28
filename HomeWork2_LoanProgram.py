# -*- coding: utf-8 -*-
"""
@author: Nicholas Gallagher
Created on Tue Aug 23 23:31:56 2022

"""
#Function to call to process inputs
def pmt(PV, rAPR, nMonths):
    """
    Parameters
    ----------
    PV : TYPE: FLOAT
        DESCRIPTION: How much money we are going to borrow.
    rAPR : TYPE: FLOAT
        DESCRIPTION: Annual % Rate
    nMonths : TYPE: Int
        DESCRIPTION: Loan term
    Returns
    -------
    payment :
        TYPE: FLOAT
        DESCRIPTION: Monthly Payment
    """
    payment = rAPR/1200*PV/(1-(1+(rAPR/1200))**(-nMonths))
    return payment

#While loop we are stuck inside until borrowed amount is zero
while(1):
    
    #Check amount and make a conversion of it from string to float
    p = (input('Enter the amount you wish to borrow (enter 0 to exit) $'))
    print(p)
    pc = float(p)
    
    #Close if amount is zero, if so leave the loop
    if p == '0':
        break
    
    #Check APR and make a conversion of it from string to float
    r = (input('Enter the APR %'))
    print(r)
    rc = float(r)
    
    #Check time and make a conversion of it from string to int
    n = (input('Enter months required to repay loan #'))
    print(n, '\n')
    nc = int(n)
    
    #Call function with users inputs
    myPayment = pmt(pc, rc, nc)
    #Round the returned result
    round(myPayment, 2)
    #Convert it to a string
    str(myPayment)
    #Print the original input amounts and the monthly payment
    print('Amount Borrowed  ${:}'.format(p))
    print('APR  %{:}'.format(r))
    print('Months to repay  #{:}'.format(n))
    print('your monthly payment will be  ${:.2f}'.format(myPayment))
    
#Peace!
print('\n', 'Goodbye...')