#!/usr/bin/env python


import subprocess


def main():
    """Main entry points
    """
    subprocess.call(['mplayer', '-endpos', '5.5', 'sound.mp3'])


if __name__ == "__main__":
    main()
