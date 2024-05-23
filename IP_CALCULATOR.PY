import re
network_adds=[] # List network address variable of first digit
Broadcast_adds=[] # List Broadcast address variable of last digit

def CheckIp(input_ip):# This finction will check Valid and Invalid IP. Return valid IP and CIDR
    CIDR="" # default value
    digit=re.findall("[^0-9 / .]",input_ip) # return alpha and symbol except [0 to 9 . /]
    if digit: #if digit have any value . it will return Invalid IP
        return f"Invalid IP {digit}: {1111}"

    elif len(input_ip.split("."))==4 and int(input_ip.split(".")[0])<256 and int(input_ip.split(".")[1])<256 and int(input_ip.split(".")[2])<256: # code will if  input_ip<=255.255.255.__
        if "/" in input_ip:
            split_ip=input_ip.split("/") # split from "/"('255.255.255.255', '32')
            if split_ip[1] and int(split_ip[1])<33 and int(split_ip[0].split(".")[-1])<256: # will run if input_ip<=555.255.255.255 and CIDR<33
                IP=split_ip[0] # will return IP part
                CIDR=split_ip[1] # will return CIDR
                return IP, CIDR
            else:
                return f"Invalid IP : {2222}" # invalid if input_ip>555.255.255.255 and CIDR>32

        elif int(input_ip.split(".")[3])<256: # will run if input_ip<=555.255.255.255
            return input_ip,CIDR
        else:
            return f"Invalid IP : {4444}" # invalid if input_ip>_._._.255 
    else:
        return f"Invalid IP : {3333}" # invalid if input_ip> 255.255.255._
######################################################################################################################################################################################## 

# It will check the IP type for classless IP or for subnetting 
def class_check(IP): #class_check() function 
    IP=IP.split(".") #Split IP ["255","255","255","255"]
    if 1<=int(IP[0])<=255 and 0<=int(IP[1])<=255 and 0<=int(IP[2])<=255 and 0<=int(IP[3])<=255:

        #For class A
        if 1<=int(IP[0])<=127 :
            if int(IP[0])==127:
                print(f"IP Type : Private (Loopback)")
            elif int(IP[0])==10:
                print(f"IP Type : Private")
            else:
                print(f"IP Type : Public")
        # For class B
        elif 128<=int(IP[0])<=191:
            if int(IP[0])==172 and 16<=int(IP[1])<=31:
                print(f"IP Type : Private")
            else:
                print(f"IP Type : Public")
        #For class C
        elif 192<=int(IP[0])<=223:
            if int(IP[0])==192 and 16<=int(IP[1])==168:
                print(f"IP Type : Private")
            else:
                print(f"IP Type : Public")
        #For class D
        elif 224<=int(IP[0])<=239:
            print(" Class D : Reserved for multicasting")
        #For class E
        elif 240<=int(IP[0])<=245:
            print(" Class E IP addresses are reserved for research and experimental purposes")
        #Limited Broadcast
        elif int(IP[0])==255:
            print(f"255.255.255.255 is the limited broadcast address.")
        else:
            print("Error in code : Class_check")

######################################################################################################################################################################################## 
#--------------For Class Less IP address---------------------
######################################################################################################################################################################################## 

def Class_classLess_IP(input_ip):
    CheckIp(input_ip) #calling CheckIp() function

    if "Invalid IP" in CheckIp(input_ip): # will run if IP is Invalid
        return CheckIp(input_ip)

    else: #will run if IP is valid
        IP,CIDR=CheckIp(input_ip)# assigining IP and CIDR value to "IP and CIDR variable"
        IP_split=IP.split(".") # Split
        class_check(IP) # calling class_check() function to check public and private IP
        if IP and CIDR: # If IP and CIDR both have value then only run
            CIDR=int(CIDR) # convert CIDR into int

            if CIDR==32:
                return f"""
    IP Address : {IP}
    Network Addredd : {IP}
    Usable host Range : NA
    Broadcast address : {IP}
    Total Number of Hosts : 1
    Number of Usable Hosts : 0
    Subnet Mark : 255.255.255.255
    Wildcard Mask : 0.0.0.0
    """
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif 0==CIDR:
                return "Please Enter CIDR beween 1 to 32"

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif 0<CIDR<=8:
                network_bit=CIDR-0 # calculate number of network bit between 24 to 32
                number_of_network=2**network_bit # maximum network range possible
                for i in range(0,256,256//number_of_network):
                    network_adds.append(i) # network address list
                    Broadcast_adds.append(i+256//number_of_network-1) # Broadast addredd list

                Subnet_Mask = f"{network_adds[-1]}" +".0.0.0" #Subnet mark 
                Wildcard_Mask =f"{255-network_adds[-1]}" +".255.255.255" # Wildcard mark
                Total_Hosts =256*256*256*(256//number_of_network)
                Usable_Hosts =256*256*256*(256//number_of_network)-2

                for j in range (len(network_adds)):
                    if network_adds[j]<=int(IP_split[0])<=Broadcast_adds[j]:
                        IP_split[0],IP_split[1],IP_split[2],IP_split[3]=str(network_adds[j]),"0","0","0"
                        network_add=".".join(IP_split) # Network address of the network

                        IP_split[0],IP_split[1],IP_split[2],IP_split[3]=str(network_adds[j]),"0","0","1"
                        first_usable_ip=".".join(IP_split) #First usable ip of the network

                        IP_split[0],IP_split[1],IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"255","255","255"
                        Broadcast_add=".".join(IP_split) # Broadcast address of the network

                        IP_split[0],IP_split[1],IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"255","255","254"
                        last_usable_ip=".".join(IP_split) # Last usable ip of the network
                        break
                    else:
                        pass

                return f"""
    IP Address : {IP}
    Network Addredd : {network_add}
    Usable host Range : {first_usable_ip} TO {last_usable_ip}
    Broadcast address : {Broadcast_add}
    Total Number of Hosts : {Total_Hosts}
    Number of Usable Hosts : {Usable_Hosts}
    Subnet Mark : {Subnet_Mask}
    Wildcard Mask : {Wildcard_Mask}
    """
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif 8<CIDR<=16:
                network_bit=CIDR-8 # calculate number of network bit between 24 to 32
                number_of_network=2**network_bit # maximum network range possible
                for i in range(0,256,256//number_of_network):
                    network_adds.append(i) # network address list
                    Broadcast_adds.append(i+256//number_of_network-1) # Broadast addredd list

                Subnet_Mask = "255." +f"{network_adds[-1]}" +".0.0" #Subnet mark 
                Wildcard_Mask ="0."+f"{255-network_adds[-1]}" +".255.255" # Wildcard mark
                Total_Hosts =256*256*(256//number_of_network)
                Usable_Hosts =256*256*(256//number_of_network)-2

                for j in range (len(network_adds)):
                    if network_adds[j]<=int(IP_split[1])<=Broadcast_adds[j]:
                        IP_split[1],IP_split[2],IP_split[3]=str(network_adds[j]),"0","0"
                        network_add=".".join(IP_split) # Network address of the network

                        IP_split[1],IP_split[2],IP_split[3]=str(network_adds[j]),"0","1"
                        first_usable_ip=".".join(IP_split) #First usable ip of the network

                        IP_split[1],IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"255","255"
                        Broadcast_add=".".join(IP_split) # Broadcast address of the network

                        IP_split[1],IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"255","254"
                        last_usable_ip=".".join(IP_split) # Last usable ip of the network
                        break
                    else:
                        pass

                return f"""
    IP Address : {IP}
    Network Addredd : {network_add}
    Usable host Range : {first_usable_ip} TO {last_usable_ip}
    Broadcast address : {Broadcast_add}
    Total Number of Hosts : {Total_Hosts}
    Number of Usable Hosts : {Usable_Hosts}
    Subnet Mark : {Subnet_Mask}
    Wildcard Mask : {Wildcard_Mask}
    """
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif 16<CIDR<=24:
                network_bit=CIDR-16 # calculate number of network bit between 24 to 32
                number_of_network=2**network_bit # maximum network range possible
                for i in range(0,256,256//number_of_network):
                    network_adds.append(i) # network address list
                    Broadcast_adds.append(i+256//number_of_network-1) # Broadast addredd list

                Subnet_Mask = "255.255." +f"{network_adds[-1]}" +".0" #Subnet mark 
                Wildcard_Mask ="0.0."+f"{255-network_adds[-1]}" +".255" # Wildcard mark
                Total_Hosts =256*(256//number_of_network)
                Usable_Hosts =256*(256//number_of_network)-2

                for j in range (len(network_adds)):
                    if network_adds[j]<=int(IP_split[2])<=Broadcast_adds[j]:
                        IP_split[2],IP_split[3]=str(network_adds[j]),"0"
                        network_add=".".join(IP_split) # Network address of the network

                        IP_split[2],IP_split[3]=str(network_adds[j]),"1"
                        first_usable_ip=".".join(IP_split) #First usable ip of the network

                        IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"255"
                        Broadcast_add=".".join(IP_split) # Broadcast address of the network

                        IP_split[2],IP_split[3]=str(Broadcast_adds[j]),"254"
                        last_usable_ip=".".join(IP_split) # Last usable ip of the network
                        break
                    else:
                        pass

                return f"""
    IP Address : {IP}
    Network Addredd : {network_add}
    Usable host Range : {first_usable_ip} TO {last_usable_ip}
    Broadcast address : {Broadcast_add}
    Total Number of Hosts : {Total_Hosts}
    Number of Usable Hosts : {Usable_Hosts}
    Subnet Mark : {Subnet_Mask}
    Wildcard Mask : {Wildcard_Mask}
    """
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif 24<CIDR<32:
                network_bit=CIDR-24 # calculate number of network bit between 24 to 32
                number_of_network=2**network_bit # maximum network range possible
                for i in range(0,256,256//number_of_network):
                    network_adds.append(i) # network address list
                    Broadcast_adds.append(i+256//number_of_network-1) # Broadast addredd list

                Subnet_Mask = "255.255.255." +f"{network_adds[-1]}" #Subnet mark 
                Wildcard_Mask ="0.0.0."+f"{255-network_adds[-1]}" # Wildcard mark
                Total_Hosts =256//number_of_network
                Usable_Hosts =256//number_of_network-2

                for j in range (len(network_adds)):
                    if network_adds[j]<=int(IP_split[-1])<=Broadcast_adds[j]:
                        IP_split[3]=str(network_adds[j])
                        network_add=".".join(IP_split) # Network address of the network

                        IP_split[3]=str(network_adds[j]+1)
                        first_usable_ip=".".join(IP_split) #First usable ip of the network

                        IP_split[3]=str(Broadcast_adds[j])
                        Broadcast_add=".".join(IP_split) # Broadcast address of the network

                        IP_split[3]=str(Broadcast_adds[j]-1)
                        last_usable_ip=".".join(IP_split) # Last usable ip of the network
                        break
                    else:
                        pass

                return f"""
    IP Address : {IP}
    Network Addredd : {network_add}
    Usable host Range : {first_usable_ip} TO {last_usable_ip}
    Broadcast address : {Broadcast_add}
    Total Number of Hosts : {Total_Hosts}
    Number of Usable Hosts : {Usable_Hosts}
    Subnet Mark : {Subnet_Mask}
    Wildcard Mask : {Wildcard_Mask}
    """

######################################################################################################################################################################################## 
# -------------Will run if IP type is Class------------------
######################################################################################################################################################################################## 

        #Will run if ip type is Class
        elif IP:
            input_ip=IP # Like input_ip="255.255.255.255"
            IP=input_ip.split(".") #split input_ip from "." ["255","255","255","255"]

            #Default IP address
            if input_ip=="0.0.0.0":
                return("""0.0.0.0
1) 0.0.0.0 has a special meaning in networking.

2) Default IP Address: It can be assigned as a placeholder or default value when a device is not configured with a specific IP address. 

3) 0.0.0.0 is not a valid private or public IP address.

4) It can also be used by a server to listen on all of its network interfaces.""")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    # Limited broadcast IP address
            elif input_ip=="255.255.255.255":
                return("""1) 255.255.255.255 is the limited broadcast address. 

2) It's a special IP address used to send data to all devices on a local network segment (also known as subnet)

3) A broadcast address tells network devices to transmit the message to all hosts on the network.

4) Limited broadcasts are restricted to the local network segment by default and typically don't cross routers.
    This address cannot be assigned to any specific device on the network.

5) 255.255.255.255 is not a public or private IP address. """)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    #Class A IP address
            elif 1<=int(IP[0])<=127:
                return(f"""IP address : {input_ip}
Class : A""")
        #Private class A IP address
                if int(IP[0])==10:
                    return(f"\nClass : Private IP\nRange : 10.0.0.0 To 10.255.255.255")
        # Loopback class A private IP address
                elif int(IP[0])==127:
                    return(f"""\nCalss : Private
Loopback addresses are used for internal communication within a single device.
In essence, the device sends data to itself using this address. 
The most commonly used loopback address is 127.0.0.1, but technically,
any address within the 127.0.0.0 to 127.255.255.255 range can be used for loopback purposes.""")
        #Public class A IP address
                else:
                    return(f"\nClass : Public IP\nRange : 1.0.0.0 to 9.255.255.255\nRange : 11.0.0.0 to 126.255.255.255")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    # Class B IP address
            elif 128<=int(IP[0])<=191:
                return(f"""IP address : {input_ip}
Class : B""")
        #Private class B IP address
                if 172==int(IP[0]) and 16<=int(IP[1])<=31:
                    return(f"\nClass : Private IP\nRange : 172.16.0.0 To 172.31.255.255")
        #Public class B IP address
                else:
                    return(f"\nClass : Public IP\nRange : 128.0.0.0 to 172.15.255.255\nRange : 172.32.0.0 to 191.255.255.255")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    # Class C IP address
            elif 192<=int(IP[0])<=223:
                return(f"""IP address : {input_ip}
Class : C""")
        #Private class C IP address
                if 192==int(IP[0]) and 168==int(IP[1]):
                    return(f"\nClass : Private IP\nRange : 192.168.0.0 To 192.168.255.255")
        #Public class c IP address
                else:
                    return(f"\nClass : Public IP\nRange : 192.0.0.0 to 192.167.255.255\nRange : 192.169.0.0 to 223.255.255.255")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    # Class D IP address
            elif 224<=int(IP[0])<=239:
                return(f"""IP Address : {input_ip}
Range : 224.0.0.0 To 239.255.255.255

Class D IP addresses are reserved for multicasting.

Multicasting is a network communication method where a single data stream is sent to a specific group of devices on a network, rather than to a single device.

This is efficient for situations where the same data needs to be delivered to many recipients simultaneously, 

Streaming services: Live video or audio streams can be multicast to a group of viewers interested in the same program, reducing network traffic compared to sending individual streams to each viewer.

Example==>>
Online gaming
Distance learning
Security updates""")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    # Class E IP address
            elif 240<=int(IP[0])<=254:
                return(f"""IP Address : {input_ip}

Class : E

Range : 1.0.0.0 To 127.255.255.255.

Class E IP addresses are reserved for research and experimental purposes.

They are not assigned for general use on the internet.

The specific purpose of research for which they were intended is not entirely clear.

Some potential areas of research could involve testing new routing protocols or developing new addressing schemes.

Many network devices simply ignore or treat Class E addresses as invalid.""")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====
            elif 255==int(IP[0]) and int(IP[1])>=0 and int(IP[2])>=0 and int(IP[3])>=0 :
                return(f"""IP Address : {input_ip}

The IP address range 255.0.0.0 to 255.255.255.254 is a special case that doesn't directly correspond to a typical public or private IP address block.

The range 255.0.0.0 to 255.255.255.254 represents a single broadcast address, not usable for individual device addressing.

It's essential to understand the concept of broadcast addresses and their role in network communication.
""")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====

            elif 0==int(IP[0]) and int(IP[1])>=0 and int(IP[2])>=0 and int(IP[3])>=0 :
                return(f"IP Address : {input_ip} information not available between 0.0.0.1 to 0.255.255.255")

#############################################################################################################################

# input_ip="1.189.102.100/8"
input_ip=input("Enter ip Address Formates are (10.11.12.1 OR 121.11.10.1/26): ")
print(Class_classLess_IP(input_ip)) # Main function to find the subnet and ip details
