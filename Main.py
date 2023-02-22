from pinging_network import NetworkPinger


Networkpinger=NetworkPinger()

network="192.168.1"
rangeIp=[0,10]
path="pingresults\PingResult.csv"


Networkpinger.Pinger(network,rangeIp,path)