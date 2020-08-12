"""
需求3：构造一个聪明的停车小弟（Smart Parking Boy），他能够将车停在空车位最多的那个停车场
"""
from Car import Car
from ParkingLot import ParkingLot
from ParkingBoy import ParkingBoy

# 继承停车小弟
class SmartParkingBoy(ParkingBoy):
    def __init__(self, name):
        super().__init__(name)

    # 重写停车方法
    def park_car(self, car, parkingLotList):
        # 求出所有停车场的空车位个数
        parkingLot_free_num_list = [parkingLot.capacity - len(parkingLot.cars) for parkingLot in parkingLotList]
        if sum(parkingLot_free_num_list) <= 0:
            raise Exception("所有停车场都已经没有空位！")
        else:
            max_index = parkingLot_free_num_list.index(max(parkingLot_free_num_list))
            parkingLot = parkingLotList[max_index]
            # 返回车票
            return parkingLot.park_car(car)

if __name__ == "__main__":
    smartParkingBoy = SmartParkingBoy("tom")
    parking_lot = ParkingLot(3)
    parking_lot1 = ParkingLot(2)
    parking_lot_list = [parking_lot, parking_lot1]
    car = Car('a')
    car1 = Car('b')
    car2 = Car('c')
    parking_lot.park_car(car)
    parking_lot.park_car(car1)
    smartParkingBoy.park_car(car2,parking_lot_list)
    print([car.get_name() for car in parking_lot.cars])
    print([car.get_name() for car in parking_lot1.cars])