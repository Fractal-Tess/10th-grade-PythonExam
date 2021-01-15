try:
    import train_manager
    import main_menu
    from sys import path
    import sys

except Exception as e:
    print("Some modules are missing:[{}]".format(e))
    sys.exit(0)


def main():
    train_manager.load_trains()

    main_menu.m_menu()


if __name__ == '__main__':
    main()
