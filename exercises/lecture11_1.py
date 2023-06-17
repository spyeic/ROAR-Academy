try:
    motto = open("motto.txt", "w")
    motto.write("Fiat Lux!\n")
except IOError:
    print("An IOError occur")
finally:
    motto.close()

try:
    motto = open("motto.txt", "r")
    for line in motto:
        print(line)
except IOError:
    print("An IOError occur")
finally:
    motto.close()

try:
    motto = open("motto.txt", "a")
    motto.write("Let there be light!")
except IOError:
    print("An IOError occur")
finally:
    motto.close()

