"""
需求5：构造停车场的经理（Parking Manager），他要管理多个停车仔，让他们停车，同时也可以自己停车
"""
from Car import Car
from ParkingLot import ParkingLot
from ParkingBoy import ParkingBoy
from SmartParkingBoy import SmartParkingBoy
from SuperParkingBoy import SuperParkingBoy

class ParkingManager(ParkingBoy):
    def __init__(self, name):
        super().__init__(name)

    # 管理停车仔停车
    def manage(self, parkingBoy:ParkingBoy, car, parkingLotList):
        parkingBoy.park_car(car, parkingLotList)

    # 自己停车，和停车仔一样顺序停车
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


if __name__ == "__main__":
    parkingManager = ParkingManager("tom")
    smartParkingBoy = SmartParkingBoy("bob")
    superParkingBoy = SuperParkingBoy("anna")

    parking_lot = ParkingLot(2)
    parking_lot1 = ParkingLot(3)
    parking_lot_list = [parking_lot, parking_lot1]
    car = Car('a')
    car1 = Car('b')
    car2 = Car('c')
    car3 = Car('d')
    parkingManager.park_car(car, parking_lot_list)
    parkingManager.manage(smartParkingBoy, car1, parking_lot_list)
    parkingManager.manage(superParkingBoy, car2, parking_lot_list)
    print([car.get_name() for car in parking_lot.cars])
    print([car.get_name() for car in parking_lot1.cars])