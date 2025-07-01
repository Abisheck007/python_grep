try:
    f = open("demofile.txt", "w")
    try:
        f.write("Now the file has more content!")
    except:
        print("An error occurred while writing to the file.")
    finally:
        f.close()
    
except:
    print("An error occurred while opening the file.")
