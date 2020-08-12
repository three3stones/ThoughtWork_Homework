"""
需求4：构造一个超级停车小弟（Super Parking Boy），他能够将车停在空置率最高的那个停车场
"""
from Car import Car
from ParkingLot import ParkingLot
from ParkingBoy import ParkingBoy

# 继承停车小弟
class SuperParkingBoy(ParkingBoy):
    def __init__(self, name):
        super().__init__(name)

    # 重写停车方法
    def park_car(self, car, parkingLotList):
        # 求出所有停车场的空置率
        parkingLot_free_per_list = [(parkingLot.capacity-len(parkingLot.cars))/parkingLot.capacity for parkingLot in parkingLotList]
        if sum(parkingLot_free_per_list) <= 0:
            raise Exception("所有停车场都已经没有空位！")
        else:
            max_index = parkingLot_free_per_list.index(max(parkingLot_free_per_list))
            parkingLot = parkingLotList[max_index]
            # 返回车票
            return parkingLot.park_car(car)

if __name__ == "__main__":
    superParkingBoy = SuperParkingBoy("tom")
    parking_lot = ParkingLot(2)
    parking_lot1 = ParkingLot(3)
    parking_lot_list = [parking_lot, parking_lot1]
    car = Car('a')
    car1 = Car('b')
    car2 = Car('c')
    car3 = Car('d')
    parking_lot.park_car(car)
    parking_lot1.park_car(car1)
    parking_lot1.park_car(car2)
    superParkingBoy.park_car(car3,parking_lot_list)
    print([car.get_name() for car in parking_lot.cars])
    print([car.get_name() for car in parking_lot1.cars])