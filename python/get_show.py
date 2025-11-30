import warnings
from paramiko import Transport
from netmiko import ConnectHandler
import yaml
import datetime

# --- 古いSSH暗号を許可（3560用） ---
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

Transport._preferred_kex = (
    'diffie-hellman-group14-sha1',
    'diffie-hellman-group1-sha1'
)
Transport._preferred_pubkeys = ('ssh-rsa',)
Transport._preferred_macs = (
    'hmac-sha1',
    'hmac-sha1-96',
    'hmac-md5',
    'hmac-md5-96'
)
Transport._preferred_ciphers = (
    'aes128-cbc',
    'aes192-cbc',
    'aes256-cbc',
    '3des-cbc'
)
# ---------------------------------------

# YAMLからデバイス情報読み込み
with open("device_info.yml") as f:
    devices = yaml.safe_load(f)

# 実行したいshowコマンド
show_commands = [
    "show version",
    "show ip interface brief"
]

for device_name, params in devices.items():
    print(f"===== Connecting to {device_name} =====")
    
    try:
        conn = ConnectHandler(
            **params,
            banner_timeout=30,
            auth_timeout=30
        )

        if "secret" in params:
            conn.enable()

        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        log_file = f"{device_name}_show_output_{now}.txt"

        with open(log_file, "w") as f:
            for cmd in show_commands:
                print(f"Running: {cmd}")
                output = conn.send_command(cmd)
                f.write(f"\n\n===== {cmd} =====\n")
                f.write(output)

        print(f"Log saved: {log_file}")
        conn.disconnect()

    except Exception as e:
        print(f"[ERROR] {device_name}: {e}")
