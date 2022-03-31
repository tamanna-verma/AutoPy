import os
import time
import getpass
import subprocess as sp 
from termcolor import colored,cprint
from cfonts import render,say



def outputcheck(output):
	if output[0] == 0:
		
		print(output[1])
		cprint("Task successfully completed !!",'green')
	else:
		cprint("Oops !! Some error occurred : {}".format(output[1]),'red')
	cprint("'Press enter' to continue :")
	input()



def linux_menu():
	while True :
		os.system("clear")
		o_p = render("LINUX",colors=['red','yellow'],align='center')
		print(o_p)
		os.system('espeak-ng "Welcome to linux menu"')
		cprint("""
                                    ====================================    ====================================================
                                    | No.  |     Services              |    | No.  |     Services                              |
                                    ====================================    ====================================================
                                    | 1.   | To Open Text Editor       |    | 2.   | To Open FireFox                           |
                                    ------------------------------------    ----------------------------------------------------
                                    | 3.   | To Open vi Text Editor    |    | 4.   | To  See Date and Time                     |
                                    ------------------------------------    ----------------------------------------------------
                                    | 5.   | To See  Calender          |    | 6.   | To  See hard disk info                    |
                                    --------------------------------------  ----------------------------------------------------
                                    | 7.   |Check Software(install or not)| | 8.   | Download and install software From a link |
                                    --------------------------------------  ----------------------------------------------------
                                    | 9.   |To open File explorer      |    | 10.  | To Open Terminal Window                   |
                                    ------------------------------------    ----------------------------------------------------
                                    | 11.  | To Open Audio Player      |    | 12.  | To Open setting                           |
                                    ------------------------------------    ----------------------------------------------------
                                    | 13.  | To Open Camera            |    | 14.  | To  Open calculator                       |
                                    ------------------------------------    ----------------------------------------------------
                                    | 15.  | To Open video player      |    | 16.  | To See All Partition and Mount info       |
                                    ------------------------------------    ----------------------------------------------------
                                    | 17.  |To SEE Memory Info(RAM)    |    | 18.  | To Go inside a Directory(Folder)          |
                                    ------------------------------------    ----------------------------------------------------
                                    | 19.  |To Delete a file           |    | 20.  | To Delete a Directory(Folder)             |
                                    ------------------------------------    ----------------------------------------------------
                                    | 21.  |To Start a Service         |    | 22.  | To Stop a Service                         |
                                    ------------------------------------    ----------------------------------------------------
                                    | 23.  |To Enable a Service        |    | 24.  | To Disable a Service                      |
                                    --------------------------------------  ----------------------------------------------------
                                    | 25.  |See files of present Directory| | 26.  |To See IP and ethernet card attached       |
                                    --------------------------------------  ----------------------------------------------------
                                    | 27.  |To Check Connectivity to ip|    | 28.  | Transfer file to other linux system       |
                                    ------------------------------------    ----------------------------------------------------
                                    | 29.  |Configure 'yum' Repository |    | 30.  | Go back to previous MENU                  |
                                    ------------------------------------    ----------------------------------------------------

""",'yellow')
		cprint("Enter your choice:",'yellow',end="")
		input_ = int(input())
		
		if input_ == 1:
			# OPEN TEXT EDITOR
			cprint("Enter file name to open a file otherwise press Enter:",'yellow',end="")
			file_name = input()
			output = sp.getstatusoutput("gedit  {} ".format(file_name))

		elif input_ == 2:
			# OPEN firefox
			output = sp.getstatusoutput("firefox &")	
		elif input_ == 3:
			# OPEN Vi 
			cprint("Enter file name :",'yellow',end="")
			file_name = input()
			output = sp.getstatusoutput("vi  {}".format(file_name))
		elif input_ == 4:
			# OPEN Date and time
			output = sp.getstatusoutput("date &")
		elif input_ == 5:
			# OPEN calender
			output = sp.getstatusoutput("cal &")
		elif input_ == 6:
			# OPEN harddisk info
			output = sp.getstatusoutput("fdisk -l")
		elif input_ == 7:
			# ask Query about Software
			cprint("Enter Software name :",'yellow',end="")
			sft_name = input()
			output = sp.getstatusoutput("rpm -q  {}".format(sft_name))
		elif input_ == 8:
			# Download Software and insall 
			cprint("Enter a link:",'yellow',end="")
			link = input()
			output = sp.getstatusoutput("yum install  {}".format(link))
		elif input_ == 9:
			#open file explorer
			output = sp.getstatusoutput("nautilus &")
		elif input_ == 10:
			#open Terminal Window
			output = sp.getstatusoutput("gnome-teminal &")
		elif input_ == 11:
			#open Audio player
			output = sp.getstatusoutput("rhythmbox &")
		elif input_ == 12:
			#open setting
			output = sp.getstatusoutput("gnome-control-center &")
		elif input_ == 13:
			#open camera
			output = sp.getstatusoutput("cheese &")
		elif input_ == 14:
			#open calculator
			output = sp.getstatusoutput("gnome-calculator &")
		elif input_ == 15:
	 		#open videoplayer
			output = sp.getstatusoutput("totem  &")
		elif input_ == 16:
			# See All Partition and Mount info
			output = sp.getstatusoutput("lsblk")
			print(output[1])
		elif input_ == 17:
			#see ram info
			output = sp.getstatusoutput("free -m")
		elif input_ == 18:
			# go inside a folder
			cprint("Enter your Path:",'yellow',end='')
			path = input()
			output = sp.getstatusoutput("cd {}".format(path))
		elif input_ == 19:
			#deleting Dirctory
			cprint("Enter your Directory Name:",'yellow',end='')
			dir_name = input()
			output = sp.getstatusoutput("rm -rf {}".format(dir_name))
		elif input_ == 20:
			#deleting File
			cprint("Enter your File Name:",'Yellow',end='')
			dir_name = input()
			output = sp.getstatusoutput("rm  {}".format(dir_name))	
			
		elif input_ == 21 :
			# start a service
			cprint("Enter service name:",'Yellow',end ="")
			service = input()
			output = sp.getstatusoutput("systemctl start {} ".format(service))
		elif input_ == 22 :
			# stop a service
			cprint("Enter service name:",'Yellow',end ="")
			service = input()
			output = sp.getstatusoutput("systemctl stop {} ".format(service))
		elif input_ == 23 :
			# enable a service
			cprint("Enter service name:",'Yellow',end ="")
			service = input()
			output = sp.getstatusoutput("systemctl enable {} ".format(service))
		elif input_ == 24 :
		# disable a service
			cprint("Enter service name:",'Yellow',end ="")
			service = input()
			output = sp.getstatusoutput("systemctl disable {} ".format(service))
				
		elif input_ == 25 :
			#See files of present Directory
			output = sp.getstatusoutput("ls")
			
		elif input_ == 26 :
			#To SEE IP OF Domain 
			output = sp.getstatusoutput("ifconfig")
		elif input_ == 27 :
			#To Check Connectivity to ip
			cprint("Enter Ip to check connectivity:",'yellow',end ="")
			ip = input()
			output = sp.getstatusoutput("ping -c 4 {} ".format(ip))
		elif input_ == 28 :
			#Transfer file to other linux system|
			cprint("Enter ip of system to which you want to Send file:",'yellow',end ="")
			ip = input()
			cprint("Enter username  to which you want to Send file:",'yellow',end ="")
			usr = input()
			cprint("Enter source file path which you want to Send :",'yellow',end ="")
			source = input()
			cprint("Enter destination path to where you want to Send file:",'yellow',end ="")
			destination = input()
			output = sp.getstatusoutput("scp {} {}@{}:{} ".format(source,usr,ip,destination))
		elif input_ == 29:
			# configure YUM
			cprint("your Yum configured",'green')
			
		elif input_ == 30:
			# go back to Previous menu
			break
		else:
			print("Invalid Choice ! Try Again",'red')
			os.system("sleep 1")
			continue
		outputcheck(output)

	
def Static_partition_menu():

	while True :
		os.system("clear")
		o_p = render("STATIC",colors=['red','yellow'],align='center')
		o_s = render("PARTITION",colors=['red','yellow'],align='center')
		print(o_p)
		print(o_s)
		os.system('espeak-ng "Welcome to static partition menu"')
		cprint("""
								===============================================================
								| No. |                    SERVICES                            |
								===============================================================
								| 1.  |  To see all disks available                            |
								----------------------------------------------------------------
								| 2.  |  To see info of all existing partitions                |
								----------------------------------------------------------------
								| 3.  |  To create a static partitions                         |
								----------------------------------------------------------------
								| 4.  |  To delete a Partition                                 |  
								----------------------------------------------------------------
								| 5.  |  To go back to main menu                               | 
								----------------------------------------------------------------
""",'yellow')     
		cprint("Enter your choice : ",'red',end = "")
		input_ = int(input())


		if input_ == 1:
			output = sp.getstatusoutput("fdisk -l")
		elif input_ == 2:
			output =sp.getstatusoutput("lsblk")
			print(output[1])
			output =sp.getstatusoutput("df -h")
		elif input_ == 3:
			disk_name =input ("Enter disk name in which you want to create partition : ")
			mount_point = input("Enter a folder path to which you want to link partition : ")
			
			cprint("Enter 'n'  to create new partition")
			cprint(" Select Partition type as ['p' for primary / 'e' for extended] : ")
			cprint("Enter 'w' to save changes after creating partition.")
			
			os.system("fdisk {}".format(disk_name))
			print(os.system("lsblk"))
			part_name = input("Enter partition name created : ")
			output = sp.getstatusoutput("mkfs.ext4 {}".format(part_name))
			print(output[1],"\n") 
			if(output[0] == 0):
				os.system("mkdir {}".format(mount_point))
				output = sp.getstatusoutput("mount {} {}".format(part_name,mountpt))
			info = sp.getstatusoutput("df -h")
			print(info[1])
				
			
		elif input_ == 4:
			disk_name =input ("Enter disk name in which you want to delete partition : ")
			part_name = input("Enter partition name to be deleted : ")
			output = sp.getstatusoutput("umount {}".format(part_name))
			
			cprint("Enter 'd' to delete partition",'yellow')
			cprint("Enter 'w' to save changes after deleting partition.",'yellow')
			
			if(output[0] == 0):
				os.system("fdisk {}".format(disk_name))
				output = sp.getstatusoutput("lsblk")

		elif input_ == 5:
			break;
		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
		
		outputcheck(output)

def Webserver():
	while True :
		os.system("clear")
		o_p = render("WEBSERVER",colors=['red','yellow'],align='center')
		print(o_p)
		os.system('espeak-ng "Welcome to webserver menu"')
		cprint("""
                                                 ====================================  =======================================
                                                 | No. |     Services               |  | No. |     Services                  |
                                                 ====================================  =======================================
                                                 | 1.  |To Configure the WebServer  |  | 2.  |To Start the Webserver         |
                                                 ------------------------------------  ---------------------------------------
                                                 | 3.  |To Host a file on webserver |  | 4.  | Go back to previous menu      |
                                                 ------------------------------------  ---------------------------------------

""",'yellow')
		cprint("Enter your choice:",'yellow',end='')
		i = int(input())
		if i == 1:
			os.system("yum install httpd")
			print("\n\n")
			os.system("systemctl start httpd")
			print("\n\n")
			os.system("systemctl stop firewalld")
			cprint("Configuration successfully!",'green')
		elif i == 2:
			os.system("systemctl start httpd")
			cprint("Started successfully!",'green')
		elif i == 3:
			cprint("Enter a file name:",'red', end='')
			file_name = input()
			os.system("cd //var//www//html && gedit {}".format(file_name))
			cprint("Started successfully!",'green')
			print("\n\n")
			cprint("Do you Know your ip (y/n):",'red',end='')
			query = input()
			print("\n\n")
			if query == "y" :
				cprint("Enter your ip address:",'red',end='')
				your_ip = input()
			elif query == "n" :
				os.system("ifconfig")
				print("--------------------------------------")
				cprint("Enter your ip address:",'red',end='')
				your_ip = input()
				
			wa = "http://"+your_ip+"/"+file_name
			cprint("your web address is {}".format(wa))
			print("\n\n")
		elif i ==4:
			break
		elif i == 5:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue


def Docker_menu():
	while True :
		os.system("clear")
		o_p = render("DOCKER",colors=['red','yellow'],align='center')
		print(o_p)
		os.system('espeak-ng "WELCOME TO DOCKER MENU"')	
		#os.system("figlet DOCKER")
		cprint("""
                                                      ----------------------------------------------------------------------------
                                                      | 1. To Search Container Images     |  | 2. To Download Container Images   |
                                                      ----------------------------------------------------------------------------
                                                      | 3. To Launch Container Images     |  | 4. To Start a Container   	 |
                                                      ----------------------------------------------------------------------------
                                                      | 5. To Attach a Container          |  | 6. To Stop a  Container           |
                                                      ----------------------------------------------------------------------------
                                                      | 7. To See Available  Images  	  |  | 8. To See All Running container   |
                                                      ----------------------------------------------------------------------------
                                                      | 9. To See All Existing container  |  | 10. To See docker info            |
                                                      ----------------------------------------------------------------------------
                                                      | 11. To Remove a Container 	  |  | 12. To Rename a Container name    |
                                                      ----------------------------------------------------------------------------
                                                      | 13. To Remove a container image   |  | 14. To See Docker logs            |
                                                      ----------------------------------------------------------------------------
                                                      | 15.To setup webserver on container|  | 16.To Setup python Interpeter     |
                                                      ----------------------------------------------------------------------------
                                                      | 17.To Go back to Main menu        |  
                                                      -------------------------------------
""",'yellow')
		cprint("Give your Choice:",'yellow',end ='')
		inp = int(input())
		
		#To Search Container Images
		if inp == 1:
			cprint("Enter Image name to search:",'yellow',end ='')
			img_name = input()
			
			output = sp.getstatusoutput("docker search {}".format(img_name))
			
		elif inp == 2:
			# Download the container
			cprint("Enter Image name to Download:",'yellow',end ='')
			img_name = input()
			
			output = sp.getstatusoutput("docker pull {}".format(img_name))
			

		elif inp == 3:
			# Launch the Container
			cprint("Enter Container name to Launch(e.g:os_name:version): ",'yellow',end='')
			img_name = input()
			cprint("Enter Os name: ",'red',end='')
			os_name = input()
			os.system("docker run -it --name {} {}".format(os_name,img_name))
			#output = sp.getstatusoutput("docker run -it --name {} {}".format(os_name,img_name))
			

		elif inp == 4:
			#Start container
			cprint("Enter Container name to Start:",'yellow',end ='')
			img_name = input()
			
			os.system("docker start {}".format(img_name))
			

		elif inp == 5:
			#attach container
			cprint("Enter Container name to Attach:",'yellow',end ='')
			img_name = input()
			
			output = sp.getstatusoutput("docker attach {}".format(img_name))
			

		elif inp == 6:
			# Stop container
			cprint("Enter Container name :",'yellow',end ='')
			img_name = input()
			output = sp.getstatusoutput("docker stop {}".format(img_name))
			

		
		elif inp == 7:
			# See Available container images
			
			output = sp.getstatusoutput("docker images")
			
		elif inp == 8:
			#See all running container
			
			output = sp.getstatusoutput("docker ps")
			
		elif inp == 9:
			#See all Existing container
			
			output = sp.getstatusoutput("docker ps -a")
			
		elif inp == 10:
			#See Container Description
			
			output = sp.getstatusoutput("docker info")
			
		elif inp == 11:
			#Remove a Container 
			cprint("Enter container name:",'yellow',end ='')
			container_name = input()
			
			output = sp.getstatusoutput("docker rm {}".format(Container_id))
			
		elif inp == 12:
			#Remove a container Image
			cprint("Enter Image name :",'yellow',end ='')
			img_name = input()
			
			output = sp.getstatusoutput("docker rmi {}".format(img_name))
			
		elif inp == 13:
			cprint("Enter OS/container name :",'yellow',end ='')
			# see docker logs
			os_name = input()
			
			output = sp.getstatusoutput("docker logs {}".format(os_name))
			
		elif inp == 14:
			cprint("Do you want to launch os then configure webserver on it(y/n)",'red',end ='')
			query = input()
			if query == "y":
				cprint("Enter Container name to Launch(e.g:os_name:version): ",'yellow',end='')
				img_name = input()
				cprint("Enter Os name: ",'red',end='')
				os_name = input()
				os.system("docker run -it --name {} {}".format(os_name,img_name))
				os.system("docker exec -it {} -y".format(os_name))
				cprint("Then Enter os name to Configure Webserver on it:",'red',end ='')
				osname = input()
				os.system("docker start {} ".format(osname))
				os.system("docker exec -it {} yum install httpd -y".format(osname))
				print("\n")
				output = sp.getstatusoutput("docker exec -it {} /usr/sbin/httpd".format(osname))

				cprint("your webserver configured on top of your container",'green')
			elif query == "n":
				cprint("Then Enter os name to Configure Webserver on it:",'red',end ='')
				osname = input()
				os.system("docker start {}".format(osname))
				os.system("docker exec -it {} yum install httpd -y".format(osname))
				print("\n")
				output = sp.getstatusoutput("docker exec -it {} /usr/sbin/httpd".format(osname))
				
		elif inp == 15:
			os.system("docker exec -it yum whatprovides python3")
			cprint("Enter name of Interpreter:",'red',end='')
			py = input()
			output = sp.getstatusoutput("docker exec -it yum install {}".format(py))
		elif inp == 16:
			break
		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
		outputcheck(output)

def lvm():

	while True :
		os.system("clear")
		o_p = render("LVM",colors=['red','yellow'],align='center')
		print(o_p)
		os.system('espeak-ng "WELCOME TO LVM MENU"')
		cprint("""
                                                              ================================================
                                                              | No.|           SERVICES                      |
                                                              ================================================
                                                              | 1. | To see all disks available              |
                                                              ------------------------------------------------
                                                              | 2. | To see all existing volume group        |
                                                              ------------------------------------------------
                                                              | 3. | To see  a existing volume  group        |
                                                              ------------------------------------------------
                                                              | 4. | To see  all logical volume(lv)          | 
                                                              ------------------------------------------------
                                                              | 5. | To see all partitions and mount points  |
                                                              ------------------------------------------------
                                                              | 6. | To create volume group                  |
                                                              ------------------------------------------------
                                                              | 7. | To create a lv partition                |
                                                              ------------------------------------------------
                                                              | 8. | To resize a lv partition                |
                                                              ------------------------------------------------
                                                              | 9. | To remove a virtual group               |
                                                              ------------------------------------------------
                                                              | 10.| To delete a Partition                   |
                                                              ------------------------------------------------
                                                              | 11.| To go back to main menu                 |
                                                              ------------------------------------------------
""",'yellow')
		cprint("Enter your Choice:",'yellow',end='')
		input_ = int(input())
		if input_ == 1:
			output = sp.getstatusoutput("fdisk -l")
		elif input_ == 2:
			output = sp.getstatusoutput("vgdisplay")
		elif input_ == 3:
			cprint("Enter a volume Group name to see info :",'yellow',end='')
			vg_name = input()
			output = sp.getstatusoutput("vgdisplay {}".format(vg_name))
		elif input_ == 4:
			#cprint("Enter logical volume name : ",'yellow',end='')
			#lv_name = input()
			output = sp.getstatusoutput("lvdisplay")
		elif input_ == 5:
			output = sp.getstatusoutput("df -h")
		elif input_ == 6:
			cprint("Enter volume group name : ",'yellow',end='')
			vg_name = input()
			cprint("Enter number of physical volume you want to add : ",'yellow',end='')
			num = input() 
			num = int(num)
			disks = [input("Enter disk {} name : ".format(i)) for i in range(num)]
			print("disks")
			s = " "
			s = s.join(disks)
			os.system("pvcreate {}".format(s))
			output = sp.getstatusoutput("vgcreate {} {}".format(vgname,s))
			info = sp.getstatusoutput("vgdisplay {}".format(vgname))
			print(info[1])
			output = sp.getstatusoutput("vgdisplay {}".format(vg_name))
		elif input_ == 7:
			cprint("Enter vgname in which you want to create partition : ",'yellow',end='')
			vg_name = input()
			cprint("Enter Logical volume name : ",'yellow',end='')
			lv_name = input()
			cprint("Enter size of lv [K,M,G] : ",'yellow',end='')
			size = input()
			cprint("Enter a folder path to which you want to link partition : ",'yellow',end='')
			mount_point = input()
			output = sp.getstatusoutput("lvcreate -n {} --size {} {} ".format(lv_name,size,vg_name))
			print(output[1],"\n")
			if(output[0] == 0):
				output = sp.getstatusoutput("mkfs.ext4 /dev/{}/{}".format(vg_name,lv_name))
				print(output[1],"\n") 
				if(output[0] == 0):
					os.system("mkdir {}".format(mount_point))
					output = sp.getstatusoutput("mount /dev/{}/{} {}".format(vg_name,lv_name,mount_point))
				info = sp.getstatusoutput("lvdisplay {}/{}".format(vg_name,lv_name))
				print(info[1])
		elif input_ == 8:
			cprint("Enter virtual group name in which logicl volume  partition is present : ",'yellow',end='')
			vg_name =input()
			cprint("Enter logival volume name : ",'yellow',end='')
			lv_name =input ()
			cprint("Enter 'R' to reduce and 'E' to extend size : ",'yellow',end='')
			option =input()
			cprint("Enter final size [K,M,G,T,P,E] you want to achieve after extend/reduce : ",'yellow',end='')
			size =input ()
			if option == 'R':
				mount_point = sp.getoutput("findmnt -n -o TARGET /dev/{}/{}".format(vg_name,lv_name))
				output = sp.getstatusoutput("umount /dev/{}/{}".format(vg_name,lv_name))
				print(output[1],"\n")
				if(output[0] == 0):
					x = os.system("e2fsck -f /dev/{}/{}".format(vg_name,lv_name))
					output = sp.getstatusoutput("resize2fs /dev/{}/{} {}".format(vg_name,lv_name,size))
					print(output[1],"\n")
					if(output[0] == 0):
						cprint("Enter y if you want to continue else enter n",'yellow')
						output = sp.getstatusoutput("lvreduce -L {} /dev/{}/{}".format(size,vg_name,lv_name))
						if(output[0] == 0):
							output=sp.getstatusoutput("mount /dev/{}/{} {}".format(vg_name,lv_name,mount_point))
			elif option == 'E':
				output = sp.getstatusoutput("lvextend -L {} /dev/{}/{}".format(size,vg_name,lv_name))
				if(output[0] == 0):
					output = sp.getstatusoutput("resize2fs /dev/{}/{}".format(vg_name,lv_name))
			info = sp.getstatusoutput("lvdisplay {}/{}".format(vg_name,lv_name))
			print(info[1])

		elif input_ == 9:
			cprint("Enter virtual group name which you want to delete : ",'yellow',end='')
			vg_name =input()
			output = sp.getstatusoutput("vgchange -a n {}".format(vgname))
			if(output[0] == 0):
				output = sp.getstatusoutput("vgremove {}".format(vg_name))
		elif input_ == 10:
			cprint("Enter virtual group name of which logical volume is a part : ",'yellow',end='')
			vg_name =input()
			cprint("Enter logical volume name which you wish to delete : ",'yellow',end='')
			lv_name =input()
			output = sp.getstatusoutput("umount /dev/{}/{}".format(vg_name,lv_name))
			if(output[0] == 0):
				output = sp.getstatusoutput("lvremove -y /dev/{}/{}".format(vg_name,lv_name))
		elif input_ == 11:
			break
		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
		outputcheck(output)	
def hadoop_menu():
	while True:
		os.system("clear")
		o_p = render("HADOOP",colors=['red','yellow'],align='center')
		print(o_p)		
		cprint("""

                                        ----------------------------------------------------------------------------------------
                                        | 1. Install Hadoop Requirements          |  2. Configure Name Node                    |
                                         -----------------------------------------   -----------------------------------------
                                        | 3. Configure Data Node                  |  4. Configure Hadoop Client                |
                                         -----------------------------------------   -----------------------------------------
                                        | 5. Limit the data node storage.         |  6. Upload Data To Hadoop Cluster          |
                                         -----------------------------------------   -----------------------------------------
                                        | 7. Read Client Data from Hadoop Cluster |  8. Delete Client Data.                    |
                                         -----------------------------------------   -----------------------------------------
                                        | 9. Stop Name Node                       |  10. Stop Data Node.                       |
                                         -----------------------------------------   -----------------------------------------
                                        | 11. Start Name Node.                    |  12. Start Data Node.                      |
                                         -----------------------------------------   -----------------------------------------
                                        | 13. Check the Hadoop Cluster Information|  14. List all the contents in the Cluster  |                 
                                         -----------------------------------------   -------------------------------------------
                                        | 15. To create an empty file in Client   |  16.To go back to the main menu.           |
                                         ---------------------------------------------------------------------------------------""",'yellow')
		cprint("Give your Choice:",'yellow',end='')
		task = input()

 
		if task == '1':
			
		   	os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
		   	os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
		   	print("\n\tHadoop Requirements Sucessfully Installed In Name Node")
		   	print("\n\t---------------------------------------------------------------------")
		   	ab = input("Enter Your Data Node IP :")
		   	os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ab))
		   	os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(ab))
		   	print("\n\tHadoop Requirements Sucessfully Installed In Data Node")
		   	print("\n\t---------------------------------------------------------------------")
		   	bb = input("Enter Your Client Node IP :")
		   	os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(bb))
		   	os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(bb))
		   	print("\n\tHadoop Requirements Sucessfully Installed In Client Node")
		   	print("\n\t---------------------------------------------------------------------")
		   

		elif task == '2':
		   	dir = input("\n\t\tEnter your Name Node directory name : ")
		   	print("\t\t\t\tConfiguring hdfs-site.xml file ............")
		   	os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
		   	os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
		   	os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
		   	os.system('echo -e "</property>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
		   	os.system('rm -rf /etc/hadoop/hdfs-site.xml')
		   	os.system('cp  /root/hdfs-site.xml  /etc/hadoop')
		   	os.system('rm -rf /root/hdfs-site.xml')
		   	print("\n\tFormatting the Name Node ..............................")
		   	print()
		   	os.system('hadoop namenode -format')
		   	print()
		   	print()
		   	nip = input("Enter Name Node IP :")
		   	print("\t\t\t\tConfiguring core-site.xml file ...........")
		   	os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
		   	os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
		   	os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
		   	os.system('echo -e "\n<property>" >> /root/core-site.xml')
		   	os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
		   	os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
		   	os.system('echo -e "</property>" >> /root/core-site.xml')
		   	os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
		   	os.system('rm -rf /etc/hadoop/core-site.xml')
		   	os.system('cp  /root/core-site.xml  /etc/hadoop')
		   	os.system('rm -rf /root/core-site.xml')
		   	print("\n\tHadoop NameNode configured successfully")
		   			
		elif task == '3':
		   	dip = input("\t\tEnter Data Node IP : ")
		   	dio = input("\t\tEnter your Data Node directory name : ")
		   	print("\t\t\t\tConfiguring hdfs-site.xml file ............")
		   	os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
		   	os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
		   	os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
		   	os.system('echo -e "</property>" >> /root/hdfs-site.xml')
		   	os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
		   	os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
		   	os.system('rm -rf /root/hdfs-site.xml')
		   	niq = input("Enter Name Node IP :")
		   	print("\t\t\t\tConfiguring core-site.xml file ...........")
		   	os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
		   	os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
		   	os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
		   	os.system('echo -e "\n<property>" >> /root/core-site.xml')
		   	os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
		   	os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
		   	os.system('echo -e "</property>" >> /root/core-site.xml')
		   	os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
		   	os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
		   	os.system('rm -rf /root/core-site.xml')
		   	cprint("\n\tHadoop DataNode Sucessfully Configured.........",'green')
		   		
		elif task == '4':
		   	yu = input("Enter Name Node IP : ")
		   	print("\t\t\t\tConfiguring core-site.xml file ...........")
		   	ip = input("\n\t\tEnter Client IP : ")
		   	os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
		   	os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
		   	os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
		   	os.system('echo -e "\n<property>" >> /root/core-site.xml')
		   	os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
		   	os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(yu))
		   	os.system('echo -e "</property>" >> /root/core-site.xml')
		   	os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
		   	os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
		   	print("\t\tHadoop Client Sucessfully Configured.........")			
					
		elif task == '5':
			ip = input("\n\tEnter Data Node IP : ")
			si = input("\n\tDo You want to extend/reduce Data Node Storage? : ")
			if si == "extend":
				os.system('ssh {} df -hT'.format(ip))
				ex = input("\n\t\tHow much you want to extend? : ")
				vg = input("\t\tEnter Your Volume Group Name : ")
				lv = input("\t\tEnter Your Logical Volume Name : ")
				os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
				print("\t\t\tSucessfully Extended the  Data Node Storage ")
				os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
				print("------------------------------------------------------------")
				os.system('ssh {} df -hT'.format(ip))
			elif si == "reduce":
				os.system('ssh {} df -hT'.format(ip))
				ex = input("\n\t\tHow much you want to reduce? : ")
				vg = input("\t\tEnter Your Volume Group Name : ")
				lv = input("\t\tEnter Your Logical Volume Name : ")
				os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
				print("\t\t\tSucessfully Reduced Data Node Storage ")
				os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
				print("------------------------------------------------------------")
				os.system('ssh {} df -hT'.format(ip))
		elif task == '6':
			ci = input("\t\tEnter Client IP : ")
			fiz = input("\t\tEnter The Name of File You want to upload on Hadoop Cluster : ")
			os.system('ssh {} hadoop fs -put {} /'.format(ci , fiz))
			print("\t\t\tFile Sucessfully Uploaded .......................")
			os.system('ssh {} hadoop fs -ls /'.format(ci))		
		elif task == '7':
			co = input("\t\tEnter Client IP : ")
			fii = input("\t\tEnter Your File Name : ")
			os.system('ssh {} hadoop fs -cat /{}'.format(co , fii))			
		elif task == '8':
			ty = input("\t\tEnter Client IP : ")
			foi = input("\t\tEnter Your File Name : ")
			os.system('ssh {} hadoop fs -rm /{}'.format(ty , foi))
			print("\t\tSucessfully Deleted File {} ".format(foi))			
		elif task == '9':
			os.system('hadoop-daemon.sh stop namenode')
			os.system('jps')
				
		elif task == '10':
			ip = input("\n\tEnter Data Node IP : ")
			os.system('ssh {} hadoop-daemon.sh stop datanode'.format(ip))
			os.system('ssh {} jps'.format(ip))
		elif task == '11':
			print("\n\t Starting Hadoop Name Node Services .............................")
			os.system('hadoop-daemon.sh start namenode') 
			os.system('jps') 
			print("\n\t--------------------------------------------------------------")
			print("\n\t Showing Hadoop Cluster Report ..............................")
			os.system('ssh {} hadoop dfsadmin -report'.format(dip))

		elif task == '12':
			dip = input("\t\tEnter Data Node IP : ")
			print("\n\t Starting Hadoop Data Node Services .............................")
			os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
			os.system('ssh {} jps'.format(dip))
			print("\n\t--------------------------------------------------------------")
			print("\n\t Showing Hadoop Cluster Report ..............................")
			os.system('ssh {} hadoop dfsadmin -report'.format(dip))

		elif task == '13':
			print("\n\t Showing Hadoop Cluster Report ..............................")
			os.system("hadoop dfsadmin -report | less")
		
		elif task == '14':
			print("\n\t Showing the contents of Hadoop Cluster")
			os.system("hadoop fs -ls /")

		elif task == '15':
			file = input("Enter file path with name which you want to create (eg - /<foldername>/<filename>) : ")
			os.system("hadoop fs -touchz {}".format(file))
			
		elif task == '16':
			break
		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
			
def aws_menu():
	while True:
		os.system("clear")
		o_p = render("AWS",colors=['red','yellow'],align='center')
		print(o_p)
		os.system('espeak-ng "WELCOME TO AWS MENU"')
		cprint("""

                                        ----------------------------------------------------------------------------------------
                                        | 1. To login to aws account              |  10. To describe instances.                |
                                         -----------------------------------------   -----------------------------------------
                                        | 2. To create a key pair                 |  11. To show existing key pairs.           |
                                         -----------------------------------------   -----------------------------------------
                                        | 3. To create a security group           |  12. To show an instance.                  |
                                         -----------------------------------------   -----------------------------------------
                                        | 4. To add inbound rules 	          |  13. To start an instance.                 |
                                         -----------------------------------------   -----------------------------------------
                                        | 5. To launch ec2 instance               |  14. To change the bucket permissions.     |
                                         -----------------------------------------   -----------------------------------------
                                        | 6. To create an ebs volume              |  15. To upload image in s3 bucket.         |
                                         -----------------------------------------   -----------------------------------------
                                        | 7. Attach ebs volume to instance        |  16. To stop an instance.                  |
                                         -----------------------------------------   -----------------------------------------
                                        | 8. To create a s3 bucket                |  17.To configure docker on ec2 instance .  |
                                         -----------------------------------------   -----------------------------------------
                                        | 9. Create a cloudfront distribution     |  18.To go to main menu or exit             |
                                        ----------------------------------------------------------------------------------------""",'green')
		cprint("Give your Choice:",'yellow')
		task = input ()
		#aws(task)
		if task == '1':
			rc=os.system("aws configure")
			if(rc == 0):
				output=(0,'Login Successful')
		elif task == '2':
			keyname = input("Enter Key name : ")
			output = sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(keyname))
		elif task == '3':
			grpname = input("Enter Security group name : ")
			description = input("Give Description of your security group : ")
			output = sp.getstatusoutput("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-c62ecead".format(grpname,description))
		elif task == '4':
			grpid = input("Enter group id : ")
			protocol = input("Enter protocol you want to add : ")
			port = input("Enter port number : ")
			output = sp.getstatusoutput("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0".format(grpid,protocol,port))
		elif task == '5':
			image = input("Enter image id : ")
			instance = input("Enter instance-type : ")
			count = input("Enter no.of instance you want to launch : ")
			sgid = input("Enter security group id : ")
			keyname = input("Enter Key name : ")
			
			output = sp.getstatusoutput("aws ec2 run-instances --image-id  {} --instance-type {} --count {}  --security-groups {} --key-name {}".format(image,instance,count,sgid,keyname))
		elif task == '6':
			size = input("Enter size of your ebs volume : ")
			az = input("Enter availability-zone in which you want to create volume : ")
			ebsname = input("Enter a name which you want to give to your volume : ")
			output = sp.getstatusoutput("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {} --tag-specifications 'ResourceType=volume,Tags=['{'Key=name,Value= {}}]'".format(size,az,ebsname))
		elif task == '7':
			print("Before attaching EBS volume to an instance make sure your EBS volume and instance are in the same availability zone")
			instance = input("Enter instance-id to which you want to attach: ")
			volid = input("Enter volume-id which you want to attach : ")
			output = sp.getstatusoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,instance))
		elif task == '8':
			bucketname = input("Enter bucket name : ")
			region = input("Enter region in which you want to create bucket : ")
			output = sp.getstatusoutput("aws s3 mb s3://{} --region {}".format(bucketname,region))
		elif task == '9':
			bucketname = input("Enter bucket name : ")
			output = sp.getstatusoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucketname))
		elif task == '10':
			output = sp.getstatusoutput("aws ec2 describe-instances")
		elif task == '11':
			output = sp.getstatusoutput("aws ec2 describe-key-pairs")
		elif task == '12':
			output = sp.getstatusoutput("aws ec2 describe-security-groups")
		elif task == '16':
			instance = input("Enter the instance id which you want to stop: ")
			output = sp.getstatusoutput("aws ec2 stop-instances --instance-ids {}".format(instance))

		elif task == '13':
			instance = input("Enter the instance id which you want to start: ")
			output = sp.getstatusoutput("aws ec2 start-instances --instance-ids {}".format(instance))
		elif task == '14':
			b_name = input("Enter bucket name: ")
			img_name = input("Enter image file name: ")
			permission = input("Enter permission you want to give eg.,public-read: ")
			ouput = sp.getstatusoutput("aws s3api put-object-acl --bucket {} --key {} --acl {}".format(b_name,img_name,permission))

		elif task == '15':
			img_path = input("Enter the complete path of the image you want to upload: ")
			b_name = input("Enter name of the bucket: ")
			output = sp.getstatusoutput("aws s3 sync \"{}\" s3\:\/\/{}\ ".format(img_path,b_name))

		elif task == '18':
			break
		#works only in case of amazon ami 
		elif task == '17':
		
                        output = sp.getstatusoutput("sudo amazon-linux-extras install docker")


		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
		outputcheck(output)


def ansible_menu():
		while True:
			os.system("clear")
			o_p = render("ANSIBLE",colors=['red','yellow'],align='center')
			print(o_p)
			cprint("""

		                                 -----------------------------------------
		                                | 1. To install httpd on ec2 instance     |  
		                                 -----------------------------------------   
		                                | 2. To install nginx on ec2 instance     |  
		                                 -----------------------------------------   
		                                | 3. To install net-tools on ec2 -instance|       
		                                 -----------------------------------------   
		                                | 4. To install tcpdump on ec2 instance	  |         
		                                 -----------------------------------------   
		                                | 5. To install python3 on ec2 instance   | 
		                                 -----------------------------------------
		                                | 6. To ping all the ip in the inventory  |
		                                 -----------------------------------------     
		                                | 7. To exit or return to the main menu.  |                                   
		                                 ----------------------------------------- """,'yellow')
			cprint("Give your Choice:",'green',end='')
			inp = int(input())
			
			if inp == 1:
				cprint("Enter the name of ip stored of the ec2 instance on which you want to install httpd ",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system('ansible {} -m package -a "name=httpd state=present" '.format(ipname))
				os.system("tput setaf 7")
			    
			elif inp == 2:
				
				cprint("Enter the name of ip stored of the ec2 instance on which you want to install nginx ",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system('ansible {} -m package -a "name=nginx state=present" '.format(ipname))
				os.system("tput setaf 7")
		       
			elif inp == 3:
				cprint("Enter the name of ip stored of the ec2 instance on which you want to install net-tools ",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system('ansible {} -m package -a "name=httpd state=present"'.format(ipname))
				os.system("tput setaf 7")

			elif inp == 4:
				cprint("Enter the name of ip stored of the ec2 instance on which you want to install tcpdump",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system('ansible {} -m package -a "name=tcpdump"'.format(ipname))
				os.system("tput setaf 7")

			elif inp == 5:
				cprint("Enter the name of ip stored of the ec2 instance on which you want to install python3 ",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system('ansible {} -m package -a "name=python3" '.format(ipname))
				os.system("tput setaf 7")

			elif inp == 6:
				cprint("To ping all the ip ",'yellow')
				ipname=input()
				os.system("tput setaf 6")
				os.system("ansible all -m ping")
				os.system("tput setaf 7")

			elif inp == 7:
				break
			
			else:
				print("Invalid Choice ! Try Again")
				os.system("sleep 1")
				continue
			


def ML_menu():
	os.system("clear")
	o_p = render("ML",colors=['red','yellow'],align='center')
	print(o_p)
	cprint("""

                                         ------------------------------------------------------------------------------------- 
                                        | 1.We can train our models and predict the details of upcoming events.               |
                                        |   We can do the prediction on docker container.                                     |                                               |                                       |   We just need to mention the name of docker container that is already present.     |
                                        |   We just need to provide the file of historical data ,                             |
                                        |   and the salary prediction can be done on the docker container itself.             |
                                        | 2. To exit and go back to the main menu.                                                                                     
                                         ------------------------------------------------------------------------------------- """,'yellow')
	cprint("Give your Choice:",'yellow',end='')
	inp = int(input ())
	
	# first we need to write the ip of the ec2  instance in the ip.txt file or whatever inventory file is configured for ansible 
	if inp == 1:
		print("\n\t\tAutomating Integration of Machine Learning &  Docker")
		hn = input("\nEnter Name of Running Docker Container : ")
		os.system('docker exec -it {} pip3 install sklearn'.format(hn))
		os.system('docker exec -it {} pip3 install pandas'.format(hn))
		os.system('docker exec -it {} pip3 install joblib'.format(hn))
		os.system('docker cp /root/salarydata.csv {}:/'.format(hn))
		os.system('docker cp /root/model.py {}:/'.format(hn))
		print("\n\t\t---------------Prediction Automation----------------------------------")
		os.system('docker exec -it {} python3 model.py'.format(hn))
           
	elif inp == 2:
		Main_menu()
#ansible_menu()			
#aws_menu()
#hadoop_menu()






def Main_menu():
	os.system("clear")
	os.system('cfonts "WELCOME " -f 3d -a center -c candy')
	os.system('cfonts "\t\tTO" -f 3d -a center -c candy')
	os.system('cfonts "\t\tAUTOPY" -f 3d -a center -c candy')
	
	os.system('espeak-ng "Welcome to AutoPy........................."')
	cprint("\n\t\t\t\t\t\t\t\t\t\t\t\t\tAUTOPY - THE WORLD OF AUTOMATION",'green')
	os.system('espeak-ng "Hello Tamanna ............Welcome to the world of Automation"')
	while True :
		os.system("clear")		
		print("\t\t\t\t\t\tAutoPy facilitates you the automation of following technologies :- Docker,Webserver,AWS,Partitioning,Ansible,Hadoop,Machine Learning")
		cprint("""
                                                                      ======================================== ========================================
                                                                      | No.|          SERVICES               | No.|         SERVICES                  |
                                                                      ======================================== ========================================
                                                                      | 1. | LINUX COMMAND      	     | 6. | STATIC PARTITION                  |
                                                                      ---------------------------------------- ----------------------------------------
                                                                      | 2. | DOCKER MENU        	     | 7. | ANSIBLE                           |
                                                                      ---------------------------------------- ----------------------------------------
                                                                      | 3. | WEBSERVER MENU    	             | 8. | HADOOP                            |
                                                                      ---------------------------------------- ----------------------------------------
                                                                      | 4. |  AWS MENU                       | 9. | MACHINE LEARNING                  |
                                                                      ---------------------------------------- ----------------------------------------
                                                                      | 5. | LOGICAL VOLUME MANAGEMENT       | 10.| EXIT                              | 
                                                                      ---------------------------------------- ----------------------------------------""",'yellow')
		cprint("for e.g : Press 1 for linux ")
		cprint("Enter your Choice:",'yellow',end="")
		input_ = int(input())
		
		if input_ == 1:
			linux_menu()
		elif input_ == 2:
			Docker_menu()
		elif input_ == 3:
			Webserver()
		elif input_ == 4:
			aws_menu()
		elif input_ == 5:
			lvm()
		elif input_ == 6:
			Static_partition_menu()
		elif input_ == 7:
			ansible_menu()
		elif input_ == 8:
			hadoop_menu()
		elif input_ == 9:
			ML_menu()
		elif input_ == 10:
			break
		else:
			print("Invalid Choice ! Try Again")
			os.system("sleep 1")
			continue
			
passwd= getpass.getpass("Enter the password : ")

if passwd == "tamanna" :
	print("\n\t\t---------------> you have successfully logged in")
	Main_menu()
else:
	print("Wrong Password")
	exit()



			















