# type a number from console and transfer it to int
tuna = int(input("what is your fav number?\n"))
print(tuna)

# catch and handle exception
while True:
    try:
        number = int(input("what is your fav number?\n"))
        print(18/number)
        break
    except ValueError: # Catch ValueError exception
        print("Make sure enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("execute it no mater what - Loop Complete")