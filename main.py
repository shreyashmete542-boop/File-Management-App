
import os


def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File {filename}: Successfully created")    
    except FileExistsError:
        print(f"file {filename} already exist")
    except Exception as E:
        print("Unexcepted Error!")

def view_all_files():
    files=os.listdir()
    if not files:
        print("No files found!")
    else:
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been successfully deleted.")
    except FileNotFoundError:
        print(f"{filename} not found!")    
    except Exception as E:
        print(f"An error occur!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occur!")        

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("Enter content:")
            f.write(content+"\n")
            print(f"content added to {filename} Successfully")
    except FileNotFoundError:
        print("File not found")  
    except Exception as e:
        print("An error occur!")

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print("1: Create file")
        print("2: view all files")
        print("3: Delete Files")
        print("4: Read files")
        print("5: Edit Files")
        print("6: Exit")

        choice=input("Enter your choices between (1-6):")

        if choice=='1':
            filename=input('Enter Filename')
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input("enter filename:")
            delete_file(filename)
        elif choice=='4':
            filename=input('Enter filename')
            read_file(filename)
        elif choice=='5':
            filename=input("Enter filename")
            edit_file(filename)
        elif choice=='6':
            print("Closing app")
            break
        else:
            print('invalid input')
if __name__=="__main__":
    main()
