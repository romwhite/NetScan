#!/usr/bin/python3
# Title: NetScan
# Description: Port scanning tool
# 9/12/2020

import argparse
from socket import *


def connectionScan(targetHost, targetPort):
    try:
        connSock = socket(AF_INET, SOCK_STREAM)
        connSock.connect((targetHost, targetPort))
        print("[+] %d - TCP open"% targetPort)
        connSock.close()
    except:
        print("[-] %d - TCP closed"% targetPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host"% targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print("\n[+] Scan results for: " + targetName)
    except:
        print("\n[+] Scan results for: " + targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print("Scanning port " + str(targetPort))
        connectionScan(targetHost, int(targetPort))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--host", help = "Host name or host IP address",
                        type = str, required = True)
    parser.add_argument("-p", "--ports", nargs = "+", type = int,
                        help = "List of port numbers separated by spaces",
                        required = True)
    args = parser.parse_args()

    portScan(args.host, args.ports)

if __name__ == '__main__':
    main()

