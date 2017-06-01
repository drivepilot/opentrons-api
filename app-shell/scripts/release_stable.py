import os

import util


def build_app():
    os.environ['CHANNEL'] = 'stable'
    print('releasing app...')


def is_tc_tag():
    try:
        res = util.get_cmd_value('git describe --exact-match --tags HEAD')
        return True
    except Exception as e:
        print('Could not detect TC tag')
        return False


if __name__ == '__main__':
    if 'TRAVIS_TAG' in os.environ:
        print('*** Detected Travis Tag')
        build_app()
    elif 'APPVEYOR_REPO_TAG_NAME' in os.environ:
        print('*** Detected AppVeyor Tag')
        build_app()
    elif is_tc_tag():
        print('*** Detected TeamCity Tag')
        build_app()
