#Cisco ACS4.x User Parser
- creating csv.file from dump.txt which is created by "csutil -d"
 - dump.txt has to be in same directoty.
 ```sh
 net stop csauth
 csutil -d
 net start csauth
 ```
 see: (http://www.cisco.com/c/en/us/td/docs/net_mgmt/cisco_secure_access_control_server_for_windows/4-2/user/guide/ACS4_2UG/A_CSUtil.html#wp417749)

Changed for use in python 3 aned addes Status: Status 1 : enabled.
