class Atm(object):
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number
        
    def cashWithdrawl(self):
        print("The cash has been withdrawn")
    def balanceInquiry(self):
        print("Your balance is 50,000")

person1=Atm(12345,2345)
person1.balanceInquiry()
