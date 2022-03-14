import os
import socket

from re          import compile, match
from sys         import stdout, argv, version_info, byteorder
from time        import sleep
from random      import randint, choice as choice_rand
from shutil      import make_archive, copy
from subprocess  import call

"""
----- COMMENTS -----
edode    : Explanation commentary
lisandro : Warning commentary or code to add etc
19111999 : Critical problem
"""

interface_path  = "/sys/class/net/"
ALPHABET_LOWER  = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
HEXADECIMAL     = "0123456789abcdef"
NUMBER          = "0123456789"

class Color:
    """

    IMPORTED FROM THE COLOR LIB #---# NOT MINE

    """

    __ALL__ = [ 'colored', 'cprint' ]

    ATTRIBUTES = dict(list(zip(['bold','dark','','underline',
                                'blink','','reverse','concealed'],
                               list(range(1, 9)))))
    del ATTRIBUTES['']

    HIGHLIGHTS = dict(list(zip(['on_grey','on_red','on_green','on_yellow',
                                'on_blue','on_magenta','on_cyan','on_white'],
                               list(range(40, 48)))))

    COLORS = dict(list(zip(['grey','red','green','yellow','blue','magenta','cyan','white',]
                           ,list(range(30, 38)))))

    RESET = '\033[0m'

    def colored(self, text, color=None, on_color=None, attrs=None):
        if os.getenv('ANSI_COLORS_DISABLED') is None:
            fmt_str = '\033[%dm%s'
            if color is not None:
                text = fmt_str % (Color.COLORS[color], text)

            if on_color is not None:
                text = fmt_str % (Color.HIGHLIGHTS[on_color], text)

            if attrs is not None:
                for attr in attrs:
                    text = fmt_str % (Color.ATTRIBUTES[attr], text)

            text += Color.RESET
        return text;

    def cprint(self, text, color=None, on_color=None, attrs=None, **kwargs):
        print((Color.colored(text, color, on_color, attrs)), **kwargs)



class ff: # edode : stands for file_folder
    def is_dir(self, path_to_dir: str) -> bool:
        if os.path.isdir(path_to_dir):
            return True;
        else:
            return False;

    def is_file(self, path_to_file: str) -> bool:
        if os.path.isfile(path_to_file):
            return True;
        else:
            return False;

    def create_file(self, path: str) -> None:
        return open(path, "w").close();

    def create_archive(self, path_to_file: str) -> str:
        """
        Can also be used to backup a folder
        """
        return make_archive(path_to_file, "zip", path_to_file);

    def backup_file(self, path: str) -> str:
        return copy(path, path + ".bak");

    def get_extension(self, file_name: str) -> str:
        filename, file_extension = os.path.splitext(file_name)
        return file_extension;

    def jp(self, path_1: str, path_2: str) -> str:
        """
        STANDS FOR JOIN PATH, jp is easier that os.path.join
        :param path_1 str:
        :param path_2 str:
        :return str:
        """
        return os.path.join(path_1, path_2)

    def list_files(self, path: str) -> list:
        """
        lists only the files contained in a directory
        :return:
        """
        file_list = []
        print(path)
        for file in os.listdir(path):
            if ff.is_file(ff.jp(path, file)):
                file_list.append(file)
        return file_list;

    def list_dir(self, path: str) -> list:
        """

        :param path str:
        :return:
        """
        i = 1
        file_list = []
        print(path)
        for dir in os.listdir(path):
            file_list.append(dir)

        return file_list;

    def dict_to_json(self, result: dict):
        """
        Convert a dictionary to a json file
        :return:
        """
        with open("result.json", "w") as f:
            json.dump(result, f, indent=4)
        f.close()
        return;



class networking:
    def check_ip_address(self, ip_address: str, ipv4: bool = True) -> bool:
        """
        :param ip_address str:
        :return true: return ('ip_address', True) -> use : print(check_ip_address("192.168.1.1")[0])
                                                           to get the ip address
        """

        if ipv4:
            regex_ip = compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
                               "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
        else:
            regex_ip = compile("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:"
                               "|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}"
                               "(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4})"
                               "{1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:)"
                               "{1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:"
                               "((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|"
                               "::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}"
                               "(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|"
                               "(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))")

        if match(regex_ip, ip_address):
            return True;
        else:
            return False;

    def is_connected(self, hostname: str = None, port_no: int = None) -> bool or str:
        """
        :param hostname str: it has to be an ip address
        :return bool:
        """
        if hostname is None:
            hostname = "1.1.1.1"
        else:
            if not networking.check_ip_address(hostname):
                return False;

        if port_no is None:
            port_no = 443

        try:
            host = socket.gethostbyname(hostname)
            s = socket.create_connection((host, port_no), 2)
            s.close()
            return True;
        except ConnectionError:
            return False;
        except socket.timeout:
            return Color.cprint("[-] Connection to port " + str(port_no) + " unsuccessful", "red");

    def interface_up(self, interface_name: str) -> bool or int: # lisandro : try it on a pure debian
        """
        Works well on kali linux
        :param interface str: name of the interface : eth0/wlan0/at0...
        """
        # edode: /sys/class/net/<INTERFACE>/flags indicates whether the device is on or off.
        # edode: /sys/class/net/<INTERFACE>/carrier works just like /sys/class/net/wlan0/operstate
        # edode: /sys/class/net/<INTERFACE>/operstate indicates if the connection is operational (packets are being sent and received).

        flag_path = os.path.join(interface_path + interface_name + "/flags")
        try:
            with open(flag_path, "r") as f:
                lines = f.readlines()
            f.close()
            for i, line in enumerate(lines):
                if line == "0x1003\n" or line == "0x9\n":
                    return True;
                if line == "0x1002\n" or line == "0x8\n":
                    return False;
        except FileNotFoundError:
            return 0;

    def interface_to_list(self) -> list:
        interface_list = []
        for iface in os.listdir(interface_path):
            interface_list.append(iface)
        return interface_list;

    def is_interface_up(self, interface_name: str) -> bool:
        for iface in os.listdir(interface_path):
            if iface == interface_name:
                if networking.interface_up(iface):
                    return True;
                else:
                    return False;
        return False;

    def display_interface(self, display_loopback: bool =None) -> None:
        """
        :param display_loopback bool: True if you want to display the loopback
        :return:
        """

        if display_loopback is None or not display_loopback:
            i = 0
            for iface in os.listdir(interface_path):
                if iface != "lo":
                    if networking.interface_up(iface):
                        print(str(i)+") "+iface+" (UP)")
                    else:
                        print(str(i)+") "+iface+" (DOWN)")
                    i+=1

        if display_loopback is not None and display_loopback:
            i = 0
            for iface in os.listdir(interface_path):
                if networking.interface_up(iface):
                    print(str(i)+") "+iface+" (UP)")
                else:
                    print(str(i)+") "+iface+" (DOWN)")
                i += 1
        return;

    def return_interface(self, return_iface: str, return_loopback: bool =None) -> None:
        """
        :param return_iface int:
        :return:
        """
        if return_loopback is None or not return_loopback:
            i = 0
            for iface in os.listdir(interface_path):
                if iface != "lo":
                    if i == return_iface:
                        if networking.interface_up(iface):
                            return True, iface;
                        else:
                            return False, "Interface has been set down during the process";
                    i += 1

        if return_loopback is not None and return_loopback:
            if return_loopback is None or not return_loopback:
                i = 0
                for iface in os.listdir(interface_path):
                    if i == return_iface:
                        return iface;
                    i += 1
        return;

    def display_mac(self, interface_name: str) -> str:
        """
        :param interface_name str:
        :return:
        """
        mac_address_path = os.path.join(interface_path + interface_name + "/address")
        with open(mac_address_path, "r") as f:
            lines = f.readlines()
        f.close()
        for i, line in enumerate(lines):
            return line;

    def macchanger(self, interface_name: str, new_mac: str) -> bool:
        """
        :param interface_name str: name of the interface
        :param new_mac str: new mac address of the designated interface
        """
        if interface_name != "lo":
            call(["sudo", "ifconfig", interface_name, "down"])
            call(["sudo", "ifconfig", interface_name, "hw", "ether", new_mac])
            call(["sudo", "ifconfig", interface_name, "up"])
            return True;
        else:
            return False;

    def macchecker(self, mac_address: str) -> bool:
        regex_mac = compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
        if match(regex_mac, mac_address):
            return True;
        else:
            return False;

    def ip_range(self, ip: str, addr_range: int or str) -> None:
        temp = ""
        for i, num in enumerate(ip.split(".")):
            if i == 3:
                ip_range = temp + str(addr_range)
                return ip, ip_range;
            temp = temp + str(num) + "."
        return;

    def in_port_range(self, port_no: int) -> bool:
        if 1 <= port_no <= 65535:
            return True;
        else:
            return False;



class misc:  # miscellaneous
    def animated_three_dots(self, text: str, number: int) -> None:
        """
        display a message with animated 3 dots at the end
        :param text string: string that will ve displayed
        :param number: number of times that the 3 points will be displayed
        :return
        """
        dot_time = int(number) * 4
        for number in range(dot_time):
            number += 1
            stdout.write("   ")
            x = number % 4
            stdout.write('\r'+text + "." * x)
            sleep(0.5)
            stdout.flush()
        return;

    def clear(self) -> os:
        if os.name == "posix":
            return os.system("clear");
        if os.name == "nt":
            return os.system("cls");

    def uptime(self) -> str:
        """
        get uptime in hours
        :return string
        """
        with open("/proc/uptime", "r") as f:
            uptime = f.read().split(" ")[0].strip()
        f.close()
        uptime = int(float(uptime))
        uptime_hours = uptime // 3600
        uptime_minutes = (uptime % 3600) // 60
        return (str(str(int(uptime_hours)) + ":" + str(int(uptime_minutes))));

    def endian(self) -> str:
        return byteorder;

    def to_binary(self, char: str):
        return (lambda x: x != "100000", [bin(ord(c))[2:] for c in char])[1][0]

    def clear_duplicates_in_list(self, list_to_clear: list) -> list:
        return list(dict.fromkeys(list_to_clear));

    def join_list(self, word: str, sep: str="") -> str:
        """
        :param word list: list of word that will be transformed to a single string
            input  -> join_list(["hello", "from", "the", "moon"], " ")
            output -> hello from the moon

        :return string
        """
        return sep.join(str(x) for x in word);

    def how_many_x_in_y(self, x: int, y:int) -> int:
        count = 0
        while True:
            if x < y:
                return count;
            else:
                x = x - y
                count += 1

    def how_many_69(self, number: int) -> int: #19111999 : do I keep those ?? <- when will I reach the 500 ?
        """
        Ahhh yes, the sex number
        OH YEAH
        :return: count
        """
        count = 0
        while True:
            if number >= 69:
                number = number - 69
                count += 1
            else:
                return count;

    def how_many_420(self, number: int) -> int:
        """
        Ahh yes, the weed number
        OH YEAH
        :return: count
        """
        count = 0
        while True:
            if number >= 420:
                number = number - 420
                count += 1
            else:
                return count;

    def swap(self, x: int, y: int) -> int:
        """
        swap two variables
        """
        x, y = y, x
        return x, y;

    def floor(self, number: float) -> int:
        number = str(number)
        left   = int(number.split(".")[0])
        return left - 1;

    def ceil(self, number: int) -> int:
        number = str(number)
        left   = int(number.split(".")[0])
        return left + 1;

    def is_even(self, number: int) -> bool:
        if number % 2 == 0:
            return True;
        else:
            return False;

    def python_version(self) -> str:
        return str(version_info[0]) + "." + str(version_info[1]);

    def get_exec_path(self, full_path: str) -> str:
        """
        19111999
        returns executable (python file) path
        :param full_path string:
        """
        temp = ""
        len_full_path = len(full_path.split("/"))
        for i, x in enumerate(full_path.split("/")):
            if i == len_full_path - 1:
                exec_path = temp
                break;
            temp = temp + x + "/"
        return exec_path;

    def second_over_the_first(self, first_value: all, second_value: all, return_value: str="") -> all:
        """
        case 1 : first = "";  second = "";  -> returns return value
        case 2 : first = "x"; second = "";  -> returns first
        case 3 : first = "";  second = "y"; -> returns second
        case 4 : first = "x"; second = "y"; -> returns second

        :param first_value  all :
        :param second_value all :
        :param return_value all :

        :return depending on the types of the parameters
        """
        if (first_value == ""):
            if (second_value == ""):
                return return_value;
            else:
                return  second_value;
        else:
            if (second_value == ""):
                return first_value;
            else:
                return second_value;

    def make_list_choice(self, choice_list: list) -> str:
        """
        Creates a list of choices that looks like this:
            0) X
            1) Y
            2) Z
            ...
        Ability to type the number of the desired choice, or the name of the choice
        :param choice_list:
        :return str: returns the right part of the choice (here, X, Y or Z)
        """
        while True:
            [print(f"{i}) {c.capitalize()}") for i, c in enumerate(choice_list)]
            option = input(f"Which option do you want to modify ? (0-{len(choice_list) - 1}) : ")
            try:
                if type(int(option)):
                    if 0 <= int(option) <= len(choice_list) - 1:
                        return choice_list[int(option)];
            except (SyntaxError, NameError, ValueError):
                if option.lower() in choice_list:
                    return option.lower();
            print("You have to enter a valid number or a option name")



class random_return:
    def random_int(self, lower: int, upper: int) -> int:
        """
        :param lower, upper int:
        :return int:
        """
        if lower > upper:
            lower, upper = upper, lower
        return randint(lower, upper);

    def random_hex(self) -> str:
        return choice_rand(HEXADECIMAL);

    def random_number(self) -> int:
        return int(choice_rand(NUMBER));

    def random_letter(self) -> str:
        return choice_rand(ALPHABET_LOWER);
