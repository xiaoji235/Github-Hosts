import os
import shutil
import requests
import tkinter as tk
from tkinter import messagebox
import subprocess

def show_message(message):
    """弹窗显示指定消息"""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("提示", message)
    root.destroy()

def flush_dns_cache():
    # DNS缓存清理
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True, shell=True)
        print("DNS缓存已刷新")
    except subprocess.CalledProcessError as e:
        print(f"刷新DNS缓存失败: {e}")

def main():
    # hosts复制与修改
    etc_dir = r"C:\Windows\System32\drivers\etc"
    hosts_path = os.path.join(etc_dir, "hosts")
    hosts_bak_path = os.path.join(etc_dir, "hosts.bak")

    # 检查是否存在 hosts.bak 文件
    if not os.path.exists(hosts_bak_path):
        # 如果不存在，则将 hosts 复制为 hosts.bak
        if os.path.exists(hosts_path):
            shutil.copy2(hosts_path, hosts_bak_path)
            print("已将 hosts 文件复制为 hosts.bak")
        else:
            print("hosts 文件不存在，无法复制")
        # 弹窗提示
        show_message("第一次使用时系统会将hosts复制为hosts.bak,如需永久写入操作，请将地址写入hosts.bak并重新运行一次！写入hosts会被覆盖！建议将hosts.bak做二次备份！")
    else:
        # 如果存在，则删除 hosts 文件并将 hosts.bak 复制为 hosts
        if os.path.exists(hosts_path):
            os.remove(hosts_path)
            print("已删除 hosts 文件")
        shutil.copy2(hosts_bak_path, hosts_path)
        print("已将 hosts.bak 复制为 hosts")

    # 获取GitHub-hosts地址
    url = "https://raw.hellogithub.com/hosts"
    response = requests.get(url)
    if response.status_code == 200:
        with open(hosts_path, "a", encoding="utf-8") as hosts_file:
            hosts_file.write("\n" + response.text)
        print("已将URL内容追加到 hosts 文件中")
    else:
        print(f"无法从 {url} 下载内容，状态码: {response.status_code}")

    # 刷新DNS缓存
    flush_dns_cache()

if __name__ == "__main__":
    main()
