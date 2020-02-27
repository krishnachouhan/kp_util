"""PACKAGE COLORS:

  kc_colors

  kc_colors1.0

  Author: Krishna Chouhan
  E-mail: krishna.chouhan34@gmail.com

  help(): help function will list all the members and methods.

  About:
    This module was suppose to be help color the outputs.
    In case of command prompt, this should work without any problem.
    In case if its not working in windows-10: 
      goto REGEDIT
      HKEY_CURRENT_USER
        Add a DWORD value
          name: VirtualTerminalLevel
          value: 1
      for Details see the issue: https://github.com/ytdl-org/youtube-dl/issues/15758
                  Image: https://user-images.githubusercontent.com/5589855/36943005-11e41fe2-1f36-11e8-9401-7ac40d300f10.png
  Known Issues:
    Doesn't works well with tqdm.

"""

_HEADER     ='\033[95m'
_OKBLUE     ='\033[94m'
_OKGREEN    ='\033[92m'
_WARNINGC   ='\033[93m'
_FAIL       ='\033[91m'
_ENDC       ='\033[0m'
_BOLD       ='\033[1m'
_UNDERLINE  ='\033[4m'
_CRED       ='\033[91m'
_CEND       ='\033[0m'
_BLACK      ='\033[30m'
_WHITE      ='\033[93m'
_RED        ='\033[31m'
_BLUE       ='\033[34m'
_GREEN      ='\033[32m'
_YELLOW     ='\033[33m'

_WARNING    = _WARNINGC + 'WARNING:\t'
_DONE       = _OKGREEN + 'DONE:\t'
_INFO       = _OKBLUE + 'INFO:\t'
_ERROR      = _FAIL + _BOLD + 'ERROR!\t'

_WARNING_B  = _BOLD + '\33[103m' + 'WARNING:\t' + _CEND + '\33[103m' 
_DONE_B     = _BOLD + '\33[102m' + 'DONE:\t' + _CEND + '\33[102m'
_INFO_B     = _BOLD + '\33[104m' + 'INFO:\t' + _CEND + '\33[104m'
_ERROR_B    = _BOLD + '\33[41m' + 'ERROR!\t' + _CEND + '\33[41m'

def _Warning(str):
  """
    _Warning(str) : Prints warning
  """
  print(_WARNING, str, _CEND)

def _Header(str):
    """
    _Header(str) : Prints header
    """
    print(_HEADER, str, _CEND)

def _Okblue(str):
    """
    _Okblue(str) : Prints OK with Blue color
    """
    print(_OKBLUE, str, _CEND)

def _Okgreen(str):
    """
    _Okgreen(str) : Prints OK with Green color
    """
    print(_OKGREEN, str, _CEND)

def _Warningc(str):
    """
    _Warningc(str) : string with warning color
    """
    print(_WARNINGC, str, _CEND)

def _Fail(str):
    """
    _Fail(str) : Failed
    """
    print(_FAIL, str, _CEND)

def _Endc(str):
    """
    _Endc(str) : End with color
    """
    print(_ENDC, str, _CEND)

def _Bold(str):
    """
    _Bold(str) : Bold string
    """
    print(_BOLD, str, _CEND)

def _Underline(str):
    """
    _Underline(str) : Prints underlined string
    """
    print(_UNDERLINE, str, _CEND)

def _Cred(str):
    """
    _Cred(str) : Red colored string
    """
    print(_CRED, str, _CEND)

def _Cend(str):
    """
    _Cred(str) : Ends color and prints in normal print
    """
    print(_CEND, str, _CEND)

def _Warning(str):
    """
    _Warning(str) : print warning and then string
    """
    print(_WARNING, str, _CEND)

def _Done(str):
    """
    _Done(str) : prints Done then string
    """
    print(_DONE, str, _CEND)

def _Info(str):
    """
    _Info(str) : Prints Info then string
    """
    print(_INFO, str, _CEND)

def _Error(str):
    """
    _Error(str) " Prints Error then string
    """
    print(_ERROR, str, _CEND)

def _Warning_B(str):
    """
    _Warning(str) : print warning and then string with background
    """    
    print(_WARNING_B, '\x1b[0;30;43m', str, _CEND)

def _Done_B(str):
    """
    _Done_B(str) : print Done and then string with background
    """    
    print(_DONE_B, '\x1b[0;30;44m', str, _CEND)

def _Info_B(str):
    """
    _Info(str) : Prints Info then string with background
    """    
    print(_INFO_B, '\x1b[0;30;42m', str, _CEND)

def _Error_B(str):
    """
    _Error(str) " Prints Error then string with background
    """    
    print(_ERROR_B, '\x1b[0;33;41m', str, _CEND)

def print_format_table(): 
    """ 
    prints table of formatted text format options 
    """
    for style in range(8): 
        for fg in range(30, 38): 
            s1 = '' 
            for bg in range(40, 48): 
                format = ';'.join([str(style), str(fg), str(bg)]) 
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format) 
            print(s1) 
        print('\n') 

def help():
    """
      Prints all available variables and functions in the package.
    """
    variables="""VARIABLES:
        _BOLD           _OKBLUE         _CRED
        _UNDERLINE      _OKGREEN        _CEND
        _BLACK          _BLUE
        _WHITE          _GREEN
        _RED            _YELLOW
        _HEADER         _WARNING        _WARNING_B
        _WARNINGC       _DONE           _DONE_B
        _ENDC           _INFO           _INFO_B
        _FAIL           _ERROR          _ERROR_B
"""

    functions = """
FUNCTIONS:
        _Warning(str)      _Warning_B(str)    _Warning(str)      _Header(str)
        _Done(str)         _Done_B(str)       _Warningc(str)     _Endc(str)
        _Info(str)         _Info_B(str)       _Fail(str)
        _Error(str)        _Error_B(str)      _Bold(str)         _Underline(str)
        _Okblue(str)       _Cred(str)         _Okgreen(str)      _Cend(str)

HELPING FUNCTIONS:
        print_format_table()
        help()"""
    print(variables,'', functions)
