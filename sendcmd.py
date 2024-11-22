from netmiko import ConnectHandler
import re
import sys
from netmiko.exceptions import (
    NetmikoTimeoutException,
)
from typing import (
    Optional,
)
import yaml

# Logging section ##############
#import logging
#logging.basicConfig(filename="test.log", level=logging.DEBUG)
#logger = logging.getLogger("netmiko")
# Logging section ##############


def enable(self,
           cmd: str = "administrator",
           pattern: str = r"Password",
           enable_pattern: Optional[str] = "#",
           check_state: bool = True,
           re_flags: int = re.IGNORECASE,
    ) -> str:
    output = ""
    msg = (
            "Failed to enter enable mode. Please ensure you pass "
            "the 'secret' argument to ConnectHandler."
            )

    # Send "enable" mode command
    self.write_channel(self.normalize_cmd(cmd))
    try:
        # Read the command echo
        if self.global_cmd_verify is not False:
            output += self.read_until_pattern(pattern=re.escape(cmd.strip()))

        # Search for trailing prompt or password pattern
        output += self.read_until_prompt_or_pattern(
            pattern=pattern, re_flags=re_flags
        )

        # Send the "secret" in response to password pattern
        if re.search(pattern, output):
            self.write_channel(self.normalize_cmd(self.secret))
            output += self.read_until_pattern(pattern='#')

    except NetmikoTimeoutException:
        raise ValueError(msg)

    return output


def iserror(output):
    if 'エラー' in output or 'Error' in output:
        return True
    else:
        return False

if len(sys.argv) < 2:
    print(f'{sys.argv[0]} config.yaml')
    sys.exit(1)

with open(sys.argv[1], 'r') as fp:
    config = yaml.safe_load(fp)

device = { k:v for k, v in config.items() }
device['device_type'] = 'yamaha'
net_connect = ConnectHandler(**device)

for line in sys.stdin:
    line = line.rstrip()
    print(line)
    if line == 'administrator':
        output = enable(net_connect)
    else:
        output = net_connect.send_command(line)
    print(output)

    if iserror(output):
        print('Erorr detected. Abort.')
        sys.exit(1)

