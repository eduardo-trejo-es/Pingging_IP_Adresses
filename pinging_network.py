from ping3 import ping, verbose_ping
import pandas as pd


class NetworkPinger:
    def __init__(self):
        pass
        
    def Pinger(self, Network,RangeIp,Pathfile):
        joined=""
        PingDict={}
        IpAdresslist=[]
        pingresultList=[]
        network=Network
        rangeIp=RangeIp
        #Network="192.168.1"
        
        for i in range(rangeIp[0],rangeIp[1]):
            joined=network+(".")+str(i)
            IpAdresslist.append(joined)
            pingresultList.append(ping(joined))
            
        PingDict["IpAdresse"]=IpAdresslist
        PingDict["Result"]=pingresultList
        PandasPingDict=pd.DataFrame.from_dict(PingDict)
        self.save_data(PandasPingDict,Pathfile)
        
    def save_data(self,PandasPingDict,Pathfile):
        pathfile=Pathfile
        PandasPingDict.to_csv(pathfile)
    

    