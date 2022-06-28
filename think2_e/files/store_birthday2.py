import dbm
import pickle

def main():
#    birthday(1,"chapolin","20/20/0000")
    read_db("birthdays")


def read_db(name):
    db = dbm.ndbm.open(name,"c")
    print(db.keys())
    for key in db.keys():
        try:
            print("{} {}".format(pickle.loads(key),pickle.loads(db.get(key))))
        except:
            print("pickle cant transform data back :)")
def birthday(identification,name,date):

    #not working _gdbm.gdbm object as no attribute values
    #working now but cant interate over it :( 
    db_bithday = dbm.ndbm.open("birthdays",'c') # c to open if exists and create if i does not exists
    to_bytes_id = pickle.dumps(identification) # id will be a integer but dbm only accepts strings need pickle

    if (None == db_bithday.get(to_bytes_id)): # if name exists dont add it 
        dic = dict()
        dic[name] = date
        to_bytes_data = pickle.dumps(dic) #string bytes :) can load later prob
        db_bithday[to_bytes_id] = to_bytes_data
        print("birthday day added")
        for key in db_bithday.keys():
            print("{} {}".format(key,db_bithday.get(key)))
        db_bithday.close()
if __name__ == "__main__":
    main()
