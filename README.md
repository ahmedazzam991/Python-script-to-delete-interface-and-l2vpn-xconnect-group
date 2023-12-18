
# Network Device Configuration Tool

The Network Device Configuration Tool is a Python script with a Tkinter-based graphical user interface (GUI) designed to interact with network devices using the Exscript library. It allows users to establish an SSH connection to a specified network device, execute commands, and make configuration changes.

## Features

- **SSH Connection:** Establishes an SSH connection to a network device using Exscript.
- **CSV Integration:** Reads login credentials, router IP information, and configuration data from CSV files.
- **Command Execution:** Executes telnet and various commands on the network device based on the CSV data.
- **Configuration Changes:** Adjusts network device configurations, including interface removal and L2VPN group adjustments.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Exscript library (`pip install Exscript`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/network-device-config-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd network-device-config-tool
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python script.py
    ```

5. Enter Aterm credentials in the GUI and press the "Submit" button.

## Configuration Files

### 'credentials and Router IP.csv'

This CSV file should have the following format:

```plaintext
username,password,login_username,login_password,router_ip
JohnDoe,secretpass,user1,password1,192.168.1.1
```

### 'input.csv'

This CSV file should have the following format:

```plaintext
interface,l2vpn_group,p2p_value
eth0,group1,value1
eth1,group2,value2
```

## User Interface

- The GUI displays input fields for Aterm credentials and a logo image.
- Press the "Submit" button to initiate the network device interaction.

## Troubleshooting

- Ensure proper file paths and permissions for reading CSV files.
- Verify that the specified network device is reachable and accessible.
- Adjust command execution based on specific network device requirements.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

