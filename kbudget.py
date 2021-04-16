import os

class budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float(input("How much is your budget? \n"))
        self.spending = self.budget * 0.5
        self.main()

    def main(self):
        os.system('cls')
        print(" your total budget is \n$",'{:.2f}'.format(self.budget))
        main_option = int(input('what would you like to do?, \n1. check out your total budget, \n2. check spending budget \n'))
        if main_option == 1:
            self.total_budget()
        elif main_option == 2:
            self.spending_budget()
        else:
            leave
    def total_budget(self):
        os.system('cls')
        option = int(input('how much do you want to save? \n1. 20% \n2. 30% \n'))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print("error, please select 1 or 2")
        self.final_saving = self.budget * self.saving
        self.extra = self.budget - self.final_saving - self.spending
        print ('\nSpending: $', '{:.2f}'.format (self.spending), '\nTo save: $', '{:.2f}'.format (self.final_saving),'\nExtra: $', '{:.2f}'.format(self.extra))
        os.system('pause')
        self.main()



    def spending_budget(self):
        os.system('cls')
        print('spending budget: $', '{:.2f}'.format(self.spending))

        Network= int(input('how much Data do you consume annually? \n'))

        books = int (input('how much is spent on books yearly? \n'))

        clothing= self.spending - Network - books

        print ('\n Expenses: \n Network: $', '{:.2f}'.format(Network), '\n books: $', '{:.2f}'.format(books), '\n clothing: $', '{:.2f}'.format(clothing))
        os.system('pause')

        Option = int(input('what would you like to do? \n1. deposit funds, \n2. withdraw funds \n3. transfer \n4. balance \n' ))

        if Option == 1:
            self.depositFunds()

        elif Option == 2:
            self.withdrawFunds()

        elif Option == 3:
            self.transferFunds()

        elif Option == 4:
            print ('\n Expenses: \n Network: $', '{:.2f}'.format(Network), '\n books: $', '{:.2f}'.format(books), '\n clothing: $', '{:.2f}'.format(clothing))
        else:
            print('invalid selection')


        self.main()


    def depositFunds(self):
        os.system('cls')
        Option = int(input('which budget class do you want to deposit funds? \n1 Network \n2 books \n3 clothing \n'))

        if Option == 1:
            add = int(input('how much do you want to deposit to the Network budget? \n'))

            print ('your Network budget for the year is', '{:.2f}'.format (self.spending + add))

        elif Option == 2:
            add2 = int(input('how much do you want deposit into books? \n'))
            print('your new books budget is ', '{:.2f}'.format (self.spending + add2))

        elif Option == 3:
            add3 = int(input('how much would yo ike to add to clothing? \n'))
            print ('your new clothing budget is ', '{:.2f}'.format (self.spending + add3))

        else:
            print('invalid selection')

        self.main()


    def withdrawFunds (self):
        os.system('cls')
        withdrawal = int(input('which budget class do you want to withdraw funds? \n1 Network \n2 books \n3 clothing \n'))

        if withdrawal == 1:
            sub = int(input('how much do you want to withdraw from the Network budget? \n'))
            print ('your Network budget for the year is', '{:.2f}'.format (self.spending - sub ))

        elif withdrawal == 2:
            sub2 = int(input('how much do you want withdraw from books? \n'))
            print('your new books budget is ', '{:.2f}'.format (self.spending - sub2))

        elif withdrawal == 3:
            sub3 = int(input('how much would you like to withdraw from clothing? \n'))
            print ('your new clothing budget is ', '{:.2f}'.format (self.spending - sub3))

        else:
            print('invalid selection')

        self.main()


    def transferFunds(self):

        os.system('cls')
        Transfer = int(input('which budget class do you want to transfer funds? \n1 Network \n2 books \n3 clothing \n'))

        if Transfer == 1:
            tran = int(input('how much do you want to transfer from the Network budget? \n'))
            tran_1 = int(input('which budget class  do you wanto transfer the fund to? \n1. books \n2. clothing \n'))
            if tran_1 == 1:

                print ('you have transferred funds from Network budget to clothing budget')
            elif tran_1 == 2:
                print ('you have transferred funds from Network budget to books budget')
            else:
                print('invalid selection')


        elif Transfer == 2:
            tran2 = int(input('how much do you want to transfer from the books budget? \n'))
            tran_2 = int(input('which budget class do you want to transfer the fund to? \n1. Network \n2. clothing \n'))
            if tran_2 == 1:
                print ('you have transferred funds from  books budget  to Network budget')
            elif tran_2 == 2:
                print ('you have transferred funds from books budget to clothing budget')
            else:
                print('invalid selection')


        elif Transfer == 3:
            tran3 = int(input('how much would you like to transfer from clothing? \n'))
            tran_3 = int(input('which budget class do you want to transfer the fund to? \n1. Network \n2. books \n'))
            if tran_3 == 1:
               print ('you have transferred funds from  clothing budget to  Network budget')
            elif tran_3 == 2:
                print ('you have transferred funds from clothing budget to books budget')
            else:
                print('invalid selection')


        else:
            print('invalid selection')

        self.main()


budget()
