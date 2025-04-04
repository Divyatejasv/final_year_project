# imports
import csv

# Global Variables
FIFTEEN_DROP=20000
TEN_DROP=10000
FIVE_DROP=5000
TWO_DROP=2500
INPUT_FILE_NAME="./data/share_data.csv"
OUTPUT_FILE_NAME="./data/output_shares_data.csv"

class SharesData:
    #Initialiser
    def __init__(self, date, price)->None:
        self.date = date
        self.price = price
        self.shares_fifteen = 0
        self.shares_ten = 0
        self.shares_five = 0
        self.shares_two = 0
        self.max = 0
    def __str__(self) -> str:
        return str(self.__class__) + ":" + str(self.__dict__)
    #Setter
    def set_max(self, max: float)->None:
        self.max = max
    def set_shares(self, max: float)->None:
        self.set_max(max)
        if self.price < 0.85*max:
            self.shares_fifteen = round(FIFTEEN_DROP/self.price)
        elif self.price < 0.9*max:
            self.shares_ten = round(TEN_DROP/self.price)
        elif self.price < 0.95*max:
            self.shares_five = round(FIVE_DROP/self.price)
        elif self.price < 0.98*max:
            self.shares_two = round(TWO_DROP/self.price)
        else:
            pass
    #Get Values as a list
    def get_as_list(self)->list:
        output = []
        output.append(self.date)
        output.append(self.price)
        output.append(self.max)
        output.append(self.shares_fifteen)
        output.append(self.shares_ten)
        output.append(self.shares_five)
        output.append(self.shares_two)
        return output

# Input to the code
def read_from_csv(file_name: str) -> list:
    with open(file_name, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        csv_iter = iter(csv_reader)
        next(csv_iter)
        mylist = []
        for [date , price] in csv_iter:
            price = float(price)
            element = SharesData(date, float(price))
            mylist.append(element)
    return mylist

# Output to the code
def write_to_csv(file_name: str, share_datas: list):
    with open(file_name, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Price", "max" ,"15% drop", "10% drop", "5% drop", "2% drop"])
        for share in share_datas:
            writer.writerow(share.get_as_list())

# Purchase Calculation
def share_calc(share_datas: list)-> list:
    max: float = 0
    for share in share_datas:
        if share.price > max:
            max = share.price
            share.set_max(max)
        else:
            share.set_shares(max)
    return share_datas

def main():
    share_datas = read_from_csv(INPUT_FILE_NAME)
    share_datas = share_calc(share_datas)
    write_to_csv(OUTPUT_FILE_NAME, share_datas)

if __name__ == "__main__":
    main()
