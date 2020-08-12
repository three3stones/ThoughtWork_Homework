"""
需求2：构造一个停车小弟（ParkingBoy），他能够将车顺序停放到多个停车场，并可以取出
"""
from Car import Car
from ParkingLot import ParkingLot

class ParkingBoy:
    def __init__(self, name):
        self.name = name
        
    def park_car(self, car, parkingLotList):
        # 停车成功标志
        flag = False
        for parkingLot in parkingLotList:
            if parkingLot.capacity <= len(parkingLot.cars):
                continue
            else:
                # 返回车票
                return parkingLot.park_car(car)
                flag = True
                break
        # 考虑所有停车场都无空位的情况，抛出异常
        if not flag:
            raise Exception("所有停车场都已经没有空位！")
    
    def take_car(self, ticket, parkingLotList):
        # 取车成功标志
        flag = False
        for parkingLot in parkingLotList:
            if ticket not in parkingLot.tickets:
                continue
            else:
                # 返回汽车
                return parkingLot.take_car(ticket)
                flag = True
                break
        # 考虑所有停车场都无该车票的情况，抛出异常
        if not flag:
            raise Exception("所有停车场都无此车票！")         


if __name__ == "__main__":
    parking_boy = ParkingBoy('bob')
    parking_lot = ParkingLot(1)
    parking_lot1 = ParkingLot(2)
    car = Car('a')
    car1 = Car('b')
    car2 = Car('c')
    car3 = Car('d')
    ticket = parking_boy.park_car(car, [parking_lot, parking_lot1])
    ticket1 = parking_boy.park_car(car1, [parking_lot, parking_lot1])
    ticket2 = parking_boy.park_car(car2, [parking_lot, parking_lot1])
    print(parking_lot.cars)
    print(parking_lot1.cars)
    print(ticket2)
    print(parking_boy.take_car(ticket2, [parking_lot, parking_lot1]))

  


