import os
import sys
import argparse
import traceback

RESET_COLOR = '\033[0m'
FG_RED = '\033[91m'

parser = argparse.ArgumentParser()

parser.add_argument(
    '--currentappname',
    default='base-android-project',
    type='str',
    action='store',
)

parser.add_argument(
    '--currentpackagename',
    default='io.github.ichisadashioko.android.base_android_project',
    type='str',
    action='store',
)

parser.add_argument(
    '--newappname',
    type='str',
    action='store',
)

parser.add_argument(
    '--newpackagename',
    type='str',
    action='store',
)

args = parser.parse_args()
print('args:', args)

SCRIPT_PATH = os.path.abspath(__file__)
MODULE_PARENT = os.path.dirname(SCRIPT_PATH)

# replace app name

def replace_string_infile(
    original_str: str,
    new_str: str,
    filepath: str,
):
    if not os.path.exists(filepath):
        print(FG_RED, end='', file=sys.stderr)
        print(f'{filepath} does not exist', file=sys.stderr, end='')
        print(RESET_COLOR, file=sys.stderr)
    else:
        file_content_bs = open(filepath, mode='rb').read()

        if len(file_content_bs) < 1:
            print(FG_RED, end='', file=sys.stderr)
            print(f'{filepath} is empty', end='', file=sys.stderr)
            print(RESET_COLOR, file=sys.stderr)
        else:
            successfully_decode_file_content = False

            try:
                file_content_str = file_content_bs.decode('utf-8')
                successfully_decode_file_content = True
            except Exception as ex:
                stack_trace_str = traceback.format_exc()
                print(FG_RED, end='', file=sys.stderr)
                print(ex, file=sys.stderr)
                print(stack_trace_str, file=sys.stderr)
                print(f'fail to decode {filepath} content', file=sys.stderr, end='')
                print(RESET_COLOR, file=sys.stderr)
                successfully_decode_file_content = False

            if successfully_decode_file_content:
                if original_str not in file_content_str:
                    print(FG_RED, end='', file=sys.stderr)
                    print(f'original_str ({original_str}) does not appear in {filepath}', file=sys.stderr, end='')
                    print(RESET_COLOR, file=sys.stderr)
                else:
                    file_content_str.replace(original_str, new_str)

project_name_filepath = os.path.join(MODULE_PARENT, 'settings.gradle')
app_name_filepath = os.path.join(MODULE_PARENT, 'app', 'src', 'main', 'res', 'values', 'strings.xml')
