from pymongo import MongoClient
from pymongo import collection
import pymongo
from bson.dbref import DBRef
import random
from Utilities import Utilities
import time
import datetime


def menu():
    print("\n1. Create a new key")#done
    print("2. Request access to a given room by a given employee")
    print("3. Capture the issue of a key to an employee")
    print("4. Capture losing a key")#done
    print("5. Report out all rooms that an employee can enter given the keys that he/she already has")#not solved
    print("6. Delete a key")#done
    print("7. Delete an employee")#done
    print("8. Add a new door that can be opened by an existing hook")#done
    print("9. Update an access request to move it to a new employee")#done
    print("10. Report all the employees who can get into a room")#Done
    print("11. End")#done
    option = int(input("Chose an option: "))
    return option

def option1():
    hook = []
    oph = db.Hooks
    for x in oph.find():
        hook.append(x["hook_number"])
    for i in range(len(hook)):
        print(f"{i+1}. hook_number {hook[i]}")
    try:
        choice = int(input("What hook do you want to create a new key for? "))
        if hook:
            db.Keys.insert_many([
                {"key_number":7, "key_id":choice}
            ])
            print("Successfully created a new Key!")
        else:
            print(f"No hook with that number {choice}")
    except Exception as e:
        print("Unsure what to do. ")

def option2():
    employee = []
    emplist = db.Employees
    for x in emplist.find():
        employee2 = []
        employee2.append(x["employee_id"])
        employee2.append(x["first_name"])
        employee2.append(x["last_name"])
        employee.append(employee2)
    print("Employee list")
    for x in range(len(employee)):
        print(f"{x + 1}. {employee[x][1]} {employee[x][2]} ID# {employee[x][0]}")
    try:
        choice1 = int(input("Which employee? "))
        rooms = []
        roomlist = db.Accesses
        for x in roomlist.find():
            rooms2 = []
            rooms2.append(x["building_name"])
            rooms2.append(x["room_number"])
            rooms.append(rooms2)
        for x in range(len(rooms)):
            print(f"{x+1}. {rooms[x][0]} Room: {rooms[x][1]}")
        choice2 = (input("Which building? "))
        db.Requests.insert_many([
            {"request_id":7,"loaned_out_date":datetime.datetime.now(),"room_number":100,"building_name":choice2,
             "employee_id":choice1,"requested_date":datetime.datetime.now(),"key_number":8,"key_id":1}
        ])
    except Exception as e:
        print("Unsure what to do. ")
def option3():
    pass
def option4():
    try:
        user = int(input("Enter your ID#: "))
        keys = []
        k = db.Keys
        for x in k.find():
            k2 = []
            k2.append(x["key_id"])
            k2.append(x["key_number"])
            keys.append(k2)
        for x in range(len(keys)):
            print(f"{x}. key_number {keys[x][1]} key_id {keys[x][0]}")
        did = int(input("What key did you lose: "))
        time = datetime.datetime.now()
        print("Alright you owe $25 dollars for losing key",did)
        db.LostKeys.insert_many([
            {"request_id":user,"lost_date":time,"fee":25}
        ])
    except Exception as e:
        print("Unsure what to do. ")
def option5():
    pass
def option6():
    keys = []
    keylist = db.Keys
    hooks = []
    hookslist = db.Keys
    for x in hookslist.find():
        hooks.append(x["key_id"])
    for x in keylist.find():
        keys.append(x["key_number"])
    for i in range(len(keys)):
        print(f"{i+1}. key_number {keys[i]}, key_id {hooks[i]}")
    try:
        choice = int(input("What key do you want to delete? "))
        db.Keys.delete_one({"key_number":choice})
        print("Key has been deleted")
    except Exception as e:
        print("Unsure what to do. ")
def option7():
    employee = []
    emplist = db.Employees
    for x in emplist.find():
        employee2 = []
        employee2.append(x["employee_id"])
        employee2.append(x["first_name"])
        employee2.append(x["last_name"])
        employee.append(employee2)
    print("Employee list")
    for x in range(len(employee)):
        print(f"{x+1}. {employee[x][1]} {employee[x][2]} ID# {employee[x][0]}")
    try:
        choice = int(input("What employee do you want to delete? Enter employee ID "))
        db.Employees.delete_one({"employee_id":choice})
        print("Employee has been deleted")
    except Exception as e:
        print("Unsure what to do. ")
def option8():
    try:
        hook = []
        oph = db.Hooks
        for x in oph.find():
            hook.append(x["hook_number"])
        for i in range(len(hook)):
            print(f"{i + 1}. hook_number {hook[i]}")
        choice1 = int(input("What hook do you want to copy? "))
        building = []
        b = db.Buildings
        for x in b.find():
            building.append(x["building_name"])
        print("Building Names")
        for i in range(len(building)):
            print(f"{i+1}. {building[i]}")
        choice2 = int(input("What building do you want to make a door in? "))
        choice3 = int(input("What room do you want to make? "))
        dn = []
        dnlist = db.DoorNames
        for x in dnlist.find():
            dn.append(x["door_name"])
        print("Door Names")
        for i in range(len(dn)):
            print(f"{i+1}. {dn[i]}")
        choice4 = int(input("What is door do you want? "))
        db.Doors.insert_many([
            {"door_name":dn[choice4-1],"room_number":choice3,"building_name":building[choice2-1]}
        ])
        db.Accesses.insert_many([
            {"hook_number": choice1,"door_name":dn[choice4-1],"room_number":choice3,"building_name":building[choice2-1]}
        ])
        #add to key table and rooms?


    except Exception as e:
        print("Unsure what to do. ")
def option9():
    employee = []
    emplist = db.Employees
    for x in emplist.find():
        employee2 = []
        employee2.append(x["employee_id"])
        employee2.append(x["first_name"])
        employee2.append(x["last_name"])
        employee.append(employee2)
    print("Employee list")
    for x in range(len(employee)):
        print(f"{x + 1}. {employee[x][1]} {employee[x][2]} ID# {employee[x][0]}")
    try:
        choice = int(input("Who are you? Enter your ID# "))
        person1 = []
        req1 = db.Requests
        for x in req1.find():
            person1.append(x["request_id"])
            person1.append(x["loaned_out_date"])
            person1.append(x["room_number"])
            person1.append(x["building_name"])
            person1.append(x["employee_id"])
            person1.append(x["requested_date"])
            person1.append(x["key_number"])
            person1.append(x["key_id"])
            break
        choice2 = int(input("Who are swapping with? "))
        person2 = []
        req2 = db.Requests
        count= 0
        for x in req2.find():
            if count != 0:
                person2.append(x["request_id"])
                person2.append(x["loaned_out_date"])
                person2.append(x["room_number"])
                person2.append(x["building_name"])
                person2.append(x["employee_id"])
                person2.append(x["requested_date"])
                person2.append(x["key_number"])
                person2.append(x["key_id"])
                break
            count+=1
        db.Requests.delete_one({"employee_id": choice})
        db.Requests.delete_one({"employee_id":choice2})
        db.Requests.insert_many([
            {}
        ])
        db.Requests.insert_many([
            {"request_id":person1[0],"loaned_out_date":person1[1],"room_number":person1[2],"building_name":person1[3],
             "employee_id":person2[4],"requested_date":person1[5],"key_number":person1[6],"key_id":person1[7]},
            {"request_id": person2[0], "loaned_out_date": person2[1], "room_number": person2[2],
             "building_name": person2[3],
             "employee_id": person1[4], "requested_date": person2[5], "key_number": person2[6], "key_id": person2[7]}
        ])
    except Exception as e:
        print("Unsure what to do. ")
def option10():
    room = []
    oph = db.Rooms
    for x in oph.find():
        room.append(x["room_number"])
    for i in range(len(room)):
        print(f"{i + 1}. room_number {room[i]}")
    try:
        choice = int(input("Enter what room you want to see which employees can enter: "))
        req = []
        req1 = db.Requests
        for x in req1.find():
            r = []
            r.append(x["room_number"])
            r.append(x["employee_id"])
            req.append(r)
        can = []
        for x in range(len(req)):
            if choice == req[x][1]:
               can.append(req[x][1])
        emp = []
        e = db.Employees
        for x in e.find():
            e2 = []
            e2.append(x["first_name"])
            e2.append(x["last_name"])
            e2.append(x["employee_id"])
            emp.append(e2)
        print("People who can enter room", choice)
        for x in range(len(can)):
            for y in range(len(emp)):
                if can[x] == emp[y][2]:
                    print(f"{emp[y]}")
    except Exception as e:
        print("Unsure what to do. ")
if __name__ == '__main__':
    db = Utilities.startup()
    #populating building
    db.Buildings.drop()
    b: collection = db.Buildings
    b.create_index([("building_name",pymongo.ASCENDING)],unique = True)
    b.insert_many([
        {"building_name": "Engineering and Computer Science"},
        {"building_name": "Fine Arts 1"},
        {"building_name": "Hall of Science"},
        {"building_name": "Horn Center"},
        {"building_name": "Psychology"},
        {"building_name": "Peterson Hall"}
    ])
    #populating employees
    db.Employees.drop()
    e: collection = db.Employees
    e. create_index([("employee_id",pymongo.ASCENDING),("first_name",pymongo.ASCENDING),("last_name",pymongo.ASCENDING)],unique = True)
    e.insert_many([
        {"employee_id": 1, "first_name": "Jose", "last_name": "Jimenez"},
        {"employee_id": 2, "first_name": "Neal", "last_name": "Terrell"},
        {"employee_id": 3, "first_name": "Darin", "last_name": "Goldstein"},
        {"employee_id": 4, "first_name": "Sarah", "last_name": "Taylor"},
        {"employee_id": 5, "first_name": "Frank", "last_name": "Murgolo"},
        {"employee_id": 6, "first_name": "David", "last_name": "Brown"}
    ])
    #populating rooms
    db.Rooms.drop()
    r: collection = db.Rooms
    r.create_index([("building_name", pymongo.ASCENDING),("room_number", pymongo.ASCENDING)],unique=True)
    buildingNames = []
    b = db.Buildings
    for line in b.find():
        buildingNames.append(line["building_name"])
    counter = 0
    roomnums = [100,101,200,308,419,518]
    for bn in buildingNames:
        r.insert_many([
            {"building_name": DBRef("Buildings", bn), "room_number": roomnums[counter]}
        ])
        counter+=1
    #populating doornames
    db.DoorNames.drop()
    dn: collection = db.DoorNames
    dn.create_index([("door_name",pymongo.ASCENDING)],unique=True)
    dn.insert_many([
        {"door_name": "front"},
        {"door_name": "back"},
        {"door_name": "north"},
        {"door_name": "south"},
        {"door_name": "east"},
        {"door_name": "west"}
    ])
    #populating hooks
    db.Hooks.drop()
    h: collection = db.Hooks
    h.create_index([("hook_number",pymongo.ASCENDING)], unique=True)
    h.insert_many([
        {"hook_number": 1},
        {"hook_number": 2},
        {"hook_number": 3},
        {"hook_number": 4},
        {"hook_number": 5},
        {"hook_number": 6}
    ])
    #populating requests
    db.Requests.drop()
    req: collection = db.Requests
    req.create_index([("request_id",pymongo.ASCENDING),("loaned_out_date", pymongo.ASCENDING)],unique = True)
    req.create_index([("room_number", pymongo.ASCENDING), ("building_name", pymongo.ASCENDING),
                      ("employee_id", pymongo.ASCENDING), ("requested_date", pymongo.ASCENDING),
                      ("key_number", pymongo.ASCENDING),("key_id", pymongo.ASCENDING)], unique=False)
    req.insert_many([
        {"request_id":1,"loaned_out_date":None,
         "room_number":100,"building_name":"Engineering and Computer Science","employee_id":1,"requested_date":datetime.datetime.now(),"key_number":1,"key_id":1},
        {"request_id": 2, "loaned_out_date":None
        , "room_number":101, "building_name":"Fine Arts 1", "employee_id":2, "requested_date":datetime.datetime.now(), "key_number":2, "key_id":2},
        {"request_id": 3, "loaned_out_date":None
        , "room_number":200, "building_name":"Hall of Science", "employee_id":3, "requested_date":datetime.datetime.now(), "key_number":3, "key_id":3},
        {"request_id": 4, "loaned_out_date":None
        , "room_number":308, "building_name":"Horn Center", "employee_id":4, "requested_date":datetime.datetime.now(), "key_number":4, "key_id":4},
        {"request_id": 5, "loaned_out_date":None
        , "room_number":419, "building_name":"Psychology", "employee_id":5, "requested_date":datetime.datetime.now(), "key_number":5, "key_id":5},
        {"request_id": 6, "loaned_out_date":None
        , "room_number":518, "building_name":"Peterson Hall", "employee_id":6, "requested_date":datetime.datetime.now(), "key_number":6, "key_id":6}
    ])
    #populating doors
    db.Doors.drop()
    d: collection = db.Doors
    d.create_index([("door_name",pymongo.ASCENDING),("room_number",pymongo.ASCENDING),("building_name",pymongo.ASCENDING)],unique = True)
    d.insert_many([
        {"door_name": "front","room_number":100,"building_name":"Engineering and Computer Science"},
        {"door_name": "back", "room_number": 101, "building_name": "Fine Arts 1"},
        {"door_name": "north", "room_number": 200, "building_name": "Hall of Science"},
        {"door_name": "south", "room_number": 308, "building_name": "Horn Center"},
        {"door_name": "east", "room_number": 419, "building_name": "Psychology"},
        {"door_name": "west", "room_number": 518, "building_name": "Peterson Hall"}
    ])
    #create access
    db.Accesses.drop()
    a: collection = db.Accesses
    a.create_index([("hook_number",pymongo.ASCENDING),("door_name",pymongo.ASCENDING),("room_number",pymongo.ASCENDING),("building_name",pymongo.ASCENDING)],unique = True)
    a.insert_many([
        {"hook_number":1,"door_name": "front", "room_number": 100, "building_name": "Engineering and Computer Science"},
        {"hook_number":2,"door_name": "back", "room_number": 101, "building_name": "Fine Arts 1"},
        {"hook_number":3,"door_name": "north", "room_number": 200, "building_name": "Hall of Science"},
        {"hook_number":4,"door_name": "south", "room_number": 308, "building_name": "Horn Center"},
        {"hook_number":5,"door_name": "east", "room_number": 419, "building_name": "Psychology"},
        {"hook_number":6,"door_name": "west", "room_number": 518, "building_name": "Peterson Hall"}
    ])
    #create lostkeys
    db.LostKeys.drop()
    lk: collection = db.LostKeys
    lk.create_index([("request_id",pymongo.ASCENDING)],unique = True)
    lk.create_index([("lost_date",pymongo.ASCENDING),("fee",pymongo.ASCENDING)],unique = False)
    #create returnkeys
    db.ReturnKeys.drop()
    rk: collection = db.ReturnKeys
    rk.create_index([("request_id",pymongo.ASCENDING)],unique = True)
    rk.create_index([("return_date",pymongo.ASCENDING)],unique = False)
    #maybe  add some into lost keys and return keys
    #create keys
    db.Keys.drop()
    k: collection = db.Keys
    k.create_index([("key_id",pymongo.ASCENDING),("key_number",pymongo.ASCENDING)],unique = True)
    k.insert_many([
        {"key_id":1, "key_number":1},
        {"key_id": 2, "key_number":2},
        {"key_id": 3, "key_number":3},
        {"key_id": 4, "key_number":4},
        {"key_id": 5, "key_number":5},
        {"key_id": 6, "key_number":6}
    ])

    #calling menu and doing the actions
    running = True
    while running:
        ans = menu()
        if ans == 1:
            option1()
            print("Check Key table in Mongo DB!")
        elif ans == 2:
            option2()
            print("Check Request table in Mongo DB!")
        elif ans == 3:
            option3()
            print("Unfortunately couldn't solve :(")
        elif ans == 4:
            option4()
            print("Check Lost Key table in Mongo DB")
        elif ans == 5:
            option5()
            print("Unfortunately couldn't solve :(")
        elif ans == 6:
            option6()
            print("Check Key table in Mongo DB!")
        elif ans == 7:
            option7()
            print("Check Employee table in Mongo DB!")
        elif ans == 8:
            option8()
            print("Check Doors and Accesses table in Mongo DB! ")
        elif ans == 9:
            option9()
            print("Check Request table in Mongo DB!")
        elif ans == 10:
            option10()
            print("Check console above!")
        elif ans == 11:
            running = False


