#!/bin/bash
import sys
import math

# parameters
MAX_SPEED = 6.0  # max forward speed
MAX_BACKWARD_SPEED = -2.0  # max back speed
MAX_ROTATION_SPEED = math.pi  # max rotate speed
dt=0.02
ROBOT_DENSITY = 20  #
MAX_TRACTION_FORCE = 250  #
MAX_TORQUE = 50  #
# ROBOT_RADIUS = 0.45  #

class robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.line_speed_x=0.0
        self.line_speed_y=0.0
        self.angle_speed=0.0
        self.direction=None#方向

        self.InServerID=None#在哪个server的范围内
        self.CarryType=None#携带的物品类型
        self.TimeValue=None#时间价值
        self.CollisionValue=None#碰撞价值
        self.moveQueue=[]#移动目标的队列


# class server:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

class server1:
    def __init__(self,x,y,ID):
        self.x = x
        self.y = y
        self.ID=ID
        self.type=1
        self.canBuy=[]
        self.workCycle=50
        self.product=1#产品类型
        self.nextSell=[4,5,9]
        self.nextServers=[] ##id:0 distance:1
        self.RemainTimeProduction=None
        self.MaterialStatus=0#原材料格子状态
        self.ProductionStatus=None#产品格子状态
        self.beChoose=0

        self.buyPrice=3000
        self.sellPrice=6000
class server2:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 2
        self.canBuy=[]
        self.nextSell = [4, 6,9]
        self.nextServers = []
        self.workCycle=50
        self.product=2
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 4400
        self.sellPrice = 7600
class server3:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 3
        self.canBuy=[]
        self.nextSell = [5, 6,9]
        self.nextServers = []
        self.workCycle=50
        self.product=3
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 5800
        self.sellPrice = 9200
class server4:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 4
        self.canBuy=[1,2]
        self.nextSell = [7, 9]
        self.nextServers = []
        self.workCycle=500
        self.product=4
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 15400
        self.sellPrice = 22500
class server5:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 5
        self.canBuy=[1,3]
        self.nextSell = [7, 9]
        self.nextServers = []
        self.workCycle=500
        self.product=5
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 17200
        self.sellPrice = 25000
class server6:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 6
        self.canBuy=[2,3]
        self.nextSell = [7, 9]
        self.nextServers = []
        self.workCycle=500
        self.product=6
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 19200
        self.sellPrice = 27500
class server7:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 7
        self.canBuy=[4,5,6]
        self.nextSell = [8, 9]
        self.nextServers = []
        self.workCycle=1000
        self.product=7
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = 0

        self.buyPrice = 76000
        self.sellPrice = 105000
class server8:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 8
        self.canBuy=[7]
        self.nextSell = []
        self.nextServers = []
        self.workCycle=1
        self.product=[]
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = -1000
class server9:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = ID
        self.type = 9
        self.canBuy=[i for i in range(1,8)]
        self.nextSell = []
        self.nextServers = []
        self.workCycle=1
        self.product=[]
        self.RemainTimeProduction=None
        self.MaterialStatus=0
        self.ProductionStatus=None
        self.beChoose = -1000

#read data init
def read_util_ok_init():
    map = []
    tmp = input()
    while tmp != "OK":
        map.append(tmp)
        tmp = input()
        pass
    return map

#read data every frame
def read_util_ok():
    server_info = []
    robot_info=[]
    K = int(input())
    for i in range(K):
        server_tmp=input()
        server_tmp=server_tmp.split(" ")
        server_tmp[0]=int(server_tmp[0])
        server_tmp[1]=float(server_tmp[1])
        server_tmp[2]=float(server_tmp[2])
        server_tmp[3]=int(server_tmp[3])
        server_tmp[4]=int(server_tmp[4])
        server_tmp[5]=int(server_tmp[5])
        server_info.append(server_tmp)
    for i in range(4):
        robot_tmp=input()
        robot_tmp=robot_tmp.split(" ")
        robot_tmp[0]=int(robot_tmp[0])
        robot_tmp[1]=int(robot_tmp[1])
        robot_tmp[2]=float(robot_tmp[2])
        robot_tmp[3]=float(robot_tmp[3])
        robot_tmp[4]=float(robot_tmp[4])
        robot_tmp[5]=float(robot_tmp[5])
        robot_tmp[6]=float(robot_tmp[6])
        robot_tmp[7]=float(robot_tmp[7])
        robot_tmp[8]=float(robot_tmp[8])
        robot_tmp[9]=float(robot_tmp[9])

        robot_info.append(robot_tmp)
    tmp=input()
    if tmp == "OK":
        return K,server_info,robot_info
    else:
        print("read error")

def finish():
    sys.stdout.write('OK\n')
    sys.stdout.flush()

def calDisBetweenServers(server1,server2):
    return math.sqrt((server1.x - server2.x) ** 2 + (server1.y - server2.y) ** 2)

def calDisBetweenRobotServer(robot,server):
    return math.sqrt((robot.x - server.x) ** 2 + (robot.y - server.y) ** 2)

# def chargeIfStoreAnythingInServer(server):
#     if server.MaterialStatus==None
#     for i in range(1,7):
#         if i>
#         if chargeIfStoreXInServer(i,server):
#             return True
#     #循环结束没有就是false
#     return False


def chargeIfStoreXInServer(x,server):
    if server.MaterialStatus==None:
        return False
    decimal_num = server.MaterialStatus
    binary_str = bin(decimal_num)[2:]
    if len(binary_str)<x:
        return False
    elif binary_str[len(binary_str)-1-x]=="1":
        return True
    else:
        return False
#
# def server_map_distance(Server):
#     for type in range(len(Server)):
#         for server1 in Server[type]:
#             nextServers=[]
#             for NextSellServer in server1.nextSell:
#                 for server2 in Server[NextSellServer-1]:
#                         nextServers.append((server2.ID,int(calDisBetweenServers(server1,server2))))
#             nextServers.sort(key=lambda x:x[1])
#             server1.nextServers=nextServers
#
# def FindserverByID(id,Server):
#     id=int(id)
#     for i in range(len(Server)):
#         if len(Server[i])>id:
#             return Server[i][id-1]
#         else:
#             id=id-len(Server[i])
#
# def findNextServerForSell(server):
#     next_count = 0
#     while next_count<len(server.nextServers) and chargeIfStoreXInServer(server.type, Server[server_index[server.nextServers[next_count][0]][0]][server_index[server.nextServers[next_count][0]][1]]) == True:
#         next_count += 1
#     return next_count
#
# def InitChoose(robot,Server):
#     ChooseQueue=[]
#     alpha=1.0
#     for type in range(3):
#         for server in Server[type]:
#             if server.beChoose<=0:
#                 if findNextServerForSell(server)<len(server.nextServers):
#                     ChooseQueue.append((server.ID, alpha*math.sqrt(calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     continue
#             elif server.beChoose==1:
#                 if server.ProductionStatus==1 and server.RemainTimeProduction*dt*MAX_SPEED<calDisBetweenRobotServer(robot,server):
#                     ChooseQueue.append((server.ID, alpha * math.sqrt(
#                         calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     continue
#             else:
#                 continue
#     if len(ChooseQueue) > 0:
#         ChooseQueue.sort(key=lambda x:x[1])
#         robot.moveQueue.append((ChooseQueue[0][0],1))
#         Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]].beChoose+=1
#     # robot.moveQueue.append((Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]].nextServers[findNextServerForSell(Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]])][0],0))
#
# def Choose1(robot,Server):
#     ChooseQueue=[]
#     alpha=1.0
#     for type in range(len(Server)):
#         for server in Server[type]:
#             ##TODO need to improve
#             if server.beChoose <= 0 and server.ProductionStatus==1:
#                 if findNextServerForSell(server) < len(server.nextServers):
#                     ChooseQueue.append((server.ID, alpha * math.sqrt(
#                         calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     continue
#             elif server.beChoose == 1:
#                 if server.ProductionStatus == 1 and server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(
#                         robot, server):
#                     ChooseQueue.append((server.ID, alpha * math.sqrt(
#                         calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     continue
#             else:
#                 continue
#     ChooseQueue.sort(key=lambda x:x[1])
#     if len(ChooseQueue) > 0:
#         robot.moveQueue.append((ChooseQueue[0][0], 1))
#         Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]].beChoose += 1
#         robot.moveQueue.append((Server[server_index[ChooseQueue[0][0]][0]][
#                                     server_index[ChooseQueue[0][0]][1]].nextServers[findNextServerForSell(
#             Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]])][0], 0))
#     # robot.moveQueue.append((ChooseQueue[0][0],1))
#     # robot.moveQueue.append(ChooseQueue[0][0].nextServers[findNextServerForSell(server)][0],0)
#     # robot.moveQueue.append((FindserverByID(ChooseQueue[0][0],Server).nextServers[findNextServerForSell(FindserverByID(ChooseQueue[0][0],Server))][0],0))
#     return ChooseQueue[0][0]
#
#
# def ChooseForBuy(robot,Server):
#     ChooseQueue=[]
#     alpha=1.0
#     for type in range(8):
#         for server in Server[type]:
#             ##TODO need to improve
#             if server.beChoose <= 0:
#                 if server.ProductionStatus==1 and findNextServerForSell(server) < len(server.nextServers):
#                     ChooseQueue.append((server.ID, alpha * math.sqrt(calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     if server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(
#                         robot, server):
#                         ChooseQueue.append((server.ID, alpha * math.sqrt(
#                             calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                     else:
#                         continue
#             elif server.beChoose == 1:
#                 if server.ProductionStatus == 1 and server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(
#                         robot, server):
#                     ChooseQueue.append((server.ID, alpha * math.sqrt(
#                         calDisBetweenServers(robot, server) + server.nextServers[findNextServerForSell(server)][1])))
#                 else:
#                     continue
#             else:
#                 continue
#     ChooseQueue.sort(key=lambda x:x[1])
#
#     return ChooseQueue[0][0]
#
# def ChooseForBuyTheNearestOne(robot,Server):
#     ChooseQueue=[]
#     for type in range(8):
#         for server in Server[type]:
#             ##TODO need to improve
#             if server.beChoose <= 0:
#                 if server.ProductionStatus==1:
#                     ChooseQueue.append((server.ID, calDisBetweenRobotServer(robot,server)))
#                 else:
#                     if server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(robot, server):
#                         ChooseQueue.append((server.ID, calDisBetweenRobotServer(robot,server)))
#                     else:
#                         continue
#             elif server.beChoose == 1:
#                 if server.ProductionStatus == 1 and server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(
#                         robot, server):
#                     ChooseQueue.append((server.ID, calDisBetweenServers(robot, server)))
#                 else:
#                     continue
#             else:
#                 continue
#     ChooseQueue.sort(key=lambda x:x[1])
#     if len(ChooseQueue)>0:
#         Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]].beChoose+=1
#         return ChooseQueue[0][0]
#     else:
#         ChooseQueue = []
#         alpha = 1.0
#         for type in range(3):
#             for server in Server[type]:
#                 if server.beChoose <= 0:
#                     ChooseQueue.append((server.ID, calDisBetweenRobotServer(robot,server)))
#                 elif server.beChoose == 1:
#                     if server.ProductionStatus == 1 and server.RemainTimeProduction * dt * MAX_SPEED < calDisBetweenRobotServer(
#                             robot, server):
#                         ChooseQueue.append((server.ID, calDisBetweenRobotServer(robot,server)))
#                     else:
#                         continue
#                 else:
#                     continue
#         if len(ChooseQueue) > 0:
#             ChooseQueue.sort(key=lambda x: x[1])
#             robot.moveQueue.append((ChooseQueue[0][0], 1))
#             Server[server_index[ChooseQueue[0][0]][0]][server_index[ChooseQueue[0][0]][1]].beChoose += 1
#             return ChooseQueue[0][0]
#
# # def calAngelDifference
#
# def ChooseServerForSell(robot,Server):
#     type=int(robot.CarryType)
#     sys.__stderr__.write(str(Server[type - 1][0].nextSell))
#     chooseQueue=[]
#     for Servertype in Server[type-1][0].nextSell:
#
#         for server_tmp in Server[Servertype-1]:
#             if chargeIfStoreXInServer(type,server_tmp)==True and (server_tmp.ID!=8 or server_tmp.ID!=9):
#                 continue
#             else:
#                 distance=calDisBetweenRobotServer(robot,server_tmp)
#                 tmp=[]
#                 tmp.append(server_tmp.ID)
#                 tmp.append(distance)
#
#                 chooseQueue.append(tmp)
#         # sys.__stderr__.write("No server for sell")
#     chooseQueue.sort(key=lambda x:x[1])
#     chooseId=chooseQueue[0][0]
#     robot.moveQueue=[(chooseId,0)]
#     return chooseId
#
# def ChooseServerBuy_AccordingToNeed(robot,Server):
#     needQueue1=[]
#     needQueue2=[]
#     needQueue3=[]
#     #TODO 可以加一个先送server7有产品的
#     for server7 in Server[6]:
#
#         #如果原材料有了一部分
#         if server7.MaterialStatus>0:
#             MaterialCount = 0
#             #找缺的是哪一种原材料
#             # MaterialCount += 1
#             for i in server7.canBuy:
#                 if chargeIfStoreXInServer(i,server7):
#                     MaterialCount+=1
#                     continue
#                 #对于缺的456
#                 else:
#                     for server_456 in Server[i-1]:
#                         #先找已有产品的456
#                         if server_456.ProductionStatus==1:
#                             #查看可以买的123类型
#                             for need_123type in server_456.canBuy:
#                                 if chargeIfStoreXInServer(need_123type,server_456):
#                                     continue
#                                 #看缺啥优先买啥
#                                 else:
#                                     for server123 in Server[need_123type-1]:
#                                         needQueue1.append((server123.ID,(calDisBetweenRobotServer(robot,server123)+calDisBetweenServers(server123,server_456))))
#                         #没有产品的456
#                         else:
#                             for need_123type in server_456.canBuy:
#                                 if chargeIfStoreXInServer(need_123type,server_456):
#                                     continue
#                                 #看缺啥优先买啥
#                                 else:
#                                     for server123 in Server[need_123type-1]:
#                                         needQueue2.append((server123.ID,(calDisBetweenRobotServer(robot,server123)+calDisBetweenServers(server123,server_456))))
#             if MaterialCount==2:
#                 sys.stderr.write("紧急选择")
#                 if len(needQueue1) > 0:
#                     needQueue1.sort(key=lambda x: x[1])
#                     return needQueue1[0][0]
#                 else:
#                     if len(needQueue2) > 0:
#                         needQueue2.sort(key=lambda x: x[1])
#                         return needQueue2[0][0]
#                     else:
#                         return ChooseServerBuy_Demo(robot, Server)
#         else:
#             for servertype in range(4,7):
#                 for server_456 in Server[servertype - 1]:
#                     # 先找已有产品的456
#                     if server_456.ProductionStatus == 1:
#                         # 查看可以买的123类型
#                         for need_123type in server_456.canBuy:
#                             if chargeIfStoreXInServer(need_123type, server_456):
#                                 continue
#                             # 看缺啥优先买啥
#                             else:
#                                 for server123 in Server[need_123type - 1]:
#                                     needQueue1.append((server123.ID, (
#                                                 calDisBetweenRobotServer(robot, server123) + calDisBetweenServers(
#                                             server123, server_456))))
#                     # 没有产品的456
#                     else:
#                         for need_123type in server_456.canBuy:
#                             if chargeIfStoreXInServer(need_123type, server_456):
#                                 continue
#                             # 看缺啥优先买啥
#                             else:
#                                 for server123 in Server[need_123type - 1]:
#                                     needQueue2.append((server123.ID, (
#                                                 calDisBetweenRobotServer(robot, server123) + calDisBetweenServers(
#                                             server123, server_456))))
#     if len(needQueue1)>0:
#         needQueue1.sort(key=lambda x:x[1])
#         return needQueue1[0][0]
#     else:
#         if len(needQueue2)>0:
#             needQueue2.sort(key=lambda x:x[1])
#             return needQueue2[0][0]
#         else:
#             return ChooseServerBuy_Demo(robot,Server)
#
# def ChooseServerBuy_AccordingToNeed2(robot,Server,Same_flag):
#     needQueue1=[]
#     needQueue2=[]
#     needQueue3=[]
#     #TODO 可以加一个先送server7有产品的
#     for server7 in Server[6]:
#
#         #如果原材料有了一部分
#         if server7.MaterialStatus>0:
#             MaterialCount = 0
#             #找缺的是哪一种原材料
#             # MaterialCount += 1
#             for i in server7.canBuy:
#                 if chargeIfStoreXInServer(i,server7):
#                     MaterialCount+=1
#                     continue
#                 #对于缺的456
#                 else:
#                     for server_456 in Server[i-1]:
#                         #先找已有产品的456
#                         if server_456.ProductionStatus==1:
#                             #查看可以买的123类型
#                             for need_123type in server_456.canBuy:
#                                 if chargeIfStoreXInServer(need_123type,server_456):
#                                     continue
#                                 #看缺啥优先买啥
#                                 else:
#                                     for server123 in Server[need_123type-1]:
#                                         needQueue1.append((server123.ID,(calDisBetweenRobotServer(robot,server123)+calDisBetweenServers(server123,server_456))))
#                         #没有产品的456
#                         else:
#                             for need_123type in server_456.canBuy:
#                                 if chargeIfStoreXInServer(need_123type,server_456):
#                                     continue
#                                 #看缺啥优先买啥
#                                 else:
#                                     for server123 in Server[need_123type-1]:
#                                         needQueue2.append((server123.ID,(calDisBetweenRobotServer(robot,server123)+calDisBetweenServers(server123,server_456))))
#             if MaterialCount==2:
#                 sys.stderr.write("紧急选择")
#                 if len(needQueue1) > Same_flag:
#                     needQueue1.sort(key=lambda x: x[1])
#                     return needQueue1[Same_flag][0]
#                 else:
#                     if len(needQueue2) > Same_flag:
#                         needQueue2.sort(key=lambda x: x[1])
#                         return needQueue2[Same_flag][0]
#                     else:
#                         return ChooseServerBuy_Demo(robot, Server)
#         else:
#             for servertype in range(4,7):
#                 for server_456 in Server[servertype - 1]:
#                     # 先找已有产品的456
#                     if server_456.ProductionStatus == 1:
#                         # 查看可以买的123类型
#                         for need_123type in server_456.canBuy:
#                             if chargeIfStoreXInServer(need_123type, server_456):
#                                 continue
#                             # 看缺啥优先买啥
#                             else:
#                                 for server123 in Server[need_123type - 1]:
#                                     needQueue1.append((server123.ID, (
#                                                 calDisBetweenRobotServer(robot, server123) + calDisBetweenServers(
#                                             server123, server_456))))
#                     # 没有产品的456
#                     else:
#                         for need_123type in server_456.canBuy:
#                             if chargeIfStoreXInServer(need_123type, server_456):
#                                 continue
#                             # 看缺啥优先买啥
#                             else:
#                                 for server123 in Server[need_123type - 1]:
#                                     needQueue2.append((server123.ID, (
#                                                 calDisBetweenRobotServer(robot, server123) + calDisBetweenServers(
#                                             server123, server_456))))
#     if len(needQueue1)>Same_flag:
#         needQueue1.sort(key=lambda x:x[1])
#         return needQueue1[Same_flag][0]
#     else:
#         if len(needQueue2)>Same_flag:
#             needQueue2.sort(key=lambda x:x[1])
#             return needQueue2[Same_flag][0]
#         else:
#             return ChooseServerBuy_Demo(robot,Server)

map1=['....................................................................................................', '.................................................1..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..............................................5..5..5...............................................', '....................................................................................................', '....................................................................................................', '...........................................5..5..9..5..5............................................', '....................................................................................................', '....................................................................................................', '........................................5..A..7..7..7..A..5.........................................', '....................................................................................................', '....................................................................................................', '...........................................9..7..8..7..9............................................', '....................................................................................................', '....................................................................................................', '.....................................4..4..A..7..7..7..A..6..6......................................', '....................................................................................................', '....................................................................................................', '.....................................4..4..4..4..9..6..6..6..6......................................', '....................................................................................................', '....................................................................................................', '........................................4..4..4.....6..6..6.........................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.2................................................................................................3.', '....................................................................................................']
map2=['....................................................................................................', '.6...............................................5................................................6.', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................7..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................1..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '...........................................2...........2............................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '...................................3...........................3....................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................A..................................................', '....................................................................................................', '.5......................8....1.................A.4.A.................1....8.......................5.', '....................................................................................................', '.................................................A..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '...................................3...........................3....................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '...........................................2...........2............................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................1..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................7..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.6...............................................5................................................6.', '....................................................................................................']
map3=['....................................................................................................', '..............................................3.......5.............................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..........................................5...............5.........................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..........................................5...............5.........................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..............................................1.......2.............................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.4......4.....4...................................................................6.....6.....6.....', '....................................................................................................', '....................................................................................................', '..................................................................................................6.', '....................................................................................................', '.................1..................................................................................', '..................................................................................2.................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.4......4.....3...................................................................................6.', '....................................................................................................', '....................................................................................................', '..................................................A...............................1.....6.....6.....', '....................................................................................................', '................................................A.9.A...............................................', '....................................................................................................', '..................................................A...............................................6.', '.4.........4........................................................................................', '....................................................................................................', '..................................................................................3.................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..................................................................................................6.', '....................................................................................................', '.4...............2................................................................6.....6......6....', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................2.......1.....................................2.......4.......3.................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..........................................................................4.........................', '................5...............3...................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..........................................................................3.........................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '................5...............5...................................................................', '..........................................................................4.........................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................5.......5.............................................1.........................', '....................................................................................................']
map4=['....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................7..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.........1.......................................1.......................................1..........', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..............2..................................2..................................2...............', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '...................3.............................3.............................3....................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '........................5........................6........................5.........................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.............................6...................5...................6..............................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '..................................A.............................A...................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.......................................A...................A........................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................8..................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '....................................................................................................', '.................................................4..................................................', '....................................................................................................', '....................................................................................................']

# # Demo中选server的实现
# def ChooseServerBuy_Demo(robot, Server):
#     ChooseQueue=[]
#     for type in range(3):
#         for server_tmp in Server[type]:
#             distance=calDisBetweenRobotServer(robot,server_tmp)
#             ChooseQueue.append((server_tmp.ID,distance))
#     ChooseQueue.sort(key=lambda x:x[1])
#     # sys.stderr.write(str(ChooseQueue))
#     return ChooseQueue[0][0]
#
# def ChooseServerBuy_Demo2(robot, Server,Same_Flag):
#     ChooseQueue=[]
#     for type in range(3):
#         for server_tmp in Server[type]:
#             distance=calDisBetweenRobotServer(robot,server_tmp)
#             ChooseQueue.append((server_tmp.ID,distance))
#     ChooseQueue.sort(key=lambda x:x[1])
#     return ChooseQueue[Same_Flag][0]
#
# #Demo中选择服务器卖
# def ChooseServerSell_Demo(robot,Server):
#     type = int(robot.CarryType)
#     chooseQueue1 = []
#     chooseQueue2 = []
#     chooseQueue3 = []
#     chooseQueue4=[]
#     #要是没地方去了就用这个
#     chooseQueue5=[]
#     for Servertype in Server[type - 1][0].nextSell:
#         for server_tmp in Server[Servertype - 1]:
#             distance = calDisBetweenRobotServer(robot, server_tmp)
#             tmp = []
#             tmp.append(server_tmp.ID)
#             tmp.append(distance)
#             chooseQueue4.append(tmp)
#             #判断是否已经有type类型存在里面了。
#             if chargeIfStoreXInServer(type, server_tmp) == True:
#                 continue
#             else:
#
#                 # 判断是否有产品：
#                 if server_tmp.ProductionStatus == 1:
#                     chooseQueue1.append(tmp)
#                 else:
#                     if (server_tmp.type != 8 and server_tmp.type != 9):
#                         if server_tmp.MaterialStatus > 0:
#                         # if server_tmp.ProductionStatus==1:
#                             chooseQueue2.append(tmp)
#                         else:
#                             chooseQueue3.append(tmp)
#     #根据优先级不同选择不同目标
#     if len(chooseQueue1)>0:
#         chooseQueue1.sort(key=lambda x:x[1])
#         return chooseQueue1[0][0]
#     else:
#         if len(chooseQueue2)>0:
#             chooseQueue2.sort(key=lambda x:x[1])
#             return chooseQueue2[0][0]
#         else:
#             if len(chooseQueue3)>0:
#                 chooseQueue3.sort(key=lambda x:x[1])
#                 return chooseQueue3[0][0]
#             else:
#                 chooseQueue4.sort(key=lambda x:x[1])
#                 return chooseQueue4[0][0]
#
#
# #Demo中选择服务器卖
# def ChooseServerSell_Demo2(robot,Server,Same_Flag):
#     type = int(robot.CarryType)
#     chooseQueue1 = []
#     chooseQueue2 = []
#     chooseQueue3 = []
#     chooseQueue4=[]
#     #要是没地方去了就用这个
#     chooseQueue5=[]
#     for Servertype in Server[type - 1][0].nextSell:
#         for server_tmp in Server[Servertype - 1]:
#             distance = calDisBetweenRobotServer(robot, server_tmp)
#             tmp = []
#             tmp.append(server_tmp.ID)
#             tmp.append(distance)
#             chooseQueue4.append(tmp)
#             #判断是否已经有type类型存在里面了。
#             if chargeIfStoreXInServer(type, server_tmp) == True:
#                 continue
#             else:
#                 # 判断是否有产品：
#
#                 if server_tmp.ProductionStatus == 1:
#                     chooseQueue1.append(tmp)
#                 else:
#                     if (server_tmp.type != 8 and server_tmp.type != 9):
#                         if server_tmp.MaterialStatus > 0:
#                             # if server_tmp.ProductionStatus==1:
#                             chooseQueue2.append(tmp)
#                         else:
#                             chooseQueue3.append(tmp)
#     #根据优先级不同选择不同目标
#     if len(chooseQueue1)-Same_Flag>0:
#         chooseQueue1.sort(key=lambda x:x[1])
#         return chooseQueue1[Same_Flag][0]
#     else:
#         if len(chooseQueue2)-Same_Flag>0:
#             chooseQueue2.sort(key=lambda x:x[1])
#             return chooseQueue2[Same_Flag][0]
#         else:
#             if len(chooseQueue3)-Same_Flag>0:
#                 chooseQueue3.sort(key=lambda x:x[1])
#                 return chooseQueue3[Same_Flag][0]
#             else:
#                 chooseQueue4.sort(key=lambda x:x[1])
#                 return chooseQueue4[0][0]


def getMoveQueue1():
    moveQueue1 = [(0, 1), (13, 0), (0, 1), (20, 0), (20, 1), (11, 0), (0, 1), (19, 0), (41, 1), (19, 0), (42, 1), (13, 0),
                  (0, 1), (20, 0), (20, 1), (12, 0), (42, 1), (13, 0), (13, 1), (11, 0), (0, 1), (19, 0), (41, 1), (38, 0),
                  (0, 1), (13, 0), (41, 1), (20, 0), (42, 1), (31, 0), (13, 1), (12, 0), (0, 1), (13, 0), (41, 1), (31, 0),(13, 1), (12, 0), (12, 1), (16, 0),
                  (31, 1), (30, 0), (13, 1), (18, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),]
    moveQueue2 = [(0, 1), (20, 0), (0, 1), (13, 0), (42, 1), (13, 0), (42, 1), (31, 0), (41, 1), (20, 0), (20, 1), (11, 0),
                  (42, 1), (38, 0), (41, 1), (38, 0), (42, 1), (38, 0), (38, 1), (11, 0), (0, 1), (19, 0), (41, 1), (31, 0),
                  (31, 1), (12, 0), (41, 1), (20, 0), (19, 1), (11, 0), (38, 1), (11, 0), (42, 1), (32, 0), (41, 1), (20, 0),
                  (20, 1), (11, 0), (32,1),(11,0),(11,1),(6,0),(42, 1), (38, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),]
    moveQueue3 = [(41, 1), (20, 0), (42,1), (13, 0), (41, 1), (31, 0), (31, 1), (11, 0), (0, 1), (13, 0), (13, 1), (11, 0),
                  (42, 1), (31, 0), (31, 1), (11, 0), (11, 1), (6, 0), (0, 1), (13, 0), (13, 1), (12, 0), (41, 1), (19, 0),
                  (19, 1), (11, 0), (11, 1), (18, 0), (41, 1), (31, 0), (0, 1), (13, 0), (42, 1), (13, 0), (13, 1), (11, 0),
                  (11,1 ), (30, 0), (42, 1), (13, 0), (0, 1), (20, 0), (20, 1), (12, 0), (12, 1), (18, 0), (42, 1), (13, 0),
                   (41, 1), (38, 0), (41, 0), (20, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),]
    moveQueue4 = [(42, 1), (31, 0), (41, 1), (31, 0), (42, 1), (13, 0), (13, 1), (11, 0), (41, 1), (20, 0), (0, 1), (20, 0),
                  (41, 1), (31, 0), (42, 1), (31, 0), (31, 1), (12, 0), (0, 1), (13, 0), (42, 1), (13, 0), (13, 1), (12, 0),
                  (12, 1), (14, 0), (41, 1), (19, 0), (19, 1), (12, 0), (0, 1), (13, 0), (0, 1), (20, 0), (41, 1), (32, 0),
                  (13, 1), (11, 0), (31, 1), (12, 0), (42, 1), (31, 0), (0, 1), (20, 0), (20, 1), (11, 0), (11, 1), (6, 0),
                  (32, 0), (30, 0), (11, 1), (6, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),]
    return moveQueue1, moveQueue2, moveQueue3, moveQueue4

def getMoveQueue2bb():
    moveQueue1 = [(6, 1), (12, 0), (17, 1), (23, 0), (11, 1), (12, 0), (12, 1), (21, 0), (20, 1), (23, 0), (23, 1),
                  (21, 0),
                  (18, 1), (12, 0), (12, 1), (3, 0), (4, 1), (1, 0), (1, 1), (3, 0), (5, 1), (24, 0), (17, 1), (24, 0),
                  (24, 1), (21, 0), (18, 1), (12, 0), (4, 1), (1, 0), (1, 1), (3, 0), (7, 1), (1, 0), (5, 1), (12, 0),
                  (19, 1), (24, 0), (17, 1), (24, 0), (24, 1), (21, 0), (20, 1), (23, 0), (18, 1), (12, 4), (17, 1),
                  (23, 0),
                  (23, 1), (21, 0), (16, 1), (1, 0), (5, 1), (0, 0), (0, 1), (3, 0), (3, 1), (14, 0), (8, 1), (1, 0),
                  (1, 1), (3, 0),
                  (3, 1), (14, 0), (13, 1), (12, 0), (6, 1), (12, 0), (21, 1), (14, 0),
                  (0, 0)
                  ]

    moveQueue2 = [(11, 1), (12, 0), (19, 1), (24, 0), (17, 1), (24, 0), (24, 1), (21, 0), (19, 1), (24, 0), (17, 1),
                  (24, 0),
                  (24, 1), (21, 0), (21, 1), (10, 0), (11, 1), (12, 0), (12, 1), (21, 0), (16, 1), (23, 0), (20, 1),
                  (23, 0),
                  (23, 1), (21, 0), (21, 1), (14, 0), (17, 1), (23, 0), (20, 1), (23, 0), (16, 1), (23, 0), (23, 1),
                  (21, 0), (21, 1), (14, 0), (13, 1), (12, 0), (19, 1), (24, 0),
                  (17, 1), (24, 0), (24, 1), (21, 0), (20, 1), (23, 0), (23, 1), (21, 0), (19, 1), (12, 0), (12, 1),
                  (21, 0), (21, 1), (10, 0),
                  (7, 1), (0, 0), (5, 1), (12, 0), (12, 1), (21, 0), (16, 1), (9, 0), (11, 1), (12, 0),(11,1),(9,0),
                  (0, 0)
                  ]

    moveQueue3 = [(17, 1), (24, 0), (20, 1), (12, 0), (4, 1), (1, 0), (7, 1), (23, 0), (20, 1), (12, 0), (20, 1),
                  (23, 0),
                  (23, 1), (21, 0), (18, 1), (12, 0), (12, 1), (21, 0), (18, 1), (0, 0), (7, 1), (0, 0), (0, 1), (3, 0),
                  (4, 1), (12, 0), (12, 1), (3, 0), (3, 1), (14, 0), (6, 1), (12, 0), (12, 1), (21, 0), (20, 1),
                  (12, 0),
                  (12, 1), (3, 0), (7, 1), (1, 0), (4, 1), (12, 0), (12, 1), (3, 0), (4, 1), (1, 0), (1, 1), (3, 0),
                  (3, 1), (14, 0), (13, 1), (12, 0), (12, 1), (3, 0), (4, 1), (12, 0), (12, 1), (21, 0), (19, 1),
                  (24, 0),
                  (17, 1), (24, 0), (24, 1), (21, 0), (20, 1), (12, 0), (7, 1), (0, 0), (0, 1), (3, 0), (3, 1), (14, 0),
                  (8, 1), (15, 0),
                  (0, 0)
                  ]

    moveQueue4 = [(20, 1), (23, 0), (19, 1), (12, 0), (7, 1), (1, 0), (5, 1), (0, 0), (7, 1), (0, 0), (7, 1), (0, 0),
                  (0, 1), (3, 0),
                  (8, 1), (1, 0), (5, 1), (12, 0), (11, 1), (12, 0), (5, 1), (0, 0), (7, 1), (0, 0), (0, 1), (3, 0),
                  (4, 1), (1, 0),
                  (1, 1), (3, 0), (5, 1), (0, 0), (5, 1), (12, 0), (7, 1), (0, 0), (0, 1), (3, 0),
                  (6, 1), (12, 0), (5, 1), (0, 0), (7, 1), (1, 0), (4, 1), (1, 0), (1, 1), (3, 0), (17, 1), (23, 0),
                  (18, 1), (12, 0),
                  (16, 1), (23, 0), (23, 1), (21, 0), (21, 1), (14, 0), (12, 1), (3, 0), (5, 1), (12, 0),
                  (0, 0)
                  ]
    return moveQueue1, moveQueue2, moveQueue3, moveQueue4

def getMoveQueue2():
    moveQueue1 = [(6, 1), (12, 0), (19, 1), (24, 0), (19, 1), (12, 0), (7, 1), (0, 0), (5, 1), (12, 0), (7, 1), (0, 0),
                  (0, 1), (3, 0), (8, 1), (24, 0), (24, 1), (21, 0), (18, 1), (0, 0), (0, 1), (3, 0), (3, 1), (14, 0),
                  (19, 1), (12, 0), (12, 1), (21, 0), (20, 1), (12, 0), (4, 1), (1, 0), (5, 1), (12, 0), (12, 1), (3, 0),
                  (4, 1), (12, 0), (12, 1), (21, 0), (21, 1), (14, 0), (8, 1), (1, 0), (1, 1), (3, 0), (5, 1), (0, 0),
                  (11, 1), (12, 0), (17, 1), (24, 0), (24, 1), (21, 0), (21,1),(10,0),(7, 1), (0, 0), (5, 1), (12, 0), (17,1 ), (24, 0),
                  (24, 1), (21, 0), (21, 1), (10, 0), (7, 1), (9, 0), (11, 1), (9, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue2 = [(13, 1), (12, 0), (16, 1), (23, 0), (20, 1), (12, 0), (12, 1), (21, 0), (20, 1), (23, 0), (23, 1), (21, 0),
                  (17, 1), (24, 0), (17, 1), (1, 0), (1, 1), (3, 0), (4, 1), (1, 0), (6,1), (24, 0), (17, 1), (24, 0),
                  (24, 1), (21, 0), (21, 1), (10, 0), (7, 1), (0, 0), (0, 1), (3, 0), (3, 1), (14, 0), (17, 1), (24, 0),
                  (24, 1), (21, 0), (19, 1), (24, 0), (19, 1), (12, 0), (4, 1), (1, 0), (5,1 ), (0, 0), (0, 1), (3, 0),
                  (3, 1), (14, 0), (19, 1), (24, 0), (13, 1), (12, 0), (12, 1), (21, 0), (20, 1), (23, 0), (19, 1), (24, 0),
                  (19, 1), (12, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue3 = [(17, 1), (24, 0), (13, 1), (12, 0), (18, 1), (24, 0), (24, 1), (21, 0), (16, 1), (23, 0), (18, 1), (0, 0),
                  (16, 1), (23, 0), (19, 1), (12, 0), (12, 1), (3, 0), (4, 1), (12, 0), (20, 1), (23, 0), (23, 1), (21, 0),
                  (16, 1), (23, 0), (19, 1), (24, 0), (20, 1), (23, 0), (16, 1), (23, 0), (23, 1), (21, 0), (20, 1), (12, 0),
                  (12, 1), (3, 0), (6, 1), (12, 0), (20, 1), (23, 0), (23, 1), (21, 0), (18,1), (12, 0), (8, 1), (1, 0),
                  (4, 1),  (1, 0), (1, 1), (3, 0), (17, 1), (23, 0), (20, 1), (23, 0),
                  (23, 1), (21, 0), (18, 1), (12, 0), (12, 1), (3, 0), (4, 1), (1, 0), (8, 0), (1, 0), (1, 1), (3, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue4 = [(20, 1), (23, 0), (19, 1), (12, 0), (5, 1), (0, 0), (4, 1), (1, 0), (8, 1), (1, 0), (4, 1), (12, 0),
                  (12, 1), (3, 0), (4, 1), (12, 0), (12, 1), (21, 0), (20, 1), (23, 0), (23, 1), (21, 0), (21, 1), (10, 0),
                  (7, 1), (1, 0), (1, 1), (3, 0), (7,1), (0, 0), (4, 1), (1, 0), (5, 1), (12, 0), (8, 1), (1, 0),
                  (1, 1), (3, 0), (5, 1), (0,0),(7, 1), (0, 0),(0,1),(3,0), (3, 1), (14, 0), (17, 1), (23, 0), (20,1), (12, 0), (12, 1),
                  (21, 0), (20, 1), (12, 0), (19,1),(12,0),(12, 1), (3, 0), (8, 1), (1, 0), (1, 1), (3, 0), (5, 1), (0, 0), (0, 1),
                  (3, 0), (3, 1), (14, 0), (13, 1), (12, 0), (12, 1), (21, 0), (23, 0), (21, 0), (20, 1), (12, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    return moveQueue1, moveQueue2, moveQueue3, moveQueue4

def getMoveQueue3():
    moveQueue1 = [(6,1), (4,0), (0, 1), (4, 0), (6, 1), (5, 0), (0, 1), (5, 0), (6, 1), (4, 0), (0, 1), (4, 0),
                  (4, 1), (24, 0),
                  (42, 1), (45, 0), (36, 1), (45, 0),(45, 1), (24, 0),
                  (6, 1), (4, 0), (0, 1), (4, 0), (4, 1), (24, 0),
                  (42, 1), (45, 0), (36, 1), (45, 0), (45, 1), (24, 0),
                  (6, 1), (4, 0), (0, 1), (4, 0), (4, 1), (24, 0),
                  (42, 1), (45, 0), (36, 1), (45, 0), (45, 1), (24, 0),
                  (6, 1), (4, 0), (0, 1), (4, 0), (4, 1), (24, 0),
                  (42, 1), (45, 0), (36, 1), (45, 0), (45, 1), (24, 0),
                  (6, 1), (4, 0), (0, 1), (4, 0), (4, 1), (24, 0),
                  (42, 1), (45, 0), (36, 1), (45, 0), (42, 1), (45, 0),(45, 1), (24, 0),
                  (6, 1), (4, 0), (0, 1), (4, 0), (4, 1), (24, 0),

                  (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  (6, 1), (4, 0), (4, 1), (24, 0),
                  (42, 1), (41, 0), (41, 1), (24, 0),
                  (37,1),(32,0),(32,1),(24,0),

                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (23, 1), (24, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue2 = [(36, 1), (41, 0), (42, 1), (41, 0), (36, 1), (45, 0), (42, 1), (45, 0), (42, 1), (41, 0), (36, 1), (41, 0),
                  (41, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (33,0),(28,1),(32, 0),(32,1),(24,0),
                  (16, 1), (22, 0), (28, 1), (22, 0), (22, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (32, 0), (32, 1), (24, 0),
                  (16, 1), (22, 0), (28, 1), (22, 0), (22, 1), (24, 0),
                  (37, 1), (33, 0), (28, 1), (33, 0), (33, 1), (24, 0),
                  (16, 1), (22, 0), (28, 1), (22, 0), (22, 1), (24, 0),
                  (37, 1), (33, 0), (28, 1), (33, 0), (33, 1), (24, 0),
                  (16, 1), (22, 0), (28, 1), (22, 0), (22, 1), (24, 0),
                  (37, 1), (33, 0), (28, 1), (33, 0), (33, 1), (24, 0),
                  (16, 1), (22, 0), (28, 1), (22, 0), (22, 1), (24, 0),
                  (37, 1), (33, 0), (28, 1), (33, 0), (33, 1), (24, 0),
                  (16, 1), (22, 0), (22, 1), (24, 0),
                  (39, 1), (33, 0), (33, 1), (24, 0),
                  (28,1),(23,0),(23,1),(24,0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue3 = [(16, 1), (22, 0), (28, 1), (32, 0), (37, 1), (32, 0), (28, 1), (23, 0), (16, 1), (23, 0), (28, 1), (22, 0),
                  (22, 1), (24, 0),
                  (6, 1), (5, 0), (0, 1), (5, 0),(5,1),(24,0),
                  (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  (6, 1), (5, 0), (0, 1), (5, 0),(0,1),(5,0), (5, 1), (24, 0),
                  (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  (6, 1), (5, 0), (0, 1), (5, 0), (5, 1), (24, 0),
                  (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  (6, 1), (5, 0), (0, 1), (5, 0), (5, 1), (24, 0),
                  (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  (6, 1), (5, 0), (0, 1), (5, 0), (5, 1), (24, 0),

                  (36, 1), (45, 0), (45, 1), (24, 0),
                  (6,1), (5,0),(5,1),(24,0),
                  (42, 1), (45, 0), (45, 1), (24, 0),
                  (6,1), (5,0),(5,1),(24,0),
                  (37,1),(38,0),(39,1),(32,0),(28,1),(22,0),(16,1),(11,0),(16,1),(22,0),(28,1),(33,0),

                  # (36, 1), (41, 0), (42, 1), (41, 0), (41, 1), (24, 0),
                  # (6, 1), (5, 0), (0, 1), (5, 0), (5, 1), (24, 0),
                  # (42, 1), (41, 0), (41, 1), (24, 0),
                  # (5, 1), (24, 0),
                  # (37,1),(38,0),(39,1),(32,0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue4 = [(28, 1), (23, 0), (16, 1), (23, 0), (28, 1), (22, 0), (16, 1), (22, 0), (28, 1), (32, 0), (37, 1), (32, 0),
                  (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0),(23,1),(24,0),
                  (37, 1), (32, 0), (28, 1), (32, 0),(37,1),(33,0), (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0), (23, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (32, 0), (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0), (23, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (32, 0), (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0), (23, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (32, 0), (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0), (23, 1), (24, 0),
                  (37, 1), (32, 0), (28, 1), (32, 0), (32, 1), (24, 0),
                  (16, 1), (23, 0), (28, 1), (23, 0), (23, 1), (24, 0),
                  (37, 1), (32, 0), (28,1),(32,0),(32, 1), (24, 0),
                  (16, 1), (23, 0), (23, 1), (24, 0),
                  (31,1),(27,0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    return moveQueue1, moveQueue2, moveQueue3, moveQueue4
def getMoveQueue4():
    moveQueue1 = [(2, 1), (17, 0), (2, 1), (17, 0), (2, 1), (17, 0), (17, 1), (0, 0), (5, 1), (17, 0), (2, 1), (17, 0),
                  (17, 1), (0, 0), (0, 1), (16, 0), (5, 1), (17, 0), (2, 1), (17, 0), (17, 1),(0,0), (0, 1), (16, 0),
                   (5, 1), (17, 0), (2, 1), (17, 0), (17, 1), (0, 0), (0, 1), (16, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue2 = [(5, 1), (17, 0), (5, 1), (17, 0), (17, 1), (0, 0), (5, 1), (17, 0), (2, 1), (17, 0), (17, 1), (0, 0),
                  (0, 1), (16, 0), (5, 1), (17, 0), (2, 1), (17, 0), (17, 1), (0, 0), (0, 1), (16, 0), (5, 1),(17, 0),
                  (2, 1), (17, 0), (17, 1), (0, 0), (0, 1), (16, 0), (5, 1), (11, 0), (8, 1), (11, 0), (8, 1), (11, 0),
                  (8, 1), (14, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    moveQueue3 = [(1, 1), (10, 0), (7,1), (10, 0), (1, 1), (10, 0), (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0),
                  (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0), (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0),
                  (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0), (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0),
                  (9, 1), (12, 0), (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0), (4, 1),(13, 0),(7, 1), (10, 0),
                  (10, 1), (0, 0), (6, 1), (15, 0),(9, 1), (12, 0), (9, 1), (15, 0), (15, 1),(0, 0),(1, 1), (10, 0),
                  (7, 1), (13,0),(7,1),(10, 0), (10, 1), (0, 0), (9, 0), (15, 0), (0, 0), (0, 0),  (0, 0), (0, 0)
                  ]
    moveQueue4 = [(6, 1), (15, 0), (9, 1), (15, 0), (6, 1), (15, 0), (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0),
                  (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0), (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0),
                  (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0), (9, 1), (15, 0), (15, 1), (0, 0), (1, 1), (10, 0),
                  (7, 1), (13, 0),(7, 1),(10, 0), (10, 1), (0, 0), (6, 1), (15, 0), (3, 1), (12, 0),(9, 1), (15, 0),
                  (15, 1), (0, 0), (1, 1), (10, 0), (7, 1), (10, 0), (10, 1), (0, 0), (6, 1), (15, 0), (9, 1), (15, 0),
                  (9, 1), (15, 0), (15, 1), (0, 0), (7, 1), (10, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                  (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
                  ]
    return moveQueue1, moveQueue2, moveQueue3, moveQueue4

def calculate_motionbb(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed/3
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed/2
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.00, angle_speed*1.0
# compute expected line_speed and angle_speed
def calculate_motion1(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > 0.2+speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed/2
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed*2/3
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.07:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.07:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.07:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.07:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.00, angle_speed*1.0

def calculate_motion2(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed/2
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed*2/3
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.0, angle_speed*1.0

def calculate_motion3(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed*2/3
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed*4/5
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.0, angle_speed*1.0

def calculate_motion4(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    target_point = [tmp for tmp in target_point]
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    alpha = 0.1
    if robot.y > 27.25 and math.sin(target_direction) < 0:
        target_point[0] = target_point[0] - distance * math.tan(alpha)
        distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
        speed = math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
        # direction
        direction_x = (target_point[0] - robot.x) / distance
        direction_y = (target_point[1] - robot.y) / distance
        # the angle needed
        target_direction = math.atan2(direction_y, direction_x)
        delta_theta = target_direction - robot.direction
        # rotate direction
        if delta_theta > math.pi:
            delta_theta -= 2 * math.pi
        elif delta_theta < -math.pi:
            delta_theta += 2 * math.pi
    if robot.y < 27.25 and math.sin(target_direction) > 0:
        target_point[0] = target_point[0] + distance * math.tan(alpha)
        distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
        speed = math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
        # direction
        direction_x = (target_point[0] - robot.x) / distance
        direction_y = (target_point[1] - robot.y) / distance
        # the angle needed
        target_direction = math.atan2(direction_y, direction_x)
        delta_theta = target_direction - robot.direction
        # rotate direction
        if delta_theta > math.pi:
            delta_theta -= 2 * math.pi
        elif delta_theta < -math.pi:
            delta_theta += 2 * math.pi


    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed*2/3
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed*4/5
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.08:
            line_speed = speed - 1.05*dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.0, angle_speed*1.0

def calculate_motion_easy(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53

    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    if delta_theta>math.pi/3 or delta_theta<(-math.pi/3):
        angle_speed=math.pi
    else:
        angle_speed=math.pi/3

    angle_speed = delta_theta / dt

    # compute line speed
    #
    # if distance >= 0.4:
    #     speed_difference = max_speed - speed
    # else:
    #     speed_difference = -speed
    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed/3
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed/2
    # for 图2
    # if delta_theta > math.pi * 2 / 3 or delta_theta < -math.pi * 2 / 3:
    #     line_speed = line_speed * 2 / 3
    # elif delta_theta > math.pi * 1 / 3 or delta_theta < -math.pi * 1 / 3:
    #     line_speed = line_speed * 3 / 4
    #for 图一
    # if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
    #     line_speed=line_speed/2
    # elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
    #     line_speed=line_speed/3

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)

    # #判断会不会撞墙2
    # if robot.x<2 or 50-robot.x<2 or robot.y<2 or 50-robot.y<2:
    #     line_speed=4
    # elif robot.x<1 or 50-robot.x<1 or robot.y<1 or 50-robot.y<1:
    #     line_speed=1
    # elif robot.x < 0.5 or 50 - robot.x < 0.5 or robot.y < 0.5 or 50 - robot.y < 0.5:
    #     line_speed = 0.5


    if distance<=0.4:
       line_speed=0

    return line_speed*1.0, angle_speed*1.0


def calculate_motionForPic3(robot, target_point, max_speed, max_backward_speed, max_rotation_speed):

    target_point=[tmp for tmp in target_point]
    ROBOT_DENSITY = 20
    if robot.CarryType==0:
        ROBOT_RADIUS=0.45
    else:
        ROBOT_RADIUS=0.53


    distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
    speed=math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
    # direction
    direction_x = (target_point[0] - robot.x) / distance
    direction_y = (target_point[1] - robot.y) / distance
    # the angle needed
    target_direction = math.atan2(direction_y, direction_x)
    delta_theta = target_direction - robot.direction
    # rotate direction
    if delta_theta > math.pi:
        delta_theta -= 2 * math.pi
    elif delta_theta < -math.pi:
        delta_theta += 2 * math.pi

    alpha=0.15
    if robot.y > 34 and math.sin(target_direction) < 0:
        target_point[0]=target_point[0]-distance*math.tan(alpha)
        distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
        speed = math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
        # direction
        direction_x = (target_point[0] - robot.x) / distance
        direction_y = (target_point[1] - robot.y) / distance
        # the angle needed
        target_direction = math.atan2(direction_y, direction_x)
        delta_theta = target_direction - robot.direction
        # rotate direction
        if delta_theta > math.pi:
            delta_theta -= 2 * math.pi
        elif delta_theta < -math.pi:
            delta_theta += 2 * math.pi
    if robot.y<34 and math.sin(target_direction) > 0:
        target_point[0] = target_point[0] + distance * math.tan(alpha)
        distance = math.sqrt((target_point[0] - robot.x) ** 2 + (target_point[1] - robot.y) ** 2)
        speed = math.sqrt((robot.line_speed_x) ** 2 + (robot.line_speed_y) ** 2)
        # direction
        direction_x = (target_point[0] - robot.x) / distance
        direction_y = (target_point[1] - robot.y) / distance
        # the angle needed
        target_direction = math.atan2(direction_y, direction_x)
        delta_theta = target_direction - robot.direction
        # rotate direction
        if delta_theta > math.pi:
            delta_theta -= 2 * math.pi
        elif delta_theta < -math.pi:
            delta_theta += 2 * math.pi


    # compute angle speed
    angle_speed = delta_theta / dt
    angle_speed = max(-max_rotation_speed, min(max_rotation_speed, angle_speed))


    if distance > speed**2/(2*MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY)):
        speed_difference = max_speed - speed
    else:
        speed_difference = -speed
    acceleration = speed_difference / dt
    acceleration = max(-MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), min(MAX_TRACTION_FORCE / (math.pi*ROBOT_RADIUS*ROBOT_RADIUS*ROBOT_DENSITY), acceleration))
    line_speed = speed + acceleration * dt
    line_speed = max(max_backward_speed, min(max_speed, line_speed))


    # 急转弯减速
    if delta_theta > math.pi*2/3 or delta_theta < -math.pi*2/3:
        line_speed=line_speed/3
    elif delta_theta > math.pi*1/3 or delta_theta < -math.pi*1/3:
        line_speed=line_speed/2

    # 判断是不是会撞墙1
    new_direction = angle_speed * dt + math.atan2(robot.line_speed_y, robot.line_speed_x)
    if new_direction > math.pi:
        new_direction -= 2 * math.pi
    elif new_direction < -math.pi:
        new_direction += 2 * math.pi
    Shift_x = (line_speed * math.cos(new_direction)) * (line_speed * math.cos(new_direction)) / (
                2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    Shift_y = (line_speed * math.sin(new_direction)) * (line_speed * math.cos(new_direction)) / (
            2 * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY))
    if math.cos(new_direction) > 0:
        if 50.0 - robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.x - Shift_x - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    if math.sin(new_direction) > 0:
        if 50.0 - robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)
    else:
        if robot.y - Shift_y - ROBOT_RADIUS < 0.05:
            line_speed = speed - dt * MAX_TRACTION_FORCE / (
                        math.pi * ROBOT_RADIUS * ROBOT_RADIUS * ROBOT_DENSITY)


    if distance<=0.4:
       line_speed=0

    return line_speed*1.01, angle_speed*1.0

if __name__ == '__main__':
    Robot=[]
    Server=[[] for i in range(9)]
    server_index=[]

    #Init Time=
    #初始化的内容读取
    map=read_util_ok_init()


    if map==map1:
        moveQueue1, moveQueue2, moveQueue3, moveQueue4 = getMoveQueue1()
    elif map==map2:
        moveQueue1, moveQueue2, moveQueue3, moveQueue4 = getMoveQueue2bb()
    elif map==map3:
        moveQueue1, moveQueue2, moveQueue3, moveQueue4 = getMoveQueue3()
    elif map==map4:
        moveQueue1, moveQueue2, moveQueue3, moveQueue4 = getMoveQueue4()


    server_count=0
    for i in range(100):
        for j in range(100):
            if map[i][j]==".":
                continue
            elif map[i][j] == "A":
                new_Robot = robot(float(j / 2 + 0.25), float(50 - i / 2 - 0.25))
                Robot.append(new_Robot)
            else:
                if map[i][j] == "1":
                    new_Server1 = server1(float((j ) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server1)
                elif map[i][j] == "2":
                    new_Server2 = server2(float((j ) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server2)
                elif map[i][j] == "3":
                    new_Server3 = server3(float((j ) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server3)
                elif map[i][j] == "4":
                    new_Server4 = server4(float((j ) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server4)
                elif map[i][j] == "5":
                    new_Server5 = server5(float((j ) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server5)
                elif map[i][j] == "6":
                    new_Server6 = server6(float(j / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server6)
                elif map[i][j] == "7":
                    new_Server7 = server7(float((j) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server7)
                elif map[i][j] == "8":
                    new_Server8 = server8(float((j) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server8)
                elif map[i][j] == "9":
                    new_Server9 = server9(float((j) / 2 + 0.25), float(50 - i / 2 - 0.25), server_count)
                    Server[int(map[i][j]) - 1].append(new_Server9)
                server_index_tmp=(int(map[i][j])-1,len(Server[int(map[i][j])-1])-1)
                server_index.append(server_index_tmp)
                server_count+=1
    finish()

    Robot[0].moveQueue=moveQueue1
    Robot[1].moveQueue=moveQueue2
    Robot[2].moveQueue=moveQueue3
    Robot[3].moveQueue=moveQueue4

    if map==map1:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.split(' ')
            frame_id = int(parts[0])
            K,server_info,robot_info=read_util_ok()
            for i in range(K):
                Server[server_index[i][0]][server_index[i][1]].RemainTimeProduction=server_info[i][3]
                Server[server_index[i][0]][server_index[i][1]].MaterialStatus= server_info[i][4]
                Server[server_index[i][0]][server_index[i][1]].ProductionStatus = server_info[i][5]

            sys.stdout.write('%d\n' % frame_id)

            # #读机器人每个帧的数据
            for i in range(4):
                Robot[i].InServerID=robot_info[i][0]
                Robot[i].CarryType=robot_info[i][1]
                Robot[i].TimeValue = robot_info[i][2]
                Robot[i].CollisionValue = robot_info[i][3]
                Robot[i].angle_speed = robot_info[i][4]
                Robot[i].line_speed_x = robot_info[i][5]
                Robot[i].line_speed_y = robot_info[i][6]
                Robot[i].direction = robot_info[i][7]
                Robot[i].x = robot_info[i][8]
                Robot[i].y = robot_info[i][9]

            #
            for i in range(4):

                server_id=Robot[i].moveQueue[0][0]
                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                if Robot[i].InServerID==server_id:
                    if Robot[i].moveQueue[0][1]==1:
                        if Robot[i].CarryType==0 and target_server.ProductionStatus==1:
                            sys.stdout.write('buy %d\n' % (i))
                            Robot[i].moveQueue=Robot[i].moveQueue[1:]
                            server_id = Robot[i].moveQueue[0][0]
                            target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                    else:
                        if not chargeIfStoreXInServer(Robot[i].CarryType, target_server):
                            if Robot[i].CarryType in target_server.canBuy:
                                sys.stdout.write('sell %d\n' % (i))
                                Robot[i].moveQueue = Robot[i].moveQueue[1:]
                                server_id = Robot[i].moveQueue[0][0]
                                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]


                target_point = (target_server.x, target_server.y)

#这部分代码用来针对性的调整机器人的移动，针对地图的避障。
                if i==1 and frame_id<280 and Robot[i].moveQueue[0][0]==0:
                    target_point=(27.75,49.25)
                elif i==1 and frame_id>720 and frame_id<875 and Robot[i].moveQueue[0][0]==0:
                    target_point=(20.5,49.25)
                elif i==1 and frame_id>1205 and frame_id<1430 and Robot[i].moveQueue[0][0]==42:
                    target_point=(49.25,3.00)
                if i==0 and frame_id>1810 and frame_id<2030 and Robot[i].moveQueue[0][0]==41:
                    target_point=(0.75,3.00)
                if i==2 and frame_id>2400 and frame_id<2680 and Robot[i].moveQueue[0][0]==42:
                    target_point=(49.25,3.00)
                if i==3 and frame_id>2525 and frame_id<2820 and Robot[i].moveQueue[0][0]==20:
                    target_point=(20.25,18.25)
                if i==2 and frame_id>3030 and frame_id<3195 and Robot[i].moveQueue[0][0]==1:
                    target_point=(27.75,49.25)
                if i==1 and frame_id>5220 and frame_id<5400 and Robot[i].moveQueue[0][0]==41:
                    target_point=(3,0.75)
                if i==0 and frame_id>5915 and frame_id<6100 and Robot[i].moveQueue[0][0]==41:
                    target_point=(3,0.75)
                if i==0 and frame_id>6450 and frame_id<6540 and Robot[i].moveQueue[0][0]==42:
                    target_point=(21.25,12.75)
                if i==1 and frame_id>7150 and frame_id<7220 and Robot[i].moveQueue[0][0]==41:
                    target_point=(21,14.75)
                if i==1 and frame_id>6700 and frame_id<6850 and Robot[i].moveQueue[0][0]==42:
                    target_point=(49.25,3.00)
                if i==2 and frame_id>7900 and frame_id<8153 and Robot[i].moveQueue[0][0]==41:
                    target_point=(3,0.75)
                # if i==0 and frame_id>8700 and frame_id<8850 and Robot[i].moveQueue[0][0]==38:
                #     target_point=(25.25,13.25)

                line_speed, angle_speed = calculate_motion1(Robot[i], target_point, MAX_SPEED, MAX_BACKWARD_SPEED,MAX_ROTATION_SPEED)

                sys.stdout.write('forward %d %f\n' % (i, line_speed))
                sys.stdout.write('rotate %d %f\n' % (i, angle_speed))

            finish()
    #bb
    elif map==map2:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.split(' ')
            frame_id = int(parts[0])
            K,server_info,robot_info=read_util_ok()
            for i in range(K):
                Server[server_index[i][0]][server_index[i][1]].RemainTimeProduction=server_info[i][3]
                Server[server_index[i][0]][server_index[i][1]].MaterialStatus= server_info[i][4]
                Server[server_index[i][0]][server_index[i][1]].ProductionStatus = server_info[i][5]

            sys.stdout.write('%d\n' % frame_id)

            #读机器人每个帧的数据
            for i in range(4):
                Robot[i].InServerID=robot_info[i][0]
                Robot[i].CarryType=robot_info[i][1]
                Robot[i].TimeValue = robot_info[i][2]
                Robot[i].CollisionValue = robot_info[i][3]
                Robot[i].angle_speed = robot_info[i][4]
                Robot[i].line_speed_x = robot_info[i][5]
                Robot[i].line_speed_y = robot_info[i][6]
                Robot[i].direction = robot_info[i][7]
                Robot[i].x = robot_info[i][8]
                Robot[i].y = robot_info[i][9]


            for i in range(4):

                server_id=Robot[i].moveQueue[0][0]
                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                if Robot[i].InServerID==server_id:
                    if Robot[i].moveQueue[0][1]==1:
                        if Robot[i].CarryType==0 and target_server.ProductionStatus==1:
                            sys.stdout.write('buy %d\n' % (i))
                            Robot[i].moveQueue=Robot[i].moveQueue[1:]
                            server_id = Robot[i].moveQueue[0][0]
                            target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                    else:
                        if not chargeIfStoreXInServer(Robot[i].CarryType, target_server):
                            if Robot[i].CarryType in target_server.canBuy:
                                sys.stdout.write('sell %d\n' % (i))
                                Robot[i].moveQueue = Robot[i].moveQueue[1:]
                                server_id = Robot[i].moveQueue[0][0]
                                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]


                target_point = (target_server.x, target_server.y)

                # if i==2 and frame_id>320 and frame_id<400 and Robot[i].moveQueue[0][0]==:
                #     target_point=(38,12.75)

                line_speed, angle_speed = calculate_motionbb(Robot[i], target_point, MAX_SPEED, MAX_BACKWARD_SPEED,MAX_ROTATION_SPEED)

                sys.stdout.write('forward %d %f\n' % (i, line_speed))
                sys.stdout.write('rotate %d %f\n' % (i, angle_speed))

            finish()
    #xxf
    # elif map==map2:
    #     while True:
    #         line = sys.stdin.readline()
    #         if not line:
    #             break
    #         parts = line.split(' ')
    #         frame_id = int(parts[0])
    #         K,server_info,robot_info=read_util_ok()
    #         for i in range(K):
    #             Server[server_index[i][0]][server_index[i][1]].RemainTimeProduction=server_info[i][3]
    #             Server[server_index[i][0]][server_index[i][1]].MaterialStatus= server_info[i][4]
    #             Server[server_index[i][0]][server_index[i][1]].ProductionStatus = server_info[i][5]
    #
    #         sys.stdout.write('%d\n' % frame_id)
    #
    #         #读机器人每个帧的数据
    #         for i in range(4):
    #             Robot[i].InServerID=robot_info[i][0]
    #             Robot[i].CarryType=robot_info[i][1]
    #             Robot[i].TimeValue = robot_info[i][2]
    #             Robot[i].CollisionValue = robot_info[i][3]
    #             Robot[i].angle_speed = robot_info[i][4]
    #             Robot[i].line_speed_x = robot_info[i][5]
    #             Robot[i].line_speed_y = robot_info[i][6]
    #             Robot[i].direction = robot_info[i][7]
    #             Robot[i].x = robot_info[i][8]
    #             Robot[i].y = robot_info[i][9]
    #
    #
    #         for i in range(4):
    #
    #             server_id=Robot[i].moveQueue[0][0]
    #             target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
    #             if Robot[i].InServerID==server_id:
    #                 if Robot[i].moveQueue[0][1]==1:
    #                     if Robot[i].CarryType==0 and target_server.ProductionStatus==1:
    #                         sys.stdout.write('buy %d\n' % (i))
    #                         Robot[i].moveQueue=Robot[i].moveQueue[1:]
    #                         server_id = Robot[i].moveQueue[0][0]
    #                         target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
    #                 else:
    #                     if not chargeIfStoreXInServer(Robot[i].CarryType, target_server):
    #                         if Robot[i].CarryType in target_server.canBuy:
    #                             sys.stdout.write('sell %d\n' % (i))
    #                             Robot[i].moveQueue = Robot[i].moveQueue[1:]
    #                             server_id = Robot[i].moveQueue[0][0]
    #                             target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
    #
    #
    #             target_point = (target_server.x, target_server.y)
    #
    #             # if i==2 and frame_id>320 and frame_id<400 and Robot[i].moveQueue[0][0]==:
    #             #     target_point=(38,12.75)
    #
    #             line_speed, angle_speed = calculate_motion2(Robot[i], target_point, MAX_SPEED, MAX_BACKWARD_SPEED,MAX_ROTATION_SPEED)
    #
    #             sys.stdout.write('forward %d %f\n' % (i, line_speed))
    #             sys.stdout.write('rotate %d %f\n' % (i, angle_speed))
    #
    #         finish()

    elif map==map3:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.split(' ')
            frame_id = int(parts[0])
            K,server_info,robot_info=read_util_ok()
            for i in range(K):
                Server[server_index[i][0]][server_index[i][1]].RemainTimeProduction=server_info[i][3]
                Server[server_index[i][0]][server_index[i][1]].MaterialStatus= server_info[i][4]
                Server[server_index[i][0]][server_index[i][1]].ProductionStatus = server_info[i][5]

            sys.stdout.write('%d\n' % frame_id)

            #读机器人每个帧的数据
            for i in range(4):
                Robot[i].InServerID=robot_info[i][0]
                Robot[i].CarryType=robot_info[i][1]
                Robot[i].TimeValue = robot_info[i][2]
                Robot[i].CollisionValue = robot_info[i][3]
                Robot[i].angle_speed = robot_info[i][4]
                Robot[i].line_speed_x = robot_info[i][5]
                Robot[i].line_speed_y = robot_info[i][6]
                Robot[i].direction = robot_info[i][7]
                Robot[i].x = robot_info[i][8]
                Robot[i].y = robot_info[i][9]


            for i in range(4):

                server_id=Robot[i].moveQueue[0][0]
                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                if Robot[i].InServerID==server_id:
                    if Robot[i].moveQueue[0][1]==1:
                        if Robot[i].CarryType==0 and target_server.ProductionStatus==1:
                            sys.stdout.write('buy %d\n' % (i))
                            Robot[i].moveQueue=Robot[i].moveQueue[1:]
                            server_id = Robot[i].moveQueue[0][0]
                            target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                    else:
                        if not chargeIfStoreXInServer(Robot[i].CarryType, target_server):
                            if Robot[i].CarryType in target_server.canBuy:
                                sys.stdout.write('sell %d\n' % (i))
                                Robot[i].moveQueue = Robot[i].moveQueue[1:]
                                server_id = Robot[i].moveQueue[0][0]
                                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]


                target_point = (target_server.x, target_server.y)

                line_speed, angle_speed = calculate_motion3(Robot[i], target_point, MAX_SPEED, MAX_BACKWARD_SPEED,MAX_ROTATION_SPEED)

                sys.stdout.write('forward %d %f\n' % (i, line_speed))
                sys.stdout.write('rotate %d %f\n' % (i, angle_speed))

            finish()


    elif map==map4:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.split(' ')
            frame_id = int(parts[0])
            K,server_info,robot_info=read_util_ok()
            for i in range(K):
                Server[server_index[i][0]][server_index[i][1]].RemainTimeProduction=server_info[i][3]
                Server[server_index[i][0]][server_index[i][1]].MaterialStatus= server_info[i][4]
                Server[server_index[i][0]][server_index[i][1]].ProductionStatus = server_info[i][5]

            sys.stdout.write('%d\n' % frame_id)

            #读机器人每个帧的数据
            for i in range(4):
                Robot[i].InServerID=robot_info[i][0]
                Robot[i].CarryType=robot_info[i][1]
                Robot[i].TimeValue = robot_info[i][2]
                Robot[i].CollisionValue = robot_info[i][3]
                Robot[i].angle_speed = robot_info[i][4]
                Robot[i].line_speed_x = robot_info[i][5]
                Robot[i].line_speed_y = robot_info[i][6]
                Robot[i].direction = robot_info[i][7]
                Robot[i].x = robot_info[i][8]
                Robot[i].y = robot_info[i][9]


            for i in range(4):

                server_id=Robot[i].moveQueue[0][0]
                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                if Robot[i].InServerID==server_id:
                    if Robot[i].moveQueue[0][1]==1:
                        if Robot[i].CarryType==0 and target_server.ProductionStatus==1:
                            sys.stdout.write('buy %d\n' % (i))
                            Robot[i].moveQueue=Robot[i].moveQueue[1:]
                            server_id = Robot[i].moveQueue[0][0]
                            target_server = Server[server_index[server_id][0]][server_index[server_id][1]]
                    else:
                        if not chargeIfStoreXInServer(Robot[i].CarryType, target_server):
                            if Robot[i].CarryType in target_server.canBuy:
                                sys.stdout.write('sell %d\n' % (i))
                                Robot[i].moveQueue = Robot[i].moveQueue[1:]
                                server_id = Robot[i].moveQueue[0][0]
                                target_server = Server[server_index[server_id][0]][server_index[server_id][1]]


                target_point = (target_server.x, target_server.y)

                line_speed, angle_speed = calculate_motion4(Robot[i], target_point, MAX_SPEED, MAX_BACKWARD_SPEED,MAX_ROTATION_SPEED)

                sys.stdout.write('forward %d %f\n' % (i, line_speed))
                sys.stdout.write('rotate %d %f\n' % (i, angle_speed))

            finish()
