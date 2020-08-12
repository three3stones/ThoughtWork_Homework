"""
需求1：构造一个停车场，停车场可以停车和取车，停车成功后得到停车票。 用户取车的时候也需要提供停车票，停车票有效，才可以成功取到车。
"""
from Car import Car
import uuid

class ParkingLot:
    def __init__(self, capacity):
        # todo: 构造停车场所需的字段
        self.capacity = capacity
        self.cars = []          # 存储汽车
        self.tickets = []         # 存储车票

    def park_car(self, car: Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        # 判断是否能够停车
        if self.capacity <= len(self.cars):
            raise Exception("该停车场已经没有空位！")
        else:
            self.cars.append(car)
            uuid_ticket = uuid.uuid4()
            self.tickets.append(uuid_ticket)
            return uuid_ticket

    def take_car(self, ticket):
        # todo: 实现通过车票取车的功能
        if len(self.cars) == 0:
            raise Exception("该停车场现在没有停放车辆！")
        if ticket not in self.tickets:
            raise Exception("非法车票！")
        else:
            index = self.tickets.index(ticket)
            self.tickets.remove(ticket)
            return self.cars.pop(index)


if __name__ == "__main__":
    parking_lot = ParkingLot(1)
    car = Car('bob')
    ticket = parking_lot.park_car(car)
    car = parking_lot.take_car(ticket)
