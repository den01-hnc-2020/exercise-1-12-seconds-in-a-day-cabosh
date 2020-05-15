def main():

    days = int(input("How many days would you like to convert into seconds? "))

    seconds = (days * 86400)

    print("There are " + str(seconds) + " seconds in " + str(days) + " days.")

if __name__ == '__main__':
    main()
