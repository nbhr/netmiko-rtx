# netmiko-yamaha-rtx

This is a small script to send commands to Yamaha RTX devices using [netmiko](https://github.com/ktbyers/netmiko) library.

The main reason I wrote this script was to workaround a bug (?) in `enable()` of the netmiko library version 4.4.0.  With my Yamaha RTX 830, it fails to find the prompt `#` after the `administrator` command seemingly because the original implementation waits for `>` only.  I do not know if this is specific to my device or if it is a general issue with Yamaha devices.  In case you know of a solution, please kindly let me know.  I am happy to delete this dirty hack and will use the official API.

## Disclaimer

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
