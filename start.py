import main_menu, classes, train_manager, station_manager
import os, sys, classes


# TODO: move this into another script


def main():
    train_manager.check_train_data_base()
    train_manager.load_trains()
    station_manager.check_for_station_data_base()
    station_manager.load_stations()

    main_menu.m_menu()

if __name__ == '__main__':
    main()

