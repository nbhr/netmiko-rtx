# netmiko-yamaha-rtx

This is a small script to send commands to Yamaha RTX devices using [netmiko](https://github.com/ktbyers/netmiko) library.

## Configuration

Copy `config.yaml.in` as `config.yaml` and update `ip`, `username`, ... according to your device.
The key-values in the YAML file is simply passed to [netmiko.base_connection.BaseConnection](https://ktbyers.github.io/netmiko/docs/netmiko/base_connection.html).

## Usage

The commands should be provided via pipe. For example, you can dump the current config by
```:bash
echo "show config" | python3 sendcmd.py config.yaml
```

If you provide `secret` in `config.yaml`, you can save the current config as follows.
```:bash
echo -e "administrator\nsave" | python3 sendcmd.py config.yaml
```

