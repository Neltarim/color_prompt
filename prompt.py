from getpass import getpass


class Prompt():

    def __init__(self):
        self.prog_name = 'Color_Prompt_1.0'
        self.txt = ''
        self.endl = ''
        self.type = 'HEADER'
        self._input = False
        self.pwd = False
        self.display_name = True
        self.name_type = 'HEADER'

        self.colors = {
            'HEADER' : '\033[95m',
            'BLUE' : '\033[94m',
            'GREEN' : '\033[92m',
            'WARNING' : '\033[93m',
            'FAIL' : '\033[91m',
            'ENDC' : '\033[0m',
        }

    def reset_conf(self):
        self.txt = ''
        self.endl = ''
        self.type = 'HEADER'
        self._input = False
        self.pwd = False
        self.name_type = 'HEADER'
        
    def base(self, endl=''):
        print(self.colors[self.type] + '{' + self.prog_name + '} :' + self.colors['ENDC'], end=endl)
        self.reset_conf()

    def print_formatted(self):
        if self.display_name:
            self.base()

        if self.pwd:
            res =  getpass(self.colors['WARNING'] + 'password :' + self.colors['ENDC'])
            self.reset_conf()
            return res

        print(self.colors[self.type] + self.txt + self.colors['ENDC'], end=self.endl)
        
        if self._input:
            res = input()
            self.reset_conf()
            return res

        self.reset_conf()


    def password(self):
        self.pwd = True
        return self.print_formatted()

    def process_args(self, txt, endl, _input):
        self.txt  = txt

        if _input:
            self._input = True
            self.endl = ''
        else:
            self.endl = endl
    
    def header(self, txt, endl='', _input=False):
        self.type = 'HEADER'

        self.process_args(txt, endl, _input)
        self.print_formatted()

    def blue(self, txt, endl='', _input=False):
        self.type = 'BLUE'

        self.process_args(txt, endl, _input)
        self.print_formatted()

    def green(self, txt, endl='', _input=False):
        self.type = 'GREEN'

        self.process_args(txt, endl, _input)
        self.print_formatted()

    def warning(self, txt, endl='', _input=False):
        self.type = 'WARNING'

        self.process_args(txt, endl, _input)
        self.print_formatted()

    def fail(self, txt, endl='', _input=False):
        self.type = 'FAIL'

        self.process_args(txt, endl, _input)
        self.print_formatted()

    def test(self):
        for name, color in self.colors:
            print(self.colors[color] + name + self.colors['ENDC'])