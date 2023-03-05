import os
import requests
import json
import time
from tqdm import tqdm
from termcolor import colored

def Invalid():
	print("Invalid!")
	raise SystemExit

def Wait():
	time.sleep(5)
	os.system('cls')

def Clear():
	os.system('cls')

def Exit():
	raise SystemExit

def Purpur():
	Clear()
	# Build + PurpurVersion/Name
	print(colored('Purpur> ', 'red'), colored('Downloading name, version, latest build...', 'yellow'))
	PurpurVersion = "1.19.3"
	PurpurName = "purpur"
	PurpurURL = "https://api.purpurmc.org/v2/" + PurpurName + "/" + PurpurVersion + "/latest"
	PurpurBuild = requests.get(PurpurURL)
	PurpurData = json.loads(PurpurBuild.text)
	PurpurLatestBuild = PurpurData["build"]
	Wait()
	# Build + PurpurVersion/Name

	# Download Link + Filename
	PurpurDownload = PurpurURL + "/download"
	PurpurRespone = requests.get(PurpurDownload, stream=True)
	PurpurJarName = PurpurName + "-" + PurpurVersion + "-" + PurpurLatestBuild + ".jar"
	# Download Link + Filename

	print(colored('Purpur> ', 'red'), colored('Creating the start_purpur.bat file...', 'yellow'))
	PurpurStartBAT = open("./server/Purpur/start_purpur.bat", "w")
	PurpurARG = "java -Xms1G -Xmx1G -jar "
	PurpurStartBAT.write("@echo off\n" + PurpurARG + PurpurJarName + " --nogui" + "\npause")
	PurpurStartBAT.close()
	Wait()

	print(colored('Purpur> ', 'red'), colored('Downloading JAR file..', 'yellow'))
	PurpurProgressBarSizeByte = int(PurpurRespone.headers.get('content-length', 0))
	PurpurProgressBarBlockSize = 1024
	PurpurProgressBar = tqdm(total=PurpurProgressBarSizeByte, unit='iB', unit_scale=True)
	with open("./server/Purpur/" + PurpurJarName, "wb") as f:
		for PurpurProgressBarData in PurpurRespone.iter_content(PurpurProgressBarBlockSize):
			PurpurProgressBar.update(len(PurpurProgressBarData))
			f.write(PurpurProgressBarData)

	PurpurProgressBar.close()
	if PurpurProgressBarSizeByte != 0 and PurpurProgressBar.n != PurpurProgressBarSizeByte:
		print("ERROR, something went wrong")

def Paper():
	Clear()
	# PaperVersion/Name/URL
	print(colored('Paper> ', 'red'), colored('Downloading name, version...', 'yellow'))
	PaperVersion = "1.19.3"
	PaperName = "paper"
	PaperURL = "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds"
	Wait()
	# PaperVersion/Name/URL

	# Build + Download Link + Filename
	print(colored('Paper> ', 'red'), colored('Downloading url latest build...', 'yellow'))
	PaperRespone = requests.get(PaperURL)
	PaperDataBuild = json.loads(PaperRespone.text)
	build = []
	for i in PaperDataBuild["builds"]:
		build.append(i["build"])

	build.sort()
	PaperDownload = PaperURL + "/" + str(build[-1]) + "/downloads/" + PaperName + "-" + PaperVersion + "-" + str(build[-1]) + ".jar"
	PaperResponeDownload = requests.get(PaperDownload, stream=True)
	PaperJarName = PaperName + "-" + PaperVersion + "-" + str(build[-1]) + ".jar"
	Wait()
	# Build + Download Link + Filename

	print(colored('Paper> ', 'red'), colored('Creating the start_paper.bat file...', 'yellow'))
	PaperStartBAT = open("./server/Paper/start_paper.bat", "w")
	PaperARG = "java -Xms1G -Xmx1G -jar "
	PaperStartBAT.write("@echo off\n" + PaperARG + PaperJarName + "\npause")
	PaperStartBAT.close()
	Wait()

	print(colored('Paper> ', 'red'), colored('Downloading JAR file...', 'yellow'))
	PaperProgressBarSizeByte = int(PaperResponeDownload.headers.get('content-length', 0))
	PaperProgressBarBlockSize = 1024
	PaperProgressBar = tqdm(total=PaperProgressBarSizeByte, unit='iB', unit_scale=True)
	with open("./server/Paper/" + PaperJarName, "wb") as f:
		for PaperProgressBarData in PaperResponeDownload.iter_content(PaperProgressBarBlockSize):
			PaperProgressBar.update(len(PaperProgressBarData))
			f.write(PaperProgressBarData)

	PaperProgressBar.close()
	if PaperProgressBarSizeByte != 0 and PaperProgressBar.n != PaperProgressBarSizeByte:
		print("ERROR, smoething went wrong")

def Velocity():
	Clear()
	# VelocityVersion/Name/URL
	print(colored('Velocity> ', 'red'), colored('Downloading name, url, version...', 'yellow'))
	VelocityVersion = "3.2.0-SNAPSHOT"
	VelocityName = "velocity"
	VelocityURL = "https://api.papermc.io/v2/projects/velocity/versions/3.2.0-SNAPSHOT/builds"
	Wait()
	# VelocityVersion/Name/URL

	# Build + Download Link + Filename
	print(colored('Velocity> ', 'red'), colored('Downloading latest build...', 'yellow'))
	VelocityRespone = requests.get(VelocityURL)
	VelocityDataBuild = json.loads(VelocityRespone.text)
	build = []
	for i in VelocityDataBuild["builds"]:
		build.append(i["build"])

	build.sort()
	VelocityDownload = VelocityURL + "/" + str(build[-1]) + "/downloads/" + VelocityName + "-" + VelocityVersion + "-" + str(build[-1]) + ".jar"
	VelocityResponeDownload = requests.get(VelocityDownload, stream=True)
	VelocityJarName = VelocityName + "-" + VelocityVersion + "-" + str(build[-1]) + ".jar"
	Wait()
	# Build + Download Link + Filename

	print(colored('Velocity> ', 'red'), colored('Creating the start_velocity.bat file...', 'yellow'))
	VelocityStartBAT = open("./proxy/Velocity/start_velocity.bat", "w")
	VelocityARG = "java -Xms512M -Xmx512M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -jar "
	VelocityStartBAT.write("@echo off\n" + VelocityARG + VelocityJarName + "\npause")
	VelocityStartBAT.close()
	Wait()

	print(colored('Velocity> ', 'red'), colored('Downloading JAR file...', 'yellow'))
	VelocityProgressBarSizeByte = int(VelocityResponeDownload.headers.get('content-length', 0))
	VelocityProgressBarBlockSize = 1024
	VelocityProgressBar = tqdm(total=VelocityProgressBarSizeByte, unit='iB', unit_scale=True)
	with open("./proxy/Velocity/" + VelocityJarName, "wb") as f:
		for VelocityProgressBarData in VelocityResponeDownload.iter_content(VelocityProgressBarBlockSize):
			VelocityProgressBar.update(len(VelocityProgressBarData))
			f.write(VelocityProgressBarData)

	VelocityProgressBar.close()
	if VelocityProgressBarSizeByte != 0 and VelocityProgressBar.n != VelocityProgressBarSizeByte:
		print("ERROR, smoething went wrong")

def Waterfall():
	Clear()
	# WaterfallVersion/Name/URL
	print(colored('Waterfall> ', 'red'), colored('Downloading name, url, version...', 'yellow'))
	WaterfallVersion = "1.19"
	WaterfallName = "waterfall"
	WaterfallURL = "https://api.papermc.io/v2/projects/waterfall/versions/1.19/builds"
	Wait()
	# WaterfallVersion/Name/URL

	# Build + Download Link + Filename
	print(colored('Waterfall> ', 'red'), colored('Downloading latest build...', 'yellow'))
	WaterfallRespone = requests.get(WaterfallURL)
	WaterfallDataBuild = json.loads(WaterfallRespone.text)
	build = []
	for i in WaterfallDataBuild["builds"]:
		build.append(i["build"])

	build.sort()
	WaterfallDownload = WaterfallURL + "/" + str(build[-1]) + "/downloads/" + WaterfallName + "-" + WaterfallVersion + "-" + str(build[-1]) + ".jar"
	WaterfallResponeDownload = requests.get(WaterfallDownload, stream=True)
	WaterfallJarName = WaterfallName + "-" + WaterfallVersion + "-" + str(build[-1]) + ".jar"
	Wait()
	# Build + Download Link + Filename

	print(colored('Waterfall> ', 'red'), colored('Creating the start_waterfall.bat file...', 'yellow'))
	WaterfallStartBAT = open("./proxy/Waterfall/start_waterfall.bat", "w")
	WaterfallARG = "java -Xms512M -Xmx512M -jar "
	WaterfallStartBAT.write("@echo off\n" + WaterfallARG + WaterfallJarName + "\npause")
	WaterfallStartBAT.close()
	Wait()

	print(colored('Waterfall> ', 'red'), colored('Downloading JAR file...', 'yellow'))
	WaterfallProgressBarSizeByte = int(WaterfallResponeDownload.headers.get('content-length', 0))
	WaterfallProgressBarBlockSize = 1024
	WaterfallProgressBar = tqdm(total=WaterfallProgressBarSizeByte, unit='iB', unit_scale=True)
	with open("./proxy/Waterfall/" + WaterfallJarName, "wb") as f:
		for WaterfallProgressBarData in WaterfallResponeDownload.iter_content(WaterfallProgressBarBlockSize):
			WaterfallProgressBar.update(len(WaterfallProgressBarData))
			f.write(WaterfallProgressBarData)

	WaterfallProgressBar.close()
	if WaterfallProgressBarSizeByte != 0 and WaterfallProgressBar.n != WaterfallProgressBarSizeByte:
		print("ERROR, something went wrong")

def BungeeCord():
	Clear()
	# BungeeCordName/URL + Build
	print(colored('BungeeCord> ', 'red'), colored('Downloading name, url, latest build...', 'yellow'))
	BungeeCordName = "BungeeCord"
	BungeeCordDownload = "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar"
	Wait()
	# BungeeCordName/URL + Build

	# Download Link + Filename
	BungeeCordRespone = requests.get(BungeeCordDownload, stream=True)
	BungeeCordJarName = BungeeCordName + ".jar"
	# Download Link + Filename

	print(colored('BungeeCord> ', 'red'), colored('Creating the start_bungeecord.bat file...', 'yellow'))
	BungeeCordStartBAT = open("./proxy/BungeeCord/start_bungeecord.bat", "w")
	BungeeCordARG = "java -Xms512M -Xmx512M -jar "
	BungeeCordStartBAT.write("@echo off\n" + "Title Proxy\n" + BungeeCordARG + BungeeCordName + "\npause")
	BungeeCordStartBAT.close()
	Wait()

	print(colored('BungeeCord> ', 'red'), colored('Downloading JAR file...', 'yellow'))
	BungeeCordProgressBarSizeByte = int(BungeeCordRespone.headers.get('content-length', 0))
	BungeeCordProgressBarBlockSize = 1024
	BungeeCordProgressBar = tqdm(total=BungeeCordProgressBarSizeByte, unit='iB', unit_scale=True)
	with open("./proxy/BungeeCord/" + BungeeCordJarName, "wb") as f:
		for BungeeCordProgressBarData in BungeeCordRespone.iter_content(BungeeCordProgressBarBlockSize):
			BungeeCordProgressBar.update(len(BungeeCordProgressBarData))
			f.write(BungeeCordProgressBarData)

	BungeeCordProgressBar.close()
	if BungeeCordProgressBarSizeByte != 0 and BungeeCordProgressBar.n != BungeeCordProgressBarSizeByte:
		print("ERROR, something went wrong")
