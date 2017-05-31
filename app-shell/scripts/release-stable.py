import os

from build_electron_app_with_builder import build_electron_app
import util


def build_app():
    os.environ['CHANNEL'] = 'stable'
    print('releasing app...')


def is_tc_tag():
    res = util.get_cmd_value('git describe --exact-match --tags HEAD')
    print('TAG value on TC is', res)
    if res.startswith('fatal'):
        return False
    return True


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
