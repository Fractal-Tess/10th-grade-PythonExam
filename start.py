try:
    import train_manager
    import main_menu
    from sys import path

except Exception as e:
    print("Some modules are missing:[{}]".format(e))


def main():
    train_manager.check_train_data_base()
    train_manager.load_trains()

    main_menu.m_menu()


if __name__ == '__main__':
    main()

