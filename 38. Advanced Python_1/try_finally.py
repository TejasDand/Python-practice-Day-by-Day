# Finally keyword, function mein return ko bhi overwrite kar deta hai. Jabki return ka kaam hai neeche ka code aage mat chalana function mein, phir bhi finally keyword execute ho rha hai.

def main():

    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("Yeh chalega hi chalega, isko return bhi nhi rok sakta!")

    print("Yeh print nhi hoga!")


main()